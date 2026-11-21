# Istoricul versiunilor

## Versiunea 7 – toate cele 7 domenii, Google + Supabase
- Capitole noi: 5 „Procese de oxidare și reducere” (10 lecții, 30 întrebări), 6 „Introducere în chimia organică”
  (10 lecții, 31 întrebări), 7 „Hidrocarburi” (11 lecții, 33 întrebări), cu structura pedagogică unitară.
- Capitolele 1–4 păstrate; adăugate obiective, greșeli frecvente, legături și exemple rezolvate suplimentare
  (`lesson_extras.py`); câteva corecturi minime de precizie științifică.
- Sursă unică pentru întrebări (`question_bank.py`); întrebările demonstrative vechi din `content.py` (inclusiv
  cele două REDOX) nu mai apar în bancă, deci nu există dubluri.
- Formulele `\[ \]` / `\( \)` din capitolele 1–4 sunt afișate corect (conversie automată pentru Streamlit).
- Urmărirea greșelilor finalizată: reluare, verificare, istoric, stare recuperată / de recapitulat, lecții de recapitulat.
- Panou de progres complet: evoluție în timp, domenii, lecții, puncte forte și zone slabe, acoperire.
- Provocarea zilei stabilă pe utilizatoare și zi, salvată o singură dată.
- `get_mistakes()` selectează explicit ultima încercare greșită; istoricul nu se șterge; migrare SQLite fără pierderi.
- Autentificare Google prin Supabase Auth (PKCE), salvare online cu RLS, mod vizitator, import local opțional.
- Teste automate (`tests/`), documentație actualizată.

## Versiunea 6 – Capitolul 4: Legile gazelor
8 lecții și 30 de întrebări originale.

## Versiunea 5 – Capitolul 3: Soluții
8 lecții și 30 de întrebări cu explicații pentru distractori.

## Versiunea 4 – Capitolul 2: Legături chimice
9 lecții și 28 de întrebări.

## Versiunea 3 – Capitolul 1: Structura atomului
Pagina „Material de studiu”, 8 lecții și 24 de întrebări.

## Versiunea 2
Programa pe 7 domenii, întrebări demonstrative, urmărirea greșelilor, panou de progres, provocarea zilei, salvare SQLite.
