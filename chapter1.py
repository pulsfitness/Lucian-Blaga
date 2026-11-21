"""Material didactic pentru Capitolul 1 – Structura atomului.

Materialul este redactat pentru pregătirea concursului Candin Liteanu.
Programa oficială 2026 menționează configurații electronice, poziția în
sistemul periodic și proprietăți periodice. Unele lecții de bază sunt
incluse ca prerechizite necesare.
"""

CHAPTERS = {
    "Structura atomului": [
        {
            "id": "atom_lesson_01",
            "title": "1.1. Alcătuirea atomului și particulele subatomice",
            "level": "Fundamente",
            "official": "Noțiuni introductive necesare pentru configurații electronice și proprietăți periodice",
            "body": r"""
## 1. Ce este atomul?

Atomul este cea mai mică unitate a unui element chimic care păstrează identitatea chimică a acelui element. El are un nucleu central și un înveliș electronic.

- **Nucleul** conține protoni și, cu excepția protiului (hidrogen-1), neutroni. Are sarcină electrică pozitivă, datorită protonilor.
- **Învelișul electronic** conține electroni, distribuiți în regiuni de energie din jurul nucleului.
- Aproape toată masa atomului este concentrată în nucleu. Volumul atomului este determinat în principal de învelișul electronic.

## 2. Particulele subatomice

| Particulă | Simbol | Sarcină relativă | Masă aproximativă |
|---|---:|---:|---:|
| Proton | p⁺ | +1 | 1 u |
| Neutron | n⁰ | 0 | 1 u |
| Electron | e⁻ | −1 | 1/1836 u |

Masele protonului și neutronului sunt apropiate, iar masa electronului este mult mai mică. Unitatea atomică de masă, notată u, este definită în raport cu izotopul carbon-12.

## 3. Atom neutru și ion

Un atom este **neutru** dacă numărul protonilor este egal cu numărul electronilor.

Un **ion** este o particulă cu sarcină electrică:
- **cationul** se formează prin cedare de electroni și are sarcină pozitivă;
- **anionul** se formează prin acceptare de electroni și are sarcină negativă.

Important: formarea ionilor schimbă numărul electronilor, nu numărul protonilor. Numărul protonilor identifică elementul chimic.

## 4. Metodă rapidă pentru probleme

1. Identifică numărul atomic Z: acesta este numărul protonilor.
2. Dacă particula este neutră, electronii sunt tot Z.
3. Dacă este ion pozitiv cu sarcina +k, electronii sunt Z − k.
4. Dacă este ion negativ cu sarcina −k, electronii sunt Z + k.

### Exemplu rezolvat

Pentru ionul Al³⁺, cu Z = 13:
- protoni: 13;
- sarcina +3 arată că atomul a cedat 3 electroni;
- electroni: 13 − 3 = 10.

**Atenție la confuzia frecventă:** numărul atomic nu devine 10. Aluminiul are în continuare 13 protoni; doar numărul electronilor s-a modificat.
""",
            "takeaways": [
                "Numărul protonilor identifică elementul chimic.",
                "Atomul neutru are același număr de protoni și electroni.",
                "Cationii au cedat electroni; anionii au acceptat electroni.",
                "Formarea ionilor nu schimbă nucleul."
            ]
        },
        {
            "id": "atom_lesson_02",
            "title": "1.2. Numărul atomic, numărul de masă și notația atomului",
            "level": "Fundamente",
            "official": "Prerechizit pentru identificarea elementelor și interpretarea configurațiilor",
            "body": r"""
## 1. Numărul atomic (Z)

Numărul atomic Z reprezintă numărul protonilor din nucleu. El stabilește identitatea elementului.

\[
Z = p
\]

Pentru un atom neutru:

\[
e = Z
\]

## 2. Numărul de masă (A)

Numărul de masă A este suma protonilor și neutronilor din nucleu:

\[
A = p+n = Z+n
\]

De aici:

\[
n = A-Z
\]

Numărul de masă este întotdeauna un număr întreg pentru un anumit nuclid.

## 3. Notația nucleară

Un atom se poate reprezenta astfel:

\[
{}^{A}_{Z}X
\]

unde X este simbolul chimic, A este numărul de masă, iar Z este numărul atomic.

### Exemplu rezolvat

Pentru \({}^{23}_{11}\mathrm{Na}\):
- protoni = Z = 11;
- neutroni = A − Z = 23 − 11 = 12;
- electroni = 11, dacă atomul este neutru.

Pentru \({}^{35}_{17}\mathrm{Cl}^{-}\):
- protoni = 17;
- neutroni = 35 − 17 = 18;
- electroni = 17 + 1 = 18.

## 4. Nu confunda A cu masa atomică relativă

Numărul de masă A se referă la un anumit atom/nuclid și este întreg. Masa atomică relativă a unui element din tabelul periodic este, de regulă, o medie ponderată a maselor izotopilor săi naturali și poate fi zecimală.
""",
            "takeaways": [
                "Z = numărul protonilor.",
                "A = protoni + neutroni.",
                "Neutroni = A − Z.",
                "Pentru ioni, numărul electronilor se ajustează după sarcină.",
                "Numărul de masă A nu este același lucru cu masa atomică relativă din tabel."
            ]
        },
        {
            "id": "atom_lesson_03",
            "title": "1.3. Izotopi și masa atomică relativă",
            "level": "Intermediar",
            "official": "Extindere utilă pentru înțelegerea atomilor și a maselor atomice",
            "body": r"""
## 1. Ce sunt izotopii?

Izotopii sunt atomi ai aceluiași element care au:
- același număr atomic Z, deci același număr de protoni;
- număr diferit de neutroni;
- numere de masă A diferite.

Exemplu: carbon-12 și carbon-14 au amândoi Z = 6, dar au 6, respectiv 8 neutroni.

## 2. Masa atomică relativă

Dacă un element are mai mulți izotopi, masa atomică relativă este aproximativ media ponderată a maselor izotopice în funcție de abundența lor naturală.

Pentru două izotopi, într-un model simplificat:

\[
A_r = \frac{m_1 \cdot x_1 + m_2 \cdot x_2}{100}
\]

unde \(m_1\) și \(m_2\) sunt valorile numerice ale maselor izotopice exprimate în u, \(x_1\) și \(x_2\) sunt procentele de abundență, iar \(x_1+x_2=100\).

### Exemplu rezolvat

Un element are doi izotopi cu mase aproximative 10 u și 11 u, în abundențe de 20% și 80%.

\[
A_r = \frac{10\cdot20+11\cdot80}{100}=10,8
\]

Masa atomică relativă rezultată este 10,8.

**Verificare intuitivă:** media trebuie să fie între 10 și 11 și mai aproape de 11, deoarece izotopul cu masa 11 este mult mai abundent.
""",
            "takeaways": [
                "Izotopii au același Z și A diferit.",
                "Diferența dintre izotopi este numărul neutronilor.",
                "Masa atomică relativă este o medie ponderată a izotopilor naturali.",
                "Rezultatul mediei trebuie să se afle între masele izotopilor considerați."
            ]
        },
        {
            "id": "atom_lesson_04",
            "title": "1.4. Învelișul electronic, straturi și substraturi",
            "level": "Intermediar",
            "official": "Bază pentru configurațiile electronice",
            "body": r"""
## 1. Electronii și energia

Electronii din atom nu pot avea orice energie. Ei ocupă stări energetice cuantificate. În descrierea folosită la liceu, electronii sunt repartizați în **straturi** și **substraturi**.

Straturile sunt caracterizate de numărul cuantic principal \(n=1,2,3,\ldots\), iar substraturile sunt notate s, p, d și f.

| Substrat | Număr de orbitali | Capacitate maximă |
|---|---:|---:|
| s | 1 | 2 electroni |
| p | 3 | 6 electroni |
| d | 5 | 10 electroni |
| f | 7 | 14 electroni |

Un orbital poate conține cel mult doi electroni, cu spini opuși.

## 2. Capacitatea straturilor

Capacitatea maximă teoretică a stratului cu numărul cuantic principal n este:

\[
N_{\max}=2n^2
\]

Exemple:
- stratul 1: maximum 2 electroni;
- stratul 2: maximum 8 electroni;
- stratul 3: maximum 18 electroni;
- stratul 4: maximum 32 electroni.

Această formulă indică numărul maxim de electroni permis într-un strat, nu ordinea exactă în care se ocupă substraturile.

## 3. Orbitali și reprezentări

Un orbital este o regiune descrisă de funcția de undă în care există o probabilitate mare de a găsi electronul. Nu este o orbită planetară fixă.

- orbitalii s au simetrie sferică;
- orbitalii p au două regiuni principale de probabilitate;
- orbitalii d și f au forme mai complexe.

**De reținut:** modelul cu electroni care se rotesc pe cercuri fixe în jurul nucleului este o schemă istorică simplificată, nu descrierea modernă completă.
""",
            "takeaways": [
                "Straturile sunt caracterizate de n.",
                "Substraturile sunt s, p, d și f.",
                "Capacitățile maxime sunt 2, 6, 10 și 14 electroni.",
                "Un orbital poate conține maximum doi electroni.",
                "Formula capacității maxime a stratului este 2n²."
            ]
        },
        {
            "id": "atom_lesson_05",
            "title": "1.5. Configurația electronică și regulile de ocupare",
            "level": "Concurs",
            "official": "Temă explicită în programa publicată pentru ediția 2026",
            "body": r"""
## 1. Ce reprezintă configurația electronică?

Configurația electronică arată modul în care electronii unui atom sunt distribuiți în substraturi.

Exemple:
- H: \(1s^1\)
- He: \(1s^2\)
- Li: \(1s^2 2s^1\)
- O: \(1s^2 2s^2 2p^4\)
- Ne: \(1s^2 2s^2 2p^6\)

Suma exponenților trebuie să fie egală cu numărul total de electroni ai atomului sau ionului descris.

## 2. Principiul Aufbau

Electronii ocupă mai întâi orbitalii disponibili cu energie mai mică. Ordinea uzuală de completare pentru primele elemente este:

\[
1s,\ 2s,\ 2p,\ 3s,\ 3p,\ 4s,\ 3d,\ 4p
\]

Ordinea energetică este importantă: nu se completează pur și simplu întregul strat cu n mai mic înainte de a începe următorul.

## 3. Principiul excluziunii Pauli

Într-un atom, doi electroni nu pot avea toate cele patru numere cuantice identice. Într-un orbital încap maximum doi electroni, cu spini opuși.

## 4. Regula lui Hund

În orbitalii de aceeași energie ai unui substrat (de exemplu cei trei orbitali p), electronii ocupă mai întâi orbitalii separat, cu spini paraleli, înainte de a se împerechea.

Pentru \(2p^3\), reprezentarea schematică este: ↑  ↑  ↑

Pentru \(2p^4\), este: ↑↓  ↑  ↑

## 5. Exemple rezolvate

**Azot (Z = 7):**

\[
1s^2\,2s^2\,2p^3
\]

Verificare: 2 + 2 + 3 = 7 electroni.

**Calciu (Z = 20):**

\[
1s^2\,2s^2\,2p^6\,3s^2\,3p^6\,4s^2
\]

Verificare: suma exponenților este 20.

**Notă de nivel concurs:** există configurații excepționale la unele elemente de tranziție, precum Cr și Cu, datorită apropierii energiilor unor substraturi. Pentru probleme, verifică dacă se cere configurația fundamentală și folosește datele/precizările oferite în enunț.
""",
            "takeaways": [
                "Suma exponenților configurației este numărul electronilor.",
                "Aufbau: se ocupă mai întâi orbitalii cu energie mai mică.",
                "Pauli: maximum doi electroni într-un orbital, cu spini opuși.",
                "Hund: orbitalii degenerați se ocupă întâi separat.",
                "Unele elemente de tranziție au configurații excepționale."
            ]
        },
        {
            "id": "atom_lesson_06",
            "title": "1.6. Electroni de valență și poziția în tabelul periodic",
            "level": "Concurs",
            "official": "Temă explicită în programa publicată pentru ediția 2026",
            "body": r"""
## 1. Electronii de valență

Electronii de valență sunt electronii implicați în mod obișnuit în formarea legăturilor chimice și în comportamentul chimic al elementului.

Pentru elementele reprezentative (blocurile s și p), aceștia sunt, în general, electronii de pe stratul cu cel mai mare număr cuantic principal.

Exemple:
- Na: \(1s^2 2s^2 2p^6 3s^1\) → 1 electron pe stratul exterior;
- Mg: ... \(3s^2\) → 2 electroni de valență;
- Cl: ... \(3s^2 3p^5\) → 7 electroni de valență.

La metalele de tranziție, electronii din substraturile ns și (n−1)d pot participa la comportamentul chimic; interpretarea este mai nuanțată.

## 2. Perioada

Numărul perioadei indică, pentru elementele reprezentative, cel mai mare număr cuantic principal n ocupat în configurația electronică fundamentală.

Exemplu: sodiul are electronul exterior în stratul n = 3, deci se află în perioada a 3-a.

## 3. Grupa

Pentru elementele reprezentative, configurația stratului exterior ajută la identificarea grupei:
- \(ns^1\): grupa 1;
- \(ns^2\): grupa 2;
- \(ns^2np^1\) până la \(ns^2np^6\): grupele 13–18.

Heliul este o excepție importantă: are configurația \(1s^2\), dar se află în grupa 18 datorită stratului complet și proprietăților sale de gaz nobil.

## 4. Blocurile tabelului periodic

Blocul este asociat cu tipul de substrat care se completează:
- blocul s: grupele 1–2 (heliul are configurație s, dar este plasat în grupa 18);
- blocul p: grupele 13–18, cu excepția heliului;
- blocul d: metalele de tranziție;
- blocul f: lantanoidele și actinoidele.

### Exemplu rezolvat

Elementul cu Z = 17 are configurația:

\[
1s^2\,2s^2\,2p^6\,3s^2\,3p^5
\]

Cel mai mare n este 3 → perioada 3. Configurația exterioară este \(3s^2 3p^5\), adică 7 electroni de valență → grupa 17. Elementul este clorul, din blocul p.
""",
            "takeaways": [
                "Configurația electronică ajută la determinarea perioadei și grupei.",
                "Pentru elementele reprezentative, perioada corespunde celui mai mare n ocupat.",
                "Configurația exterioară permite identificarea grupei la elementele reprezentative.",
                "Blocurile s, p, d și f reflectă substratul care se completează."
            ]
        },
        {
            "id": "atom_lesson_07",
            "title": "1.7. Variația proprietăților periodice",
            "level": "Concurs",
            "official": "Temă explicită în programa publicată pentru ediția 2026",
            "body": r"""
## 1. De ce sunt periodice proprietățile?

Elementele sunt ordonate în tabelul periodic după numărul atomic. Repetarea configurațiilor electronice exterioare produce repetarea periodică a unor proprietăți chimice și fizice.

Tendințele de mai jos sunt reguli generale; există excepții și situații în care definiția folosită contează.

## 2. Raza atomică

- Într-o perioadă, de la stânga la dreapta, raza atomică tinde să **scadă**, deoarece crește sarcina nucleară efectivă.
- Într-o grupă, de sus în jos, raza atomică tinde să **crească**, deoarece se adaugă straturi electronice.

Pentru ioni:
- cationul este, de regulă, mai mic decât atomul neutru din care provine;
- anionul este, de regulă, mai mare decât atomul neutru din care provine.

## 3. Energia de ionizare

Energia de ionizare este energia necesară pentru îndepărtarea unui electron dintr-un atom izolat în fază gazoasă.

Tendință generală:
- crește de la stânga la dreapta într-o perioadă;
- scade de sus în jos într-o grupă.

Atomii mici, cu electroni exteriori atrași puternic de nucleu, au în general energii de ionizare mai mari.

## 4. Electronegativitatea

Electronegativitatea exprimă tendința unui atom legat chimic de a atrage către sine densitatea electronică a legăturii.

Tendință generală:
- crește de la stânga la dreapta;
- scade de sus în jos.

Fluorul este elementul cu electronegativitatea cea mai mare pe scara Pauling. Gazele nobile sunt adesea omise din comparațiile introductive, deoarece electronegativitatea lor nu este definită în același mod pentru toate situațiile.

## 5. Caracterul metalic

Caracterul metalic este tendința de a ceda electroni și de a forma cationi. În general:
- crește de sus în jos într-o grupă;
- crește de la dreapta la stânga într-o perioadă.

### Tabel de recapitulare

| Proprietate | Stânga → dreapta | Sus → jos |
|---|---|---|
| Rază atomică | scade, în general | crește |
| Energie de ionizare | crește, în general | scade |
| Electronegativitate | crește, în general | scade |
| Caracter metalic | scade | crește |

### Cum compari două elemente?

1. Identifică dacă sunt în aceeași perioadă sau grupă.
2. Aplică tendința corespunzătoare.
3. Dacă sunt poziționate diferit, folosește poziția lor în tabel și explică raționamentul.
4. Fii atent la formulări precum „în general” și la excepțiile cerute explicit.
""",
            "takeaways": [
                "Raza atomică scade în general pe perioadă și crește pe grupă.",
                "Energia de ionizare și electronegativitatea au tendințe generale opuse razei.",
                "Caracterul metalic crește spre stânga și în jos.",
                "Tendințele periodice sunt reguli generale, nu legi fără excepții."
            ]
        },
        {
            "id": "atom_lesson_08",
            "title": "1.8. Recapitulare și strategie pentru probleme",
            "level": "Concurs",
            "official": "Sinteză și aplicații originale pentru antrenament",
            "body": r"""
## Fișa de recapitulare

| Mărime/noțiune | Ce reprezintă | Relație utilă |
|---|---|---|
| Număr atomic Z | numărul protonilor | \(Z=p\) |
| Număr de masă A | protoni + neutroni | \(A=p+n\) |
| Neutroni n | particule neutre din nucleu | \(n=A-Z\) |
| Atom neutru | protoni = electroni | \(e=Z\) |
| Capacitatea stratului | numărul maxim teoretic de electroni | \(2n^2\) |
| Substrat s/p/d/f | regiuni de stări energetice | 2/6/10/14 electroni max. |

## Strategie pentru configurații electronice

1. Determină numărul de electroni. Pentru un atom neutru, este Z; pentru un ion, ajustează după sarcină.
2. Completează substraturile în ordinea energetică uzuală.
3. Respectă principiile Aufbau, Pauli și regula lui Hund.
4. Verifică suma exponenților.
5. Identifică stratul exterior și substratul în curs de completare.
6. Deduce perioada, grupa și blocul, ținând cont de excepții.

## Strategie pentru tendințe periodice

Nu memora doar săgețile. Explică motivul:
- mai multe straturi ocupate → rază mai mare;
- atracție nucleară efectivă mai puternică → electroni atrași mai puternic;
- îndepărtarea unui electron necesită mai multă energie când acesta este ținut mai puternic de nucleu.

## Greșeli frecvente

- Confundarea numărului de masă A cu masa atomică relativă.
- Scăderea electronilor din Z la anioni în loc să îi adaugi.
- Considerarea electronilor ca fiind pe orbite circulare fixe.
- Omiterea verificării sumei exponenților configurației.
- Aplicarea mecanică a tendințelor periodice fără a identifica poziția elementelor.
"""
            ,
            "takeaways": [
                "Verifică întotdeauna numărul total de electroni.",
                "Separă datele despre nucleu de cele despre învelișul electronic.",
                "Explică tendințele periodice prin structură electronică și atracție nucleară.",
                "Citește cu atenție sarcina ionului și unitățile."
            ]
        }
    ]
}

def _q(qid, lesson, topic, question, options, answer, explanation, distractors):
    return {
        "id": qid,
        "domain": "Structura atomului",
        "lesson": lesson,
        "topic": topic,
        "question": question,
        "options": options,
        "answer": answer,
        "explanation": explanation,
        "option_explanations": distractors,
        "level": "Fundamente" if lesson in ("1.1", "1.2") else "Concurs"
    }

OPTIONS = {
    "p11": ["A. 10", "B. 11", "C. 12", "D. 23", "E. Niciuna dintre variantele A–D"],
    "p18": ["A. 6", "B. 8", "C. 10", "D. 16", "E. Niciuna dintre variantele A–D"],
    "p17": ["A. 17", "B. 18", "C. 35", "D. 52", "E. Niciuna dintre variantele A–D"],
    "p13": ["A. 10", "B. 13", "C. 16", "D. 26", "E. Niciuna dintre variantele A–D"],
    "p14": ["A. 6", "B. 8", "C. 10", "D. 12", "E. Niciuna dintre variantele A–D"],
}

CHAPTER1_QUESTIONS = [
    _q("atom1_001","1.1","Particule subatomice","Un atom neutru de sodiu are Z = 11. Câți electroni conține?",OPTIONS["p11"],"B. 11","Într-un atom neutru, numărul electronilor este egal cu numărul protonilor, iar Z este numărul protonilor.",{"A. 10":"Ar fi numărul electronilor unui ion Na⁺, nu al atomului neutru.","C. 12":"Atomul neutru nu are un electron în plus față de protoni.","D. 23":"23 poate fi numărul de masă al izotopului Na-23, nu numărul electronilor.","E. Niciuna dintre variantele A–D":"Există o variantă corectă: B."}),
    _q("atom1_002","1.1","Particule subatomice","Care particulă are sarcină electrică relativă −1?",["A. Protonul","B. Neutronul","C. Electronul","D. Nucleul","E. Niciuna dintre variantele A–D"],"C. Electronul","Electronul are sarcină −1; protonul are +1, iar neutronul este neutru.",{"A. Protonul":"Protonul are sarcină relativă +1.","B. Neutronul":"Neutronul are sarcină electrică zero.","D. Nucleul":"Nucleul are sarcină pozitivă datorită protonilor.","E. Niciuna dintre variantele A–D":"Varianta C este corectă."}),
    _q("atom1_003","1.1","Ioni","Un atom de magneziu cu Z = 12 formează ionul Mg²⁺. Câți electroni are ionul?",["A. 10","B. 12","C. 14","D. 24","E. Niciuna dintre variantele A–D"],"A. 10","Sarcina +2 arată că atomul a cedat doi electroni: 12 − 2 = 10.",{"B. 12":"Acesta este numărul electronilor atomului neutru de Mg.","C. 14":"La formarea Mg²⁺ din atomul neutru se cedează doi electroni, nu se acceptă doi.","D. 24":"24 nu reprezintă numărul electronilor; este o confuzie cu alte valori.","E. Niciuna dintre variantele A–D":"Varianta A este corectă."}),
    _q("atom1_004","1.2","Număr de masă","Un atom are A = 39 și Z = 19. Câți neutroni are?",["A. 19","B. 20","C. 39","D. 58","E. Niciuna dintre variantele A–D"],"B. 20","Numărul neutronilor este A − Z = 39 − 19 = 20.",{"A. 19":"19 este numărul protonilor.","C. 39":"39 este numărul de masă, adică protoni plus neutroni.","D. 58":"Adunarea lui A și Z nu determină neutronii.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
    _q("atom1_005","1.2","Notație nucleară","Pentru atomul neutru ^{35}_{17}Cl, numărul electronilor este:",["A. 17","B. 18","C. 35","D. 52","E. Niciuna dintre variantele A–D"],"A. 17","Atomul este neutru, deci are 17 electroni, egal cu Z.",{"B. 18":"18 este numărul neutronilor (35 − 17), nu al electronilor.","C. 35":"35 este numărul de masă.","D. 52":"Suma A + Z nu reprezintă numărul electronilor.","E. Niciuna dintre variantele A–D":"Varianta A este corectă."}),
    _q("atom1_006","1.2","Ioni","Câți electroni are ionul O²⁻ dacă oxigenul are Z = 8?",OPTIONS["p18"],"C. 10","Oxigenul neutru are 8 electroni. Sarcina 2− arată că a acceptat doi electroni: 8 + 2 = 10.",{"A. 6":"Ar corespunde pierderii a doi electroni, nu formării anionului.","B. 8":"Acesta este numărul electronilor atomului neutru.","D. 16":"Numărul de masă sau dublarea lui Z nu determină electronii ionului.","E. Niciuna dintre variantele A–D":"Varianta C este corectă."}),
    _q("atom1_007","1.3","Izotopi","Doi izotopi ai aceluiași element au obligatoriu același număr de:",["A. neutroni","B. masă","C. protoni","D. nucleoni","E. Niciuna dintre variantele A–D"],"C. protoni","Izotopii aparțin aceluiași element, deci au același Z și același număr de protoni; diferă prin numărul neutronilor.",{"A. neutroni":"Numărul neutronilor diferă între izotopii unui element.","B. masă":"Numerele de masă sunt diferite pentru izotopi diferiți.","D. nucleoni":"Numărul total de nucleoni este numărul de masă și diferă.","E. Niciuna dintre variantele A–D":"Varianta C este corectă."}),
    _q("atom1_008","1.3","Izotopi","Izotopul carbon-14 are Z = 6. Câți neutroni are nucleul său?",["A. 6","B. 8","C. 14","D. 20","E. Niciuna dintre variantele A–D"],"B. 8","Numărul neutronilor este A − Z = 14 − 6 = 8.",{"A. 6":"6 este numărul protonilor.","C. 14":"14 este numărul de masă.","D. 20":"Adunarea lui A și Z nu determină neutronii.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
    _q("atom1_009","1.3","Masă atomică relativă","Un element are doi izotopi cu mase aproximative 10 u și 11 u, în abundențe 20% și 80%. Care este masa atomică relativă aproximativă?",["A. 10,2","B. 10,5","C. 10,8","D. 11,2","E. Niciuna dintre variantele A–D"],"C. 10,8","Media ponderată este (10×20 + 11×80)/100 = 10,8.",{"A. 10,2":"Ar corespunde unei ponderi mult mai mari pentru izotopul cu masa 10.","B. 10,5":"Este media simplă, care ar presupune abundențe egale.","D. 11,2":"Media nu poate depăși masa celui mai greu izotop în acest model.","E. Niciuna dintre variantele A–D":"Varianta C este corectă."}),
    _q("atom1_010","1.4","Substraturi","Câți electroni poate conține maximum un substrat p?",["A. 2","B. 3","C. 6","D. 10","E. Niciuna dintre variantele A–D"],"C. 6","Substratul p conține trei orbitali, fiecare cu maximum doi electroni: 3 × 2 = 6.",{"A. 2":"2 este capacitatea unui singur orbital, nu a întregului substrat p.","B. 3":"3 este numărul orbitalilor p.","D. 10":"10 este capacitatea maximă a unui substrat d.","E. Niciuna dintre variantele A–D":"Varianta C este corectă."}),
    _q("atom1_011","1.4","Straturi electronice","Care este capacitatea maximă teoretică a stratului cu n = 3?",["A. 8","B. 10","C. 18","D. 32","E. Niciuna dintre variantele A–D"],"C. 18","Capacitatea maximă a unui strat este 2n². Pentru n = 3: 2 × 3² = 18.",{"A. 8":"8 este capacitatea stratului n = 2.","B. 10":"10 este capacitatea unui substrat d.","D. 32":"32 este capacitatea maximă a stratului n = 4.","E. Niciuna dintre variantele A–D":"Varianta C este corectă."}),
    _q("atom1_012","1.5","Configurații electronice","Configurația electronică fundamentală a oxigenului (Z = 8) este:",["A. 1s² 2s² 2p²","B. 1s² 2s² 2p⁴","C. 1s² 2s⁴ 2p²","D. 1s² 2p⁶","E. Niciuna dintre variantele A–D"],"B. 1s² 2s² 2p⁴","Oxigenul are 8 electroni: 2 în 1s, 2 în 2s și 4 în 2p. Suma exponenților este 8.",{"A. 1s² 2s² 2p²":"Această configurație însumează 6 electroni, corespunzând carbonului.","C. 1s² 2s⁴ 2p²":"Un orbital s poate conține maximum doi electroni; 2s⁴ este imposibil.","D. 1s² 2p⁶":"Nu respectă ordinea de ocupare și nu reprezintă configurația fundamentală a oxigenului.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
    _q("atom1_013","1.5","Regula lui Hund","Conform regulii lui Hund, în orbitalii de aceeași energie electronii:",["A. se împerechează imediat în primul orbital","B. ocupă mai întâi orbitalii separat, cu spini paraleli","C. ocupă întotdeauna orbitalii cu energie mai mare","D. nu pot avea spini opuși","E. Niciuna dintre variantele A–D"],"B. ocupă mai întâi orbitalii separat, cu spini paraleli","Electronii ocupă individual orbitalii degenerați înainte de împerechere, cu spini paraleli.",{"A. se împerechează imediat în primul orbital":"Contrazice regula lui Hund.","C. ocupă întotdeauna orbitalii cu energie mai mare":"Principiul Aufbau favorizează ocuparea orbitalilor cu energie mai mică.","D. nu pot avea spini opuși":"Principiul Pauli permite doi electroni într-un orbital cu spini opuși.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
    _q("atom1_014","1.5","Principiul Pauli","Numărul maxim de electroni care pot ocupa un singur orbital este:",["A. 1","B. 2","C. 6","D. 8","E. Niciuna dintre variantele A–D"],"B. 2","Principiul excluziunii Pauli permite maximum doi electroni într-un orbital, cu spini opuși.",{"A. 1":"Un orbital poate conține și doi electroni, dacă au spini opuși.","C. 6":"6 este capacitatea întregului substrat p, format din trei orbitali.","D. 8":"8 este capacitatea stratului n = 2, nu a unui orbital.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
    _q("atom1_015","1.6","Poziția în tabelul periodic","Elementul cu Z = 17 are configurația exterioară 3s² 3p⁵. În ce perioadă se află?",["A. 2","B. 3","C. 5","D. 7","E. Niciuna dintre variantele A–D"],"B. 3","Cel mai mare număr cuantic principal ocupat este n = 3, deci elementul se află în perioada a 3-a.",{"A. 2":"Stratul exterior ocupat este n = 3, nu n = 2.","C. 5":"Exponentul 5 din 3p⁵ reprezintă numărul electronilor din substrat, nu perioada.","D. 7":"Nu există un strat exterior n = 7 în configurația dată.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
    _q("atom1_016","1.6","Grupa elementelor reprezentative","Un element reprezentativ are configurația exterioară ns² np⁵. În ce grupă se află?",["A. 2","B. 15","C. 17","D. 18","E. Niciuna dintre variantele A–D"],"C. 17","ns²np⁵ înseamnă 7 electroni de valență pentru un element reprezentativ din grupa 17.",{"A. 2":"ns² fără electroni p exteriori corespunde în mod obișnuit grupei 2.","B. 15":"Grupa 15 are configurația exterioară ns²np³.","D. 18":"Grupa 18 are în general ns²np⁶, cu excepția heliului.","E. Niciuna dintre variantele A–D":"Varianta C este corectă."}),
    _q("atom1_017","1.6","Blocuri periodice","Un element a cărui configurație se termină în 3p⁴ aparține blocului:",["A. s","B. p","C. d","D. f","E. Niciuna dintre variantele A–D"],"B. p","Blocul unui element reprezentativ este indicat de substratul în curs de completare; 3p⁴ indică blocul p.",{"A. s":"Configurațiile de tip ns se asociază blocului s.","C. d":"Blocul d implică ocuparea unui substrat d.","D. f":"Blocul f implică ocuparea unui substrat f.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
    _q("atom1_018","1.7","Raza atomică","În general, cum variază raza atomică de la stânga la dreapta într-o perioadă?",["A. crește","B. scade","C. rămâne mereu constantă","D. devine egală cu numărul atomic","E. Niciuna dintre variantele A–D"],"B. scade","Într-o perioadă crește sarcina nucleară efectivă, iar electronii sunt atrași mai puternic; raza atomică tinde să scadă.",{"A. crește":"Creșterea razei este tendința generală în josul unei grupe.","C. rămâne mereu constantă":"Raza variază de-a lungul perioadei.","D. devine egală cu numărul atomic":"Raza și numărul atomic sunt mărimi diferite.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
    _q("atom1_019","1.7","Energie de ionizare","Care este tendința generală a energiei de ionizare într-o grupă, de sus în jos?",["A. crește","B. scade","C. rămâne identică","D. devine zero","E. Niciuna dintre variantele A–D"],"B. scade","De sus în jos crește numărul straturilor și electronul exterior este, în general, mai îndepărtat și mai ecranat, deci se îndepărtează mai ușor.",{"A. crește":"Tendința generală de creștere este de la stânga la dreapta într-o perioadă.","C. rămâne identică":"Energia de ionizare variază în cadrul grupei.","D. devine zero":"Îndepărtarea electronului necesită energie; valoarea nu devine zero.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
    _q("atom1_020","1.7","Electronegativitate","Care element are cea mai mare electronegativitate pe scara Pauling?",["A. Oxigenul","B. Clorul","C. Fluorul","D. Sodiul","E. Niciuna dintre variantele A–D"],"C. Fluorul","Fluorul are cea mai mare electronegativitate pe scara Pauling.",{"A. Oxigenul":"Oxigenul este foarte electronegativ, dar valoarea sa este sub cea a fluorului.","B. Clorul":"Clorul este electronegativ, dar fluorul are valoarea mai mare.","D. Sodiul":"Sodiul este un metal alcalin cu electronegativitate mică.","E. Niciuna dintre variantele A–D":"Varianta C este corectă."}),
    _q("atom1_021","1.7","Caracter metalic","Într-o perioadă, caracterul metalic are în general tendința să:",["A. crească de la stânga la dreapta","B. scadă de la stânga la dreapta","C. rămână constant","D. crească odată cu electronegativitatea","E. Niciuna dintre variantele A–D"],"B. scadă de la stânga la dreapta","Caracterul metalic scade, în general, de la stânga la dreapta, pe măsură ce crește tendința de atragere a electronilor.",{"A. crească de la stânga la dreapta":"Este inversul tendinței generale.","C. rămână constant":"Proprietățile se modifică periodic.","D. crească odată cu electronegativitatea":"Caracterul metalic și electronegativitatea au tendințe generale opuse.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
    _q("atom1_022","1.7","Rază ionică","Comparativ cu atomul neutru de sodiu, ionul Na⁺ are raza:",["A. mai mare","B. mai mică","C. identică în toate condițiile","D. infinită","E. Niciuna dintre variantele A–D"],"B. mai mică","Na⁺ se formează prin cedarea electronului exterior. Scade repulsia electronică și se pierde stratul exterior ocupat, astfel ionul este mai mic.",{"A. mai mare":"Creșterea razei este tipică, în general, pentru anioni față de atomii neutri corespunzători.","C. identică în toate condițiile":"Formarea ionului modifică distribuția electronică și raza.","D. infinită":"Raza ionică este finită.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
    _q("atom1_023","1.8","Configurație și perioadă","Un atom neutru are configurația 1s² 2s² 2p⁶ 3s¹. Care este numărul său atomic?",["A. 1","B. 10","C. 11","D. 12","E. Niciuna dintre variantele A–D"],"C. 11","Suma electronilor este 2 + 2 + 6 + 1 = 11. Pentru atomul neutru, Z = 11.",{"A. 1":"1 este doar exponentul electronului din 3s.","B. 10":"10 este suma electronilor până la 2p⁶; lipsește electronul 3s.","D. 12":"Suma exponenților nu este 12.","E. Niciuna dintre variantele A–D":"Varianta C este corectă."}),
    _q("atom1_024","1.8","Comparație periodică","Care dintre elementele Na și Cl, aflate în aceeași perioadă, are în general raza atomică mai mică?",["A. Na","B. Cl","C. au raze egale","D. nu se poate compara fără numărul de masă","E. Niciuna dintre variantele A–D"],"B. Cl","În aceeași perioadă, raza atomică scade în general de la stânga la dreapta. Cl este la dreapta lui Na.",{"A. Na":"Sodiul este mai la stânga și are raza atomică mai mare în tendința generală.","C. au raze egale":"Raza variază de-a lungul perioadei.","D. nu se poate compara fără numărul de masă":"Pentru tendința periodică nu este necesar numărul de masă.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."})
]
