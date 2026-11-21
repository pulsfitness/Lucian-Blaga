"""Calculul statisticilor din istoricul REAL de încercări (fără valori demonstrative).

Funcțiile primesc lista de încercări (dict-uri cu cel puțin: question_id, domain, lesson,
correct, created_at) și sunt identice pentru salvarea locală (SQLite) și cea online (Supabase).
"""
from __future__ import annotations

from collections import OrderedDict, defaultdict
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

TZ = ZoneInfo("Europe/Bucharest")
MIN_ATTEMPTS_FOR_VERDICT = 4     # sub acest număr nu tragem concluzii despre un domeniu/lecție
STRONG_THRESHOLD = 0.80
WEAK_THRESHOLD = 0.60


def parse_ts(value) -> datetime:
    """Acceptă 'YYYY-MM-DD HH:MM:SS' (SQLite, UTC) sau ISO 8601 (Supabase)."""
    if isinstance(value, datetime):
        dt = value
    else:
        text = str(value).strip().replace("Z", "+00:00")
        if " " in text and "T" not in text:
            text = text.replace(" ", "T", 1)
        dt = datetime.fromisoformat(text)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(TZ)


def fmt_ts(value) -> str:
    try:
        return parse_ts(value).strftime("%d.%m.%Y, %H:%M")
    except Exception:
        return str(value)


def _rate(correct: int, total: int) -> float:
    return correct / total if total else 0.0


def summary(attempts: list[dict]) -> dict:
    total = len(attempts)
    correct = sum(1 for a in attempts if a["correct"])
    return {"total": total, "correct": correct, "wrong": total - correct,
            "rate": _rate(correct, total),
            "distinct_questions": len({a["question_id"] for a in attempts})}


def by_domain(attempts: list[dict], domain_order: list[str]) -> list[dict]:
    stats = {d: {"domain": d, "total": 0, "correct": 0} for d in domain_order}
    for a in attempts:
        s = stats.setdefault(a["domain"], {"domain": a["domain"], "total": 0, "correct": 0})
        s["total"] += 1
        s["correct"] += 1 if a["correct"] else 0
    for s in stats.values():
        s["wrong"] = s["total"] - s["correct"]
        s["rate"] = _rate(s["correct"], s["total"])
    return list(stats.values())


def by_lesson(attempts: list[dict]) -> list[dict]:
    stats: dict[tuple, dict] = {}
    for a in attempts:
        key = (a["domain"], a.get("lesson") or "—")
        s = stats.setdefault(key, {"domain": key[0], "lesson": key[1], "total": 0, "correct": 0})
        s["total"] += 1
        s["correct"] += 1 if a["correct"] else 0
    for s in stats.values():
        s["wrong"] = s["total"] - s["correct"]
        s["rate"] = _rate(s["correct"], s["total"])
    return sorted(stats.values(), key=lambda s: (s["domain"], _lesson_sort_key(s["lesson"])))


def _lesson_sort_key(lesson: str):
    try:
        return tuple(int(p) for p in lesson.split("."))
    except ValueError:
        return (999,)


def timeline(attempts: list[dict]) -> list[dict]:
    """Evoluția pe zile (ora României): încercări, corecte, procent zilnic și procent cumulat."""
    days: "OrderedDict[str, dict]" = OrderedDict()
    for a in sorted(attempts, key=lambda x: parse_ts(x["created_at"])):
        day = parse_ts(a["created_at"]).date().isoformat()
        d = days.setdefault(day, {"day": day, "total": 0, "correct": 0})
        d["total"] += 1
        d["correct"] += 1 if a["correct"] else 0
    cum_t = cum_c = 0
    out = []
    for d in days.values():
        cum_t += d["total"]; cum_c += d["correct"]
        out.append({**d, "rate": _rate(d["correct"], d["total"]), "cumulative_rate": _rate(cum_c, cum_t)})
    return out


def latest_mistakes(attempts: list[dict]) -> list[dict]:
    """Echivalentul Python al database.get_mistakes(): pentru fiecare întrebare greșită cel puțin
    o dată, răspunsul și data celei mai recente încercări GREȘITE + starea ultimei încercări."""
    ordered = sorted(attempts, key=lambda x: (parse_ts(x["created_at"]), x.get("id") or 0))
    info: dict[str, dict] = {}
    for a in ordered:
        s = info.setdefault(a["question_id"], {"attempts": 0, "wrong_count": 0, "last_wrong": None, "last": None})
        s["attempts"] += 1
        if not a["correct"]:
            s["wrong_count"] += 1
            s["last_wrong"] = a
        s["last"] = a
    out = []
    for qid, s in info.items():
        w = s["last_wrong"]
        if w is None:
            continue
        out.append({"question_id": qid, "domain": w["domain"], "topic": w.get("topic"), "lesson": w.get("lesson"),
                    "question": w.get("question"), "chosen": w["chosen"], "answer": w.get("answer"),
                    "latest": w["created_at"], "attempts": s["attempts"], "wrong_count": s["wrong_count"],
                    "last_correct": int(bool(s["last"]["correct"])), "last_attempt_at": s["last"]["created_at"]})
    out.sort(key=lambda m: parse_ts(m["latest"]), reverse=True)
    return out


def open_mistakes(mistakes: list[dict]) -> list[dict]:
    """Greșelile încă nerecuperate: ultima încercare a întrebării este greșită."""
    return [m for m in mistakes if not m["last_correct"]]


def strengths_and_weaknesses(attempts: list[dict], domain_order: list[str], mistakes: list[dict]):
    """Puncte forte și zone care necesită atenție, numai pe baza datelor reale."""
    dom = [d for d in by_domain(attempts, domain_order) if d["total"] >= MIN_ATTEMPTS_FOR_VERDICT]
    strong = [d for d in dom if d["rate"] >= STRONG_THRESHOLD]
    weak = [d for d in dom if d["rate"] < WEAK_THRESHOLD]
    lessons = [l for l in by_lesson(attempts) if l["total"] >= 2]
    open_by_lesson = defaultdict(int)
    for m in open_mistakes(mistakes):
        open_by_lesson[(m["domain"], m.get("lesson") or "—")] += 1
    weak_lessons = []
    for l in lessons:
        pending = open_by_lesson.get((l["domain"], l["lesson"]), 0)
        if l["rate"] < WEAK_THRESHOLD or pending >= 2:
            weak_lessons.append({**l, "open_mistakes": pending})
    weak_lessons.sort(key=lambda l: (l["rate"], -l["open_mistakes"]))
    strong.sort(key=lambda d: -d["rate"]); weak.sort(key=lambda d: d["rate"])
    untouched = [d for d in by_domain(attempts, domain_order) if d["total"] == 0]
    return {"strong": strong, "weak": weak, "weak_lessons": weak_lessons, "untouched": untouched}
