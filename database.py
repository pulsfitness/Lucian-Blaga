"""Salvarea locală a progresului în SQLite (dezvoltare locală / mod offline).

Reguli importante:
- fișierul data/laborator.db NU este suprascris și NU este șters; schema se completează doar
  prin CREATE TABLE IF NOT EXISTS și ALTER TABLE ... ADD COLUMN (coloane noi, opționale);
- fiecare răspuns este o încercare nouă: istoricul nu se șterge niciodată;
- calea poate fi schimbată cu variabila de mediu LAB_DB_PATH (util pentru teste).
"""
from __future__ import annotations

import os
import sqlite3
import uuid
from pathlib import Path

DEFAULT_DB = Path(__file__).parent / "data" / "laborator.db"


def db_path() -> Path:
    return Path(os.environ.get("LAB_DB_PATH") or DEFAULT_DB)


def connect() -> sqlite3.Connection:
    path = db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def _columns(c: sqlite3.Connection, table: str) -> set[str]:
    return {row["name"] for row in c.execute(f"PRAGMA table_info({table})")}


def init_db() -> None:
    """Creează tabelele lipsă și adaugă coloanele noi fără a modifica datele existente."""
    with connect() as c:
        c.execute("""CREATE TABLE IF NOT EXISTS answers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id TEXT NOT NULL, domain TEXT NOT NULL, topic TEXT NOT NULL,
            question TEXT NOT NULL, chosen TEXT NOT NULL, answer TEXT NOT NULL,
            correct INTEGER NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
        cols = _columns(c, "answers")
        # Coloane adăugate în versiunea 7 (bazele v2–v6 nu le au; rândurile vechi rămân cu NULL / 'test').
        if "lesson" not in cols:
            c.execute("ALTER TABLE answers ADD COLUMN lesson TEXT")
        if "source" not in cols:
            c.execute("ALTER TABLE answers ADD COLUMN source TEXT NOT NULL DEFAULT 'test'")
        c.execute("CREATE INDEX IF NOT EXISTS idx_answers_question ON answers(question_id, id)")
        c.execute("""CREATE TABLE IF NOT EXISTS daily_challenges(
            challenge_date TEXT PRIMARY KEY,
            question_id TEXT NOT NULL, chosen TEXT NOT NULL, correct INTEGER NOT NULL,
            answer_id INTEGER, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
        c.execute("CREATE TABLE IF NOT EXISTS meta(key TEXT PRIMARY KEY, value TEXT NOT NULL)")
        c.execute("INSERT OR IGNORE INTO meta(key, value) VALUES('install_id', ?)", (uuid.uuid4().hex,))


def install_id() -> str:
    with connect() as c:
        row = c.execute("SELECT value FROM meta WHERE key='install_id'").fetchone()
        return row["value"] if row else "necunoscut"


def save_answer(q: dict, chosen: str, correct: bool, source: str = "test") -> int:
    with connect() as c:
        cur = c.execute(
            """INSERT INTO answers(question_id, domain, topic, question, chosen, answer, correct, lesson, source)
               VALUES(?,?,?,?,?,?,?,?,?)""",
            (q["id"], q["domain"], q["topic"], q["question"], chosen, q["answer"], int(bool(correct)),
             q.get("lesson"), source))
        return int(cur.lastrowid)


def get_attempts() -> list[dict]:
    """Toate încercările, în ordine cronologică (cea mai veche prima)."""
    with connect() as c:
        rows = c.execute("""SELECT id, question_id, domain, topic, lesson, question, chosen, answer,
                                   correct, source, created_at
                            FROM answers ORDER BY id""").fetchall()
        return [dict(r) for r in rows]


def get_summary() -> dict:
    with connect() as c:
        r = c.execute("""SELECT COUNT(*) total, COALESCE(SUM(correct),0) correct,
                         COUNT(*)-COALESCE(SUM(correct),0) wrong FROM answers""").fetchone()
        return dict(r)


def get_mistakes() -> list[dict]:
    """O intrare pentru fiecare întrebare greșită cel puțin o dată.

    Răspunsul ales (`chosen`) și data (`latest`) provin EXPLICIT din cea mai recentă încercare
    greșită (rândul cu id maxim dintre încercările greșite ale întrebării). Se adaugă și starea
    ultimei încercări (oricare ar fi), pentru a ști dacă greșeala a fost recuperată.
    """
    with connect() as c:
        rows = c.execute("""
            SELECT w.question_id, w.domain, w.topic, w.lesson, w.question, w.chosen, w.answer,
                   w.created_at AS latest,
                   stats.attempts, stats.wrong_count,
                   last.correct AS last_correct, last.created_at AS last_attempt_at
            FROM answers w
            JOIN (SELECT question_id, COUNT(*) attempts, SUM(correct = 0) wrong_count, MAX(id) last_id
                  FROM answers GROUP BY question_id) stats ON stats.question_id = w.question_id
            JOIN answers last ON last.id = stats.last_id
            WHERE w.id = (SELECT MAX(b.id) FROM answers b
                          WHERE b.question_id = w.question_id AND b.correct = 0)
            ORDER BY w.id DESC""").fetchall()
        return [dict(r) for r in rows]


def get_domain_stats() -> list[dict]:
    with connect() as c:
        rows = c.execute("""SELECT domain, COUNT(*) total, COALESCE(SUM(correct),0) correct
                            FROM answers GROUP BY domain ORDER BY domain""").fetchall()
        return [dict(x) for x in rows]


def get_daily(challenge_date: str) -> dict | None:
    with connect() as c:
        row = c.execute("SELECT * FROM daily_challenges WHERE challenge_date=?", (challenge_date,)).fetchone()
        return dict(row) if row else None


def save_daily(challenge_date: str, q: dict, chosen: str, correct: bool) -> bool:
    """Înregistrează provocarea zilei o singură dată pe zi.

    Totul se face într-o singură tranzacție: dacă ziua există deja (de exemplu după o reîncărcare
    a paginii sau un dublu clic), nu se adaugă nimic și funcția întoarce False.
    """
    conn = connect()
    try:
        with conn:
            cur = conn.execute(
                """INSERT OR IGNORE INTO daily_challenges(challenge_date, question_id, chosen, correct)
                   VALUES(?,?,?,?)""", (challenge_date, q["id"], chosen, int(bool(correct))))
            if cur.rowcount == 0:
                return False
            ans = conn.execute(
                """INSERT INTO answers(question_id, domain, topic, question, chosen, answer, correct, lesson, source)
                   VALUES(?,?,?,?,?,?,?,?, 'daily')""",
                (q["id"], q["domain"], q["topic"], q["question"], chosen, q["answer"], int(bool(correct)),
                 q.get("lesson")))
            conn.execute("UPDATE daily_challenges SET answer_id=? WHERE challenge_date=?",
                         (ans.lastrowid, challenge_date))
        return True
    finally:
        conn.close()
