"""Material didactic pentru Capitolul 4 – Legile gazelor.
Conținut original de pregătire, construit în jurul tematicii publicate pentru Candin Liteanu 2026.
Nu reprezintă subiecte oficiale; programa ediției 2027 trebuie verificată la publicare.
"""

CHAPTER4_LESSONS = [
{
"id":"gas_lesson_01","title":"4.1. Gazele și parametrii de stare","level":"Fundamente","official":"Legile gazelor: parametrii de stare",
"body":r"""
## 1. Ce este un gaz?

Gazul este o stare de agregare în care particulele sunt foarte mobile, se află la distanțe relativ mari unele de altele și ocupă întregul volum al recipientului. Gazele sunt compresibile și exercită presiune asupra pereților vasului.

## 2. Parametrii de stare

Starea unei cantități de gaz este descrisă prin patru mărimi uzuale:
- **Presiunea (p)** – forța exercitată pe unitatea de suprafață; unitatea SI este pascalul (Pa).
- **Volumul (V)** – spațiul ocupat; unitatea SI este metrul cub (m³).
- **Temperatura absolută (T)** – exprimată în kelvini (K).
- **Cantitatea de substanță (n)** – exprimată în moli (mol).

Pentru calcule, temperatura trebuie transformată în kelvini:

\[
T(K)=t(°C)+273,15
\]

Exemplu: 27 °C = 300,15 K.

## 3. Presiunea și unitățile

\[
1\,atm=101325\,Pa=101,325\,kPa
\]

\[
1\,bar=100000\,Pa
\]

În probleme, folosește unități compatibile în aceeași ecuație. Nu combina presiunea în atm cu o constantă a gazelor exprimată pentru Pa fără conversie.

## 4. Gaz ideal și gaz real

Gazul ideal este un model: particulele sunt considerate punctiforme, iar interacțiunile dintre ele sunt neglijabile, cu excepția ciocnirilor. Gazele reale se apropie de comportarea ideală la presiuni mici și temperaturi suficient de mari, în condiții obișnuite departe de condensare.

**Idee-cheie:** temperatura din ecuațiile gazelor este temperatura absolută, nu grade Celsius.
""",
"takeaways":["Parametrii de stare uzuali sunt p, V, T și n.","Temperatura se exprimă în kelvini în ecuațiile gazelor.","Gazul ideal este un model aproximativ, nu descrierea perfectă a oricărui gaz real.","Unitățile trebuie să fie compatibile."]
},
{
"id":"gas_lesson_02","title":"4.2. Temperatura absolută și transformări simple","level":"Fundamente – intermediar","official":"Parametrii de stare și transformări ale gazelor",
"body":r"""
## 1. Scara Kelvin

Scara Kelvin începe de la zero absolut. Conversia folosită în probleme este:

\[
T=t+273,15
\]

Diferențele de temperatură au aceeași valoare numerică în kelvini și grade Celsius, dar valorile absolute nu sunt interschimbabile.

## 2. Transformare izotermă

Temperatura rămâne constantă. Pentru o cantitate fixă de gaz ideal:

\[
pV=const.
\quad\Rightarrow\quad p_1V_1=p_2V_2
\]

Dacă volumul scade la jumătate, presiunea se dublează, la temperatură constantă.

## 3. Transformare izobară

Presiunea rămâne constantă:

\[
\frac{V}{T}=const.
\quad\Rightarrow\quad \frac{V_1}{T_1}=\frac{V_2}{T_2}
\]

Volumul este direct proporțional cu temperatura absolută, pentru aceeași cantitate de gaz și presiune constantă.

## 4. Transformare izocoră

Volumul rămâne constant:

\[
\frac{p}{T}=const.
\quad\Rightarrow\quad \frac{p_1}{T_1}=\frac{p_2}{T_2}
\]

Presiunea este direct proporțională cu temperatura absolută, pentru aceeași cantitate de gaz și volum constant.

## 5. Cum alegi relația?

Mai întâi identifică ce parametru rămâne constant:
- T constantă → relația pV;
- p constantă → relația V/T;
- V constant → relația p/T.

**Atenție:** rapoartele se calculează folosind kelvini.
""",
"takeaways":["Izotermă: T constantă și p₁V₁ = p₂V₂.","Izobară: p constantă și V₁/T₁ = V₂/T₂.","Izocoră: V constant și p₁/T₁ = p₂/T₂.","Temperaturile din rapoarte sunt în kelvini."]
},
{
"id":"gas_lesson_03","title":"4.3. Legea Boyle–Mariotte","level":"Intermediar – calcule","official":"Legile gazelor",
"body":r"""
## 1. Enunț

La temperatură constantă, pentru o cantitate fixă de gaz ideal, presiunea este invers proporțională cu volumul.

\[
pV=const.
\]

Prin urmare:

\[
p_1V_1=p_2V_2
\]

## 2. Interpretare

Dacă micșorăm volumul disponibil, particulele ajung mai des în contact cu pereții recipientului, iar presiunea crește. Dacă volumul se dublează, presiunea scade la jumătate, în condițiile legii.

## 3. Exemplu rezolvat

Un gaz ocupă 4,0 L la 150 kPa. Este comprimat izoterm până la 2,5 L. Determină presiunea finală.

\[
p_2=\frac{p_1V_1}{V_2}
=\frac{150\cdot4,0}{2,5}=240\,kPa
\]

Presiunea finală este 240 kPa.

## 4. Greșeli frecvente

- Nu folosi legea dacă temperatura sau cantitatea de gaz se schimbă.
- Păstrează aceleași unități de volum în ambele stări.
- Verifică sensul rezultatului: comprimarea izotermă trebuie să mărească presiunea.
""",
"takeaways":["Legea Boyle–Mariotte se aplică izoterm pentru cantitate fixă de gaz.","p₁V₁ = p₂V₂.","Presiunea și volumul variază invers proporțional.","La comprimare izotermă, presiunea crește."]
},
{
"id":"gas_lesson_04","title":"4.4. Legea Charles și legea Gay-Lussac","level":"Intermediar – calcule","official":"Legile gazelor",
"body":r"""
## 1. Legea Charles – transformare izobară

La presiune constantă, volumul unei cantități fixe de gaz ideal este direct proporțional cu temperatura absolută:

\[
\frac{V}{T}=const.
\quad\Rightarrow\quad \frac{V_1}{T_1}=\frac{V_2}{T_2}
\]

Exemplu: un gaz are 2,0 L la 300 K. La 450 K și aceeași presiune:

\[
V_2=2,0\cdot\frac{450}{300}=3,0\,L
\]

## 2. Legea Gay-Lussac – transformare izocoră

La volum constant, presiunea este direct proporțională cu temperatura absolută:

\[
\frac{p}{T}=const.
\quad\Rightarrow\quad \frac{p_1}{T_1}=\frac{p_2}{T_2}
\]

Exemplu: un gaz are 100 kPa la 300 K. Dacă temperatura crește la 360 K, volumul rămânând constant:

\[
p_2=100\cdot\frac{360}{300}=120\,kPa
\]

## 3. Atenție la denumiri

În unele manuale, denumirile legilor Charles și Gay-Lussac pot fi atribuite diferit. Pentru a evita confuzia, identifică întotdeauna condiția fizică și folosește relația corectă: la p constant V/T, la V constant p/T.

**Regulă de concurs:** nu memora doar numele legii; memorează parametrul constant și ecuația.
""",
"takeaways":["La presiune constantă, V/T este constant.","La volum constant, p/T este constant.","Se folosesc temperaturi absolute.","Identifică procesul fizic, indiferent de denumirea folosită în manual."]
},
{
"id":"gas_lesson_05","title":"4.5. Ecuația de stare a gazului ideal","level":"Intermediar – avansat","official":"Ecuația de stare a gazului ideal",
"body":r"""
## 1. Ecuația Clapeyron–Mendeleev

Relația care leagă presiunea, volumul, temperatura și cantitatea de substanță este:

\[
pV=nRT
\]

unde:
- p = presiunea;
- V = volumul;
- n = cantitatea de substanță;
- R = constanta universală a gazelor;
- T = temperatura absolută.

Valori uzuale ale lui R:
\[
R=8,314\,\frac{J}{mol\cdot K}
\]
sau
\[
R=0,082057\,\frac{L\cdot atm}{mol\cdot K}
\]

Alege valoarea lui R în funcție de unitățile presiunii și volumului.

## 2. Forme utile

\[
n=\frac{pV}{RT}
\qquad
V=\frac{nRT}{p}
\qquad
T=\frac{pV}{nR}
\]

## 3. Exemplu rezolvat

Ce volum ocupă 0,50 mol gaz ideal la 300 K și 1 atm?

\[
V=\frac{nRT}{p}
=\frac{0,50\cdot0,082057\cdot300}{1}
\approx12,31\,L
\]

## 4. Ecuația generală pentru două stări

Pentru aceeași cantitate de gaz:

\[
\frac{p_1V_1}{T_1}=\frac{p_2V_2}{T_2}
\]

Aceasta reunește relațiile transformărilor izotermă, izobară și izocoră.

**Verificare dimensională:** dacă folosești R = 0,082057, utilizează p în atm și V în litri.
""",
"takeaways":["Ecuația gazului ideal este pV = nRT.","Temperatura trebuie să fie în kelvini.","R = 8,314 J·mol⁻¹·K⁻¹ sau aproximativ 0,082057 L·atm·mol⁻¹·K⁻¹.","Pentru aceeași cantitate de gaz, pV/T rămâne constant."]
},
{
"id":"gas_lesson_06","title":"4.6. Volumul molar al gazelor","level":"Intermediar","official":"Volum molar",
"body":r"""
## 1. Definiție

Volumul molar \(V_m\) este volumul ocupat de un mol de substanță în condiții precizate:

\[
V_m=\frac{V}{n}
\]

Pentru un gaz ideal:

\[
V_m=\frac{RT}{p}
\]

Volumul molar depinde de temperatură și presiune. Nu există o singură valoare universală pentru toate condițiile.

## 2. Condiții normale și alte condiții

În convenția școlară frecventă, condițiile normale sunt 0 °C (273,15 K) și 1 atm; pentru gaz ideal:

\[
V_m\approx22,4\,L/mol
\]

La 25 °C și 1 atm, valoarea este aproximativ 24,5 L/mol. Verifică întotdeauna condițiile precizate în enunț sau valorile furnizate de organizatori.

## 3. Exemplu

Ce volum ocupă 2,0 mol gaz ideal în condiții normale, folosind 22,4 L/mol?

\[
V=nV_m=2,0\cdot22,4=44,8\,L
\]

## 4. Greșeală frecventă

Nu utiliza automat 22,4 L/mol dacă temperatura și presiunea nu corespund condițiilor pentru care este valabilă această valoare.
""",
"takeaways":["Volumul molar este V/n.","Volumul molar depinde de temperatură și presiune.","În convenția 0 °C și 1 atm, gazul ideal are aproximativ 22,4 L/mol.","Citește condițiile înainte de a alege volumul molar."]
},
{
"id":"gas_lesson_07","title":"4.7. Densitatea și masa molară a gazelor","level":"Intermediar – avansat","official":"Densitatea gazelor",
"body":r"""
## 1. Densitatea

Densitatea este masa raportată la volum:

\[
\rho=\frac{m}{V}
\]

Pentru un gaz ideal, pornind de la pV=nRT și n=m/M:

\[
\rho=\frac{pM}{RT}
\]

unde M este masa molară exprimată în unități compatibile (de exemplu kg/mol dacă folosești SI).

## 2. Legătura cu masa molară

La aceeași temperatură și presiune, densitatea gazului este direct proporțională cu masa sa molară. Un gaz cu masă molară mai mare are densitate mai mare în aceleași condiții, în modelul gazului ideal.

## 3. Densitatea relativă față de alt gaz

În aceleași condiții de temperatură și presiune:

\[
d_{A/B}=\frac{\rho_A}{\rho_B}=\frac{M_A}{M_B}
\]

Față de hidrogen:
\[
d_{A/H_2}=\frac{M_A}{2}
\]

Față de aer, se folosește frecvent masa molară medie aproximativă 29 g/mol în problemele școlare.

## 4. Exemplu rezolvat

Calculează densitatea dioxidului de carbon la 300 K și 1 atm. Folosim M = 44 g/mol = 0,044 kg/mol, R = 8,314 J·mol⁻¹·K⁻¹ și p = 101325 Pa.

\[
\rho=\frac{101325\cdot0,044}{8,314\cdot300}
\approx1,79\,kg/m^3
\]

## 5. Atenție la unități

Nu combina masa molară în g/mol cu R exprimată în J/(mol·K) fără conversie. În SI, folosește kg/mol, Pa, m³ și kelvini.
""",
"takeaways":["Densitatea este ρ = m/V.","Pentru gaz ideal, ρ = pM/(RT).","La aceeași temperatură și presiune, densitatea este proporțională cu masa molară.","Unitățile trebuie convertite coerent."]
},
{
"id":"gas_lesson_08","title":"4.8. Probleme integrate și strategie de concurs","level":"Concurs","official":"Aplicații: ecuația gazului ideal, volum molar și densitate",
"body":r"""
## 1. Algoritm pentru probleme

1. Notează datele și necunoscuta.
2. Transformă temperatura în kelvini.
3. Verifică unitățile pentru presiune și volum.
4. Stabilește dacă este aceeași cantitate de gaz sau dacă se modifică n.
5. Alege legea transformării sau ecuația pV=nRT.
6. Izolează necunoscuta și verifică dacă rezultatul are sens fizic.

## 2. Exemplu integrat

Un recipient rigid conține un gaz la 100 kPa și 300 K. Gazul este încălzit la 450 K, fără schimbarea volumului sau a cantității de gaz. Presiunea finală:

\[
p_2=p_1\frac{T_2}{T_1}
=100\cdot\frac{450}{300}=150\,kPa
\]

Recipient rigid înseamnă volum constant; folosim relația p/T = constant.

## 3. Exemplu cu ecuația gazului ideal

Un gaz ocupă 10,0 L la 200 kPa și 300 K. Folosind R = 8,314 kPa·L·mol⁻¹·K⁻¹:

\[
n=\frac{pV}{RT}
=\frac{200\cdot10,0}{8,314\cdot300}
\approx0,802\,mol
\]

Această valoare a lui R este exprimată în kPa·L/(mol·K), deoarece 1 kPa·L = 1 J.

## 4. Capcane tipice

- Celsius introdus direct în ecuație;
- confundarea transformării izobare cu cea izocoră;
- utilizarea lui 22,4 L/mol fără verificarea condițiilor;
- uitarea conversiei g/mol în kg/mol;
- utilizarea unei ecuații pentru o cantitate de gaz care nu rămâne constantă.

**Strategie:** identificarea condiției constante rezolvă adesea jumătate din problemă.
""",
"takeaways":["Începe prin conversia temperaturii și verificarea unităților.","Recipient rigid indică volum constant.","22,4 L/mol este valabil doar în condițiile corespunzătoare.","Verifică dacă n rămâne constant înainte de a folosi ecuația combinată."]
}
]

def q(id, lesson, topic, question, options, answer, explanation, option_explanations):
    return {"id":id,"domain":"Legile gazelor","lesson":lesson,"topic":topic,
            "question":question,"options":options,"answer":answer,
            "explanation":explanation,"option_explanations":option_explanations}

CHAPTER4_QUESTIONS = [
q("gas_01","4.1","Temperatura","Ce temperatură absolută corespunde aproximativ valorii de 27 °C?",
["A. 246 K","B. 273 K","C. 300 K","D. 310 K","E. Niciuna dintre variantele A–D"],"C. 300 K",
"T = 27 + 273,15 = 300,15 K, aproximativ 300 K.",
{"A":"Conversia a scăzut temperatura în loc să adauge 273,15.","B":"273 K corespunde aproximativ lui 0 °C.","D":"310 K corespunde aproximativ lui 37 °C."}),
q("gas_02","4.1","Unități","Care este unitatea SI pentru presiune?",
["A. litru","B. pascal","C. mol","D. kelvin","E. Niciuna dintre variantele A–D"],"B. pascal",
"Unitatea SI a presiunii este pascalul (Pa), echivalent cu N/m².",
{"A":"Litrul este unitate de volum.","C":"Molul măsoară cantitatea de substanță.","D":"Kelvinul măsoară temperatura."}),
q("gas_03","4.1","Gaz ideal","Modelul gazului ideal presupune că particulele:",
["A. au volum propriu foarte mare față de recipient","B. nu se mișcă","C. sunt în repaus permanent","D. nu interacționează decât prin ciocniri în modelul simplificat","E. Niciuna dintre variantele A–D"],"D. nu interacționează decât prin ciocniri în modelul simplificat",
"În modelul cinetic ideal, volumul propriu al particulelor este neglijabil, iar interacțiunile sunt neglijabile în afara ciocnirilor.",
{"A":"Volumul propriu este considerat neglijabil.","B":"Particulele se află în mișcare dezordonată continuă.","C":"Gazul nu este în repaus la nivel microscopic."}),
q("gas_04","4.2","Transformări","Ce parametru rămâne constant într-o transformare izotermă?",
["A. Presiunea","B. Volumul","C. Temperatura","D. Cantitatea de substanță se dublează","E. Niciuna dintre variantele A–D"],"C. Temperatura",
"Izoterm înseamnă temperatură constantă.",
{"A":"Aceasta este condiția unei transformări izobare.","B":"Aceasta este condiția unei transformări izocore.","D":"Nu definește o transformare izotermă."}),
q("gas_05","4.2","Transformări","Într-o transformare izobară a unei cantități fixe de gaz ideal, dacă temperatura Kelvin se dublează, volumul:",
["A. se înjumătățește","B. se dublează","C. rămâne constant","D. devine zero","E. Niciuna dintre variantele A–D"],"B. se dublează",
"La presiune constantă V/T este constant, deci dublarea lui T dublează V.",
{"A":"Ar indica o proporționalitate inversă, nu directă.","C":"Volumul variază cu temperatura la presiune constantă.","D":"Nu rezultă din legea izobară."}),
q("gas_06","4.2","Transformări","Într-o transformare izocoră, presiunea unui gaz ideal este:",
["A. invers proporțională cu temperatura Kelvin","B. independentă de temperatură","C. direct proporțională cu temperatura Kelvin","D. direct proporțională cu volumul","E. Niciuna dintre variantele A–D"],"C. direct proporțională cu temperatura Kelvin",
"La volum constant p/T este constant, deci p este direct proporțională cu T.",
{"A":"Relația este directă, nu inversă.","B":"Presiunea se modifică odată cu temperatura.","D":"Volumul este constant în această transformare."}),
q("gas_07","4.3","Boyle–Mariotte","Un gaz ocupă 6 L la 100 kPa. Este comprimat izoterm la 3 L. Presiunea finală este:",
["A. 50 kPa","B. 100 kPa","C. 150 kPa","D. 200 kPa","E. Niciuna dintre variantele A–D"],"D. 200 kPa",
"p₂ = p₁V₁/V₂ = 100·6/3 = 200 kPa.",
{"A":"Ar corespunde unei creșteri a volumului, nu comprimării.","B":"Presiunea nu poate rămâne aceeași când volumul se înjumătățește izoterm.","C":"Nu respectă produsul pV constant."}),
q("gas_08","4.3","Boyle–Mariotte","Pentru o transformare izotermă, produsul p·V:",
["A. crește mereu","B. scade mereu","C. este constant","D. este egal cu temperatura în °C","E. Niciuna dintre variantele A–D"],"C. este constant",
"Legea Boyle–Mariotte afirmă pV = constant pentru o cantitate fixă de gaz la temperatură constantă.",
{"A":"Nu este o creștere obligatorie; produsul rămâne constant.","B":"Nu este o scădere obligatorie; produsul rămâne constant.","D":"Nu există această egalitate."}),
q("gas_09","4.4","Legea izobară","Un gaz ocupă 4 L la 200 K. La presiune constantă este încălzit la 300 K. Volumul final este:",
["A. 2 L","B. 4 L","C. 5 L","D. 6 L","E. Niciuna dintre variantele A–D"],"D. 6 L",
"V₂ = V₁T₂/T₁ = 4·300/200 = 6 L.",
{"A":"Arată o variație inversă nejustificată.","B":"Volumul trebuie să crească odată cu T la presiune constantă.","C":"Nu rezultă din raportul temperaturilor."}),
q("gas_10","4.4","Legea izocoră","Un gaz are presiunea 120 kPa la 400 K. La volum constant și 300 K, presiunea devine:",
["A. 80 kPa","B. 90 kPa","C. 120 kPa","D. 160 kPa","E. Niciuna dintre variantele A–D"],"B. 90 kPa",
"p₂ = p₁T₂/T₁ = 120·300/400 = 90 kPa.",
{"A":"Calculul corect este 90 kPa.","C":"Presiunea nu rămâne constantă într-o transformare izocoră cu T schimbată.","D":"Ar corespunde creșterii temperaturii."}),
q("gas_11","4.5","Ecuația gazului ideal","Care este ecuația de stare a gazului ideal?",
["A. pV = nRT","B. p/T = nV","C. p + V = nRT","D. pV = RT/n","E. Niciuna dintre variantele A–D"],"A. pV = nRT",
"Ecuația Clapeyron–Mendeleev este pV = nRT.",
{"B":"Nu este ecuația de stare.","C":"Presiunea și volumul nu se adună în această relație.","D":"n trebuie să înmulțească RT, nu să împartă."}),
q("gas_12","4.5","Ecuația gazului ideal","Ce cantitate de substanță ocupă 24,6 L la 1 atm și 300 K? Folosește R = 0,082 L·atm·mol⁻¹·K⁻¹.",
["A. 0,5 mol","B. 1,0 mol","C. 1,5 mol","D. 2,0 mol","E. Niciuna dintre variantele A–D"],"B. 1,0 mol",
"n = pV/RT = 1·24,6/(0,082·300) = 24,6/24,6 = 1 mol.",
{"A":"Este jumătate din valoarea calculată.","C":"Este cu 50% mai mare decât rezultatul.","D":"Este dublul rezultatului corect."}),
q("gas_13","4.5","Constanta gazelor","Dacă folosești R = 0,082057 L·atm·mol⁻¹·K⁻¹, ce unități sunt potrivite pentru p și V?",
["A. Pa și m³","B. atm și L","C. kPa și m³","D. bar și cm³ fără conversie","E. Niciuna dintre variantele A–D"],"B. atm și L",
"Valoarea 0,082057 este exprimată în L·atm/(mol·K), deci p în atm și V în litri.",
{"A":"Pentru Pa și m³ este potrivit R = 8,314 J/(mol·K).","C":"Ar necesita o altă conversie sau constantă exprimată compatibil.","D":"Unitățile trebuie convertite coerent."}),
q("gas_14","4.6","Volum molar","Volumul molar este definit prin relația:",
["A. n/V","B. m/V","C. V/n","D. pV","E. Niciuna dintre variantele A–D"],"C. V/n",
"Volumul molar este volumul împărțit la cantitatea de substanță: Vₘ = V/n.",
{"A":"Este inversul volumului molar.","B":"Este densitatea masică.","D":"Nu este definiția volumului molar."}),
q("gas_15","4.6","Condiții normale","În convenția școlară 0 °C și 1 atm, volumul molar aproximativ al unui gaz ideal este:",
["A. 2,24 L/mol","B. 11,2 L/mol","C. 22,4 L/mol","D. 24,5 L/mol","E. Niciuna dintre variantele A–D"],"C. 22,4 L/mol",
"La 273,15 K și 1 atm, volumul molar ideal este aproximativ 22,4 L/mol.",
{"A":"Este de zece ori mai mic.","B":"Este jumătate din valoarea aproximativă.","D":"Aproximativ 24,5 L/mol corespunde mai degrabă la 25 °C și 1 atm."}),
q("gas_16","4.6","Volum molar","Ce volum ocupă 0,25 mol de gaz ideal în condițiile pentru care Vm = 22,4 L/mol?",
["A. 2,8 L","B. 5,6 L","C. 11,2 L","D. 22,4 L","E. Niciuna dintre variantele A–D"],"B. 5,6 L",
"V = nVm = 0,25·22,4 = 5,6 L.",
{"A":"Este jumătate din valoarea corectă.","C":"Este de două ori mai mare.","D":"Este volumul unui mol, nu al unui sfert de mol."}),
q("gas_17","4.7","Densitate","Densitatea unui gaz este:",
["A. V/m","B. m/V","C. n/V","D. M/T","E. Niciuna dintre variantele A–D"],"B. m/V",
"Densitatea masică este masa împărțită la volum.",
{"A":"Este volumul specific, inversul densității.","C":"Este concentrația molară, nu densitatea masică.","D":"Nu reprezintă definiția densității."}),
q("gas_18","4.7","Densitate","La aceeași temperatură și presiune, care gaz ideal are densitatea mai mare?",
["A. Cel cu masa molară mai mare","B. Cel cu masa molară mai mică","C. Toate au aceeași densitate","D. Cel cu numărul atomic mai mare în mod obligatoriu","E. Niciuna dintre variantele A–D"],"A. Cel cu masa molară mai mare",
"Din ρ = pM/(RT), la p și T constante, densitatea este direct proporțională cu masa molară.",
{"B":"Ar avea densitate mai mică, nu mai mare.","C":"Densitățile depind de masele molare.","D":"Numărul atomic nu determină singur masa molară a moleculei."}),
q("gas_19","4.7","Densitate","Ce masă molară are un gaz cu densitatea relativă față de H₂ egală cu 16?",
["A. 8 g/mol","B. 16 g/mol","C. 24 g/mol","D. 32 g/mol","E. Niciuna dintre variantele A–D"],"D. 32 g/mol",
"d(gaz/H₂) = M(gaz)/M(H₂); M(gaz) = 16·2 = 32 g/mol.",
{"A":"A împărțit factorul 16 la 2, în loc să îl înmulțească.","B":"A omis masa molară a hidrogenului molecular.","C":"Nu rezultă din relația densităților relative."}),
q("gas_20","4.7","Densitate","În relația ρ = pM/(RT), dacă se utilizează unități SI, masa molară M trebuie exprimată în:",
["A. g/mol","B. kg/mol","C. g/L","D. mol/kg","E. Niciuna dintre variantele A–D"],"B. kg/mol",
"Pentru p în Pa, R în J/(mol·K), iar densitatea în kg/m³, M trebuie exprimată în kg/mol.",
{"A":"Ar produce un factor 1000 de eroare dacă nu se convertește.","C":"Aceasta este unitate de densitate, nu de masă molară.","D":"Este inversul unității de masă molară."}),
q("gas_21","4.8","Problemă integrată","Un gaz într-un recipient rigid este încălzit de la 250 K la 500 K. Presiunea inițială este 80 kPa. Presiunea finală este:",
["A. 40 kPa","B. 80 kPa","C. 120 kPa","D. 160 kPa","E. Niciuna dintre variantele A–D"],"D. 160 kPa",
"Volumul și cantitatea sunt constante, deci p₂ = 80·500/250 = 160 kPa.",
{"A":"Ar presupune scăderea temperaturii la jumătate.","B":"Presiunea se modifică proporțional cu temperatura Kelvin.","C":"Nu respectă raportul 500/250 = 2."}),
q("gas_22","4.8","Problemă integrată","Un gaz ideal are p = 100 kPa, V = 5,0 L și T = 300 K. Folosind R = 8,314 kPa·L·mol⁻¹·K⁻¹, n este aproximativ:",
["A. 0,10 mol","B. 0,20 mol","C. 0,50 mol","D. 2,0 mol","E. Niciuna dintre variantele A–D"],"B. 0,20 mol",
"n = pV/(RT) = 500/(8,314·300) ≈ 0,200 mol.",
{"A":"Este aproximativ jumătate din rezultat.","C":"Este de 2,5 ori mai mare.","D":"Este de zece ori mai mare."}),
q("gas_23","4.2","Conversii","La ce temperatură Kelvin corespund 0 °C?",
["A. 0 K","B. 100 K","C. 273,15 K","D. 373,15 K","E. Niciuna dintre variantele A–D"],"C. 273,15 K",
"T(K) = t(°C) + 273,15; pentru 0 °C rezultă 273,15 K.",
{"A":"Zero kelvin este zero absolut, nu 0 °C.","B":"Nu respectă conversia.","D":"Corespunde aproximativ lui 100 °C."}),
q("gas_24","4.3","Boyle–Mariotte","Un gaz este comprimat izoterm de la 8 L la 2 L. Presiunea finală este de câte ori mai mare decât cea inițială?",
["A. De 2 ori","B. De 3 ori","C. De 4 ori","D. De 8 ori","E. Niciuna dintre variantele A–D"],"C. De 4 ori",
"p₂/p₁ = V₁/V₂ = 8/2 = 4.",
{"A":"Ar corespunde unei reduceri a volumului la jumătate.","B":"Raportul real este 4.","D":"Raportul volumelor este 4, nu 8."}),
q("gas_25","4.4","Legea izobară","La presiune constantă, un gaz se răcește de la 400 K la 200 K. Volumul:",
["A. se dublează","B. se înjumătățește","C. rămâne constant","D. crește de patru ori","E. Niciuna dintre variantele A–D"],"B. se înjumătățește",
"V₂/V₁ = T₂/T₁ = 200/400 = 1/2.",
{"A":"Ar fi cazul încălzirii de la 200 K la 400 K.","C":"Volumul variază direct cu temperatura la presiune constantă.","D":"Nu rezultă din raportul temperaturilor."}),
q("gas_26","4.5","Ecuația gazului ideal","Dacă n și T rămân constante, iar volumul se triplează, presiunea:",
["A. se triplează","B. se înjumătățește","C. scade la o treime","D. rămâne constantă","E. Niciuna dintre variantele A–D"],"C. scade la o treime",
"Din pV = nRT, la n și T constante, p este invers proporțională cu V.",
{"A":"Presiunea variază invers, nu direct cu volumul.","B":"Ar fi corect dacă volumul s-ar dubla.","D":"Presiunea se schimbă când volumul se schimbă."}),
q("gas_27","4.6","Volum molar","La aceeași presiune, dacă temperatura absolută crește, volumul molar al gazului ideal:",
["A. scade","B. crește","C. rămâne constant","D. devine independent de presiune și temperatură","E. Niciuna dintre variantele A–D"],"B. crește",
"Vm = RT/p; la p constant, Vm este direct proporțional cu T.",
{"A":"Contrazice relația Vm = RT/p.","C":"Volumul molar depinde de temperatură.","D":"Volumul molar depinde de p și T."}),
q("gas_28","4.7","Densitate relativă","Densitatea relativă a unui gaz A față de gazul B, la aceeași temperatură și presiune, este egală cu:",
["A. M_B/M_A","B. M_A/M_B","C. M_A+M_B","D. M_A·M_B","E. Niciuna dintre variantele A–D"],"B. M_A/M_B",
"La aceeași T și p, raportul densităților este egal cu raportul maselor molare.",
{"A":"Raportul este inversat.","C":"Masele molare nu se adună în această relație.","D":"Nu este un raport de densități."}),
q("gas_29","4.8","Alegerea legii","Un piston mobil menține presiunea gazului constantă. Ce relație descrie legătura dintre volum și temperatura absolută?",
["A. pV = constant","B. V/T = constant","C. p/T = constant","D. V·T = constant","E. Niciuna dintre variantele A–D"],"B. V/T = constant",
"Pistonul mobil menține presiunea constantă; pentru cantitate fixă de gaz ideal, V/T este constant.",
{"A":"Este relația izotermă, pentru T constantă.","C":"Este relația izocoră, pentru V constant.","D":"Nu este legea transformării izobare."}),
q("gas_30","4.8","Problemă integrată","Un gaz are volumul 10 L la 300 K. Este încălzit la 600 K la presiune constantă. Volumul final este:",
["A. 5 L","B. 10 L","C. 15 L","D. 20 L","E. Niciuna dintre variantele A–D"],"D. 20 L",
"V₂ = V₁T₂/T₁ = 10·600/300 = 20 L.",
{"A":"Ar rezulta din folosirea raportului invers.","B":"Volumul nu rămâne constant la presiune constantă și temperatură dublată.","C":"Nu rezultă din proporționalitatea directă."})
]
