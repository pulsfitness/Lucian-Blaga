"""Sursa unică pentru lecții și întrebări.

Fiecare domeniu are UN SINGUR modul sursă (chapter1.py … chapter7.py). Întrebările demonstrative
vechi din content.py nu mai intră în bancă (se păstrează doar pentru a afișa corect istoricul vechi).
Aici se normalizează formatul (număr de lecție, chei de explicații pe literă, conversia
formulelor pentru Streamlit) fără a modifica fișierele de capitol.
"""
from __future__ import annotations

import re

from content import DOMAIN_ORDER, LEGACY_DEMO_QUESTIONS
from chapter1 import CHAPTERS as _CH1, CHAPTER1_QUESTIONS
from chapter2 import CHAPTER2_LESSONS, CHAPTER2_QUESTIONS
from chapter3 import CHAPTER3_LESSONS, CHAPTER3_QUESTIONS
from chapter4 import CHAPTER4_LESSONS, CHAPTER4_QUESTIONS
from chapter5 import CHAPTER5_LESSONS, CHAPTER5_QUESTIONS
from chapter6 import CHAPTER6_LESSONS, CHAPTER6_QUESTIONS
from chapter7 import CHAPTER7_LESSONS, CHAPTER7_QUESTIONS
from lesson_extras import LESSON_EXTRAS

E_OPTION = "E. Niciuna dintre variantele A–D"
LETTERS = "ABCDE"

_RAW = [
    ("Structura atomului", _CH1["Structura atomului"], CHAPTER1_QUESTIONS),
    ("Legături chimice", CHAPTER2_LESSONS, CHAPTER2_QUESTIONS),
    ("Soluții", CHAPTER3_LESSONS, CHAPTER3_QUESTIONS),
    ("Legile gazelor", CHAPTER4_LESSONS, CHAPTER4_QUESTIONS),
    ("Procese de oxidare și reducere", CHAPTER5_LESSONS, CHAPTER5_QUESTIONS),
    ("Introducere în chimia organică", CHAPTER6_LESSONS, CHAPTER6_QUESTIONS),
    ("Hidrocarburi", CHAPTER7_LESSONS, CHAPTER7_QUESTIONS),
]

# ---------------------------------------------------------------- formule
_DISPLAY = re.compile(r"\\\[(.+?)\\\]", re.S)
_INLINE = re.compile(r"\\\((.+?)\\\)", re.S)
_MATH = re.compile(r"(\$\$.+?\$\$|\$[^$\n]+?\$)", re.S)
_DECIMAL = re.compile(r"(\d),(\d)")
_BLOCK = re.compile(r"[ \t]*\$\$(.+?)\$\$[ \t]*", re.S)


def to_streamlit_math(text: str) -> str:
    """Streamlit (KaTeX) recunoaște doar $...$ și $$...$$. Capitolele 1–4 folosesc \\[ \\] și \\( \\),
    care altfel ar apărea ca text brut. În interiorul formulelor, virgula zecimală devine {,}
    (fără spațiu după virgulă)."""
    if not text:
        return text
    text = _DISPLAY.sub(lambda m: "\n$$\n" + m.group(1).strip() + "\n$$\n", text)
    text = _INLINE.sub(lambda m: "$" + m.group(1).strip() + "$", text)
    text = _MATH.sub(lambda m: _DECIMAL.sub(r"\1{,}\2", m.group(0)), text)
    # Formulele afișate ($$…$$) au nevoie de linii goale în jur, altfel Streamlit le afișează în text.
    text = _BLOCK.sub(lambda m: "\n\n$$" + m.group(1) + "$$\n\n", text)
    return re.sub(r"\n{3,}", "\n\n", text)


# ---------------------------------------------------------------- lecții
def _lesson_number(lesson: dict) -> str:
    if lesson.get("number"):
        return lesson["number"]
    return ".".join(lesson["title"].split(".")[:2]).strip()


def _normalize_lesson(lesson: dict, domain: str, chapter_no: int) -> dict:
    extras = LESSON_EXTRAS.get(lesson["id"], {})
    out = dict(lesson)
    out["domain"] = domain
    out["chapter"] = chapter_no
    out["number"] = _lesson_number(lesson)
    for key in ("objectives", "mistakes", "connections"):
        out[key] = list(lesson.get(key) or extras.get(key) or [])
    out["worked_examples"] = lesson.get("worked_examples") or extras.get("worked_examples") or ""
    out["takeaways"] = list(lesson.get("takeaways") or [])
    out["body"] = to_streamlit_math(lesson.get("body", ""))
    out["worked_examples"] = to_streamlit_math(out["worked_examples"])
    return out


# ---------------------------------------------------------------- întrebări
def _letter_key(key: str) -> str:
    key = key.strip()
    return key[0] if key and key[0] in LETTERS and (len(key) == 1 or key[1] == ".") else key


def _normalize_question(q: dict) -> dict:
    out = dict(q)
    out["question"] = to_streamlit_math(q["question"])
    out["explanation"] = to_streamlit_math(q["explanation"])
    out.setdefault("level", "Concurs" if str(q.get("lesson", "")).endswith((".8", ".9", ".10", ".11")) else "Intermediar")
    out.setdefault("type", "teorie")
    answer_letter = q["answer"][0]
    raw = q.get("option_explanations") or {}
    expl = {_letter_key(k): to_streamlit_math(v) for k, v in raw.items()}
    # Capitolele 3–4 nu explicau varianta E; explicația este deterministă și corectă:
    # E („niciuna dintre A–D”) este greșită exact atunci când una dintre A–D este corectă.
    if answer_letter != "E" and not expl.get("E"):
        expl["E"] = (f"Varianta E ar fi corectă doar dacă niciuna dintre variantele A–D nu ar fi corectă. "
                     f"Aici varianta {answer_letter} este corectă, deci E este greșită.")
    expl.pop(answer_letter, None)
    out["option_explanations"] = {k: expl[k] for k in LETTERS if k in expl}
    out["answer_letter"] = answer_letter
    return out


CHAPTERS: dict[str, list[dict]] = {}
ALL_QUESTIONS: list[dict] = []
for _no, (_domain, _lessons, _questions) in enumerate(_RAW, start=1):
    CHAPTERS[_domain] = [_normalize_lesson(l, _domain, _no) for l in _lessons]
    ALL_QUESTIONS.extend(_normalize_question(q) for q in _questions)

QUESTIONS_BY_ID = {q["id"]: q for q in ALL_QUESTIONS}
LESSONS_BY_KEY = {(d, l["number"]): l for d, ls in CHAPTERS.items() for l in ls}
LEGACY_BY_ID = {q["id"]: q for q in LEGACY_DEMO_QUESTIONS}


def questions_for(domain: str, lesson_number: str | None = None) -> list[dict]:
    return [q for q in ALL_QUESTIONS if q["domain"] == domain and (lesson_number is None or q["lesson"] == lesson_number)]


def resolve_question(question_id: str, stored_text: str | None = None) -> dict | None:
    """Găsește întrebarea pentru un rând din istoric. Dacă textul salvat diferă de cel din bancă
    (de exemplu un ID refolosit al unei întrebări demonstrative vechi), folosește varianta veche."""
    q = QUESTIONS_BY_ID.get(question_id)
    if q and (not stored_text or _same(stored_text, q["question"])):
        return q
    legacy = LEGACY_BY_ID.get(question_id)
    if legacy and (not stored_text or _same(stored_text, legacy["question"])):
        return _normalize_question(legacy)
    return q


def _same(a: str, b: str) -> bool:
    return to_streamlit_math(a).strip() == b.strip() or a.strip() == b.strip()


def lesson_title(domain: str, number: str | None) -> str:
    lesson = LESSONS_BY_KEY.get((domain, number or ""))
    return lesson["title"] if lesson else (f"Lecția {number}" if number else "Lecție nespecificată")


def validate_bank() -> list[str]:
    """Verificări structurale ale întregii bănci. Întoarce lista problemelor (goală = totul în regulă)."""
    problems = []
    ids, texts = set(), set()
    for domain in DOMAIN_ORDER:
        if not CHAPTERS.get(domain):
            problems.append(f"Domeniul {domain} nu are lecții")
    for q in ALL_QUESTIONS:
        qid = q["id"]
        if qid in ids:
            problems.append(f"ID duplicat: {qid}")
        ids.add(qid)
        norm = re.sub(r"\s+", " ", q["question"].strip().lower())
        if norm in texts:
            problems.append(f"Enunț duplicat: {qid}")
        texts.add(norm)
        if q["domain"] not in DOMAIN_ORDER:
            problems.append(f"{qid}: domeniu necunoscut")
        if (q["domain"], q.get("lesson")) not in LESSONS_BY_KEY:
            problems.append(f"{qid}: lecția {q.get('lesson')!r} nu există în {q['domain']}")
        opts = q["options"]
        if len(opts) != 5 or [o[:3] for o in opts] != [f"{l}. " for l in LETTERS]:
            problems.append(f"{qid}: trebuie exact 5 variante A–E")
        if opts and opts[-1] != E_OPTION:
            problems.append(f"{qid}: varianta E nu respectă modelul")
        if q["answer"] not in opts:
            problems.append(f"{qid}: răspunsul corect nu e printre variante")
        if len(q.get("explanation", "")) < 20:
            problems.append(f"{qid}: lipsește explicația")
        missing = [l for l in LETTERS if l != q["answer_letter"] and not q["option_explanations"].get(l)]
        if missing:
            problems.append(f"{qid}: lipsesc explicațiile pentru {''.join(missing)}")
        for f in ("topic", "lesson", "domain"):
            if not q.get(f):
                problems.append(f"{qid}: câmp gol {f}")
    for domain, lessons in CHAPTERS.items():
        for l in lessons:
            for f in ("title", "level", "body", "takeaways", "objectives", "mistakes"):
                if not l.get(f):
                    problems.append(f"{l['id']}: lipsește {f}")
            if not questions_for(domain, l["number"]):
                problems.append(f"{l['id']}: nu are întrebări asociate")
    return problems
