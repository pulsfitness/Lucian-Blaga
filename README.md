# LABORATORUL OFICIAL AL DOMNITORULUI LUCIAN BLAGA — versiunea 7

> spor la învățare gang!!  
> Chimia nu se învață singură. Din păcate.

Platformă **independentă** de pregătire (Python + Streamlit) pentru o elevă de clasa a XII-a care participă
la Concursul profesional de chimie „Candin Liteanu”, organizat de Facultatea de Chimie și Inginerie Chimică
a UBB Cluj-Napoca. **Aplicația nu este oficială și nu este afiliată UBB**; „oficial” face parte doar din numele
de brand. Întrebările sunt materiale **originale de antrenament**, nu subiecte oficiale.

Programa de referință este cea publicată pentru **ediția 2026**. Când apare programa ediției 2027, trebuie
verificată din nou (domeniile, formatul cu 5 variante A–E și regula variantei E).

## Ce conține versiunea 7

| Domeniu | Modul | Lecții | Întrebări |
|---|---|---:|---:|
| 1. Structura atomului | `chapter1.py` | 8 | 24 |
| 2. Legături chimice | `chapter2.py` | 9 | 28 |
| 3. Soluții | `chapter3.py` | 8 | 30 |
| 4. Legile gazelor | `chapter4.py` | 8 | 30 |
| 5. Procese de oxidare și reducere | `chapter5.py` | 10 | 30 |
| 6. Introducere în chimia organică | `chapter6.py` | 10 | 31 |
| 7. Hidrocarburi | `chapter7.py` | 11 | 33 |
| **Total** | | **64** | **206** |

Fiecare lecție afișează: titlu și nivel, obiective, explicație teoretică, definiții, formule cu explicarea
simbolurilor, exemple rezolvate pas cu pas, interpretarea rezultatelor, greșeli frecvente, idei esențiale și
legături cu alte lecții. Pentru capitolele 1–4 (scrise în versiunile anterioare) obiectivele, greșelile
frecvente, legăturile și, unde lipseau, exemplele rezolvate suplimentare sunt în `lesson_extras.py`, fără a
rescrie lecțiile originale.

Fiecare întrebare are: ID unic, domeniu, subiect, lecția asociată (format `"<capitol>.<lecție>"`, de ex. `5.7`),
nivel, tip (teorie / calcul / interpretare / aplicație), cinci variante A–E (E = „Niciuna dintre variantele
A–D”), răspunsul corect, explicația detaliată și explicația fiecărei variante greșite.

### Paginile aplicației
- **Acasă**, **Programa concursului**, **Material de studiu** (cu buton „Rezolvă întrebările acestei lecții”).
- **Teste pe domenii** – filtrare pe domeniu, lecție și nivel; după verificare apar explicația răspunsului corect,
  motivul pentru care varianta aleasă e greșită și, la cerere, explicațiile tuturor distractorilor.
- **Urmărirea greșelilor** – greșelile se salvează automat; pentru fiecare întrebare: ultimul răspuns greșit și
  data lui, numărul de încercări, istoricul complet, starea (de recapitulat / recuperată), reluarea întrebării cu
  verificare și explicații, plus lista lecțiilor care necesită recapitulare (cu link spre lecție).
- **Panou de progres** – total încercări, corecte, greșite, procent, acoperirea băncii, evoluția zilnică și
  cumulată, performanța pe fiecare domeniu, puncte forte, domenii și lecții care necesită atenție, rezultate pe
  lecții. Totul se calculează din istoricul real.
- **Provocarea zilei** – o întrebare pe zi (ora României), aceeași pentru aceeași utilizatoare pe toată ziua;
  rezultatul se salvează **o singură dată** (reîncărcarea paginii, dublul clic sau un alt dispozitiv nu creează
  rezultate duplicate) și intră în istoricul de progres.

## Structura proiectului

```
app.py                 interfața și navigarea
question_bank.py       sursa unică a lecțiilor și întrebărilor (normalizare, validare)
chapter1.py … chapter7.py   conținutul pe domenii
lesson_extras.py       obiective / greșeli frecvente / legături pentru capitolele 1–4
content.py             programa pe 7 domenii + întrebările demonstrative vechi (NU mai intră în bancă)
progress.py            calculul statisticilor din istoric
database.py            salvarea locală SQLite (data/laborator.db)
storage.py             alegerea salvării: locală, online (Supabase) sau vizitator
auth.py                autentificarea Google prin Supabase Auth (PKCE)
supabase_schema.sql    schema bazei de date online, cu Row Level Security
.streamlit/config.toml tema verde / alb / albastru
.streamlit/secrets.toml.example  model pentru secrete
tests/                 teste automate (pytest)
tools/                 verificatoare pentru capitole și ecuații
```

## Pornire locală

1. Instalează Python 3.10 sau mai nou.
2. În folderul proiectului:
   ```bash
   python -m venv .venv
   # Windows:  .venv\Scripts\activate
   # macOS/Linux:  source .venv/bin/activate
   pip install -r requirements.txt
   streamlit run app.py
   ```
3. Se deschide `http://localhost:8501`.

Fără secrete Supabase, aplicația funcționează **local**: progresul se salvează în `data/laborator.db`.
Fișierul nu este inclus în arhivă; dacă există deja (de la o versiune anterioară), **nu este suprascris și nu
este șters** – la pornire se adaugă doar tabelele și coloanele noi (migrare fără pierderi). Poți forța modul
local chiar dacă ai configurat Supabase cu variabila de mediu `LAB_STORAGE=local`.

### Teste
```bash
pip install -r requirements-dev.txt
python -m pytest -q
```
Testele verifică banca de întrebări (ID-uri unice, 5 variante, răspuns existent, explicații complete, asocierea
cu lecțiile, fără duplicate), salvarea și migrarea SQLite, interogarea ultimei greșeli, statisticile, deschiderea
tuturor paginilor și a tuturor celor 64 de lecții, salvarea răspunsurilor, reluarea greșelilor, provocarea zilei
la reîncărcare și fluxul de autentificare (URL Google cu PKCE, erori clare, expirarea sesiunii).

## Salvare online cu Google (Supabase)

### 1. Proiectul Supabase
1. Creează un proiect pe [supabase.com](https://supabase.com).
2. **SQL Editor** → lipește tot conținutul din `supabase_schema.sql` → **Run**. Fișierul poate fi rulat din nou
   oricând (completează schema fără să șteargă date).
3. **Project Settings → API Keys**: notează *Project URL* și cheia **publică** (`anon` sau `sb_publishable_…`).
   Nu pune niciodată cheia `service_role` / secretă în aplicație.

### 2. Google OAuth
1. [Google Cloud Console](https://console.cloud.google.com) → APIs & Services → **OAuth consent screen**:
   tip *External*, numele aplicației, e-mailul de contact. Cât timp aplicația este în modul *Testing*, adaugă
   adresa Gmail a elevei la *Test users* (sau publică ecranul de consimțământ).
2. **Credentials → Create credentials → OAuth client ID → Web application**.
   La *Authorized redirect URIs* adaugă exact: `https://ID-PROIECT.supabase.co/auth/v1/callback`.
3. Copiază *Client ID* și *Client secret* în Supabase → **Authentication → Sign In / Providers → Google**
   și activează providerul. (Client secret-ul Google stă doar în Supabase, nu în aplicație.)

### 3. Adresele de întoarcere
Supabase → **Authentication → URL Configuration**:
- *Site URL*: adresa publică a aplicației, de ex. `https://laborator-chimie.streamlit.app`;
- *Redirect URLs*: adaugă `http://localhost:8501/**` și `https://laborator-chimie.streamlit.app/**`.

### 4. Secretele aplicației
Local: copiază `.streamlit/secrets.toml.example` ca `.streamlit/secrets.toml` și completează-l.
Alternativ, variabile de mediu: `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `APP_URL`.
`.streamlit/secrets.toml` este în `.gitignore` – nu îl urca pe GitHub.

### Cum funcționează
- Butonul „Conectează-te cu Google” duce la pagina Google; **parola nu ajunge niciodată la aplicație** și nu
  este cerută sau salvată.
- Fluxul este OAuth cu PKCE: verificatorul rămâne pe server, e valabil 10 minute și se folosește o singură dată.
- Fiecare rând din `answers` și `daily_challenges` are `user_id` = UUID-ul contului; **Row Level Security**
  permite fiecărei utilizatoare să citească și să adauge **doar propriile rânduri**. Rolul anonim nu are acces.
  Istoricul nu poate fi modificat sau șters din aplicație.
- Tokenul de acces se reîmprospătează automat; dacă sesiunea a expirat definitiv apare mesajul „Sesiunea a
  expirat. Conectează-te din nou…”. Erorile de conectare (link expirat, provider dezactivat, adresă de întoarcere
  nepermisă, conectare anulată) au mesaje clare în română.
- Fără conectare (când Supabase este configurat), aplicația rulează în **mod vizitator**: se poate exersa, dar
  răspunsurile se păstrează doar până la închiderea paginii.
- Sesiunea este păstrată în pagina deschisă; după o reîncărcare completă a paginii din browser poate fi nevoie de
  o nouă conectare.

### Progresul local existent → contul online
Nu se încarcă nimic automat. Când ești conectată și pe același calculator există `data/laborator.db` cu
încercări, în meniul lateral apare „Progres local găsit”. Importul pornește **doar** după bifarea confirmării și
apăsarea butonului; rândurile sunt **copiate** (datele locale rămân neatinse), iar fiecare primește un
identificator unic (`client_ref`), deci reimportul nu creează dubluri.

## Publicare pe Streamlit Community Cloud
1. Urcă proiectul într-un depozit GitHub (fără `.streamlit/secrets.toml` și fără `data/*.db`).
2. [share.streamlit.io](https://share.streamlit.io) → **Create app** → alege depozitul, ramura și fișierul
   principal `app.py`; în *Advanced settings* alege Python 3.11 sau mai nou.
3. **Advanced settings → Secrets**: lipește conținutul din `secrets.toml`, cu
   `redirect_url = "https://NUME.streamlit.app"`.
4. Adaugă aceeași adresă la *Redirect URLs* în Supabase (pasul 3 de mai sus).
5. Pe Community Cloud fișierele locale nu sunt permanente, deci progresul trebuie salvat online (Supabase).

**Limite:** planurile gratuite Streamlit Community Cloud și Supabase au limite (resurse, inactivitate –
aplicațiile/proiectele nefolosite pot fi puse în pauză –, număr de utilizatori, spațiu) și politici care se pot
schimba. Verifică periodic condițiile actuale ale fiecărui serviciu; nu există garanția funcționării gratuite
nelimitate.

## Verificări efectuate pentru versiunea 7
- Toate fișierele Python se compilează; aplicația pornește fără erori; 30 de teste automate trec.
- Toate cele 7 domenii, 64 de lecții și 206 întrebări sunt disponibile; validatorul băncii nu raportează probleme.
- Ecuațiile din capitolele 5–7 au fost verificate pentru conservarea atomilor, a sarcinii și a electronilor, iar
  calculele au fost refăcute numeric; capitolele 1–4 au fost auditate, cu corecturi minime de precizie.
- Schema Supabase a fost testată pe PostgreSQL 17 cu un mediu care imită Supabase (roluri `anon` /
  `authenticated`, `auth.uid()`): o utilizatoare nu poate citi sau scrie datele alteia, rolul anonim este refuzat,
  provocarea zilei se înregistrează o singură dată, importul nu dublează rândurile, datele din schema v6 se păstrează.
- Conectarea reală cu Google trebuie testată în proiectul Supabase propriu, după pașii de mai sus (necesită
  conturile și cheile tale).

Pentru capitole noi: `python tools/validate_chapter.py chapterN.py` verifică structura lecțiilor și a întrebărilor, iar `python tools/balance_check.py "2H2 + O2 -> 2H2O"` verifică egalarea ecuațiilor (atomi și sarcină).

Istoricul versiunilor: vezi `CHANGELOG.md`.
