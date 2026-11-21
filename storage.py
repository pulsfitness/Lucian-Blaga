"""Stratul de salvare: aceeași interfață pentru SQLite local, Supabase online și vizitator.

- LocalBackend   – SQLite (data/laborator.db), folosit când Supabase nu este configurat.
- SupabaseBackend – PostgreSQL online; fiecare rând are user_id = UUID-ul utilizatoarei,
                    iar Row Level Security garantează că se citesc doar propriile date.
- GuestBackend   – Supabase este configurat, dar nimeni nu e conectat: răspunsurile se țin doar
                    în sesiunea curentă a browserului (nu se amestecă cu ale altcuiva).
"""
from __future__ import annotations

from datetime import datetime, timezone

import streamlit as st

import database
import progress

IMPORT_BATCH = 200


class LocalBackend:
    kind = "local"
    label = "Salvare locală pe acest calculator (SQLite)"
    user_key = "local"

    def __init__(self):
        database.init_db()

    def save_answer(self, q, chosen, correct, source="test"):
        database.save_answer(q, chosen, correct, source)

    def attempts(self):
        return database.get_attempts()

    def mistakes(self):
        return database.get_mistakes()

    def daily_get(self, day):
        return database.get_daily(day)

    def daily_save(self, day, q, chosen, correct):
        return database.save_daily(day, q, chosen, correct)


class GuestBackend:
    kind = "guest"
    label = "Vizitator – răspunsurile se păstrează doar până închizi pagina"
    user_key = "vizitator"

    def _rows(self):
        return st.session_state.setdefault("guest_attempts", [])

    def save_answer(self, q, chosen, correct, source="test"):
        rows = self._rows()
        rows.append({"id": len(rows) + 1, "question_id": q["id"], "domain": q["domain"], "topic": q["topic"],
                     "lesson": q.get("lesson"), "question": q["question"], "chosen": chosen, "answer": q["answer"],
                     "correct": int(bool(correct)), "source": source,
                     "created_at": datetime.now(timezone.utc).isoformat()})

    def attempts(self):
        return list(self._rows())

    def mistakes(self):
        return progress.latest_mistakes(self.attempts())

    def daily_get(self, day):
        return st.session_state.setdefault("guest_daily", {}).get(day)

    def daily_save(self, day, q, chosen, correct):
        daily = st.session_state.setdefault("guest_daily", {})
        if day in daily:
            return False
        daily[day] = {"challenge_date": day, "question_id": q["id"], "chosen": chosen, "correct": int(bool(correct))}
        self.save_answer(q, chosen, correct, source="daily")
        return True


class SupabaseBackend:
    kind = "supabase"

    def __init__(self, cfg, user):
        self.cfg = cfg
        self.user = user
        self.user_key = user["user_id"]
        self.label = f"Salvare online în contul {user.get('email') or 'Google'}"

    def _db(self):
        import auth
        return auth.data_client(self.cfg)

    @staticmethod
    def _row(q, chosen, correct, source):
        return {"question_id": q["id"], "domain": q["domain"], "topic": q["topic"], "lesson": q.get("lesson"),
                "question_text": q["question"], "chosen": chosen, "correct_answer": q["answer"],
                "is_correct": bool(correct), "source": source}

    def save_answer(self, q, chosen, correct, source="test"):
        row = {**self._row(q, chosen, correct, source), "user_id": self.user_key}
        self._db().table("answers").insert(row).execute()

    def attempts(self):
        rows, start, page = [], 0, 1000
        db = self._db()
        while True:
            res = (db.table("answers")
                   .select("id,question_id,domain,topic,lesson,question_text,chosen,correct_answer,is_correct,source,created_at")
                   .eq("user_id", self.user_key).order("id").range(start, start + page - 1).execute())
            batch = res.data or []
            rows.extend(batch)
            if len(batch) < page:
                break
            start += page
        return [{"id": r["id"], "question_id": r["question_id"], "domain": r["domain"], "topic": r["topic"],
                 "lesson": r.get("lesson"), "question": r.get("question_text"), "chosen": r["chosen"],
                 "answer": r["correct_answer"], "correct": int(bool(r["is_correct"])), "source": r.get("source"),
                 "created_at": r["created_at"]} for r in rows]

    def mistakes(self):
        return progress.latest_mistakes(self.attempts())

    def daily_get(self, day):
        res = (self._db().table("daily_challenges").select("challenge_date,question_id,chosen,is_correct")
               .eq("user_id", self.user_key).eq("challenge_date", day).limit(1).execute())
        if not res.data:
            return None
        r = res.data[0]
        return {"challenge_date": r["challenge_date"], "question_id": r["question_id"], "chosen": r["chosen"],
                "correct": int(bool(r["is_correct"]))}

    def daily_save(self, day, q, chosen, correct):
        """Funcția SQL submit_daily_challenge scrie atomic provocarea și încercarea; dacă ziua
        există deja întoarce false (protecție la reîncărcare / dublu clic / alt dispozitiv)."""
        res = self._db().rpc("submit_daily_challenge", {
            "p_challenge_date": day, "p_question_id": q["id"], "p_domain": q["domain"], "p_topic": q["topic"],
            "p_lesson": q.get("lesson"), "p_question_text": q["question"], "p_chosen": chosen,
            "p_correct_answer": q["answer"], "p_is_correct": bool(correct)}).execute()
        return bool(res.data)

    # ----- import opțional al progresului local (numai la cererea explicită a utilizatoarei)
    def imported_refs(self):
        refs, start, page = set(), 0, 1000
        db = self._db()
        while True:
            res = (db.table("answers").select("client_ref").eq("user_id", self.user_key)
                   .not_.is_("client_ref", "null").range(start, start + page - 1).execute())
            batch = res.data or []
            refs.update(r["client_ref"] for r in batch)
            if len(batch) < page:
                break
            start += page
        return refs

    def import_local(self, local_rows, install_id):
        """Copiază (nu mută) încercările locale; fiecare rând primește client_ref unic, deci
        importul repetat nu creează dubluri. Datele locale rămân neatinse."""
        existing = self.imported_refs()
        payload = []
        for r in local_rows:
            ref = f"sqlite:{install_id}:{r['id']}"
            if ref in existing:
                continue
            created = progress.parse_ts(r["created_at"]).astimezone(timezone.utc).isoformat()
            payload.append({"user_id": self.user_key, "question_id": r["question_id"], "domain": r["domain"],
                            "topic": r["topic"], "lesson": r.get("lesson"), "question_text": r.get("question"),
                            "chosen": r["chosen"], "correct_answer": r["answer"], "is_correct": bool(r["correct"]),
                            "source": r.get("source") or "test", "client_ref": ref, "created_at": created})
        db = self._db()
        for i in range(0, len(payload), IMPORT_BATCH):
            db.table("answers").insert(payload[i:i + IMPORT_BATCH]).execute()
        return len(payload)


def get_backend():
    """Alege salvarea potrivită pentru sesiunea curentă."""
    import auth
    cfg = auth.get_config()
    if cfg is None:
        return LocalBackend(), None
    user = auth.current_user(cfg)
    if user:
        return SupabaseBackend(cfg, user), cfg
    return GuestBackend(), cfg
