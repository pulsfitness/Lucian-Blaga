"""Material didactic pentru Capitolul 2 – Legături chimice.

Lecțiile dezvoltă domeniul „Legături chimice” din tematica publicată
pentru ediția 2026 a concursului Candin Liteanu. Întrebările sunt originale,
create pentru antrenament și nu sunt subiecte oficiale.
"""

CHAPTER2_LESSONS = [
    {
        "id": "bond_lesson_01",
        "title": "2.1. De ce se formează legăturile chimice? Regula octetului",
        "level": "Fundamente",
        "official": "Noțiuni introductive și regula octetului",
        "body": r"""
## 1. De ce se leagă atomii?

Majoritatea atomilor formează legături chimice deoarece combinația rezultată poate avea energie mai mică și stabilitate mai mare decât atomii separați. În formarea unei legături se modifică distribuția electronilor de valență.

**Electronii de valență** sunt electronii implicați în mod obișnuit în formarea legăturilor chimice. Pentru elementele reprezentative, ei sunt electronii stratului exterior.

## 2. Regula octetului

Multe elemente reprezentative tind să ajungă la o configurație electronică asemănătoare gazului nobil apropiat, cu opt electroni pe stratul exterior. Această observație este numită **regula octetului**.

Exemple:
- Na cedează un electron și poate forma Na⁺;
- Cl acceptă un electron și poate forma Cl⁻;
- doi atomi de Cl pot pune în comun o pereche de electroni, formând Cl₂.

## 3. Regula duetului

Primul strat electronic poate conține maximum doi electroni. Hidrogenul poate atinge configurația de tip heliu prin punerea în comun a unei perechi de electroni într-o legătură covalentă.

## 4. Limitele regulii octetului

Regula octetului este un instrument introductiv, nu o lege universală:
- H și He urmează regula duetului;
- Be și B pot apărea în molecule cu octet incomplet;
- unele molecule au număr impar de electroni;
- pentru elementele din perioadele 3 și mai jos, există compuși descriși în modele introductive cu octet extins.

**Idee-cheie:** stabilitatea nu se reduce mecanic la „toți atomii vor opt electroni”. Contează energia totală a sistemului și natura legăturilor.
""",
        "takeaways": [
            "Legăturile se formează când starea rezultată este energetic favorabilă.",
            "Electronii de valență participă la formarea legăturilor.",
            "Regula octetului este utilă pentru multe elemente reprezentative, dar are excepții.",
            "Hidrogenul urmărește în mod obișnuit configurația de duet."
        ]
    },
    {
        "id": "bond_lesson_02",
        "title": "2.2. Simboluri Lewis și reprezentarea electronilor de valență",
        "level": "Fundamente",
        "official": "Structuri Lewis – instrument de reprezentare a legăturilor",
        "body": r"""
## 1. Ce este simbolul Lewis?

Simbolul Lewis reprezintă simbolul elementului înconjurat de puncte care indică electronii de valență. Punctele se așază în jurul simbolului, câte unul pe fiecare latură înainte de a forma perechi.

Exemple orientative:
- H are 1 electron de valență;
- C are 4;
- N are 5;
- O are 6;
- Cl are 7.

## 2. Perechi de electroni

În structurile Lewis distingem:
- **perechi neparticipante** (libere): electroni care nu sunt reprezentați ca pereche de legătură;
- **perechi de legătură**: electroni puși în comun între doi atomi.

O linie între doi atomi reprezintă o pereche de electroni comună.

## 3. Exemple

**H₂:** fiecare H contribuie cu un electron; perechea comună formează o legătură simplă.

\[
H-H
\]

**Cl₂:** fiecare Cl are 7 electroni de valență și pune în comun câte unul. Fiecare atom ajunge la un octet în modelul Lewis.

**H₂O:** oxigenul formează două legături O–H și păstrează două perechi neparticipante.

**NH₃:** azotul formează trei legături N–H și păstrează o pereche neparticipantă.

## 4. Pași pentru desenarea unei structuri Lewis simple

1. Calculează numărul total de electroni de valență.
2. Alege atomul central (de regulă, nu H; adesea atomul mai puțin electronegativ).
3. Unește atomii prin legături simple.
4. Completează duetul hidrogenului și octeții atomilor periferici.
5. Plasează electronii rămași pe atomul central.
6. Dacă este necesar, formează legături multiple și verifică numărul total de electroni.

Pentru ioni, numărul total de electroni se ajustează după sarcină: se adaugă electroni pentru sarcina negativă și se scad pentru sarcina pozitivă.

**Atenție:** o structură Lewis arată conectivitatea și perechile electronice, dar nu reprezintă exact forma tridimensională a moleculei.
""",
        "takeaways": [
            "Punctele Lewis reprezintă electronii de valență.",
            "O linie reprezintă o pereche de electroni de legătură.",
            "Perechile neparticipante nu sunt folosite direct la legătura reprezentată.",
            "Verifică întotdeauna numărul total de electroni de valență."
        ]
    },
    {
        "id": "bond_lesson_03",
        "title": "2.3. Legătura ionică și formarea ionilor",
        "level": "Intermediar",
        "official": "Legătura ionică",
        "body": r"""
## 1. Cum se formează o legătură ionică?

Legătura ionică este atracția electrostatică dintre ioni cu sarcini opuse. În modelul introductiv, ea apare frecvent după transferul unuia sau mai multor electroni de la un atom la altul.

- atomul care cedează electroni devine **cation**;
- atomul care acceptă electroni devine **anion**.

Exemplu: formarea clorurii de sodiu.

\[
Na \rightarrow Na^+ + e^-
\]
\[
Cl + e^- \rightarrow Cl^-
\]

Apoi ionii Na⁺ și Cl⁻ se atrag electrostatic și formează un solid ionic.

## 2. Formula compușilor ionici

Formula trebuie să respecte electroneutralitatea: suma sarcinilor pozitive și negative este zero.

Exemple:
- Na⁺ și Cl⁻ → NaCl;
- Mg²⁺ și Cl⁻ → MgCl₂;
- Al³⁺ și O²⁻ → Al₂O₃.

Pentru Al₂O₃: 2 × (+3) + 3 × (−2) = 0.

## 3. Proprietăți tipice ale substanțelor ionice

Multe solide ionice:
- formează rețele cristaline;
- au temperaturi de topire relativ ridicate;
- sunt casante;
- conduc curentul electric când sunt topite sau dizolvate în apă, dacă ionii devin mobili;
- nu conduc, în general, curentul în stare solidă, deoarece ionii sunt fixați în rețea.

Acestea sunt tendințe generale, nu descrieri identice pentru orice compus ionic.

## 4. Energia rețelei

Atracția electrostatică dintre ioni contribuie la stabilitatea cristalului. În general, atracția crește când sarcinile ionilor sunt mai mari și distanța dintre centrele ionilor este mai mică.

**Nu confunda:** într-un cristal precum NaCl nu există molecule individuale NaCl izolate în sensul obișnuit; formula indică raportul numeric minim dintre ioni.
""",
        "takeaways": [
            "Legătura ionică este atracția electrostatică dintre ioni de sarcini opuse.",
            "Cationii cedează electroni, anionii acceptă electroni.",
            "Formula compusului ionic trebuie să fie electroneutră.",
            "Cristalele ionice conduc curentul când ionii se pot deplasa."
        ]
    },
    {
        "id": "bond_lesson_04",
        "title": "2.4. Legătura covalentă: polară și nepolară",
        "level": "Intermediar",
        "official": "Legătura covalentă",
        "body": r"""
## 1. Ce este legătura covalentă?

Legătura covalentă se formează prin punerea în comun a uneia sau mai multor perechi de electroni între atomi. Este întâlnită frecvent între nemetale.

Exemple:
- H₂: H–H;
- Cl₂: Cl–Cl;
- HCl: H–Cl;
- H₂O: legături O–H.

## 2. Legătura covalentă nepolară

Dacă perechea de electroni este atrasă aproximativ egal de cei doi atomi, legătura este nepolară.

Exemple uzuale: H–H, Cl–Cl. Atomii identici au aceeași electronegativitate, astfel diferența este zero.

## 3. Legătura covalentă polară

Dacă unul dintre atomi atrage mai puternic perechea comună, distribuția electronilor devine inegală. Apar sarcini parțiale:
- \(\delta^-\) la atomul mai electronegativ;
- \(\delta^+\) la atomul mai puțin electronegativ.

În H–Cl, clorul este mai electronegativ, deci legătura este polarizată spre Cl.

## 4. Diferența de electronegativitate

Diferența de electronegativitate este un ghid pentru estimarea polarității legăturii. Nu există o limită universală exactă care să separe toate legăturile ionice de cele covalente; caracterul legăturii poate avea grade diferite.

## 5. Legătura polară nu înseamnă automat moleculă polară

Polaritatea moleculei depinde atât de polaritatea legăturilor, cât și de geometria moleculei.

Exemplu:
- CO₂ are legături C=O polare, dar molecula liniară este nepolară deoarece dipolii se compensează;
- H₂O are legături O–H polare și geometrie unghiulară, deci dipolii nu se compensează; molecula este polară.
""",
        "takeaways": [
            "Legătura covalentă implică perechi de electroni comune.",
            "Legătura nepolară are distribuție aproximativ egală a electronilor.",
            "Legătura polară are distribuție inegală și sarcini parțiale.",
            "Polaritatea moleculei depinde și de geometrie, nu doar de legături."
        ]
    },
    {
        "id": "bond_lesson_05",
        "title": "2.5. Legături simple, duble și triple. Legături sigma și pi",
        "level": "Concurs",
        "official": "Legături covalente simple, duble și triple",
        "body": r"""
## 1. Ordinul legăturii

Doi atomi pot pune în comun una, două sau trei perechi de electroni:
- legătură simplă: o pereche comună;
- legătură dublă: două perechi comune;
- legătură triplă: trei perechi comune.

Exemple:
- H–H: simplă;
- O=O: dublă;
- N≡N: triplă.

În general, pentru aceeași pereche de atomi, creșterea ordinului legăturii este asociată cu o legătură mai scurtă și mai puternică.

## 2. Legătura sigma (σ)

Legătura sigma se formează prin suprapunerea orbitalilor de-a lungul axei care unește nucleele. Toate legăturile simple sunt legături sigma.

## 3. Legătura pi (π)

Legătura pi se formează prin suprapunere laterală a orbitalilor, de regulă p, cu densitate electronică deasupra și dedesubtul axei internucleare.

- legătură simplă: 1 σ;
- legătură dublă: 1 σ + 1 π;
- legătură triplă: 1 σ + 2 π.

## 4. Exemple

În etena, H₂C=CH₂, legătura dublă C=C conține o legătură σ și una π.

În etină, HC≡CH, legătura triplă C≡C conține o legătură σ și două legături π.

**Atenție:** legătura pi nu înlocuiește legătura sigma. O legătură multiplă conține întotdeauna o componentă sigma.
""",
        "takeaways": [
            "Legătura simplă are o pereche comună; dubla două; tripla trei.",
            "Legătura simplă este sigma.",
            "Dubla = 1 sigma + 1 pi.",
            "Tripla = 1 sigma + 2 pi.",
            "Legăturile multiple sunt în general mai scurte decât legăturile simple corespunzătoare."
        ]
    },
    {
        "id": "bond_lesson_06",
        "title": "2.6. Legătura coordinativă (dativă)",
        "level": "Concurs",
        "official": "Legătura coordinativă",
        "body": r"""
## 1. Definiție

Legătura covalentă coordinativă (numită și dativă) este o legătură covalentă în care ambii electroni ai perechii comune provin inițial de la același atom, numit donor. Celălalt atom/ion acceptă perechea și se numește acceptor.

După formare, legătura este o legătură covalentă; originea perechii de electroni este cea care o caracterizează drept coordinativă în modelul Lewis.

## 2. Exemplu: ionul amoniu

Molecula NH₃ are o pereche neparticipantă pe atomul de azot. Ionul H⁺ poate accepta această pereche:

\[
NH_3 + H^+ \rightarrow NH_4^+
\]

Azotul este donorul perechii, iar protonul este acceptorul.

## 3. Donor și acceptor

- donorul trebuie să aibă o pereche de electroni disponibilă;
- acceptorul trebuie să poată accepta perechea (de exemplu, să aibă un orbital disponibil).

## 4. Reprezentare

Uneori legătura este desenată cu o săgeată de la donor la acceptor. Săgeata indică sensul donării perechii la formare, nu o sarcină pozitivă care „curge” prin legătură.

**Important:** după formarea ionului NH₄⁺, cele patru legături N–H sunt echivalente în ionul rezultat; nu trebuie tratată una ca fiind permanent diferită doar pentru că a fost formată coordinativ.
""",
        "takeaways": [
            "Ambii electroni ai perechii provin inițial de la donor.",
            "Donorul are o pereche neparticipantă disponibilă.",
            "Exemplu clasic: NH₃ + H⁺ → NH₄⁺.",
            "După formare, legătura este covalentă și poate deveni echivalentă cu celelalte legături."
        ]
    },
    {
        "id": "bond_lesson_07",
        "title": "2.7. Geometria moleculelor și polaritatea moleculei",
        "level": "Concurs",
        "official": "Geometria și polaritatea moleculelor – dezvoltare didactică",
        "body": r"""
## 1. De ce contează geometria?

Perechile de electroni din jurul atomului central se resping reciproc și se aranjează astfel încât repulsiile să fie cât mai mici. Modelul VSEPR (repulsia perechilor de electroni din stratul de valență) ajută la estimarea formei moleculelor simple.

Perechile neparticipante ocupă spațiu și pot modifica unghiurile dintre legături.

## 2. Geometrii uzuale

| Tip simplificat | Geometrie | Exemplu |
|---|---|---|
| 2 regiuni de legătură, fără perechi libere | liniară | CO₂ |
| 3 regiuni de legătură, fără perechi libere | trigonal plană | BF₃ |
| 4 regiuni, fără perechi libere | tetraedrică | CH₄ |
| 3 legături + 1 pereche liberă | piramidală trigonală | NH₃ |
| 2 legături + 2 perechi libere | unghiulară | H₂O |

Acestea sunt modele introductive pentru molecule simple.

## 3. Momentul dipolar

O legătură polară are un moment dipolar orientat spre atomul mai electronegativ. Molecula este polară dacă suma vectorială a dipolilor nu este zero.

## 4. Exemple importante

**CO₂:** moleculă liniară și simetrică. Dipolii celor două legături C=O sunt egali și opuși, deci se compensează. Molecula este nepolară.

**H₂O:** moleculă unghiulară. Dipolii legăturilor O–H nu se compensează, deci molecula este polară.

**CH₄:** geometrie tetraedrică simetrică. Legăturile C–H sunt distribuite simetric, iar molecula este nepolară.

**NH₃:** geometrie piramidală trigonală; dipolii nu se compensează, molecula este polară.

**Metodă:** întâi stabilește geometria, apoi analizează dacă dipolii se compensează.
""",
        "takeaways": [
            "Forma moleculei influențează polaritatea totală.",
            "CO₂ este nepolar, deși legăturile C=O sunt polare.",
            "H₂O este polară datorită geometriei unghiulare.",
            "Perechile neparticipante influențează geometria."
        ]
    },
    {
        "id": "bond_lesson_08",
        "title": "2.8. Interacțiuni intermoleculare și legături de hidrogen",
        "level": "Concurs",
        "official": "Interacțiuni intermoleculare",
        "body": r"""
## 1. Legături intramoleculare și interacțiuni intermoleculare

Legăturile intramoleculare țin atomii împreună în interiorul unei molecule (de exemplu, legături covalente).

Interacțiunile intermoleculare acționează între molecule sau particule. Ele sunt, în general, mai slabe decât legăturile covalente sau ionice, dar influențează puternic proprietățile fizice.

## 2. Forțele de dispersie London

Apar din fluctuații temporare ale distribuției electronilor, care induc dipoli temporari în particulele vecine. Sunt prezente între toate atomii și moleculele, inclusiv cele nepolare.

În general, polarizabilitatea crește odată cu numărul de electroni și cu dimensiunea norului electronic, ceea ce poate intensifica dispersia.

## 3. Interacțiuni dipol–dipol

Apar între molecule polare, ale căror dipoli permanenți se pot orienta astfel încât capetele cu sarcini parțiale opuse să se atragă.

## 4. Legături de hidrogen

Legătura de hidrogen este o interacțiune atractivă relativ puternică, întâlnită când hidrogenul legat covalent de un atom foarte electronegativ (în mod tipic N, O sau F) interacționează cu o pereche de electroni a unui alt atom electronegativ.

Exemple:
- între moleculele de apă;
- între moleculele de HF;
- între moleculele de amoniac, în anumite condiții;
- în structuri biologice, precum ADN și proteine.

## 5. Efecte asupra proprietăților fizice

Interacțiunile intermoleculare influențează:
- temperaturile de fierbere și topire;
- vâscozitatea;
- tensiunea superficială;
- solubilitatea.

De regulă, interacțiuni intermoleculare mai puternice pot conduce la temperaturi de fierbere mai mari pentru substanțe comparabile ca masă și structură. Nu compara fără atenție substanțe foarte diferite.

## 6. Comparație orientativă

- dispersie London: prezentă la toate particulele;
- dipol–dipol: necesită molecule polare;
- legătura de hidrogen: caz special de interacțiune între H legat de N/O/F și un acceptor potrivit.

Aceste interacțiuni pot exista simultan într-o substanță moleculară.
""",
        "takeaways": [
            "Interacțiunile intermoleculare acționează între molecule/particule.",
            "Forțele London apar la toate particulele.",
            "Interacțiunile dipol–dipol apar între molecule polare.",
            "Legăturile de hidrogen implică H legat de N, O sau F și un acceptor potrivit.",
            "Interacțiunile influențează fierberea, topirea, vâscozitatea și solubilitatea."
        ]
    },
    {
        "id": "bond_lesson_09",
        "title": "2.9. Recapitulare și comparația tipurilor de legături",
        "level": "Concurs",
        "official": "Sinteză și aplicații originale pentru antrenament",
        "body": r"""
## 1. Comparație rapidă

| Tip | Cum apare | Exemplu |
|---|---|---|
| Ionică | atracție electrostatică între ioni | NaCl |
| Covalentă nepolară | punere în comun aproape egală | H₂, Cl₂ |
| Covalentă polară | punere în comun inegală | HCl |
| Coordinativă | perechea comună provine inițial de la donor | NH₄⁺ |
| London | dipoli temporari/induşi | între molecule de I₂ |
| Dipol–dipol | atracție între dipoli permanenți | HCl···HCl |
| Legătură de hidrogen | interacțiune specifică a H legat de N/O/F | H₂O···H₂O |

## 2. Cum abordezi o problemă?

1. Identifică particulele: atomi, molecule sau ioni.
2. Determină electronii de valență și sarcinile.
3. Decide dacă se formează ioni sau se pun în comun electroni.
4. Dacă ai o moleculă, identifică legăturile și geometria.
5. Pentru polaritate, verifică atât legăturile, cât și forma moleculei.
6. Pentru puncte de fierbere/solubilitate, analizează interacțiunile intermoleculare.

## 3. Confuzii frecvente

- Legătura covalentă polară nu înseamnă automat moleculă polară.
- Legătura de hidrogen nu este aceeași cu legătura covalentă H–O din interiorul apei.
- Toate particulele au forțe de dispersie London.
- Legătura coordinativă este covalentă; donorul furnizează inițial ambii electroni ai perechii.
- Formula unui compus ionic trebuie să fie neutră electric.
- Regula octetului are excepții.
"""
        ,
        "takeaways": [
            "Separă legăturile intramoleculare de interacțiunile intermoleculare.",
            "Polaritatea moleculei depinde de geometrie și de dipolii legăturilor.",
            "Verifică electroneutralitatea formulelor ionice.",
            "Folosește regula octetului ca ghid, nu ca regulă fără excepții."
        ]
    }
]

def _question(qid, lesson, topic, question, options, answer, explanation, option_explanations, level="Concurs"):
    return {
        "id": qid,
        "domain": "Legături chimice",
        "lesson": lesson,
        "topic": topic,
        "question": question,
        "options": options,
        "answer": answer,
        "explanation": explanation,
        "option_explanations": option_explanations,
        "level": level
    }

def _opts(a,b,c,d):
    return [f"A. {a}", f"B. {b}", f"C. {c}", f"D. {d}", "E. Niciuna dintre variantele A–D"]

CHAPTER2_QUESTIONS = [
_question("bond2_001","2.1","Regula octetului","Care este ideea de bază a regulii octetului pentru multe elemente reprezentative?",_opts("atomii tind să aibă opt protoni","atomii tind să aibă opt electroni pe stratul exterior","toți atomii au exact opt straturi","moleculele conțin obligatoriu opt atomi"),"B. atomii tind să aibă opt electroni pe stratul exterior","Regula octetului descrie tendința multor elemente reprezentative de a ajunge la o configurație cu opt electroni de valență, asemănătoare gazelor nobile.",{"A. atomii tind să aibă opt protoni":"Numărul protonilor definește elementul; nu este scopul regulii octetului.","C. toți atomii au exact opt straturi":"Octetul se referă la electronii stratului exterior, nu la numărul straturilor.","D. moleculele conțin obligatoriu opt atomi":"Regula nu descrie numărul atomilor din moleculă.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."},"Fundamente"),
_question("bond2_002","2.1","Regula duetului","Hidrogenul formează de obicei o legătură covalentă pentru a ajunge la configurația:",_opts("de octet","de duet","de 10 electroni","de 18 electroni"),"B. de duet","Primul strat poate conține maximum doi electroni. Printr-o legătură covalentă, hidrogenul poate avea acces la o pereche comună și la configurația de tip heliu.",{"A. de octet":"Primul strat nu poate conține opt electroni.","C. de 10 electroni":"Nu este configurația urmărită de hidrogen în modelul obișnuit.","D. de 18 electroni":"18 electroni nu pot ocupa primul strat.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."},"Fundamente"),
_question("bond2_003","2.2","Simboluri Lewis","Câți electroni de valență are atomul neutru de oxigen?",_opts("2","4","6","8"),"C. 6","Oxigenul se află în grupa 16 și are configurația exterioară 2s²2p⁴, deci șase electroni de valență.",{"A. 2":"2 este numărul electronilor din substratul 2s, nu totalul electronilor de valență.","B. 4":"4 este numărul electronilor din 2p⁴, dar trebuie incluși și cei 2 din 2s.","D. 8":"8 este numărul total de electroni ai atomului de oxigen, nu numărul de valență.","E. Niciuna dintre variantele A–D":"Varianta C este corectă."},"Fundamente"),
_question("bond2_004","2.2","Structuri Lewis","Într-o structură Lewis, o linie simplă între doi atomi reprezintă:",_opts("un proton transferat","o pereche de electroni comună","doi neutroni","o pereche de protoni"),"B. o pereche de electroni comună","O linie într-o structură Lewis reprezintă o pereche de electroni implicată într-o legătură covalentă.",{"A. un proton transferat":"Legătura covalentă este reprezentată prin electroni comuni, nu transfer de protoni.","C. doi neutroni":"Neutronii se află în nucleu și nu sunt reprezentați prin linia de legătură.","D. o pereche de protoni":"Protonii nu formează perechea de legătură covalentă.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."},"Fundamente"),
_question("bond2_005","2.3","Legătura ionică","Ce particule se atrag electrostatic într-un compus ionic?",_opts("doi cationi","doi anioni","ioni cu sarcini opuse","doi atomi neutri identici"),"C. ioni cu sarcini opuse","Legătura ionică este atracția electrostatică dintre cationi și anioni.",{"A. doi cationi":"Sarcinile pozitive se resping electrostatic.","B. doi anioni":"Sarcinile negative se resping electrostatic.","D. doi atomi neutri identici":"Aceasta nu definește legătura ionică.","E. Niciuna dintre variantele A–D":"Varianta C este corectă."}),
_question("bond2_006","2.3","Formula compușilor ionici","Care este formula neutră a compusului format din Mg²⁺ și Cl⁻?",_opts("MgCl","MgCl₂","Mg₂Cl","Mg₂Cl₃"),"B. MgCl₂","Un ion Mg²⁺ necesită doi ioni Cl⁻ pentru ca suma sarcinilor să fie zero: +2 + 2(−1) = 0.",{"A. MgCl":"Sarcina totală ar fi +1, deci formula nu este neutră.","C. Mg₂Cl":"Sarcina totală ar fi +3.","D. Mg₂Cl₃":"Sarcina totală ar fi +1.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
_question("bond2_007","2.3","Proprietăți ionice","De ce un cristal ionic solid nu conduce, în general, curentul electric?",_opts("nu conține particule încărcate","ionii sunt fixați în rețeaua cristalină și nu se pot deplasa liber","electronii au masă prea mare","cristalul nu are legături"),"B. ionii sunt fixați în rețeaua cristalină și nu se pot deplasa liber","Conducția ionică necesită particule încărcate mobile. În solid, ionii ocupă poziții fixe în rețea; în topitură sau soluție, ei se pot deplasa.",{"A. nu conține particule încărcate":"Cristalul conține cationi și anioni.","C. electronii au masă prea mare":"Conducția în cristalele ionice este explicată prin mobilitatea ionilor, nu prin masa electronilor.","D. cristalul nu are legături":"Ionii sunt ținuți împreună de atracții electrostatice puternice.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
_question("bond2_008","2.4","Legătură covalentă","Într-o legătură covalentă, atomii:",_opts("pun în comun una sau mai multe perechi de electroni","transferă obligatoriu toți electronii de valență","își unesc nucleele","schimbă neutroni"),"A. pun în comun una sau mai multe perechi de electroni","Legătura covalentă se bazează pe perechi de electroni comune între atomi.",{"B. transferă obligatoriu toți electronii de valență":"Transferul de electroni este asociat formării ionilor, nu definiției legăturii covalente.","C. își unesc nucleele":"Nucleele nu se unesc în formarea unei legături chimice obișnuite.","D. schimbă neutroni":"Neutronii nu sunt schimbați în legăturile chimice.","E. Niciuna dintre variantele A–D":"Varianta A este corectă."},"Fundamente"),
_question("bond2_009","2.4","Polaritatea legăturii","În legătura H–Cl, densitatea electronică a legăturii este deplasată în principal spre:",_opts("hidrogen","clor","ambii atomi în mod perfect egal","nucleul hidrogenului"),"B. clor","Clorul este mai electronegativ decât hidrogenul și atrage mai puternic perechea comună; Cl capătă sarcină parțială δ−.",{"A. hidrogen":"H este mai puțin electronegativ decât Cl.","C. ambii atomi în mod perfect egal":"Distribuția este inegală, deci legătura este polară.","D. nucleul hidrogenului":"Densitatea electronică este deplasată spre atomul mai electronegativ, nu spre nucleul H.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
_question("bond2_010","2.4","Polaritatea moleculei","Molecula CO₂ are legături C=O polare. De ce molecula este totuși nepolară?",_opts("legăturile C=O sunt de fapt nepolare","molecula este liniară, iar dipolii egali se compensează","carbonul nu are electroni","molecula nu are legături"),"B. molecula este liniară, iar dipolii egali se compensează","CO₂ este liniară și simetrică. Cei doi dipoli de legătură sunt orientați în sensuri opuse și au aceeași mărime, astfel suma vectorială este zero.",{"A. legăturile C=O sunt de fapt nepolare":"Legăturile C=O sunt polare din cauza diferenței de electronegativitate.","C. carbonul nu are electroni":"Carbonul are electroni și participă la legături covalente.","D. molecula nu are legături":"CO₂ conține două legături covalente duble.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
_question("bond2_011","2.5","Legături sigma și pi","O legătură covalentă dublă este alcătuită din:",_opts("două legături sigma","două legături pi","o legătură sigma și una pi","o legătură sigma și două pi"),"C. o legătură sigma și una pi","O legătură dublă conține o componentă sigma și o componentă pi.",{"A. două legături sigma":"O legătură dublă are o singură componentă sigma.","B. două legături pi":"Orice legătură multiplă conține o componentă sigma.","D. o legătură sigma și două pi":"Aceasta este compoziția unei legături triple.","E. Niciuna dintre variantele A–D":"Varianta C este corectă."}),
_question("bond2_012","2.5","Legături sigma și pi","Câte legături pi conține o legătură triplă?",_opts("0","1","2","3"),"C. 2","O legătură triplă este alcătuită dintr-o legătură sigma și două legături pi.",{"A. 0":"O legătură triplă conține componente pi.","B. 1":"O legătură dublă conține o legătură pi.","D. 3":"A treia componentă este sigma, nu pi.","E. Niciuna dintre variantele A–D":"Varianta C este corectă."}),
_question("bond2_013","2.5","Ordinul legăturii","Comparativ cu o legătură simplă între aceeași pereche de atomi, o legătură triplă este în general:",_opts("mai lungă și mai slabă","mai scurtă și mai puternică","identică în lungime și tărie","fără electroni comuni"),"B. mai scurtă și mai puternică","Creșterea ordinului legăturii este, în general, asociată cu o distanță internucleară mai mică și o energie de disociere mai mare.",{"A. mai lungă și mai slabă":"Este tendința opusă celei generale.","C. identică în lungime și tărie":"Ordinul legăturii influențează lungimea și tăria.","D. fără electroni comuni":"Legătura covalentă implică electroni comuni.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
_question("bond2_014","2.6","Legătura coordinativă","În formarea ionului NH₄⁺ din NH₃ și H⁺, cine furnizează inițial ambii electroni ai perechii coordinative?",_opts("hidrogenul din H⁺","azotul din NH₃","un neutron","un electron din nucleu"),"B. azotul din NH₃","Azotul din NH₃ are o pereche neparticipantă pe care o donează protonului H⁺, acceptorul perechii.",{"A. hidrogenul din H⁺":"H⁺ nu are electroni; el acceptă perechea.","C. un neutron":"Neutronii nu participă la legături covalente.","D. un electron din nucleu":"Electronii de legătură provin din învelișul electronic, nu din nucleu.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
_question("bond2_015","2.6","Donor și acceptor","Pentru formarea unei legături coordinative, donorul trebuie să aibă:",_opts("o pereche de electroni disponibilă","un proton suplimentar în nucleu","doi neutroni liberi","electronegativitate zero"),"A. o pereche de electroni disponibilă","Donorul furnizează inițial ambii electroni ai perechii comune, de obicei dintr-o pereche neparticipantă.",{"B. un proton suplimentar în nucleu":"Numărul protonilor nu definește capacitatea de a dona o pereche electronică.","C. doi neutroni liberi":"Neutronii nu formează perechea de legătură.","D. electronegativitate zero":"Electronegativitatea zero nu este o condiție pentru donor.","E. Niciuna dintre variantele A–D":"Varianta A este corectă."}),
_question("bond2_016","2.7","Geometrie moleculară","Care este geometria moleculei CH₄?",_opts("liniară","unghiulară","piramidală trigonală","tetraedrică"),"D. tetraedrică","În CH₄, atomul de carbon are patru regiuni de legătură și nicio pereche neparticipantă; geometria este tetraedrică.",{"A. liniară":"Liniară este, de exemplu, geometria CO₂.","B. unghiulară":"Unghiulară este geometria H₂O.","C. piramidală trigonală":"Piramidală trigonală este geometria NH₃.","E. Niciuna dintre variantele A–D":"Varianta D este corectă."}),
_question("bond2_017","2.7","Geometrie moleculară","Care este geometria moleculei de apă, H₂O?",_opts("liniară","unghiulară","trigonal plană","tetraedrică regulată"),"B. unghiulară","Oxigenul are două perechi de legătură și două perechi neparticipante. Geometria moleculei, luând în considerare pozițiile atomilor, este unghiulară.",{"A. liniară":"Perechile neparticipante de pe oxigen conduc la o geometrie unghiulară.","C. trigonal plană":"Aceasta ar presupune trei regiuni electronice în jurul atomului central.","D. tetraedrică regulată":"Distribuția perechilor electronice este aproximativ tetraedrică, dar geometria moleculară nu este tetraedrică regulată deoarece două poziții sunt ocupate de perechi libere.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
_question("bond2_018","2.7","Polaritatea moleculei","Care dintre moleculele de mai jos este polară?",_opts("CO₂","CH₄","H₂O","BF₃"),"C. H₂O","H₂O are legături polare și geometrie unghiulară, astfel dipolii nu se compensează.",{"A. CO₂":"Este liniară și dipolii se compensează.","B. CH₄":"Este tetraedrică și simetrică, cu dipoli care se compensează.","D. BF₃":"Este trigonal plană și simetrică, iar dipolii se compensează.","E. Niciuna dintre variantele A–D":"Varianta C este corectă."}),
_question("bond2_019","2.8","Forțe London","Forțele de dispersie London:",_opts("apar numai între molecule polare","apar între toate particulele, inclusiv cele nepolare","sunt legături covalente","apar numai când există hidrogen legat de fluor"),"B. apar între toate particulele, inclusiv cele nepolare","Fluctuațiile temporare ale distribuției electronilor pot genera dipoli instantanei și dipoli induși; de aceea forțele London sunt prezente la toate particulele.",{"A. apar numai între molecule polare":"Ele apar și între atomi sau molecule nepolare.","C. sunt legături covalente":"Sunt interacțiuni intermoleculare, nu legături covalente intramoleculare.","D. apar numai când există hidrogen legat de fluor":"Aceasta descrie o condiție asociată legăturilor de hidrogen, nu forțele London.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
_question("bond2_020","2.8","Interacțiuni dipol–dipol","Interacțiunile dipol–dipol apar în principal între:",_opts("molecule polare","ioni pozitivi identici","molecule care nu au dipol permanent în nicio situație","nuclee atomice"),"A. molecule polare","Moleculele polare au dipoli permanenți care pot interacționa electrostatic.",{"B. ioni pozitivi identici":"Aceasta nu definește interacțiunea dipol–dipol dintre molecule.","C. molecule care nu au dipol permanent în nicio situație":"Interacțiunea dipol–dipol permanentă necesită molecule polare.","D. nuclee atomice":"Interacțiunile intermoleculare discutate sunt între molecule/particule, nu între nuclee izolate.","E. Niciuna dintre variantele A–D":"Varianta A este corectă."}),
_question("bond2_021","2.8","Legături de hidrogen","În care dintre substanțele următoare moleculele pot forma legături de hidrogen între ele?",_opts("CH₄","H₂O","CO₂","CCl₄"),"B. H₂O","În apă, hidrogenul este legat covalent de oxigen, iar moleculele vecine au perechi de electroni disponibile pe oxigen; se pot forma legături de hidrogen.",{"A. CH₄":"Legăturile C–H nu îndeplinesc condiția uzuală pentru legături de hidrogen puternice.","C. CO₂":"Molecula nu conține hidrogen.","D. CCl₄":"Molecula nu conține hidrogen.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
_question("bond2_022","2.8","Interacțiuni intermoleculare","Care interacțiune explică în mare măsură temperatura de fierbere neobișnuit de ridicată a apei comparativ cu molecule mici similare?",_opts("legăturile metalice","legăturile de hidrogen dintre molecule","legăturile ionice din moleculele de apă","lipsa interacțiunilor intermoleculare"),"B. legăturile de hidrogen dintre molecule","Moleculele de apă formează o rețea extinsă de legături de hidrogen, iar separarea moleculelor necesită energie.",{"A. legăturile metalice":"Apa moleculară nu are legături metalice.","C. legăturile ionice din moleculele de apă":"Legăturile O–H din molecula de apă sunt covalente polare.","D. lipsa interacțiunilor intermoleculare":"Apa are interacțiuni intermoleculare puternice.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
_question("bond2_023","2.9","Comparația legăturilor","Care afirmație despre legătura ionică este corectă?",_opts("este atracția dintre ioni cu sarcini opuse","implică întotdeauna două perechi de electroni comune","apare exclusiv între atomi identici","este același lucru cu legătura de hidrogen"),"A. este atracția dintre ioni cu sarcini opuse","Definiția legăturii ionice se bazează pe atracția electrostatică dintre cationi și anioni.",{"B. implică întotdeauna două perechi de electroni comune":"Aceasta nu definește legătura ionică; perechile comune caracterizează legătura covalentă.","C. apare exclusiv între atomi identici":"Compușii ionici sunt formați din ioni pozitivi și negativi, adesea proveniți din elemente diferite.","D. este același lucru cu legătura de hidrogen":"Legătura de hidrogen este o interacțiune specifică, intermoleculară sau intramoleculară.","E. Niciuna dintre variantele A–D":"Varianta A este corectă."}),
_question("bond2_024","2.9","Polaritate și geometrie","O moleculă are legături polare, dar este simetrică astfel încât toți dipolii de legătură se compensează. Molecula este:",_opts("neapărat ionică","nepolară","întotdeauna un radical","obligatoriu încărcată pozitiv"),"B. nepolară","Polaritatea moleculară depinde de suma vectorială a momentelor dipolare. Dacă se compensează, momentul dipolar molecular este zero.",{"A. neapărat ionică":"Polaritatea moleculară și caracterul ionic sunt concepte diferite.","C. întotdeauna un radical":"Radicalii sunt specii cu electroni nepereche; nu rezultă din compensarea dipolilor.","D. obligatoriu încărcată pozitiv":"O moleculă poate fi neutră și nepolară.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
_question("bond2_025","2.9","Formula ionică","Ce formulă rezultă din combinarea ionilor Al³⁺ și O²⁻ astfel încât compusul să fie neutru?",_opts("AlO","Al₂O₃","Al₃O₂","AlO₂"),"B. Al₂O₃","Cel mai mic multiplu comun al sarcinilor 3 și 2 este 6: doi ioni Al³⁺ dau +6, iar trei ioni O²⁻ dau −6.",{"A. AlO":"Sarcina totală ar fi +1.","C. Al₃O₂":"Sarcinile +9 și −4 nu se compensează.","D. AlO₂":"Sarcina totală ar fi −1.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."}),
_question("bond2_026","2.9","Interacțiuni intermoleculare","Care dintre următoarele afirmații este adevărată?",_opts("forțele London apar numai la moleculele nepolare","legăturile de hidrogen sunt legături covalente obișnuite H–O din interiorul moleculei","forțele London pot exista simultan cu interacțiuni dipol–dipol","moleculele polare nu au forțe London"),"C. forțele London pot exista simultan cu interacțiuni dipol–dipol","Forțele London sunt prezente la toate particulele, inclusiv la moleculele polare, unde pot coexista cu interacțiuni dipol–dipol.",{"A. forțele London apar numai la moleculele nepolare":"Ele apar la toate particulele.","B. legăturile de hidrogen sunt legături covalente obișnuite H–O din interiorul moleculei":"Legătura de hidrogen este o interacțiune între un H legat de un atom electronegativ și un acceptor, de obicei intermoleculară în exemplele introductive.","D. moleculele polare nu au forțe London":"Moleculele polare au și forțe London.","E. Niciuna dintre variantele A–D":"Varianta C este corectă."}),
_question("bond2_027","2.9","Tipuri de legături","Într-o legătură covalentă coordinativă, perechea comună de electroni:",_opts("provine inițial de la un singur atom donor","provine obligatoriu din doi protoni","este formată din doi neutroni","nu conține electroni"),"A. provine inițial de la un singur atom donor","Donorul furnizează inițial ambii electroni ai perechii, iar acceptorul pune la dispoziție un orbital/stare acceptoare.",{"B. provine obligatoriu din doi protoni":"Protonii nu sunt electronii perechii de legătură.","C. este formată din doi neutroni":"Neutronii nu formează legătura covalentă.","D. nu conține electroni":"Legătura este definită printr-o pereche de electroni.","E. Niciuna dintre variantele A–D":"Varianta A este corectă."}),
_question("bond2_028","2.9","Legături sigma și pi","Câte legături sigma și pi există în molecula N₂, dacă între atomii de azot este o legătură triplă?",_opts("3 σ și 0 π","1 σ și 2 π","2 σ și 1 π","0 σ și 3 π"),"B. 1 σ și 2 π","O legătură triplă este alcătuită dintr-o legătură sigma și două pi.",{"A. 3 σ și 0 π":"O legătură triplă nu conține trei componente sigma.","C. 2 σ și 1 π":"Aceasta nu este descompunerea corectă a unei legături triple.","D. 0 σ și 3 π":"Orice legătură multiplă conține o componentă sigma.","E. Niciuna dintre variantele A–D":"Varianta B este corectă."})
]
