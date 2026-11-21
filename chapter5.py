# Material original de antrenament; nu reprezintă subiecte oficiale.
DOMAIN = 'Procese de oxidare și reducere'

CHAPTER5_LESSONS = [
    {
        'id': 'redox_lesson_01',
        'number': '5.1',
        'title': '5.1. Numărul de oxidare: definiție și reguli',
        'level': 'Fundamente',
        'official': 'Numărul de oxidare și regulile de atribuire',
        'objectives': ['Să poți defini numărul de oxidare ca instrument formal',
 'Să poți aplica regulile pentru substanțe simple și compuși',
 'Să poți deosebi numărul de oxidare de sarcina reală a atomului'],
        'body': r"""## Explicație teoretică
### Un model de contabilizare a electronilor
Numărul de oxidare (N.O.) este sarcina formală atribuită unui atom dacă electronii fiecărei legături heteronucleare ar aparține complet atomului mai electronegativ. Electronii unei legături între atomi identici se împart egal. Această convenție permite urmărirea electronilor fără a presupune că orice substanță este ionică. În apă, oxigenului i se atribuie −II, dar molecula nu conține obligatoriu un ion oxid izolat. N.O. este un număr fără unitate, cu semn; îl notăm uzual prin cifre romane în text și numere cu semn în calcule.
### Ordinea regulilor
În substanțe simple, fiecare atom are N.O. zero: Fe, H₂, O₂, O₃ și S₈. Într-un ion monoatomic, N.O. coincide cu numărul de sarcini elementare: pentru Fe³⁺ este +III. În compușii uzuali, metalele alcaline au +I, iar cele alcalino-pământoase +II. Fluorul are −I în compuși. Oxigenul este de obicei −II, dar în peroxizi este −I; în OF₂ are +II, fiind mai puțin electronegativ decât fluorul. Hidrogenul este de obicei +I, dar în hidrurile metalice are −I.
### Regula globală
Suma numerelor de oxidare ale tuturor atomilor, cu multiplicitățile lor, este zero într-o specie neutră și egală cu sarcina unui ion. Nu aduni doar valorile elementelor distincte: în apă există doi atomi de hidrogen. Pentru ioni poliatomici, parantezele și indicii aparțin compoziției, în timp ce sarcina scrisă sus privește întregul ion. Aplici mai întâi regulile sigure, apoi determini necunoscuta din sumă.

## Definiții și concepte importante
- **Număr de oxidare**: sarcină formală atribuită printr-o convenție de electronegativitate.
- **Substanță simplă**: specie alcătuită dintr-un singur element; N.O. este zero.
- **Ion monoatomic**: un singur atom cu sarcină; N.O. este numărul său de sarcini elementare.
- **Electroneutralitate**: suma algebrică a sarcinilor unei specii neutre este zero.

## Formule și relații
$$\sum_i n_i x_i=q$$
Aici $n_i$ este numărul atomilor de tip $i$ din specie, $x_i$ este N.O. al acestora, iar $q$ este numărul algebric de sarcini elementare al speciei; toate sunt fără unitate. Relația folosește un singur $x_i$ numai dacă atomii respectivi au aceeași stare formală sau dacă se cere media.

$$2(+1)+x=0\quad\Rightarrow\quad x=-2$$
În această aplicare la H₂O, 2 este numărul atomilor H, +1 este N.O. al H, iar $x$ este N.O. al O; niciun termen nu are unitate.

## Exemple rezolvate pas cu pas
### Exemplul 1 – Apa și substanțele simple
1. În H₂O, alegem H cu +I, deoarece nu este hidrură metalică.
2. Notăm cu $x$ N.O. al O: $2(+1)+x=0$, deci $x=-2$.
3. În H₂ și O₂, legăturile sunt între atomi identici; N.O. este zero pentru ambele elemente, nu +I sau −II.
4. La formarea apei, patru atomi H își cresc N.O. cu o unitate, iar doi atomi O îl scad cu două unități. Bilanțul formal este 4 electroni cedați și 4 acceptați.


$$\mathrm{2H_{2} + O_{2} \rightarrow 2H_{2}O}$$

### Exemplul 2 – Azotul din ionul amoniu
1. Specia NH₄⁺ are patru H cu +I; nu confundăm sarcina totală +1 cu N.O. al N.
2. Scriem $x+4(+1)=+1$.
3. Rezultă $x=1-4=-3$, deci N are −III.
4. Verificarea sumei dă $-3+4=+1$, exact sarcina ionului. Legăturile covalente nu invalidează această contabilizare formală.

## Interpretarea rezultatelor
Un N.O. negativ arată atribuirea formală a unui exces de electroni față de atomul neutru, nu numărul de electroni liberi din moleculă. În amoniu, un atom cu N.O. negativ aparține unui ion global pozitiv: nu există contradicție, deoarece cele patru valori pozitive ale hidrogenului domină suma. Verificarea finală trebuie să compare suma cu sarcina speciei, nu automat cu zero. Pentru a decide dacă există o reacție redox, vei compara N.O. înainte și după reacție, nu vei căuta doar ioni în enunț.""",
        'mistakes': ['Greșeala: consideri N.O. o sarcină reală în orice moleculă → Cum o eviți: folosește definiția formală',
 'Greșeala: atribui O mereu −II → Cum o eviți: caută peroxizi și compuși cu fluor',
 'Greșeala: egalezi suma cu zero pentru ioni → Cum o eviți: citește sarcina totală'],
        'takeaways': ['N.O. este o convenție formală.',
 'În substanțe simple N.O. este zero.',
 'Ionii monoatomici au N.O. egal cu sarcina numerică.',
 'Suma ponderată reproduce sarcina speciei.'],
        'connections': ['Lecția 5.2 – excepții și medii ale numerelor de oxidare.'],
    },
    {
        'id': 'redox_lesson_02',
        'number': '5.2',
        'title': '5.2. Calculul numerelor de oxidare în compuși',
        'level': 'Intermediar – calcule',
        'official': 'Determinarea numerelor de oxidare în compuși și ioni',
        'objectives': ['Să poți calcula N.O. în ioni poliatomici',
 'Să poți recunoaște peroxizii și hidrurile metalice',
 'Să poți interpreta corect valori medii fracționare'],
        'body': r"""## Explicație teoretică
### Alegerea necunoscutei
O formulă chimică oferă proporții de atomi, nu automat structura. Pentru SO₄²⁻, regula oxigenului uzual și sarcina ionului determină N.O. al sulfului. Pentru H₂O₂, aplicarea mecanică a valorii −II pentru O ar încălca electroneutralitatea; prezența grupei peroxid justifică −I. În NaH, metalul alcalin are +I, deci hidrogenul este −I. Nu schimba arbitrar regula metalului pentru a păstra hidrogenul pozitiv.
### N.O. mediu și atomi neechivalenți
Când atomii aceluiași element nu au toți aceeași stare, ecuația globală dă o medie ponderată. În Fe₃O₄, oxigenul cu −II impune suma +8 pentru trei Fe; media este +8/3. Descrierea formală uzuală este un Fe(II) și doi Fe(III) per unitate de formulă. Media fracționară nu dovedește existența unor ioni izolați cu sarcina +8/3 și nu descrie în detaliu distribuția electronică în solid.
În tetrationat, S₄O₆²⁻, oxigenii au −II, deci cei patru atomi S au suma +10 și media +2,5. Structura cu un lanț de patru atomi de sulf și câte trei oxigeni la capete permite atribuirea +V atomilor terminali și 0 celor doi centrali. Legăturile S–S nu contribuie la diferența de N.O., deoarece sunt homonucleare. Formula singură oferă media, nu localizarea tuturor stărilor.
### Procedură reproductibilă
Transcrie mai întâi specia cu sarcina ei. Marchează regulile certe, numără atomii, scrie suma și rezolvă. Dacă rezultatul este neobișnuit, verifică dacă este o excepție sau o medie; nu rotunji N.O. pentru a obține un întreg. Media are sens de contabilitate și poate servi la bilanț doar cu multiplicitatea corectă.

## Definiții și concepte importante
- **Peroxid**: compus cu grupare O–O în care O are N.O. −I.
- **Hidrură metalică**: compus în care H are formal −I.
- **N.O. mediu**: suma N.O. pentru atomii unui element împărțită la numărul lor.
- **Valență mixtă**: descriere formală cu mai multe stări de oxidare ale aceluiași element.

## Formule și relații
$$\overline{x}=\frac{q-\sum_j n_j x_j}{n}$$
$\overline{x}$ este N.O. mediu al elementului urmărit, $q$ este sarcina numerică totală, $n$ este numărul atomilor săi, iar $n_j$ și $x_j$ sunt numărul și N.O. atomilor celorlalte elemente. Toate mărimile sunt fără unitate.

$$x_{\mathrm O}(\mathrm{H_2O_2})=-1,\qquad x_{\mathrm H}(\mathrm{NaH})=-1$$
$x$ reprezintă N.O., iar indicii identifică elementul; valorile sunt fără unitate și se aplică speciilor indicate, nu tuturor compușilor lor.

## Exemple rezolvate pas cu pas
### Exemplul 1 – Sulfat și permanganat
1. Pentru SO₄²⁻, scriem $x+4(-2)=-2$.
2. Obținem $x=+6$ pentru S; verificarea este $6-8=-2$.
3. Pentru MnO₄⁻, scriem $y+4(-2)=-1$, deci $y=+7$.
4. Ambii ioni au patru O, dar sarcini diferite, deci atomii centrali nu au aceeași valoare.
### Exemplul 2 – Două medii fracționare
1. În Fe₃O₄, $3x+4(-2)=0$, deci $x=8/3$.
2. Verificăm descrierea formală: $2+3+3=8$ și $8-8=0$.
3. În S₄O₆²⁻, $4y+6(-2)=-2$, deci $4y=10$ și $y=2{,}5$.
4. Cu structura precizată în teorie, $5+0+0+5=10$. Rezultatul nu înseamnă că fiecare S este în starea +2,5.
### Exemplul 3 – Excepțiile nu sunt opționale
1. În H₂O₂, $2(+1)+2x=0$ dă $x=-1$.
2. În NaH, $(+1)+y=0$ dă $y=-1$.
3. În OF₂, $z+2(-1)=0$ dă $z=+2$ pentru O.

## Interpretarea rezultatelor
Media +8/3 se păstrează exact, nu se înlocuiește cu +III. Rotunjirea ar introduce o sarcină totală greșită în oxidul neutru. În tetrationat, suma stărilor este mai robustă decât o atribuire individuală făcută fără structură. Pentru un bilanț redox ulterior, patru atomi cu media +2,5 au aceeași sumă inițială +10, dar reacția poate implica transformări diferite la capete și în centru. Așadar, distinge ceea ce rezultă strict din formulă de ceea ce necesită informație structurală.""",
        'mistakes': ['Greșeala: rotunjești +8/3 la +III → Cum o eviți: păstrează fracția exactă',
 'Greșeala: atribui fiecărui S valoarea medie → Cum o eviți: separă media de stările locale',
 'Greșeala: tratezi NaH ca acid → Cum o eviți: recunoaște hidrura metalică'],
        'takeaways': ['Sulfatul are S(+VI).',
 'Peroxizii au O(−I).',
 'Hidrurile metalice au H(−I).',
 'Fe₃O₄ are media +8/3 pentru Fe.',
 'Tetrationatul are media +2,5 pentru S.'],
        'connections': ['Lecția 5.1 – suma N.O. și sarcina speciei.', 'Lecția 5.6 – bilanț cu multiplicități.'],
    },
    {
        'id': 'redox_lesson_03',
        'number': '5.3',
        'title': '5.3. Oxidarea și reducerea: transferul de electroni',
        'level': 'Fundamente',
        'official': 'Oxidare, reducere și bilanț electronic',
        'objectives': ['Să poți asocia oxidarea cu cedarea de electroni',
 'Să poți scrie semireacții simple cu sarcini',
 'Să poți stabili raportul molar din transferul electronic'],
        'body': r"""## Explicație teoretică
### Două procese inseparabile
Oxidarea este cedare de electroni și creștere a N.O.; reducerea este acceptare de electroni și scădere a N.O. Într-un proces global închis din punct de vedere electronic, electronii cedați trebuie acceptați de altă specie. De aceea cele două transformări apar împreună. Sensul istoric de combinare cu oxigen este util doar pentru unele exemple; definiția prin electroni acoperă și reacții fără oxigen.
### Semireacția este o contabilitate
O semireacție arată explicit electronii. La oxidare, electronii sunt în dreapta, iar la reducere în stânga. Ea trebuie să conserve atomii și sarcina. O semireacție izolată nu este neapărat o transformare care poate fi realizată singură într-un pahar: are nevoie de cuplare cu procesul complementar sau cu un circuit exterior.
### Raportul stoechiometric
Dacă un atom cedează doi electroni și altul acceptă un electron, ai nevoie de doi acceptori pentru un donor. Coeficienții se aleg prin cel mai mic multiplu comun al numerelor de electroni. Nu se adună electroni în ecuația finală: după egalarea semireacțiilor ei se simplifică. Această anulare exprimă conservarea electronilor, nu dispariția lor fizică.
În reacțiile moleculare, transferul este adesea o convenție formală; nu implică întotdeauna electroni liberi care traversează soluția. Într-o pilă, separarea spațială a semireacțiilor permite circulația electronilor prin conductorul exterior. Distincția între bilanț formal și mecanism previne interpretările excesive ale ecuației.

## Definiții și concepte importante
- **Oxidare**: creștere a N.O., asociată cedării de electroni.
- **Reducere**: scădere a N.O., asociată acceptării de electroni.
- **Semireacție**: ecuație pentru una dintre cele două transformări electronice.
- **Bilanț electronic**: egalitatea cantităților de electroni cedați și acceptați.

## Formule și relații
$$n_{e,\mathrm{cedați}}=n_{e,\mathrm{acceptați}},\qquad n_e=z\,n$$
$n_e$ este cantitatea de electroni în mol, $n$ cantitatea de specie în mol, iar $z$ numărul de electroni transferați per particulă (fără unitate). Pentru o specie cu mai mulți atomi reactivi, $z$ include toate variațiile de N.O. relevante.

$$\Delta x=x_f-x_i$$
$x_i$ și $x_f$ sunt N.O. inițial și final; $\Delta x$ este variația lor, fără unitate. Semnul pozitiv arată oxidare; numărul electronilor transferați folosește modulul variației.

## Exemple rezolvate pas cu pas
### Exemplul 1 – Zinc în soluție cu ioni de cupru
1. Zn trece de la 0 la +II: cedează doi electroni.


$$\mathrm{Zn \rightarrow Zn^{2+} + 2e^{-}}$$

2. Cu trece de la +II la 0: acceptă doi electroni.


$$\mathrm{Cu^{2+} + 2e^{-} \rightarrow Cu}$$

3. Semireacțiile au deja același număr de electroni. Le adunăm:


$$\mathrm{Zn + Cu^{2+} \rightarrow Zn^{2+} + Cu}$$

4. Un mol Zn corespunde unui mol Cu²⁺. Sarcina totală este +2 în fiecare membru; numărul atomilor din fiecare element se conservă.
### Exemplul 2 – Fier(II) și un acceptor de cinci electroni
1. Pentru Fe²⁺ care devine Fe³⁺, variația este $3-2=1$.


$$\mathrm{Fe^{2+} \rightarrow Fe^{3+} + e^{-}}$$

2. Reducerea unui ion MnO₄⁻ la Mn²⁺ în acid cere cinci electroni, deoarece $7-2=5$.
3. Sunt necesari cinci ioni Fe²⁺ pentru fiecare ion MnO₄⁻. Pentru 0,020 mol permanganat se consumă $5\cdot0{,}020=0{,}100$ mol Fe²⁺.
4. Bilanțul este 0,100 mol electroni de ambele părți. Apa și protonii necesari ecuației complete se introduc în lecția 5.7.

## Interpretarea rezultatelor
În primul exemplu, masa cuprului depus nu trebuie confundată cu masa zincului consumat: cantitățile sunt egale în mol, dar masele molare diferă. În al doilea exemplu, raportul 5:1 provine din variațiile N.O., nu din sarcinile inițiale luate separat. Fe²⁺ nu cedează doi electroni pentru a deveni Fe³⁺, ci unul. Verificarea sarcinii unei semireacții este obligatorie: în oxidarea fierului, +2 în stânga este egal cu +3−1 în dreapta. Scrierea unui electron în membrul greșit ar încălca imediat această egalitate.""",
        'mistakes': ['Greșeala: confunzi oxidarea cu acceptarea → Cum o eviți: urmărește creșterea N.O.',
 'Greșeala: folosești sarcina inițială ca număr de electroni → Cum o eviți: calculează diferența final minus '
 'inițial',
 'Greșeala: lași electroni în ecuația globală → Cum o eviți: egalează-i înainte de adunare'],
        'takeaways': ['Oxidarea cedează electroni.',
 'Reducerea acceptă electroni.',
 'Semireacțiile conservă și sarcina.',
 'Coeficienții rezultă din egalarea electronilor.'],
        'connections': ['Lecția 5.7 – semireacții cu apă și protoni.'],
    },
    {
        'id': 'redox_lesson_04',
        'number': '5.4',
        'title': '5.4. Agenți oxidanți și agenți reducători',
        'level': 'Intermediar',
        'official': 'Oxidanți și reducători uzuali; influența mediului',
        'objectives': ['Să poți identifica agentul care se reduce',
 'Să poți explica dublul caracter al peroxidului de hidrogen',
 'Să poți corela mediul cu produsul de reducere al permanganatului'],
        'body': r"""## Explicație teoretică
### Agentul provoacă procesul complementar
Oxidantul acceptă electroni și se reduce; el provoacă oxidarea partenerului. Reducătorul cedează electroni și se oxidează. Numele agentului nu descrie transformarea pe care o suferă el, ci efectul asupra partenerului. Un N.O. ridicat sugerează uneori un oxidant, dar singur nu garantează reacția în orice condiții: contează mediul, partenerul și condițiile experimentale.
### Exemple uzuale și limite
KMnO₄ și K₂Cr₂O₇ sunt oxidanți frecvenți, de regulă utilizați în mediu acid pentru reducerile la Mn²⁺ și Cr³⁺. HNO₃ este acid oxidant: azotul(+V) se poate reduce, iar hidrogenul acidului nu formează obligatoriu H₂ în reacția cu un metal. Metalele active sunt reducători prin trecerea la cationi. H₂, C și CO pot reduce oxizi metalici în condiții adecvate, adesea la încălzire; nu presupunem că reduc orice oxid.
### Permanganatul depinde de mediu
În acid suficient, Mn(+VII) ajunge uzual la Mn(+II), cu cinci electroni acceptați. În mediu neutru sau slab bazic, produsul frecvent este MnO₂, cu Mn(+IV) și trei electroni acceptați. În mediu puternic bazic, în condiții care stabilizează manganatul și cu reducere controlată, se poate obține MnO₄²⁻, cu Mn(+VI) și un electron acceptat. Bazicitatea nu garantează singură oprirea la manganat: contează și reducătorul.
### Peroxidul: starea intermediară
Oxigenul din H₂O₂ are −I. Poate coborî la −II în apă, caz în care peroxidul este oxidant, sau poate urca la 0 în O₂, caz în care este reducător. Identificăm rolul numai după produsul său, nu după numele substanței.

## Definiții și concepte importante
- **Oxidant**: specie care acceptă electroni și se reduce.
- **Reducător**: specie care cedează electroni și se oxidează.
- **Dublu caracter redox**: posibilitatea de a funcționa ca oxidant sau reducător în reacții diferite.
- **Mediu de reacție**: condiții, inclusiv aciditate, care influențează speciile și produșii.

## Formule și relații
$$z_{\mathrm{Mn}}=7-x_f$$
$z_{\mathrm{Mn}}$ este numărul de electroni acceptați per ion permanganat, fără unitate, iar $x_f$ este N.O. final al Mn, tot fără unitate. Pentru $x_f=2,4,6$ rezultă, respectiv, 5, 3 și 1 electroni.


$$\mathrm{MnO_{4}^{-} + 8H^{+} + 5e^{-} \rightarrow Mn^{2+} + 4H_{2}O}$$



$$\mathrm{MnO_{4}^{-} + 2H_{2}O + 3e^{-} \rightarrow MnO_{2} + 4OH^{-}}$$



$$\mathrm{MnO_{4}^{-} + e^{-} \rightarrow MnO_{4}^{2-}}$$

Coeficienții sunt numere stoechiometrice fără unitate; H⁺ indică protonii, OH⁻ ionii hidroxid, iar e⁻ electronii. Fiecare ecuație conservă atomii și sarcina.

## Exemple rezolvate pas cu pas
### Exemplul 1 – Alegerea rolului H₂O₂
1. În reducerea peroxidului la apă, O trece de la −I la −II. Doi atomi acceptă în total doi electroni; H₂O₂ este oxidant.


$$\mathrm{H_{2}O_{2} + 2H^{+} + 2e^{-} \rightarrow 2H_{2}O}$$

2. În oxidarea peroxidului la oxigen, O trece de la −I la 0. Doi atomi cedează doi electroni; H₂O₂ este reducător.


$$\mathrm{H_{2}O_{2} \rightarrow O_{2} + 2H^{+} + 2e^{-}}$$

3. Cu permanganat acid, se aplică al doilea rol. Nu atribuim ambilor reactanți rol de oxidant.
### Exemplul 2 – CO la reducerea unui oxid
1. În Fe₂O₃, Fe este +III; în fierul metalic este 0. Doi Fe acceptă șase electroni.


$$\mathrm{Fe_{2}O_{3} + 3CO \rightarrow 2Fe + 3CO_{2}}$$

2. În CO, C este +II, iar în CO₂ este +IV. Fiecare C cedează doi electroni; trei CO cedează șase.
3. CO este reducătorul, iar oxidul de fier este oxidantul. Raportul 1:3 se confirmă prin cei șase electroni și prin cei șase atomi O în fiecare membru.

## Interpretarea rezultatelor
Culoarea violetă a permanganatului poate dispărea prin formarea ionului Mn²⁺ în soluție acidă; apariția unui solid brun sugerează MnO₂ și un bilanț diferit. Observația experimentală susține alegerea produsului, dar nu înlocuiește datele explicite ale problemei. Nu folosi automat factorul de cinci electroni dacă mediul este bazic. Dublul caracter al H₂O₂ arată de ce un tabel de substanțe „mereu oxidante” sau „mereu reducătoare” este prea simplist pentru rezolvarea problemelor.""",
        'mistakes': ['Greșeala: numești oxidant specia care se oxidează → Cum o eviți: urmărește acceptarea electronilor',
 'Greșeala: folosești mereu cinci electroni pentru permanganat → Cum o eviți: precizează produsul și mediul',
 'Greșeala: consideri H₂O₂ doar oxidant → Cum o eviți: verifică N.O. final al O'],
        'takeaways': ['Oxidantul se reduce.',
 'Reducătorul se oxidează.',
 'H₂O₂ are dublu caracter.',
 'Permanganatul acceptă 5, 3 sau 1 electroni în transformările indicate.',
 'Mediul și partenerul determină produsul.'],
        'connections': ['Lecția 5.8 – bilanțuri în mediu bazic.'],
    },
    {
        'id': 'redox_lesson_05',
        'number': '5.5',
        'title': '5.5. Recunoașterea reacțiilor REDOX',
        'level': 'Intermediar',
        'official': 'Identificarea reacțiilor redox; disproporționare și comproporționare',
        'objectives': ['Să poți distinge redox de neutralizare și precipitare',
 'Să poți identifica disproporționarea',
 'Să poți recunoaște comproporționarea'],
        'body': r"""## Explicație teoretică
### Criteriul decisiv este variația N.O.
O reacție este redox dacă cel puțin un element își modifică numărul de oxidare și bilanțul cuprinde oxidare și reducere. Simplul fapt că se formează un precipitat, un gaz sau apă nu decide clasificarea. Aceste observații pot apărea atât în reacții redox, cât și în transformări fără schimbare de N.O. Într-un schimb ionic simplu, ionii își pot schimba partenerii fără transfer electronic.
### Reacții fără transfer electronic
În neutralizarea dintre H⁺ și OH⁻, H rămâne +I și O rămâne −II. În precipitarea AgCl din Ag⁺ și Cl⁻, Ag rămâne +I, iar Cl rămâne −I. Sarcinile ionilor pot dispărea ca sarcină globală a produsului, dar aceasta nu înseamnă reducerea ambilor ioni: neutralitatea compusului nu este N.O. zero pentru fiecare atom.
### Disproporționare
Același element din aceeași stare inițială ajunge în două stări, una mai joasă și una mai înaltă. Cl₂ cu NaOH rece și diluat formează clorură și hipoclorit: Cl(0) ajunge la −I și +I. Cu NaOH cald și concentrat, produsul oxigenat uzual este cloratul, cu Cl(+V); raportul atomilor reduși și oxidați se schimbă. Și H₂O₂ se poate disproporționa: O(−I) formează O(−II) în apă și O(0) în oxigen.
### Comproporționare
Două stări inițiale ale aceluiași element conduc la o stare intermediară comună. Fe(0) și Fe(+III) pot forma Fe(+II). Faptul că este prezent un singur element cu variații nu împiedică reacția să fie redox: atomii acelui element îndeplinesc roluri complementare. Clasificarea cere urmărirea stărilor, nu doar numărarea elementelor.

## Definiții și concepte importante
- **Reacție redox**: transformare cu bilanț de oxidare și reducere.
- **Neutralizare**: reacție acido-bazică, fără a implica obligatoriu redox.
- **Disproporționare**: o stare inițială conduce la o stare mai oxidată și una mai redusă.
- **Comproporționare**: două stări diferite conduc la o stare comună intermediară.

## Formule și relații
$$a(x_0-x_r)=b(x_o-x_0)$$
$a$ este numărul atomilor reduși, $b$ numărul atomilor oxidați, $x_0$ N.O. inițial, $x_r$ cel redus și $x_o$ cel oxidat. Toate sunt fără unitate. Relația exprimă egalitatea electronilor în disproporționare; numără atomi, nu molecule diatomice.


$$\mathrm{H^{+} + OH^{-} \rightarrow H_{2}O}$$



$$\mathrm{Ag^{+} + Cl^{-} \rightarrow AgCl}$$

Coeficienții sunt fără unitate; absența electronilor nu este singură un criteriu, fiindcă și ecuațiile globale redox se scriu fără electroni expliciți.

## Exemple rezolvate pas cu pas
### Exemplul 1 – Clor în condiții diferite
1. La rece și în soluție diluată, Cl(0) trece la −I și +I: câte un atom pentru fiecare rol.


$$\mathrm{Cl_{2} + 2NaOH \rightarrow NaCl + NaClO + H_{2}O}$$

2. La cald și în soluție concentrată, Cl(0) trece la −I și +V.
3. Un atom oxidat cedează cinci electroni; sunt necesari cinci atomi reduși, fiecare acceptând unul.


$$\mathrm{3Cl_{2} + 6NaOH \rightarrow 5NaCl + NaClO_{3} + 3H_{2}O}$$

4. Cele șase poziții ale clorului cer trei molecule Cl₂; nu cinci molecule Cl₂.
### Exemplul 2 – Aceeași specie finală din două stări
1. Fe metalic trece de la 0 la +II și cedează doi electroni.
2. Fiecare Fe³⁺ devine Fe²⁺ și acceptă un electron; folosim doi ioni Fe³⁺.


$$\mathrm{Fe + 2Fe^{3+} \rightarrow 3Fe^{2+}}$$

3. Se obțin trei ioni Fe²⁺. Sarcina totală este +6 de ambele părți.
4. Aceasta este comproporționare, nu disproporționare. Pentru comparație, descompunerea de mai jos este disproporționare a O(−I):


$$\mathrm{2H_{2}O_{2} \rightarrow 2H_{2}O + O_{2}}$$



## Interpretarea rezultatelor
În reacția cu NaOH cald, raportul clorură:clorat este 5:1 în mol; nu înseamnă că cinci șesimi din molecule rămân nemodificate. Fiecare moleculă de clor furnizează doi atomi. Pentru AgCl, apariția solidului nu schimbă stările Ag(+I) și Cl(−I), astfel că reacția rămâne neredox. O reacție poate avea simultan caracter acido-bazic și redox, dar atunci clasificarea redox trebuie demonstrată prin variația N.O.; categoriile nu sunt etichete exclusiv determinate de aspectul experimental.""",
        'mistakes': ['Greșeala: declari orice precipitare redox → Cum o eviți: compară N.O. înainte și după',
 'Greșeala: consideri N.O. zero în orice produs neutru → Cum o eviți: separă sarcina globală de stările '
 'atomilor',
 'Greșeala: inversezi disproporționarea și comproporționarea → Cum o eviți: numără stările inițiale și '
 'finale'],
        'takeaways': ['Schimbarea N.O. este criteriul redox.',
 'Neutralizarea simplă nu schimbă N.O.',
 'Precipitarea AgCl nu este redox.',
 'Disproporționarea are o stare inițială și două finale.',
 'Comproporționarea converge spre o stare intermediară.'],
        'connections': ['Lecția 5.3 – transferul de electroni.', 'Lecția 5.8 – clorul în mediu bazic.'],
    },
    {
        'id': 'redox_lesson_06',
        'number': '5.6',
        'title': '5.6. Egalarea prin metoda numerelor de oxidare',
        'level': 'Intermediar – calcule',
        'official': 'Egalarea ecuațiilor prin bilanțul numerelor de oxidare',
        'objectives': ['Să poți construi bilanțul electronic',
 'Să poți stabili coeficienții moleculari minimi',
 'Să poți verifica atomii după egalarea electronilor'],
        'body': r"""## Explicație teoretică
### Ce stabilește și ce nu stabilește bilanțul
Metoda numerelor de oxidare stabilește raportul dintre cantitățile atomilor care se oxidează și se reduc. Nu determină singură coeficienții apei, ai acidului sau ai ionilor spectatori. După bilanțul electronic trebuie egalate toate elementele. Nu modificăm indicii din formule: schimbarea lui H₂O în H₂O₂ ar schimba substanța, nu coeficientul.
### Algoritm în pași
Scriem reactanții și produșii corecți pentru condițiile date. Atribuim N.O. elementelor care se modifică. Calculăm variația pentru fiecare atom, apoi ținem cont de numărul atomilor dintr-o formulă. Alegem multiplicatori pentru egalitatea electronilor. Transferăm raportul în ecuația moleculară, egalăm restul elementelor și reducem coeficienții la cel mai mic raport întreg. La sfârșit verificăm separat atomii și, pentru formele ionice, sarcina.
### Atenție la reactivii cu mai multe roluri
În reacția cu HNO₃, o parte din azotul(+V) se reduce, dar altă parte rămâne în ionii nitrat din sarea metalului. Acidul asigură și mediul acid. Prin urmare, coeficientul total al HNO₃ nu este egal doar cu numărul atomilor N reduși. În reacția dicromatului cu HCl, clorura furnizează atât clorul oxidat la Cl₂, cât și clorurile din produși. Numărarea doar a atomilor care schimbă N.O. produce o ecuație incompletă.
Produșii depind de condiții. Pentru exemplele școlare cu Cu, acidul azotic diluat conduce uzual la NO, iar cel concentrat la NO₂. Nu extrapolăm regula la orice metal sau orice concentrație. NO este incolor, dar în contact cu aerul se poate transforma ulterior; ecuația cerută descrie etapa specificată, nu toate procesele secundare.

## Definiții și concepte importante
- **Bilanț electronic**: egalarea variațiilor totale ale N.O.
- **Coeficient stoechiometric**: număr pus în fața formulei, care multiplică întreaga specie.
- **Indice chimic**: număr din formulă, care nu se modifică la egalare.
- **Ion spectator**: ion fără schimbare netă în ecuația ionică redusă.

## Formule și relații
$$a\,p\,\Delta x_{\mathrm{ox}}=b\,r\,|\Delta x_{\mathrm{red}}|$$
$a$ și $b$ sunt coeficienți ai speciilor reactive, $p$ și $r$ numerele atomilor care schimbă N.O. per formulă, iar $\Delta x$ variațiile per atom. Toți termenii sunt fără unitate; pentru moli, aceeași relație exprimă cantități de electroni în mol.

$$N_{E,\mathrm{st}}=N_{E,\mathrm{dr}}$$
$N_E$ este numărul atomilor elementului $E$ în fiecare membru, fără unitate; verificarea se repetă pentru fiecare element, nu doar pentru cel oxidat.

## Exemple rezolvate pas cu pas
### Exemplul 1 – Cupru și acid azotic diluat
1. Cu(0) ajunge la Cu(+II): doi electroni cedați per Cu. N(+V) ajunge în NO la +II: trei electroni acceptați per N.
2. Multiplu comun 6: trei Cu cedează șase electroni, doi N acceptă șase.
3. Trei Cu formează trei unități Cu(NO₃)₂, care păstrează șase atomi N ca nitrat. Împreună cu cei doi N reduși sunt necesare opt HNO₃.
4. Opt H impun patru H₂O; oxigenul se verifică: 24 în fiecare membru.


$$\mathrm{3Cu + 8HNO_{3} \rightarrow 3Cu(NO_{3})_{2} + 2NO + 4H_{2}O}$$

### Exemplul 2 – Cupru și acid azotic concentrat
1. N(+V) ajunge la +IV în NO₂, deci acceptă un electron per N.
2. Un Cu cedează doi electroni, deci formează două NO₂. Alți doi nitrați rămân în sare.
3. În total, patru HNO₃ furnizează patru N și patru H; rezultă două H₂O.


$$\mathrm{Cu + 4HNO_{3} \rightarrow Cu(NO_{3})_{2} + 2NO_{2} + 2H_{2}O}$$

4. Verificarea oxigenului: $4\cdot3=6+2\cdot2+2=12$.
### Exemplul 3 – Dicromat și acid clorhidric
1. Doi Cr(+VI) acceptă șase electroni pentru a deveni Cr(+III).
2. Șase Cl(−I) cedează șase electroni și dau trei Cl₂. Alte opt cloruri formează sărurile.


$$\mathrm{K_{2}Cr_{2}O_{7} + 14HCl \rightarrow 2KCl + 2CrCl_{3} + 3Cl_{2} + 7H_{2}O}$$

3. Cele șapte O dau șapte H₂O, care cer 14 HCl. Sunt 14 Cl în fiecare membru.

## Interpretarea rezultatelor
Egalitatea electronilor este necesară, dar nu suficientă. Pentru Cu și HNO₃ diluat, coeficientul acidului este opt, nu doi; cei doi atomi de azot reduși reprezintă doar o parte a acidului. Compară separat inventarul de N, H și O. În ecuația dicromatului, cei doi atomi Cr sunt deja în aceeași formulă; omiterea factorului doi ar înjumătăți greșit necesarul de electroni. Toate ecuațiile moleculare de aici au sarcină totală zero în ambii membri.""",
        'mistakes': ['Greșeala: schimbi indicii formulelor → Cum o eviți: modifică numai coeficienții',
 'Greșeala: numeri doar azotul redus → Cum o eviți: include nitrații din sare',
 'Greșeala: uiți cei doi Cr din dicromat → Cum o eviți: multiplică variația per atom cu doi'],
        'takeaways': ['Produșii se aleg înainte de egalare.',
 'Bilanțul electronic dă raportul speciilor reactive.',
 'Acidul poate avea mai multe roluri.',
 'Toți atomii trebuie verificați la final.'],
        'connections': ['Lecția 5.7 – metoda ion-electron ca alternativă.'],
    },
    {
        'id': 'redox_lesson_07',
        'number': '5.7',
        'title': '5.7. Metoda ion-electron: semireacții (mediu acid)',
        'level': 'Intermediar – calcule',
        'official': 'Egalarea redox în mediu acid prin semireacții',
        'objectives': ['Să poți egala oxigenul cu apă și hidrogenul cu protoni',
 'Să poți conserva sarcina cu electroni',
 'Să poți reconstrui ecuația moleculară din cea ionică'],
        'body': r"""## Explicație teoretică
### De ce separăm procesele
În soluție, ecuația ionică redusă izolează speciile care se transformă și elimină ionii spectatori. Metoda ion-electron conservă explicit masa și sarcina în fiecare semireacție; de aceea este mai sigură când intervin apă, protoni și oxoanioni. Alegerea mediului acid permite folosirea H⁺, dar nu justifică introducerea oricărui anion fără a verifica dacă reacționează.
### Ordinea operațiilor
Pentru fiecare semireacție: egalăm întâi elementele altele decât O și H; egalăm O cu H₂O; egalăm H cu H⁺; egalăm sarcina cu electroni. Înmulțim semireacțiile până au același număr de electroni, le adunăm și simplificăm speciile identice din ambii membri. În final verificăm că ecuația globală nu conține electroni și că sarcina totală coincide.
### Alegerea acidului la permanganometrie
Pentru oxidarea Fe²⁺ cu permanganat folosim uzual acid sulfuric suficient. HCl poate introduce oxidarea clorurii, iar HNO₃ este el însuși oxidant și poate afecta analitul; nu sunt înlocuitori neutri. La trecerea la ecuația moleculară, K⁺ și SO₄²⁻ trebuie distribuiți în sărurile indicate, cu respectarea inventarului, fără a le atribui schimbări de N.O.
Metoda nu prezice singură produsul: trebuie să știm că MnO₄⁻ se reduce la Mn²⁺ în mediul acid considerat. Dacă produsul ar fi MnO₂, numărul de electroni ar fi altul. Egalarea unei ecuații cu produși greșiți nu o face automat potrivită situației experimentale.

## Definiții și concepte importante
- **Ecuație ionică redusă**: ecuație din care au fost eliminați ionii spectatori.
- **Mediu acid**: mediu care permite folosirea protonilor în bilanțul reacției.
- **Simplificare**: eliminarea aceleiași cantități de specie din ambii membri.
- **Reconstrucție moleculară**: adăugarea ionilor spectatori în proporții compatibile cu sărurile.

## Formule și relații
$$Q_{\mathrm{st}}=\sum_i \nu_i q_i=Q_{\mathrm{dr}}$$
$Q$ este sarcina totală exprimată în unități de sarcină elementară, $\nu_i$ coeficientul speciei $i$, iar $q_i$ sarcina numerică a acelei specii; toate sunt fără unitate. Electronul contribuie cu −1.


$$\mathrm{MnO_{4}^{-} + 8H^{+} + 5e^{-} \rightarrow Mn^{2+} + 4H_{2}O}$$

La această semireacție, sarcina din stânga este $-1+8-5=+2$, iar cea din dreapta este +2. Cei patru atomi O și cei opt atomi H (câte doi în fiecare moleculă) se regăsesc în cele patru molecule de apă.

## Exemple rezolvate pas cu pas
### Exemplul 1 – Permanganat și fier(II)
1. Scriem reducerea permanganatului din secțiunea anterioară.
2. Oxidarea unui Fe²⁺ produce un electron:


$$\mathrm{Fe^{2+} \rightarrow Fe^{3+} + e^{-}}$$

3. Înmulțim oxidarea cu cinci și adunăm. Cei cinci electroni se simplifică:


$$\mathrm{MnO_{4}^{-} + 5Fe^{2+} + 8H^{+} \rightarrow Mn^{2+} + 5Fe^{3+} + 4H_{2}O}$$

4. Sarcina din stânga este $-1+10+8=17$, iar din dreapta $2+15=17$.
5. Pentru săruri sulfat și KMnO₄, dublăm ecuația ionică și reintroducem ionii spectatori:


$$\mathrm{2KMnO_{4} + 10FeSO_{4} + 8H_{2}SO_{4} \rightarrow K_{2}SO_{4} + 2MnSO_{4} + 5Fe_{2}(SO_{4})_{3} + 8H_{2}O}$$

6. Numărăm sulfații: zece din FeSO₄ și opt din acid, în total 18; în produși sunt $1+2+5\cdot3=18$.
### Exemplul 2 – Permanganat și peroxid de hidrogen
1. H₂O₂ este reducător; semireacția sa produce doi electroni și doi protoni.


$$\mathrm{H_{2}O_{2} \rightarrow O_{2} + 2H^{+} + 2e^{-}}$$

2. Înmulțim reducerea permanganatului cu doi și oxidarea peroxidului cu cinci. Se anulează zece electroni și zece protoni.


$$\mathrm{2MnO_{4}^{-} + 5H_{2}O_{2} + 6H^{+} \rightarrow 2Mn^{2+} + 5O_{2} + 8H_{2}O}$$

3. Rămân șase protoni consumați; sarcina globală este +4 în fiecare membru.
4. Cu acid sulfuric și sare de potasiu, forma moleculară este:


$$\mathrm{2KMnO_{4} + 5H_{2}O_{2} + 3H_{2}SO_{4} \rightarrow K_{2}SO_{4} + 2MnSO_{4} + 5O_{2} + 8H_{2}O}$$



## Interpretarea rezultatelor
Apariția protonilor în ambele semireacții nu este o problemă; se păstrează numai diferența după adunare. În reacția peroxidului, șaisprezece protoni sunt consumați de reducere și zece produși de oxidare, rezultând șase consumați net. Dacă ai obținut șaisprezece în ecuația globală, ai omis simplificarea. În reacția cu fierul, raportul permanganat:fier(II) este 1:5 indiferent dacă scrii ecuația ionică sau dublezi coeficienții pentru forma moleculară; raporturile nu se schimbă prin multiplicarea întregii ecuații.""",
        'mistakes': ['Greșeala: egalezi numai atomii → Cum o eviți: verifică separat sarcina',
 'Greșeala: uiți simplificarea H⁺ → Cum o eviți: scade coeficienții de pe cele două părți',
 'Greșeala: folosești HCl automat la titrare → Cum o eviți: alege acid sulfuric pentru a evita reacții '
 'parazite'],
        'takeaways': ['În acid, O se egalează cu apă.',
 'H se egalează cu H⁺.',
 'Sarcina se egalează cu electroni.',
 'Electronii dispar prin adunare.',
 'Ionii spectatori se adaugă numai la forma moleculară.'],
        'connections': ['Lecția 5.9 – titrare permanganometrică.'],
    },
    {
        'id': 'redox_lesson_08',
        'number': '5.8',
        'title': '5.8. Egalarea în mediu bazic',
        'level': 'Avansat',
        'official': 'Metoda ion-electron în mediu bazic',
        'objectives': ['Să poți transforma un bilanț acid într-unul bazic',
 'Să poți egala reducerea permanganatului la MnO₂',
 'Să poți verifica disproporționarea clorului în bază'],
        'body': r"""## Explicație teoretică
### De la acid la bazic
O metodă robustă este egalarea provizorie ca în mediu acid, urmată de adăugarea aceluiași număr de OH⁻ în ambii membri pentru a neutraliza fiecare H⁺. Perechile H⁺ și OH⁻ se înlocuiesc cu apă, apoi se simplifică apa comună. Această procedură este algebrică: protonii din bilanțul intermediar nu afirmă că soluția bazică are exces de acid.
### Varianta directă
Poți egala direct H și O cu apă și OH⁻, dar poziția lor trebuie dedusă prin conservare, nu memorată. Electronii rămân necesari pentru egalarea sarcinii. La reducerea permanganatului la MnO₂, oxigenul rămas și hidrogenul apei conduc la patru OH⁻ în produși. Semireacția consumă trei electroni, deoarece Mn trece de la +VII la +IV.
### Mediul inițial și bilanțul net
Dacă ecuația produce OH⁻, aceasta nu înseamnă că reacția a început obligatoriu într-o soluție puternic bazică. Un mediu neutru poate deveni bazic în cursul reacției. Invers, apariția apei ca reactant nu presupune că apa este reducătorul: rolul redox se stabilește prin N.O.
Pentru Cl₂, condițiile reci și diluate favorizează hipocloritul, iar condițiile calde și concentrate favorizează cloratul în exemplele uzuale. Nu combina ecuația pentru hipoclorit cu raportul electronic al cloratului. Dacă problema precizează manganat drept produs, reducerea Mn(+VII) la +VI cere un electron și nu trebuie înlocuită cu semireacția la MnO₂.

## Definiții și concepte importante
- **Neutralizare algebrică**: eliminarea H⁺ din bilanț prin adăugare egală de OH⁻.
- **Mediu bazic**: mediu în care folosim apă și OH⁻ în ecuația finală.
- **Bilanț net**: ecuația rămasă după simplificarea speciilor comune.
- **Produs specificat**: specie finală care fixează variația N.O. și numărul electronilor.

## Formule și relații
$$n(\mathrm{OH^-})_{\mathrm{adăugat}}=n(\mathrm{H^+})_{\mathrm{de\ eliminat}}$$
$n$ reprezintă cantități în mol; în algoritmul cu coeficienți se folosește aceeași egalitate pentru numere stoechiometrice fără unitate. OH⁻ se adaugă în ambii membri în aceeași cantitate, nu doar lângă protoni.


$$\mathrm{MnO_{4}^{-} + 2H_{2}O + 3e^{-} \rightarrow MnO_{2} + 4OH^{-}}$$

Coeficienții 1, 2, 3, 1 și 4 sunt fără unitate; sarcina totală este −4 în fiecare membru. Electronii apar în stânga, conform reducerii.

## Exemple rezolvate pas cu pas
### Exemplul 1 – Permanganat și sulfit, cu MnO₂ ca produs
1. Reducerea permanganatului este semireacția de mai sus, cu trei electroni acceptați.
2. Sulful trece de la +IV în sulfit la +VI în sulfat și cedează doi electroni:


$$\mathrm{SO_{3}^{2-} + 2OH^{-} \rightarrow SO_{4}^{2-} + H_{2}O + 2e^{-}}$$

3. Multiplu comun 6: înmulțim reducerea cu doi și oxidarea cu trei.
4. După adunare, simplificăm șase OH⁻ și trei H₂O, obținând:


$$\mathrm{2MnO_{4}^{-} + 3SO_{3}^{2-} + H_{2}O \rightarrow 2MnO_{2} + 3SO_{4}^{2-} + 2OH^{-}}$$

5. Verificăm sarcina: stânga $-2-6=-8$, dreapta $-6-2=-8$. Oxigenul total este 18 în fiecare membru.
### Exemplul 2 – Clor în NaOH rece și diluat
1. Reducerea clorului acceptă doi electroni:


$$\mathrm{Cl_{2} + 2e^{-} \rightarrow 2Cl^{-}}$$

2. Oxidarea la hipoclorit cedează doi electroni:


$$\mathrm{Cl_{2} + 4OH^{-} \rightarrow 2ClO^{-} + 2H_{2}O + 2e^{-}}$$

3. Adunăm și împărțim toți coeficienții la doi:


$$\mathrm{Cl_{2} + 2OH^{-} \rightarrow Cl^{-} + ClO^{-} + H_{2}O}$$

4. Reintroducem doi ioni Na⁺ ca spectatori și obținem ecuația moleculară cu NaCl, NaClO și H₂O. Sarcina ionică netă este −2 în fiecare membru; clorul are două roluri.

## Interpretarea rezultatelor
În primul exemplu, cei doi OH⁻ rămași în produși sunt rezultatul diferenței dintre opt produși de reducere și șase consumați de oxidare. Cantitatea de apă este de asemenea o diferență, nu suma coeficienților intermediari. MnO₂ este solidul brun uzual, iar sulfatul păstrează S(+VI). În al doilea exemplu, împărțirea la doi se face pentru întreaga ecuație, inclusiv apă și OH⁻; împărțirea selectivă ar distruge conservarea. O ecuație bazică finală nu trebuie să păstreze simultan protoni nesimplificați și un exces de hidroxid.""",
        'mistakes': ['Greșeala: adaugi OH⁻ într-un singur membru → Cum o eviți: păstrează aceeași cantitate în ambii',
 'Greșeala: lași H⁺ în ecuația bazică finală → Cum o eviți: neutralizează și simplifică apa',
 'Greșeala: folosești cinci electroni pentru MnO₂ → Cum o eviți: calculează 7−4=3'],
        'takeaways': ['OH⁻ neutralizează H⁺ în ambii membri.',
 'Apa comună se simplifică.',
 'Reducerea la MnO₂ cere trei electroni.',
 'Produsul final, nu doar eticheta mediului, fixează bilanțul.'],
        'connections': ['Lecția 5.4 – dependența permanganatului de condiții.'],
    },
    {
        'id': 'redox_lesson_09',
        'number': '5.9',
        'title': '5.9. Probleme complexe și aplicații REDOX',
        'level': 'Avansat',
        'official': 'Stoechiometrie redox, permanganometrie, coroziune și pile',
        'objectives': ['Să poți calcula o cantitate prin echivalență electronică',
 'Să poți rezolva o titrare permanganometrică simplă',
 'Să poți descrie rolul anodului și catodului în aplicații'],
        'body': r"""## Explicație teoretică
### De la ecuație la cantitate
O problemă cantitativă cere întâi produsul redox și ecuația, apoi conversia datelor în moli. Pentru o soluție folosim concentrația molară și volumul în litri; pentru o probă solidă folosim masa și masa molară. Raportul molar se ia din ecuația egalată, nu din raportul maselor și nici din sarcinile inițiale ale ionilor. În amestecuri, se adună cantitățile de electroni furnizate de fiecare componentă.
### Titrare permanganometrică
În mediu suficient acid, un mol MnO₄⁻ acceptă cinci moli de electroni și oxidează cinci moli Fe²⁺. La echivalență, cantitatea de oxidant adăugată corespunde exact electronilor furnizați de analit. Permanganatul poate servi drept autoindicator: un foarte mic exces produce o colorație roz pal persistentă. În calculele ideale de liceu neglijăm acest exces, presupunem reacție cantitativă și concentrație cunoscută a titrantului. Aceste ipoteze trebuie distinse de particularitățile unui experiment real.
### Pile și coroziune: aceeași contabilitate
La anod are loc oxidarea, la catod reducerea. În pila galvanică Zn/Cu, zincul furnizează electroni către circuitul exterior, iar ionii Cu²⁺ îi acceptă. Puntea salină asigură continuitatea ionică și limitează acumularea de sarcină; electronii nu sunt transportați prin ea. La coroziunea fierului în apă aerată, fierul se poate oxida la Fe²⁺, în timp ce oxigenul se reduce în zone catodice. Rugina este un ansamblu de produși oxidați și hidratați, nu o singură specie perfect stoechiometrică. Acoperirile protectoare sau protecția cu un metal mai activ pot limita coroziunea, prin mecanisme diferite.

## Definiții și concepte importante
- **Echivalență electronică**: egalitatea molilor de electroni cedați și acceptați.
- **Titrant**: soluție de concentrație cunoscută folosită la determinare.
- **Anod**: electrodul unde se produce oxidarea.
- **Catod**: electrodul unde se produce reducerea.
- **Coroziune**: degradare chimică/electrochimică a unui material în mediul său.

## Formule și relații
$$n=cV,\qquad n=\frac{m}{M},\qquad z_{\mathrm{ox}}n_{\mathrm{ox}}=z_{\mathrm{red}}n_{\mathrm{red}}$$
$n$ este cantitatea în mol, $c$ concentrația în mol/L, $V$ volumul în L, $m$ masa în g, $M$ masa molară în g/mol, iar $z$ numărul electronilor acceptați sau cedați per particulă, fără unitate. Indicii ox și red desemnează agentul oxidant, respectiv reducător, nu procesul suferit de acesta.


$$\mathrm{Fe \rightarrow Fe^{2+} + 2e^{-}}$$



$$\mathrm{O_{2} + 2H_{2}O + 4e^{-} \rightarrow 4OH^{-}}$$

În aceste semireacții de coroziune, coeficienții sunt fără unitate. Prima cedează doi electroni, a doua acceptă patru; cuplarea ar necesita dublarea primei.

## Exemple rezolvate pas cu pas
### Exemplul 1 – Determinarea Fe²⁺ prin titrare
1. O probă de 25,00 mL soluție Fe²⁺ consumă 20,00 mL KMnO₄ de 0,0200 mol/L în H₂SO₄ suficient. Ecuația ionică este cea din lecția 5.7, cu raport 1:5.
2. Convertim volumul titrantului: $20{,}00\ \mathrm{mL}=0{,}02000\ \mathrm L$.
3. $n(\mathrm{MnO_4^-})=0{,}0200\cdot0{,}02000=0{,}000400\ \mathrm{mol}$.
4. $n(\mathrm{Fe^{2+}})=5\cdot0{,}000400=0{,}00200\ \mathrm{mol}$.
5. $c(\mathrm{Fe^{2+}})=0{,}00200/0{,}02500=0{,}0800\ \mathrm{mol/L}$.
### Exemplul 2 – Zinc consumat într-o pilă idealizată
1. În pila Zn/Cu, folosim ecuația ionică din lecția 5.3, cu raport Zn:Cu de 1:1. Se consumă 0,010 mol Zn.
2. Se formează 0,010 mol Cu; cu $M(\mathrm{Cu})=64\ \mathrm{g/mol}$, masa depusă este $0{,}010\cdot64=0{,}640\ \mathrm g$.
3. Zincul cedează $2\cdot0{,}010=0{,}020\ \mathrm{mol}$ electroni, acceptați integral de Cu²⁺.
4. Cu $M(\mathrm{Zn})=65\ \mathrm{g/mol}$, se consumă $0{,}650\ \mathrm g$ Zn. Masele nu sunt egale, deși cantitățile în mol sunt.

## Interpretarea rezultatelor
Concentrația fierului este de patru ori concentrația titrantului, nu de cinci ori, deoarece volumele celor două soluții diferă. Egalitatea electronică nu implică egalitatea concentrațiilor sau volumelor. În pilă, masa totală a întregului sistem se conservă, dar masa unui electrod poate crește în timp ce a celuilalt scade. Nu extrapolăm semnul electric al anodului galvanic la orice dispozitiv: definiția sigură, comună pilelor și electrolizei, rămâne oxidarea. Exemplele sunt calcule ideale de antrenament, fără corecții instrumentale ori cinetice.""",
        'mistakes': ['Greșeala: introduci mL în n=cV cu c în mol/L → Cum o eviți: convertește mL în L',
 'Greșeala: egalezi volumele la echivalență → Cum o eviți: egalează electronii',
 'Greșeala: definești anodul doar prin semn → Cum o eviți: reține oxidarea la anod'],
        'takeaways': ['Calculele pornesc de la ecuația corectă.',
 'La titrare se egalează molii de electroni.',
 'Un permanganat acid corespunde la cinci Fe²⁺.',
 'Anodul este locul oxidării.',
 'Catodul este locul reducerii.'],
        'connections': ['Lecția 5.7 – ecuația titrării.', 'Lecția 5.3 – transferul în pila Zn/Cu.'],
    },
    {
        'id': 'redox_lesson_10',
        'number': '5.10',
        'title': '5.10. Recapitulare și simulare de nivel concurs',
        'level': 'Concurs',
        'official': 'Sinteză și aplicații integrate ale proceselor redox',
        'objectives': ['Să poți alege metoda de egalare potrivită',
 'Să poți rezolva un bilanț într-un amestec',
 'Să poți controla un rezultat prin două metode independente'],
        'body': r"""## Explicație teoretică
### O strategie înaintea calculelor
Începe prin a identifica exact specia, sarcina, mediul și produsul indicat. Atribuie N.O. doar după verificarea excepțiilor. Numește oxidantul și reducătorul prin transformarea suferită, apoi alege bilanțul N.O. pentru o ecuație moleculară simplă sau metoda ion-electron când apa și ionii participă explicit. Nu porni de la o proporție memorată înainte de a verifica dacă mediul o justifică.
### Probleme cu amestecuri
Într-un amestec de reducători, fiecare componentă poate furniza alt număr de electroni per mol. Cantitatea totală de electroni este suma contribuțiilor, nu numărul total de moli din amestec. Dacă sunt cerute două cantități necunoscute, ai nevoie de două informații independente, de exemplu masa totală și consumul oxidantului. O ecuație de masă folosește mase molare; ecuația electronică folosește electroni per particulă. Nu interschimba aceste ponderi.
### Verificare de concurs
După rezultat, reconstituie datele inițiale. Cantitățile negative într-un amestec indică date incompatibile sau o eroare de model. Raportul dintre molii de electroni și molii totali de reducători trebuie să fie între capacitățile individuale ale componentelor. La gaz, condițiile sunt esențiale: 22,4 L/mol se aplică numai în convenția de condiții normale dată în problemă. În final, răspunde în unitatea cerută și nu rotunji prematur fracțiile intermediare.
Materialul de față este original, pentru antrenament independent; nu reprezintă subiecte oficiale de concurs. Scopul unei simulări este să verifice alegerea modelului și argumentarea, nu doar rapiditatea calculului. Un rezultat numeric plauzibil trebuie susținut de conservarea atomilor, sarcinii și electronilor.

## Definiții și concepte importante
- **Model stoechiometric**: sistem de relații bazat pe compoziție și ecuația reacției.
- **Contribuție electronică**: moli de specie înmulțiți cu electronii transferați per particulă.
- **Control independent**: verificare care nu repetă exact aceiași pași de calcul.
- **Condiții normale**: convenția problemei pentru folosirea volumului molar de 22,4 L/mol.

## Formule și relații
$$n_{e,\mathrm{total}}=\sum_i z_i n_i,\qquad V_{\mathrm{gaz}}=n_{\mathrm{gaz}}V_m$$
$n_{e,\mathrm{total}}$ este cantitatea totală de electroni în mol, $z_i$ este numărul electronilor per particulă din componenta $i$, fără unitate, iar $n_i$ este cantitatea acesteia în mol. $V_{\mathrm{gaz}}$ este volumul în L, $n_{\mathrm{gaz}}$ cantitatea de gaz în mol și $V_m$ volumul molar în L/mol, aici 22,4 L/mol la c.n.

$$m_{\mathrm{total}}=\sum_i n_i M_i$$
$m_{\mathrm{total}}$ este masa în g, iar $M_i$ masa molară a componentei $i$ în g/mol. Această relație nu include automat masa solventului dacă problema se referă numai la solut.

## Exemple rezolvate pas cu pas
### Exemplul 1 – Amestec de două surse de electroni
1. O probă conține 0,010 mol Fe²⁺ și 0,005 mol H₂O₂, singurii reducători, și este oxidată cantitativ cu permanganat în acid, fără reacții secundare. Fe²⁺ devine Fe³⁺, iar H₂O₂ formează O₂. Calculăm consumul total, fără a presupune că un astfel de amestec este stabil la păstrare.
2. Fierul furnizează $1\cdot0{,}010=0{,}010\ \mathrm{mol}$ electroni; peroxidul furnizează $2\cdot0{,}005=0{,}010\ \mathrm{mol}$ electroni.
3. Totalul este 0,020 mol electroni; necesarul de permanganat este $0{,}020/5=0{,}0040\ \mathrm{mol}$.
4. La concentrația 0,100 mol/L, volumul este $0{,}0040/0{,}100=0{,}040\ \mathrm L=40\ \mathrm{mL}$. Verificăm separat: 0,0020 mol pentru fiecare componentă.
### Exemplul 2 – Cupru, acid diluat și volum de gaz
1. O probă de 9,60 g Cu pur reacționează complet cu HNO₃ diluat în exces; produsul azotat redus este NO. Se dă Cu=64 și $V_m=22{,}4\ \mathrm{L/mol}$ la c.n.
2. Ecuația egalată din lecția 5.6 dă raportul Cu:NO:HNO₃ de 3:2:8.
3. $n(\mathrm{Cu})=9{,}60/64=0{,}150\ \mathrm{mol}$; $n(\mathrm{NO})=(2/3)\cdot0{,}150=0{,}100\ \mathrm{mol}$.
4. $V(\mathrm{NO})=0{,}100\cdot22{,}4=2{,}24\ \mathrm L$ la c.n., pentru NO considerat înaintea reacțiilor ulterioare cu aerul.
5. Acidul consumat este $(8/3)\cdot0{,}150=0{,}400\ \mathrm{mol}$. Control electronic: $0{,}150\cdot2=0{,}100\cdot3=0{,}300\ \mathrm{mol}$ electroni.

## Interpretarea rezultatelor
În amestec, împărțirea sumei molilor reactanților la cinci ar fi greșită, deoarece H₂O₂ cedează doi electroni, iar Fe²⁺ unul. Ipoteza absenței reacțiilor secundare este importantă: fierul și peroxidul pot interacționa, astfel că exemplul este un bilanț idealizat al capacității reducătoare totale, nu o recomandare de preparare și stocare. În problema cu gaz, folosirea raportului 1:2 valabil pentru Cu și NO₂ ar tripla eronat cantitatea de produs. Corectitudinea rezultă din verificarea concomitentă a raportului molecular și a electronilor, nu din potrivirea cu o valoare așteptată.""",
        'mistakes': ['Greșeala: aduni molii fără ponderi electronice → Cum o eviți: înmulțește fiecare cantitate cu z',
 'Greșeala: folosești 22,4 L/mol la orice condiții → Cum o eviți: citește condițiile gazului',
 'Greșeala: aplici raportul NO₂ pentru NO → Cum o eviți: verifică produsul înainte de calcul'],
        'takeaways': ['Citește mediul înainte de bilanț.',
 'Adună contribuțiile electronice, nu doar molii.',
 'Verifică rezultatul prin reconstrucția datelor.',
 'Nu confunda NO cu NO₂.',
 'Rotunjește numai la final.'],
        'connections': ['Lecția 5.6 – Cu și acid azotic.', 'Lecția 5.9 – echivalență electronică.'],
    },
]

CHAPTER5_QUESTIONS = [{'id': 'redox5_001',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.1',
  'topic': 'Definiția N.O.',
  'level': 'Fundamente',
  'type': 'teorie',
  'question': 'Care afirmație descrie corect numărul de oxidare?',
  'options': ['A. Este o sarcină formală atribuită printr-o convenție.',
              'B. Este întotdeauna sarcina electrică reală a atomului.',
              'C. Este numărul total de electroni ai atomului.',
              'D. Este întotdeauna pozitiv.',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'A. Este o sarcină formală atribuită printr-o convenție.',
  'explanation': 'N.O. rezultă din atribuirea formală a electronilor legăturilor atomului mai electronegativ. Nu '
                 'presupune existența unor ioni izolați în orice compus și poate fi pozitiv, negativ sau zero.',
  'option_explanations': {'B': 'În molecule covalente, atribuirea este formală, nu o sarcină ionică reală.',
                          'C': 'Numărul total de electroni nu este o variație formală față de atomul neutru.',
                          'D': 'Oxigenul din apă are −II, contraexemplu pentru semnul obligatoriu pozitiv.',
                          'E': 'Varianta A este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_002',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.1',
  'topic': 'Substanțe simple',
  'level': 'Fundamente',
  'type': 'interpretare',
  'question': 'Care pereche conține numai specii în care oxigenul are N.O. zero?',
  'options': ['A. H₂O și O₂', 'B. O₂ și O₃', 'C. H₂O₂ și O₃', 'D. OF₂ și H₂O', 'E. Niciuna dintre variantele A–D'],
  'answer': 'B. O₂ și O₃',
  'explanation': 'O₂ și O₃ sunt substanțe simple: legăturile sunt între atomi identici, astfel că fiecare atom O '
                 'are N.O. zero. Numărul atomilor din moleculă nu schimbă această regulă.',
  'option_explanations': {'A': 'În apă, oxigenul este −II, nu zero.',
                          'C': 'În peroxid, oxigenul este −I, chiar dacă în ozon este zero.',
                          'D': 'În OF₂ oxigenul este +II, iar în apă −II.',
                          'E': 'Varianta B este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_003',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.1',
  'topic': 'Ionul amoniu',
  'level': 'Fundamente',
  'type': 'calcul',
  'question': 'Ce N.O. are azotul în NH₄⁺?',
  'options': ['A. +V', 'B. −IV', 'C. −III', 'D. +I', 'E. Niciuna dintre variantele A–D'],
  'answer': 'C. −III',
  'explanation': 'Fiecare H are +I. Pentru întregul ion, suma trebuie să fie +1: x+4=1, de unde x=−3. Verificarea '
                 'este −3+4=+1, deci azotul are −III.',
  'option_explanations': {'A': '+V ar da suma +9, incompatibilă cu sarcina +1.',
                          'B': '−IV rezultă dacă egalezi suma cu zero, uitând sarcina ionului.',
                          'D': '+I este sarcina globală a ionului, nu N.O. al N.',
                          'E': 'Varianta C este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_004',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.2',
  'topic': 'Oxoanion',
  'level': 'Fundamente',
  'type': 'calcul',
  'question': 'Care este N.O. al Cr în Cr₂O₇²⁻?',
  'options': ['A. +III', 'B. +VII', 'C. +XII', 'D. +VI', 'E. Niciuna dintre variantele A–D'],
  'answer': 'D. +VI',
  'explanation': 'Oxigenul este −II. Relația 2x+7(−2)=−2 conduce la 2x=12, deci x=+6. Valoarea +12 este suma '
                 'pentru ambii atomi Cr, nu valoarea fiecăruia.',
  'option_explanations': {'A': '+III este o stare redusă uzuală a cromului, nu starea sa din dicromat.',
                          'B': '+VII ar rezulta din omiterea sarcinii ionului.',
                          'C': '+XII confundă suma pentru doi atomi cu valoarea per atom.',
                          'E': 'Varianta D este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_005',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.2',
  'topic': 'N.O. mediu',
  'level': 'Fundamente',
  'type': 'interpretare',
  'question': 'În Fe₃O₄, ce valoare are N.O. mediu al Fe? Se consideră O(−II).',
  'options': ['A. +II', 'B. +III', 'C. +IV', 'D. +VIII', 'E. Niciuna dintre variantele A–D'],
  'answer': 'E. Niciuna dintre variantele A–D',
  'explanation': 'Electroneutralitatea impune 3x−8=0, deci media este +8/3. Formal, un Fe(II) și doi Fe(III) dau '
                 'suma +8. Niciuna dintre valorile A–D nu este media exactă.',
  'option_explanations': {'A': '+II ar da suma +6, insuficientă pentru cei patru O.',
                          'B': '+III este o rotunjire nepermisă: suma ar fi +9.',
                          'C': '+IV ar da suma +12.',
                          'D': '+VIII este suma N.O. ale celor trei Fe, nu media lor.'}},
 {'id': 'redox5_006',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.2',
  'topic': 'Excepții și structură',
  'level': 'Fundamente',
  'type': 'interpretare',
  'question': 'Care afirmație este corectă pentru speciile indicate?',
  'options': ['A. În S₄O₆²⁻ media N.O. al S este +2,5; nu rezultă că toți atomii S au această stare.',
              'B. În H₂O₂ oxigenul are −II.',
              'C. În NaH hidrogenul are +I.',
              'D. În OF₂ oxigenul are −II.',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'A. În S₄O₆²⁻ media N.O. al S este +2,5; nu rezultă că toți atomii S au această stare.',
  'explanation': 'Pentru tetrationat, 4x−12=−2 dă x=+2,5. Structura uzuală permite S terminal(+V) și S '
                 'central(0); media nu este o stare individuală obligatorie. Peroxidul, hidrura și fluorura '
                 'oxigenului sunt excepții importante.',
  'option_explanations': {'B': 'În H₂O₂ oxigenul este −I; valoarea −II ar încălca neutralitatea.',
                          'C': 'În NaH, Na are +I, deci H are −I.',
                          'D': 'Fluorul are −I, deci în OF₂ oxigenul este +II.',
                          'E': 'Varianta A este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_007',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.3',
  'topic': 'Sensul transferului',
  'level': 'Fundamente',
  'type': 'teorie',
  'question': 'La trecerea Fe²⁺ la Fe³⁺, ce proces are loc?',
  'options': ['A. Reducere cu acceptarea unui electron',
              'B. Oxidare cu cedarea unui electron',
              'C. Oxidare cu cedarea a trei electroni',
              'D. Reducere cu acceptarea a doi electroni',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'B. Oxidare cu cedarea unui electron',
  'explanation': 'N.O. crește de la +II la +III, deci procesul este oxidare. Diferența este o unitate, astfel că '
                 'fiecare ion Fe²⁺ cedează un electron; nu se utilizează direct sarcina finală drept număr de '
                 'electroni.',
  'option_explanations': {'A': 'Acceptarea ar micșora sarcina pozitivă, nu ar crește-o.',
                          'C': 'Trei este sarcina finală, nu variația acesteia.',
                          'D': 'Atât sensul, cât și numărul electronilor sunt incompatibile cu variația +2 la +3.',
                          'E': 'Varianta B este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_008',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.3',
  'topic': 'Molii de electroni',
  'level': 'Fundamente',
  'type': 'calcul',
  'question': 'Câți moli de electroni acceptă 0,030 mol Cu²⁺ la formarea Cu metalic?',
  'options': ['A. 0,015 mol', 'B. 0,030 mol', 'C. 0,060 mol', 'D. 0,090 mol', 'E. Niciuna dintre variantele A–D'],
  'answer': 'C. 0,060 mol',
  'explanation': 'Cu trece de la +II la 0 și acceptă doi electroni per ion. Cantitatea este n(e⁻)=2·0,030=0,060 '
                 'mol. Cantitatea de cupru format rămâne 0,030 mol, dar electronii sunt de două ori mai mulți în '
                 'mol.',
  'option_explanations': {'A': 'Ai împărțit la doi în loc să înmulțești cu numărul electronilor per ion.',
                          'B': 'Ai presupus un singur electron per ion Cu²⁺.',
                          'D': 'Factorul trei nu corespunde diferenței de N.O., care este doi.',
                          'E': 'Varianta C este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_009',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.3',
  'topic': 'Semireacție',
  'level': 'Fundamente',
  'type': 'interpretare',
  'question': 'În semireacția de oxidare a Zn metalic la Zn²⁺, unde se află electronii și câți sunt per atom?',
  'options': ['A. Un electron în stânga',
              'B. Doi electroni în stânga',
              'C. Un electron în dreapta',
              'D. Doi electroni în dreapta',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'D. Doi electroni în dreapta',
  'explanation': 'Zincul trece de la 0 la +II, cedând doi electroni. Ei se scriu în dreapta. Sarcina netă în '
                 'dreapta este +2−2=0, egală cu sarcina zincului metalic din stânga.',
  'option_explanations': {'A': 'Electronul în stânga ar indica acceptare, iar un singur electron nu compensează '
                               '+2.',
                          'B': 'Doi electroni în stânga descriu reducerea Zn²⁺, nu oxidarea Zn.',
                          'C': 'Poziția este potrivită oxidării, dar lipsește un electron pentru conservarea '
                               'sarcinii.',
                          'E': 'Varianta D este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_010',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.4',
  'topic': 'Oxidant și reducător',
  'level': 'Intermediar',
  'type': 'teorie',
  'question': 'În reacția dintre Zn și Cu²⁺ cu formare de Zn²⁺ și Cu, care specie este agentul oxidant?',
  'options': ['A. Cu²⁺', 'B. Zn', 'C. Zn²⁺', 'D. Cu', 'E. Niciuna dintre variantele A–D'],
  'answer': 'A. Cu²⁺',
  'explanation': 'Cu²⁺ acceptă doi electroni și se reduce la Cu. Specia care acceptă electroni este oxidantul. Zn '
                 'cedează electroni și este reducător, în timp ce Zn²⁺ și Cu sunt produșii reacției indicate.',
  'option_explanations': {'B': 'Zn se oxidează, deci este reducător, nu oxidant.',
                          'C': 'Zn²⁺ este produsul oxidării, nu oxidantul reactant în sensul indicat.',
                          'D': 'Cu este produsul reducerii, nu specia care primește electroni în sensul indicat.',
                          'E': 'Varianta A este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_011',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.4',
  'topic': 'Dublul caracter',
  'level': 'Intermediar',
  'type': 'interpretare',
  'question': 'H₂O₂ reacționează cu MnO₄⁻ în acid și formează O₂. Care este rolul H₂O₂?',
  'options': ['A. Oxidant, deoarece conține oxigen',
              'B. Reducător, deoarece O trece de la −I la 0',
              'C. Catalizator, deoarece eliberează gaz',
              'D. Acid tare, deoarece pierde protoni',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'B. Reducător, deoarece O trece de la −I la 0',
  'explanation': 'În H₂O₂ oxigenul are −I, iar în O₂ are zero. Creșterea N.O. arată oxidare, deci peroxidul '
                 'cedează electroni și este reducător. Doi atomi O cedează împreună doi electroni per moleculă.',
  'option_explanations': {'A': 'Prezența oxigenului nu definește rolul; aici peroxidul se oxidează.',
                          'C': 'H₂O₂ se consumă stoechiometric, nu doar accelerează reacția.',
                          'D': 'Rolul redox nu este aciditate, iar H₂O₂ nu este acid tare.',
                          'E': 'Varianta B este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_012',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.4',
  'topic': 'Permanganat bazic',
  'level': 'Intermediar',
  'type': 'calcul',
  'question': 'Câți electroni acceptă un ion MnO₄⁻ dacă produsul specificat este MnO₂?',
  'options': ['A. Un electron',
              'B. Doi electroni',
              'C. Patru electroni',
              'D. Cinci electroni',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'E. Niciuna dintre variantele A–D',
  'explanation': 'Mn este +VII în permanganat și +IV în MnO₂. Diferența 7−4=3 arată acceptarea a trei electroni '
                 'per ion. Niciuna dintre valorile A–D nu este trei.',
  'option_explanations': {'A': 'Un electron corespunde reducerii la manganat, cu Mn(+VI).',
                          'B': 'Doi electroni ar conduce formal la Mn(+V), nu la +IV.',
                          'C': 'Patru este N.O. final al Mn, nu numărul de electroni acceptați.',
                          'D': 'Cinci electroni sunt necesari pentru Mn²⁺ în acid, nu pentru MnO₂.'}},
 {'id': 'redox5_013',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.5',
  'topic': 'Redox versus precipitare',
  'level': 'Intermediar',
  'type': 'interpretare',
  'question': 'Care transformare NU este redox?',
  'options': ['A. Zn se transformă în Zn²⁺, iar Cu²⁺ în Cu',
              'B. H₂O₂ se descompune în apă și oxigen',
              'C. Ag⁺ și Cl⁻ formează AgCl solid',
              'D. Cl₂ formează clorură și hipoclorit în bază',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'C. Ag⁺ și Cl⁻ formează AgCl solid',
  'explanation': 'La precipitarea AgCl, Ag rămâne +I și Cl rămâne −I. Nu există variație a N.O. În celelalte '
                 'transformări se produc oxidare și reducere, inclusiv disproporționări în B și D.',
  'option_explanations': {'A': 'Zn crește de la 0 la +II, iar Cu scade de la +II la 0.',
                          'B': 'O(−I) trece simultan la −II în apă și 0 în O₂.',
                          'D': 'Cl(0) trece la −I și +I, deci are loc disproporționare redox.',
                          'E': 'Varianta C este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_014',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.5',
  'topic': 'Comproporționare',
  'level': 'Intermediar',
  'type': 'teorie',
  'question': 'Cum clasifici transformarea în care Fe(0) și Fe(+III) formează exclusiv Fe(+II)?',
  'options': ['A. Neutralizare fără redox',
              'B. Precipitare fără redox',
              'C. Disproporționare',
              'D. Comproporționare',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'D. Comproporționare',
  'explanation': 'Două stări inițiale diferite ale aceluiași element conduc la o stare intermediară comună. Fe(0) '
                 'se oxidează și Fe(+III) se reduce, așadar transformarea este o comproporționare redox.',
  'option_explanations': {'A': 'Nu este doar transfer de protoni: se schimbă N.O. al fierului.',
                          'B': 'Formarea unei stări intermediare implică transfer electronic, nu doar separarea '
                               'unui solid.',
                          'C': 'Disproporționarea pornește dintr-o singură stare spre două stări diferite.',
                          'E': 'Varianta D este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_015',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.5',
  'topic': 'Clor la cald',
  'level': 'Intermediar',
  'type': 'calcul',
  'question': 'La disproporționarea Cl₂ în NaOH cald și concentrat, care este raportul molar NaCl:NaClO₃?',
  'options': ['A. 5:1', 'B. 1:1', 'C. 3:1', 'D. 1:5', 'E. Niciuna dintre variantele A–D'],
  'answer': 'A. 5:1',
  'explanation': 'Un atom Cl trece de la 0 la +V și cedează cinci electroni. Cinci atomi Cl trec la −I și acceptă '
                 'câte unul. Rezultă cinci moli de clorură pentru fiecare mol de clorat, deci raportul 5:1.',
  'option_explanations': {'B': 'Raportul 1:1 corespunde hipocloritului format la rece, nu cloratului.',
                          'C': 'Trei este coeficientul Cl₂ în ecuația cu întregi minimi, nu raportul sărurilor.',
                          'D': 'Ai inversat numărul atomilor reduși și oxidați.',
                          'E': 'Varianta A este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_016',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.6',
  'topic': 'Cu și HNO₃ diluat',
  'level': 'Intermediar',
  'type': 'calcul',
  'question': 'În ecuația cu întregi minimi a reacției Cu cu HNO₃ diluat, produșii fiind Cu(NO₃)₂, NO și apă, ce '
              'coeficient are HNO₃?',
  'options': ['A. 2', 'B. 8', 'C. 6', 'D. 4', 'E. Niciuna dintre variantele A–D'],
  'answer': 'B. 8',
  'explanation': 'Trei Cu cedează șase electroni, acceptați de doi N(+V) care devin N(+II) în NO. Trei Cu(NO₃)₂ '
                 'păstrează șase atomi N, iar două NO conțin alți doi. Sunt necesare opt HNO₃ și se formează '
                 'patru H₂O.',
  'option_explanations': {'A': 'Doi este numărul N reduși, dar ignoră nitrații din sare.',
                          'C': 'Șase acoperă doar nitrații din sare, nu azotul din NO.',
                          'D': 'Patru este coeficientul acidului în reacția cu NO₂ și un singur Cu.',
                          'E': 'Varianta B este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_017',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.6',
  'topic': 'Cu și acid concentrat',
  'level': 'Intermediar',
  'type': 'calcul',
  'question': 'Pentru Cu cu HNO₃ concentrat, produsul redus fiind NO₂, câți moli de acid se consumă la un mol de '
              'Cu?',
  'options': ['A. 1 mol', 'B. 2 mol', 'C. 4 mol', 'D. 8 mol', 'E. Niciuna dintre variantele A–D'],
  'answer': 'C. 4 mol',
  'explanation': 'Cu cedează doi electroni. Fiecare N din NO₂ acceptă un electron, deci se formează doi moli NO₂. '
                 'Încă doi moli nitrat rămân în Cu(NO₃)₂; necesarul total este patru moli HNO₃ pentru un mol Cu.',
  'option_explanations': {'A': 'Un mol de acid nu asigură nici măcar cei doi nitrați ai sării.',
                          'B': 'Doi numără numai azotul redus sau numai nitrații sării, nu ambele contribuții.',
                          'D': 'Opt este un coeficient asociat ecuației cu trei Cu și NO, nu necesarul per Cu '
                               'aici.',
                          'E': 'Varianta C este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_018',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.6',
  'topic': 'Dicromat și clorură',
  'level': 'Intermediar',
  'type': 'calcul',
  'question': 'Un mol K₂Cr₂O₇ reacționează complet cu HCl în exces, formând CrCl₃ și Cl₂. Câți moli de Cl₂ '
              'rezultă?',
  'options': ['A. 1 mol', 'B. 2 mol', 'C. 6 mol', 'D. 7 mol', 'E. Niciuna dintre variantele A–D'],
  'answer': 'E. Niciuna dintre variantele A–D',
  'explanation': 'Doi Cr(+VI) devin Cr(+III) și acceptă în total șase moli de electroni. Doi ioni Cl⁻ cedează doi '
                 'electroni pentru fiecare Cl₂, astfel că se formează 6/2=3 mol Cl₂. Valoarea trei nu apare în '
                 'A–D.',
  'option_explanations': {'A': 'Un mol Cl₂ ar furniza numai doi moli de electroni, insuficienți pentru dicromat.',
                          'B': 'Doi moli ar furniza patru moli de electroni, tot insuficienți.',
                          'C': 'Șase este numărul molilor de atomi Cl oxidați, nu al moleculelor Cl₂.',
                          'D': 'Șapte este coeficientul apei în ecuație, fără legătură cu molii Cl₂.'}},
 {'id': 'redox5_019',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.7',
  'topic': 'Sarcina semireacției',
  'level': 'Intermediar',
  'type': 'interpretare',
  'question': 'La reducerea în acid a MnO₄⁻ la Mn²⁺, după adăugarea a 8 H⁺ și formarea a 4 H₂O, cum se egalează '
              'sarcina?',
  'options': ['A. Se adaugă cinci electroni în dreapta.',
              'B. Se adaugă trei electroni în stânga.',
              'C. Se adaugă opt electroni în dreapta.',
              'D. Se adaugă cinci electroni în stânga.',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'D. Se adaugă cinci electroni în stânga.',
  'explanation': 'Înainte de electroni, sarcina din stânga este −1+8=+7, iar în dreapta +2. Cinci electroni în '
                 'stânga reduc sarcina la +2. Aceștia sunt acceptați, conform reducerii Mn(+VII) la Mn(+II).',
  'option_explanations': {'A': 'În dreapta ar micșora sarcina produselor la −3 și ar indica oxidare.',
                          'B': 'Trei electroni lasă sarcina stângă +4, nu +2.',
                          'C': 'Numărul opt provine din protoni, nu din diferența sarcinilor.',
                          'E': 'Varianta D este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_020',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.7',
  'topic': 'Sulfat în ecuația moleculară',
  'level': 'Intermediar',
  'type': 'calcul',
  'question': 'În ecuația cu întregi minimi pentru KMnO₄ + FeSO₄ + H₂SO₄ cu produși K₂SO₄, MnSO₄, Fe₂(SO₄)₃ și '
              'apă, ce coeficient are H₂SO₄?',
  'options': ['A. 8', 'B. 5', 'C. 10', 'D. 16', 'E. Niciuna dintre variantele A–D'],
  'answer': 'A. 8',
  'explanation': 'Ecuația folosește doi permanganați și zece FeSO₄. Reducerea celor doi permanganați consumă 16 '
                 'H⁺, deci opt H₂SO₄. Cei 18 sulfați inițiali se regăsesc în 1 K₂SO₄, 2 MnSO₄ și 5 Fe₂(SO₄)₃.',
  'option_explanations': {'B': 'Cinci este coeficientul Fe₂(SO₄)₃, nu al acidului.',
                          'C': 'Zece este coeficientul FeSO₄.',
                          'D': 'Șaisprezece numără protonii, dar fiecare H₂SO₄ furnizează doi în bilanț.',
                          'E': 'Varianta A este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_021',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.7',
  'topic': 'Peroxid și protoni',
  'level': 'Intermediar',
  'type': 'calcul',
  'question': 'În ecuația ionică acidă a reacției dintre 2 mol MnO₄⁻ și cantitatea stoechiometrică de H₂O₂, cu '
              'Mn²⁺ și O₂ drept produși redox, câți moli de H⁺ se consumă net?',
  'options': ['A. 16 mol', 'B. 6 mol', 'C. 10 mol', 'D. 8 mol', 'E. Niciuna dintre variantele A–D'],
  'answer': 'B. 6 mol',
  'explanation': 'Doi permanganați acceptă zece electroni și consumă 16 mol H⁺ în semireacția de reducere. Cinci '
                 'H₂O₂ cedează zece electroni și produc 10 mol H⁺. Consumul net este 16−10=6 mol H⁺.',
  'option_explanations': {'A': 'Șaisprezece ignoră protonii produși de oxidarea peroxidului.',
                          'C': 'Zece reprezintă protonii produși, nu consumul net.',
                          'D': 'Opt este numărul molilor de apă formați, nu al protonilor consumați.',
                          'E': 'Varianta B este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_022',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.8',
  'topic': 'Sulfit și permanganat',
  'level': 'Intermediar',
  'type': 'calcul',
  'question': 'În mediu neutru/slab bazic, MnO₄⁻ oxidează SO₃²⁻ la SO₄²⁻ și se reduce la MnO₂. Ce raport molar '
              'MnO₄⁻:SO₃²⁻ este necesar?',
  'options': ['A. 1:1', 'B. 3:2', 'C. 2:3', 'D. 1:5', 'E. Niciuna dintre variantele A–D'],
  'answer': 'C. 2:3',
  'explanation': 'Fiecare Mn acceptă trei electroni, iar fiecare S trece de la +IV la +VI și cedează doi. Cel mai '
                 'mic multiplu comun este șase: doi permanganați acceptă șase electroni, trei sulfiți cedează '
                 'șase, deci raportul este 2:3.',
  'option_explanations': {'A': 'Un raport 1:1 ar lăsa trei electroni acceptați, dar numai doi cedați.',
                          'B': 'Este inversul raportului corect și nu conservă electronii.',
                          'D': 'Raportul 1:5 este specific permanganatului acid cu Fe²⁺, nu sulfitului cu MnO₂.',
                          'E': 'Varianta C este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_023',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.8',
  'topic': 'Trecerea la bazic',
  'level': 'Intermediar',
  'type': 'interpretare',
  'question': 'O semireacție provizorie conține 4 H⁺ în stânga. Care operație este corectă pentru trecerea la '
              'mediu bazic?',
  'options': ['A. Ștergi cei patru H⁺ fără alte modificări.',
              'B. Adaugi 4 OH⁻ numai în stânga.',
              'C. Muți protonii în dreapta fără schimbări.',
              'D. Adaugi 4 OH⁻ în ambii membri, formezi apă și simplifici.',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'D. Adaugi 4 OH⁻ în ambii membri, formezi apă și simplifici.',
  'explanation': 'Adăugarea aceleiași cantități de OH⁻ în ambii membri păstrează egalitatea atomilor și sarcinii. '
                 'În stânga, 4 H⁺ și 4 OH⁻ formează 4 H₂O; apoi apa comună se simplifică. Ștergerea protonilor '
                 'singuri nu conservă bilanțul.',
  'option_explanations': {'A': 'Ștergerea unilaterală modifică atât numărul atomilor H, cât și sarcina.',
                          'B': 'Adăugarea numai într-un membru strică egalitatea atomilor și a sarcinii.',
                          'C': 'Mutarea unei specii nu este operație validă asupra unei ecuații chimice fără '
                               'compensare.',
                          'E': 'Varianta D este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_024',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.8',
  'topic': 'Clor în bază rece',
  'level': 'Intermediar',
  'type': 'aplicație',
  'question': 'Câți moli de NaOH se consumă pentru 0,25 mol Cl₂ în soluție rece și diluată, cu formare de NaCl și '
              'NaClO?',
  'options': ['A. 0,50 mol', 'B. 0,25 mol', 'C. 0,125 mol', 'D. 1,50 mol', 'E. Niciuna dintre variantele A–D'],
  'answer': 'A. 0,50 mol',
  'explanation': 'Ecuația moleculară are raportul Cl₂:NaOH de 1:2. Pentru 0,25 mol Cl₂, necesarul este '
                 '2·0,25=0,50 mol NaOH. Se formează câte 0,25 mol NaCl și NaClO; atomii și electronii se '
                 'conservă.',
  'option_explanations': {'B': 'Ai presupus un raport 1:1 și ai omis al doilea ion Na⁺ necesar.',
                          'C': 'Ai inversat raportul și ai împărțit la doi.',
                          'D': 'Factorul șase este coeficientul NaOH pentru trei Cl₂ în ecuația la cald, nu per '
                               'un Cl₂.',
                          'E': 'Varianta A este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_025',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.9',
  'topic': 'Titrare',
  'level': 'Concurs',
  'type': 'calcul',
  'question': 'În prezența unei cantități suficiente de acid sulfuric, o probă de 10,00 mL de soluție de Fe²⁺ este titrată cu 12,00 mL de soluție de KMnO₄ de 0,0100 mol/L. '
              'Ce concentrație are Fe²⁺?',
  'options': ['A. 0,0120 mol/L',
              'B. 0,0240 mol/L',
              'C. 0,0500 mol/L',
              'D. 0,120 mol/L',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'E. Niciuna dintre variantele A–D',
  'explanation': 'Permanganatul este 0,01200·0,0100=0,000120 mol. Fierul(II) cedează un electron per ion, iar '
                 'permanganatul acceptă cinci, deci n(Fe²⁺)=0,000600 mol. Împărțirea la 0,01000 L dă 0,0600 '
                 'mol/L, absentă în A–D.',
  'option_explanations': {'A': 'Ai folosit raportul 1:1 în loc de 5:1.',
                          'B': 'Factorul doi nu este numărul electronilor cedați în oxidarea Fe²⁺ la Fe³⁺.',
                          'C': 'Ai înmulțit concentrația titrantului cu cinci fără corecția volumelor diferite.',
                          'D': 'Este dublul rezultatului, ca și cum volumul probei ar fi fost 5,00 mL.'}},
 {'id': 'redox5_026',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.9',
  'topic': 'Pilă galvanică',
  'level': 'Concurs',
  'type': 'aplicație',
  'question': 'Într-o pilă galvanică Zn/Cu funcțională, care afirmație este corectă?',
  'options': ['A. Electronii trec prin puntea salină de la Zn la Cu.',
              'B. Zincul este anod și se oxidează.',
              'C. Ionii Cu²⁺ se oxidează la catod.',
              'D. Electrodul de Cu pierde obligatoriu masă prin reducere.',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'B. Zincul este anod și se oxidează.',
  'explanation': 'Zincul cedează electroni și formează Zn²⁺: este anodul. Electronii circulă prin conductorul '
                 'exterior către catodul unde Cu²⁺ se reduce la Cu. Puntea salină transportă ioni, iar depunerea '
                 'cuprului mărește masa catodului în modelul ideal.',
  'option_explanations': {'A': 'Puntea salină asigură transport ionic; electronii circulă prin firul exterior.',
                          'C': 'La catod se produce reducere, nu oxidare.',
                          'D': 'Depunerea Cu crește masa electrodului, nu o micșorează.',
                          'E': 'Varianta B este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_027',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.9',
  'topic': 'Masă de fier',
  'level': 'Concurs',
  'type': 'calcul',
  'question': 'O probă conține exclusiv Fe²⁺ ca reducător și consumă 25,0 mL KMnO₄ de 0,0200 mol/L în acid '
              'sulfuric. Ce masă de Fe conține proba? Se dă Fe=56.',
  'options': ['A. 0,0280 g', 'B. 0,0700 g', 'C. 0,140 g', 'D. 0,280 g', 'E. Niciuna dintre variantele A–D'],
  'answer': 'C. 0,140 g',
  'explanation': 'n(MnO₄⁻)=0,0250·0,0200=0,000500 mol. Raportul Fe²⁺:MnO₄⁻ este 5:1, deci n(Fe)=0,00250 mol. Masa '
                 'este 0,00250·56=0,140 g; se cere fierul, nu masa unei sări hidratate.',
  'option_explanations': {'A': 'Este masa obținută prin folosirea raportului eronat 1:1.',
                          'B': 'Este jumătate din masa corectă, ca și cum ai atribui fierului doi electroni '
                               'cedați per ion.',
                          'D': 'Este dublul masei corecte, prin folosirea factorului zece în loc de cinci.',
                          'E': 'Varianta C este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_028',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.10',
  'topic': 'Simulare cu gaz',
  'level': 'Concurs',
  'type': 'calcul',
  'question': '6,40 g Cu pur reacționează complet cu HNO₃ diluat în exces, produsul redus fiind NO. Ce volum de '
              'NO rezultă la c.n., înaintea reacțiilor cu aerul? Cu=64; volumul molar la c.n. este 22,4 L/mol.',
  'options': ['A. 4,48/3 L', 'B. 2,24 L', 'C. 4,48 L', 'D. 2,24/3 L', 'E. Niciuna dintre variantele A–D'],
  'answer': 'A. 4,48/3 L',
  'explanation': 'n(Cu)=6,40/64=0,100 mol. Raportul Cu:NO este 3:2, deci n(NO)=0,200/3 mol. Volumul este '
                 '(0,200/3)·22,4=4,48/3 L, adică aproximativ 1,493 L. Controlul electronic dă '
                 '0,100·2=(0,200/3)·3=0,200 mol electroni.',
  'option_explanations': {'B': 'Ai folosit raportul Cu:NO de 1:1 în loc de 3:2.',
                          'C': 'Raportul 1:2 corespunde NO₂ la acid concentrat, nu NO.',
                          'D': 'Ai omis factorul doi din coeficientul NO.',
                          'E': 'Varianta A este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_029',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.10',
  'topic': 'Capacitate reducătoare totală',
  'level': 'Concurs',
  'type': 'calcul',
  'question': 'Într-un bilanț idealizat, 0,0060 mol Fe²⁺ și 0,0020 mol H₂O₂ sunt singurii reducători oxidați '
              'cantitativ de MnO₄⁻ în acid, la Fe³⁺ și O₂, fără reacții secundare. Ce cantitate de MnO₄⁻ se '
              'consumă?',
  'options': ['A. 0,0016 mol',
              'B. 0,0020 mol',
              'C. 0,0040 mol',
              'D. 0,0100 mol',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'B. 0,0020 mol',
  'explanation': 'Fe²⁺ furnizează 0,0060 mol electroni, iar H₂O₂ furnizează 2·0,0020=0,0040 mol electroni. '
                 'Totalul este 0,0100 mol electroni. Permanganatul acceptă cinci per ion, deci n=0,0100/5=0,0020 '
                 'mol. Ipoteza exclude procesele secundare ale unui amestec real.',
  'option_explanations': {'A': 'Ai adunat direct molii reducătorilor și ai împărțit la cinci, omițând factorul '
                               'doi al peroxidului.',
                          'C': 'Ai împărțit la un factor care nu este capacitatea de cinci electroni a '
                               'permanganatului acid.',
                          'D': 'Este cantitatea totală de electroni, nu de permanganat.',
                          'E': 'Varianta B este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}},
 {'id': 'redox5_030',
  'domain': 'Procese de oxidare și reducere',
  'lesson': '5.10',
  'topic': 'Puritate și reducerea unui oxid',
  'level': 'Concurs',
  'type': 'calcul',
  'question': 'O probă de 20,0 g conține Fe₂O₃ și impurități inerte. La reducerea completă cu CO se obțin 11,2 g '
              'Fe. Care este puritatea masică în Fe₂O₃? Fe=56; O=16.',
  'options': ['A. 56,0%', 'B. 70,0%', 'C. 80,0%', 'D. 100%', 'E. Niciuna dintre variantele A–D'],
  'answer': 'C. 80,0%',
  'explanation': 'n(Fe)=11,2/56=0,200 mol. Un mol Fe₂O₃ produce doi moli Fe, deci n(Fe₂O₃)=0,100 mol. '
                 'M(Fe₂O₃)=2·56+3·16=160 g/mol; masa oxidului este 16,0 g. Puritatea este 16,0/20,0·100=80,0%. '
                 'Bilanțul implică 0,300 mol CO și 0,600 mol electroni transferați.',
  'option_explanations': {'A': '56,0% este procentul fierului obținut raportat la probă, nu al oxidului inițial.',
                          'B': '70,0% este procentul Fe în Fe₂O₃ pur, nu puritatea probei.',
                          'D': 'Impuritățile reprezintă 4,0 g, deci proba nu este oxid pur.',
                          'E': 'Varianta C este corectă, conform bilanțului explicat; nu este justificată '
                               'excluderea tuturor variantelor A–D.'}}]
