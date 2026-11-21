"""LABORATORUL OFICIAL AL DOMNITORULUI LUCIAN BLAGA – versiunea 7.

Platformă independentă de pregătire pentru Concursul profesional de chimie „Candin Liteanu”.
Nu este o aplicație oficială a UBB și nu este afiliată Facultății de Chimie și Inginerie Chimică.
"""
from __future__ import annotations

import hashlib
import re
from collections import Counter, defaultdict
from datetime import datetime

import altair as alt
import pandas as pd
import streamlit as st

import auth
import database
import progress
from content import CURRICULUM, DOMAIN_ORDER
from question_bank import (ALL_QUESTIONS, CHAPTERS, LESSONS_BY_KEY, lesson_title, questions_for,
                           resolve_question)
from storage import get_backend

APP_VERSION = "7"
PAGES = ["Acasă", "Programa concursului", "Material de studiu", "Teste pe domenii", "Urmărirea greșelilor",
         "Panou de progres", "Provocarea zilei"]
ALL_LESSONS = "Toate lecțiile"
SOURCE_LABELS = {"test": "Teste pe domenii", "daily": "Provocarea zilei", "mistake_retry": "Reluarea greșelilor"}

st.set_page_config(page_title="Laboratorul Oficial al Domnitorului Lucian Blaga", page_icon="🧪", layout="wide")

st.markdown("""
<style>
:root {--verde:#176b45; --verde-inchis:#123d2b; --verde-deschis:#e7f2e9; --albastru:#1f5fa8; --alb:#ffffff;}
.stApp {background:#f5faf6;}
h1,h2,h3 {color:#174d35;}
[data-testid="stSidebar"] {background:var(--verde-deschis);}
div.stButton>button {background:var(--verde);color:var(--alb);border:0;border-radius:10px;}
div.stButton>button:hover {background:#105437;color:var(--alb);}
div.stButton>button:disabled {background:#9bb8a8;color:var(--alb);}
.hero {padding:2rem;border-radius:18px;background:linear-gradient(120deg,var(--verde-inchis),#20744d);color:var(--alb);margin-bottom:1.4rem;}
.hero h1 {color:var(--alb);line-height:1.15;margin:.3rem 0 .6rem 0;}
.hero p {color:#e3f3e8;font-size:1.1rem;margin-bottom:.4rem;}
.hero .eyebrow {font-size:.8rem;letter-spacing:.08em;color:#cfe8d9;}
.hero .gang {display:inline-block;margin-top:.4rem;padding:.25rem .7rem;border-radius:999px;background:var(--alb);color:var(--albastru);font-weight:700;}
.small-note {color:#5f6f65;font-size:.88rem;}
.pill {display:inline-block;padding:.1rem .55rem;border-radius:999px;background:#e3eefb;color:var(--albastru);font-size:.8rem;margin-right:.3rem;}
a.google-btn {display:block;text-align:center;padding:.55rem .8rem;border-radius:10px;background:var(--alb);
  color:var(--albastru) !important;border:1.5px solid var(--albastru);font-weight:600;text-decoration:none !important;}
a.google-btn:hover {background:#eef4fc;}
@media (max-width: 640px) {
  .hero {padding:1.2rem;border-radius:14px;}
  .hero h1 {font-size:1.45rem;}
  .hero p {font-size:1rem;}
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------ sesiune și salvare
CFG = auth.get_config()
if CFG:
    auth.handle_oauth_callback(CFG)
BACKEND, CFG = get_backend()


def load_history():
    try:
        attempts = BACKEND.attempts()
        mistakes = BACKEND.mistakes()
        return attempts, mistakes, None
    except Exception as exc:  # noqa: BLE001
        return [], [], exc


ATTEMPTS, MISTAKES, LOAD_ERROR = load_history()


def today_str() -> str:
    return datetime.now(progress.TZ).date().isoformat()


def pct(x: float) -> str:
    return f"{x * 100:.0f}%"


# ------------------------------------------------------------------ navigare
def go_to(page: str, **state):
    st.session_state["nav"] = page
    for k, v in state.items():
        st.session_state[k] = v


st.session_state.setdefault("nav", PAGES[0])
page = st.sidebar.radio("Navigare", PAGES, key="nav")
st.sidebar.markdown("---")
st.sidebar.caption("spor la învățare gang!!")


# ------------------------------------------------------------------ cont și sincronizare
def sidebar_account():
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Contul tău**")
    if CFG is None:
        st.sidebar.caption("Progresul se salvează local pe acest calculator (SQLite). Salvarea online cu Google "
                           "devine disponibilă după configurarea Supabase (vezi README).")
        return
    if BACKEND.kind == "supabase":
        user = BACKEND.user
        st.sidebar.success(f"Conectată ca {user.get('name') or user.get('email')}")
        st.sidebar.caption(user.get("email") or "")
        if st.sidebar.button("Deconectare", key="logout_btn"):
            auth.logout(CFG)
            st.rerun()
        local_import_box()
    else:
        st.sidebar.info("Nu ești conectată. Poți exersa, dar răspunsurile se păstrează doar până închizi pagina.")
        try:
            url = auth.google_login_url(CFG)
            st.sidebar.markdown(f'<a class="google-btn" href="{url}" target="_top">Conectează-te cu Google</a>',
                                unsafe_allow_html=True)
            st.sidebar.caption("Te conectezi pe pagina Google. Aplicația nu vede și nu salvează parola ta.")
        except Exception:  # noqa: BLE001
            st.sidebar.error("Conectarea cu Google nu poate fi pregătită acum. Verifică adresa și cheia Supabase.")


def local_import_box():
    """Import local → online NUMAI la cererea explicită; datele locale nu sunt șterse."""
    path = database.db_path()
    if not path.exists():
        return
    try:
        database.init_db()
        rows = database.get_attempts()
    except Exception:  # noqa: BLE001
        return
    if not rows:
        return
    with st.sidebar.expander(f"Progres local găsit ({len(rows)} încercări)"):
        st.caption("Pe acest calculator există progres salvat local. Îl poți copia în contul tău online. "
                   "Datele locale rămân neatinse, iar importul repetat nu creează dubluri.")
        ok = st.checkbox("Confirm că progresul local îmi aparține și vreau să îl adaug în acest cont.", key="imp_ok")
        if st.button("Importă progresul local", key="imp_btn", disabled=not ok):
            try:
                n = BACKEND.import_local(rows, database.install_id())
                st.success(f"Am importat {n} încercări noi." if n else "Totul era deja importat.")
            except Exception:  # noqa: BLE001
                st.error("Importul nu a reușit. Verifică dacă schema Supabase este actualizată (supabase_schema.sql).")


sidebar_account()
notice = auth.pop_notice()
if notice:
    getattr(st, notice[0])(notice[1])
if LOAD_ERROR is not None:
    st.error("Istoricul nu a putut fi citit. Dacă folosești salvarea online, verifică conexiunea și dacă ai rulat "
             "supabase_schema.sql în proiectul Supabase. Poți continua să exersezi.")
if BACKEND.kind == "guest":
    st.caption("🔒 Mod vizitator: conectează-te cu Google din meniul lateral pentru a-ți păstra progresul online.")


# ------------------------------------------------------------------ componente comune
def option_by_letter(q, letter):
    return next((o for o in q["options"] if o.startswith(letter + ".")), letter)


def show_feedback(q, choice, correct):
    if correct:
        st.success(f"Corect! {q['answer']}")
    else:
        st.error(f"Ai ales {choice}. Răspunsul corect este {q['answer']}.")
        why = q["option_explanations"].get(choice[0])
        if why:
            st.markdown(f"**De ce varianta {choice[0]} nu este corectă:** {why}")
    st.markdown("**Explicația răspunsului corect**")
    st.markdown(q["explanation"])
    with st.expander("Explicațiile variantelor greșite"):
        for letter, reason in q["option_explanations"].items():
            st.markdown(f"**{option_by_letter(q, letter)}** — {reason}")


def _reset_question(key):
    st.session_state.pop(f"res_{key}", None)
    st.session_state.pop(f"choice_{key}", None)


def render_question(q, key, source="test", show_meta=True):
    res_key = f"res_{key}"
    result = st.session_state.get(res_key)
    if show_meta:
        st.markdown(f'<span class="pill">{q["level"]}</span><span class="pill">{q["type"]}</span>'
                    f'<span class="small-note">Lecția {q["lesson"]} · {q["topic"]}</span>', unsafe_allow_html=True)
    st.markdown(f"**{q['question']}**")
    choice = st.radio("Alege o variantă:", q["options"], key=f"choice_{key}", index=None,
                      disabled=result is not None, label_visibility="collapsed")
    if result is None:
        if st.button("Verifică", key=f"check_{key}"):
            if choice is None:
                st.warning("Selectează o variantă înainte de verificare.")
            else:
                correct = choice == q["answer"]
                try:
                    BACKEND.save_answer(q, choice, correct, source)
                    saved = True
                except Exception:  # noqa: BLE001
                    saved = False
                st.session_state[res_key] = {"choice": choice, "correct": correct, "saved": saved}
                st.rerun()
        return None
    show_feedback(q, result["choice"], result["correct"])
    if not result["saved"]:
        st.warning("Răspunsul a fost verificat, dar NU a putut fi salvat în istoric (problemă de conexiune).")
    st.button("Încearcă din nou", key=f"again_{key}", on_click=_reset_question, args=(key,))
    return result


_HEADING = re.compile(r"^(#{2,5}) ", re.M)


def demote(md: str) -> str:
    """Titlurile din lecții coboară un nivel, ca titlul lecției să rămână cel mai mare."""
    return _HEADING.sub(lambda m: "#" + m.group(1) + " ", md)


def render_lesson(domain, lesson):
    st.subheader(lesson["title"])
    st.caption(f"Nivel: {lesson['level']} · Programă: {lesson['official']}")
    if lesson["objectives"]:
        with st.container(border=True):
            st.markdown("**Obiectivele lecției**")
            for item in lesson["objectives"]:
                st.markdown(f"- {item}")
    st.markdown(demote(lesson["body"]))
    if lesson.get("worked_examples"):
        st.markdown("### Exemple rezolvate pas cu pas" if "Exemple rezolvate" not in lesson["body"]
                    else "### Exemple rezolvate suplimentare")
        st.markdown(demote(lesson["worked_examples"]))
    if lesson["mistakes"]:
        st.markdown("### Greșeli frecvente și cum le eviți")
        for item in lesson["mistakes"]:
            st.markdown(f"- {item}")
    with st.expander("Ideile esențiale ale lecției", expanded=True):
        for item in lesson["takeaways"]:
            st.markdown(f"- {item}")
    if lesson["connections"]:
        st.markdown("**Legături cu alte lecții**")
        for item in lesson["connections"]:
            st.markdown(f"- {item}")


def domain_coverage(domain):
    qs = {q["id"] for q in ALL_QUESTIONS if q["domain"] == domain}
    done = {a["question_id"] for a in ATTEMPTS if a["question_id"] in qs}
    return len(done), len(qs)


# ------------------------------------------------------------------ pagini
def page_home():
    st.markdown('<div class="hero"><div class="eyebrow">PLATFORMĂ INDEPENDENTĂ DE PREGĂTIRE LA CHIMIE</div>'
                '<h1>LABORATORUL OFICIAL AL DOMNITORULUI LUCIAN BLAGA</h1>'
                '<p>Chimia nu se învață singură. Din păcate.</p>'
                '<span class="gang">spor la învățare gang!!</span></div>', unsafe_allow_html=True)
    st.subheader("Pregătire pentru Concursul profesional de chimie „Candin Liteanu”")
    st.write("Materia este organizată după cele șapte domenii din tematica publicată pentru ediția 2026. "
             "Fiecare lecție are teorie explicată, exemple rezolvate și întrebări de antrenament cu explicații.")
    s = progress.summary(ATTEMPTS)
    a, b, c = st.columns(3)
    a.metric("Întrebări rezolvate", s["total"])
    b.metric("Răspunsuri corecte", s["correct"])
    c.metric("De recapitulat", len(progress.open_mistakes(MISTAKES)))
    st.subheader("Cele 7 domenii")
    for i, domain in enumerate(DOMAIN_ORDER, 1):
        done, total = domain_coverage(domain)
        st.markdown(f"**{i}. {domain}** · {len(CHAPTERS[domain])} lecții · {total} întrebări · "
                    f"ai încercat {done} din {total}")
    st.caption("Întrebările sunt materiale originale de antrenament, nu subiecte oficiale. Aplicația este un proiect "
               "independent și nu este afiliată Universității Babeș-Bolyai. Verifică programa oficială a ediției "
               "la care participi (programa 2027 trebuie reverificată la publicare).")


def page_curriculum():
    st.title("Programa de pregătire")
    st.caption("Structurată pe baza tematicii Candin Liteanu publicate pentru ediția 2026. Lista de subteme este o "
               "dezvoltare didactică pentru recapitulare, nu o citare integrală a programei oficiale.")
    for domain in DOMAIN_ORDER:
        with st.expander(f"{domain} · {len(CURRICULUM[domain])} subteme · {len(CHAPTERS[domain])} lecții"):
            for topic in CURRICULUM[domain]:
                st.markdown(f"- {topic}")
            st.markdown("**Lecțiile din aplicație:** " + "; ".join(l["title"] for l in CHAPTERS[domain]))


def _on_study_domain_change():
    st.session_state.pop("study_lesson", None)


def page_study():
    st.title("Material de studiu")
    domain = st.selectbox("Alege capitolul", DOMAIN_ORDER, key="study_domain", on_change=_on_study_domain_change)
    lessons = CHAPTERS[domain]
    titles = [l["title"] for l in lessons]
    if st.session_state.get("study_lesson") not in titles:
        st.session_state["study_lesson"] = titles[0]
    selected = st.selectbox("Alege lecția", titles, key="study_lesson")
    lesson = lessons[titles.index(selected)]
    render_lesson(domain, lesson)
    related = questions_for(domain, lesson["number"])
    st.markdown("---")
    st.subheader("Exersează lecția")
    st.write(f"În banca de antrenament sunt {len(related)} întrebări pentru lecția {lesson['number']}.")
    st.button("Rezolvă întrebările acestei lecții", key="to_tests", on_click=go_to,
              args=("Teste pe domenii",), kwargs={"test_domain": domain, "test_lesson": lesson["title"]})


def _on_test_domain_change():
    st.session_state["test_lesson"] = ALL_LESSONS


def page_tests():
    st.title("Teste pe domenii")
    domain = st.selectbox("Alege domeniul", DOMAIN_ORDER, key="test_domain", on_change=_on_test_domain_change)
    lesson_options = [ALL_LESSONS] + [l["title"] for l in CHAPTERS[domain]]
    if st.session_state.get("test_lesson") not in lesson_options:
        st.session_state["test_lesson"] = ALL_LESSONS
    col1, col2 = st.columns([3, 2])
    lesson_choice = col1.selectbox("Lecția", lesson_options, key="test_lesson")
    levels = sorted({q["level"] for q in questions_for(domain)})
    level_choice = col2.multiselect("Nivel", levels, default=levels, key=f"test_levels_{domain}")
    lesson_no = None if lesson_choice == ALL_LESSONS else lesson_choice.split(". ")[0]
    qs = [q for q in questions_for(domain, lesson_no) if q["level"] in level_choice]
    answered = {a["question_id"] for a in ATTEMPTS}
    st.caption(f"{len(qs)} întrebări · ai încercat deja {sum(q['id'] in answered for q in qs)} dintre ele. "
               "Fiecare verificare se salvează ca o încercare nouă în istoric.")
    if not qs:
        st.info("Nu există întrebări pentru filtrele alese.")
    for i, q in enumerate(qs, 1):
        with st.container(border=True):
            st.markdown(f"**Întrebarea {i}**")
            render_question(q, key=f"t_{q['id']}", source="test")


def page_mistakes():
    st.title("Urmărirea greșelilor")
    if not MISTAKES:
        st.success("Nu ai greșeli salvate momentan. Greșelile din teste și din provocarea zilei apar aici automat.")
        return
    open_m = progress.open_mistakes(MISTAKES)
    a, b, c = st.columns(3)
    a.metric("De recapitulat", len(open_m))
    b.metric("Recuperate", len(MISTAKES) - len(open_m), help="Întrebări greșite anterior, la care ultima încercare a fost corectă.")
    c.metric("Întrebări greșite cel puțin o dată", len(MISTAKES))

    if open_m:
        st.subheader("Subiecte care necesită recapitulare")
        groups = Counter((m["domain"], m.get("lesson")) for m in open_m)
        for (domain, lesson_no), n in groups.most_common():
            lesson = LESSONS_BY_KEY.get((domain, lesson_no or ""))
            cols = st.columns([4, 1])
            cols[0].markdown(f"**{domain}** · {lesson_title(domain, lesson_no)} — {n} "
                             f"{'întrebare' if n == 1 else 'întrebări'} de reluat")
            if lesson:
                cols[1].button("Recitește lecția", key=f"rev_{domain}_{lesson_no}", on_click=go_to,
                               args=("Material de studiu",),
                               kwargs={"study_domain": domain, "study_lesson": lesson["title"]})

    st.subheader("Lista greșelilor")
    f1, f2 = st.columns(2)
    status = f1.radio("Arată", ["De recapitulat", "Recuperate", "Toate"], horizontal=True, key="mist_status")
    domains = sorted({m["domain"] for m in MISTAKES}, key=lambda d: DOMAIN_ORDER.index(d) if d in DOMAIN_ORDER else 99)
    dom_filter = f2.selectbox("Domeniu", ["Toate domeniile"] + domains, key="mist_domain")
    items = {"De recapitulat": open_m, "Recuperate": [m for m in MISTAKES if m["last_correct"]],
             "Toate": MISTAKES}[status]
    if dom_filter != "Toate domeniile":
        items = [m for m in items if m["domain"] == dom_filter]
    if not items:
        st.info("Nicio greșeală pentru filtrele alese.")
    history = defaultdict(list)
    for att in ATTEMPTS:
        history[att["question_id"]].append(att)
    for m in items:
        q = resolve_question(m["question_id"], m.get("question"))
        with st.container(border=True):
            st.caption(f"{m['domain']} · {lesson_title(m['domain'], m.get('lesson') or (q or {}).get('lesson'))} · {m.get('topic') or ''}")
            st.markdown(f"**{q['question'] if q else m.get('question')}**")
            state = "✅ recuperată (ultima încercare corectă)" if m["last_correct"] else "❗ de recapitulat"
            st.write(f"Ultimul răspuns greșit: **{m['chosen']}** · {progress.fmt_ts(m['latest'])}")
            st.write(f"Încercări: {m['attempts']} · greșite: {m['wrong_count']} · stare: {state}")
            with st.expander("Istoricul încercărilor"):
                for att in reversed(history.get(m["question_id"], [])):
                    mark = "✅" if att["correct"] else "❌"
                    st.markdown(f"{mark} {progress.fmt_ts(att['created_at'])} — {att['chosen']} "
                                f"<span class='small-note'>({SOURCE_LABELS.get(att.get('source'), 'Test')})</span>",
                                unsafe_allow_html=True)
            if q and q["id"] in {x["id"] for x in ALL_QUESTIONS}:
                with st.expander("Reia întrebarea", expanded=False):
                    render_question(q, key=f"m_{q['id']}", source="mistake_retry", show_meta=False)
            else:
                st.caption(f"Întrebare demonstrativă veche, care nu mai face parte din bancă. Răspuns corect: {m.get('answer')}")


def page_dashboard():
    st.title("Panou de progres")
    s = progress.summary(ATTEMPTS)
    if not s["total"]:
        st.info("Încă nu există încercări. Statisticile apar după primele răspunsuri verificate.")
        return
    a, b, c, d = st.columns(4)
    a.metric("Încercări", s["total"])
    b.metric("Corecte", s["correct"])
    c.metric("Greșite", s["wrong"])
    d.metric("Procent corecte", pct(s["rate"]))
    st.progress(s["distinct_questions"] / len(ALL_QUESTIONS),
                text=f"Acoperire: ai încercat {s['distinct_questions']} din {len(ALL_QUESTIONS)} întrebări distincte")

    st.subheader("Evoluția în timp")
    tl = pd.DataFrame(progress.timeline(ATTEMPTS))
    tl["Zi"] = pd.to_datetime(tl["day"])
    rates = pd.concat([
        pd.DataFrame({"Zi": tl["Zi"], "Procent": tl["rate"] * 100, "Serie": "Procent zilnic"}),
        pd.DataFrame({"Zi": tl["Zi"], "Procent": tl["cumulative_rate"] * 100, "Serie": "Procent cumulat"}),
    ])
    line = (alt.Chart(rates).mark_line(point=True)
            .encode(x=alt.X("Zi:T", title="Ziua", axis=alt.Axis(format="%d.%m")),
                    y=alt.Y("Procent:Q", title="% răspunsuri corecte", scale=alt.Scale(domain=[0, 100])),
                    color=alt.Color("Serie:N", title=None,
                                    scale=alt.Scale(range=["#1f5fa8", "#176b45"]),
                                    legend=alt.Legend(orient="bottom")),
                    tooltip=[alt.Tooltip("Zi:T", format="%d.%m.%Y"), "Serie:N", alt.Tooltip("Procent:Q", format=".0f")])
            .properties(height=260))
    st.altair_chart(line, width="stretch")
    counts = pd.concat([
        pd.DataFrame({"Zi": tl["Zi"], "Încercări": tl["correct"], "Rezultat": "Corecte"}),
        pd.DataFrame({"Zi": tl["Zi"], "Încercări": tl["total"] - tl["correct"], "Rezultat": "Greșite"}),
    ])
    bars = (alt.Chart(counts).mark_bar(size=18)
            .encode(x=alt.X("Zi:T", title="Ziua", axis=alt.Axis(format="%d.%m")),
                    y=alt.Y("Încercări:Q", title="Încercări pe zi", stack=True),
                    color=alt.Color("Rezultat:N", title=None, scale=alt.Scale(domain=["Corecte", "Greșite"],
                                    range=["#176b45", "#d9534f"]), legend=alt.Legend(orient="bottom")),
                    tooltip=[alt.Tooltip("Zi:T", format="%d.%m.%Y"), "Rezultat:N", "Încercări:Q"])
            .properties(height=220))
    st.altair_chart(bars, width="stretch")

    st.subheader("Performanța pe domenii")
    for row in progress.by_domain(ATTEMPTS, DOMAIN_ORDER):
        done, total_q = domain_coverage(row["domain"])
        if row["total"]:
            st.markdown(f"**{row['domain']}** — {row['correct']} corecte din {row['total']} încercări "
                        f"({pct(row['rate'])}) · întrebări încercate: {done}/{total_q}")
            st.progress(row["rate"])
        else:
            st.markdown(f"**{row['domain']}** — încă neînceput · {total_q} întrebări disponibile")

    sw = progress.strengths_and_weaknesses(ATTEMPTS, DOMAIN_ORDER, MISTAKES)
    left, right = st.columns(2)
    with left:
        st.subheader("Puncte forte")
        if sw["strong"]:
            for d in sw["strong"]:
                st.markdown(f"- **{d['domain']}** – {pct(d['rate'])} din {d['total']} încercări")
        else:
            st.caption(f"Un domeniu devine punct forte la cel puțin {progress.MIN_ATTEMPTS_FOR_VERDICT} încercări "
                       f"și minimum {pct(progress.STRONG_THRESHOLD)} răspunsuri corecte.")
    with right:
        st.subheader("Necesită mai multă atenție")
        shown = False
        for d in sw["weak"]:
            shown = True
            st.markdown(f"- **{d['domain']}** – {pct(d['rate'])} din {d['total']} încercări")
        for l in sw["weak_lessons"][:8]:
            shown = True
            st.markdown(f"- {lesson_title(l['domain'], l['lesson'])} – {pct(l['rate'])} din {l['total']} încercări"
                        + (f", {l['open_mistakes']} greșeli nerecuperate" if l["open_mistakes"] else ""))
        if not shown:
            st.caption("Nicio zonă slabă detectată din datele de până acum.")
        if sw["untouched"]:
            st.caption("Domenii neîncepute: " + ", ".join(d["domain"] for d in sw["untouched"]))

    with st.expander("Rezultate pe lecții"):
        rows = [{"Domeniu": l["domain"], "Lecție": lesson_title(l["domain"], l["lesson"]), "Încercări": l["total"],
                 "Corecte": l["correct"], "Procent": f"{l['rate'] * 100:.0f}%"} for l in progress.by_lesson(ATTEMPTS)]
        st.dataframe(pd.DataFrame(rows), hide_index=True, width="stretch")
    with st.expander("Încercări după sursă"):
        src = Counter(SOURCE_LABELS.get(a.get("source"), "Teste pe domenii") for a in ATTEMPTS)
        for k, v in src.items():
            st.markdown(f"- {k}: {v}")


def daily_question(user_key: str, day: str) -> dict:
    """Aceeași întrebare pentru aceeași utilizatoare pe tot parcursul zilei (ora României)."""
    ordered = sorted(ALL_QUESTIONS, key=lambda q: q["id"])
    digest = hashlib.sha256(f"{user_key}|{day}".encode()).hexdigest()
    return ordered[int(digest, 16) % len(ordered)]


def page_daily():
    st.title("Provocarea zilei")
    day = today_str()
    try:
        existing = BACKEND.daily_get(day)
    except Exception:  # noqa: BLE001
        existing = None
        st.warning("Nu am putut verifica dacă ai rezolvat deja provocarea de azi.")
    q = resolve_question(existing["question_id"]) if existing else daily_question(BACKEND.user_key, day)
    q = q or daily_question(BACKEND.user_key, day)
    st.caption(f"{datetime.now(progress.TZ).strftime('%d.%m.%Y')} · {q['domain']} · "
               f"{lesson_title(q['domain'], q['lesson'])}")
    if existing:
        st.markdown(f"**{q['question']}**")
        for opt in q["options"]:
            st.markdown(f"- {opt}")
        st.info("Ai rezolvat deja provocarea de azi. Rezultatul a fost salvat o singură dată; revino mâine pentru una nouă.")
        show_feedback(q, existing["chosen"], bool(existing["correct"]))
    else:
        st.markdown(f"**{q['question']}**")
        choice = st.radio("Alege o variantă:", q["options"], key=f"daily_choice_{day}", index=None,
                          label_visibility="collapsed")
        if st.button("Verifică provocarea", key="daily_check"):
            if choice is None:
                st.warning("Alege un răspuns.")
            else:
                try:
                    BACKEND.daily_save(day, q, choice, choice == q["answer"])
                except Exception:  # noqa: BLE001
                    st.error("Răspunsul nu a putut fi salvat. Încearcă din nou.")
                    return
                st.rerun()
    daily = [a for a in ATTEMPTS if a.get("source") == "daily"]
    if daily:
        st.markdown("---")
        ok = sum(a["correct"] for a in daily)
        st.caption(f"Provocări rezolvate: {len(daily)} · corecte: {ok}")


{"Acasă": page_home, "Programa concursului": page_curriculum, "Material de studiu": page_study,
 "Teste pe domenii": page_tests, "Urmărirea greșelilor": page_mistakes, "Panou de progres": page_dashboard,
 "Provocarea zilei": page_daily}[page]()

st.sidebar.markdown("---")
st.sidebar.caption(f"Versiunea {APP_VERSION} · toate cele 7 domenii · {sum(len(v) for v in CHAPTERS.values())} lecții · "
                   f"{len(ALL_QUESTIONS)} întrebări · {BACKEND.label}.")
st.sidebar.caption("Proiect independent de pregătire, neafiliat UBB. Întrebările sunt originale, nu subiecte oficiale.")
