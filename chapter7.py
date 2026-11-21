"""Hidrocarburi: material original de antrenament, nu subiecte oficiale."""

DOMAIN = "Hidrocarburi"

CHAPTER7_LESSONS = [
    {
        'id': 'hydro_lesson_01',
        'number': '7.1',
        'title': '7.1. Clasificarea hidrocarburilor și formulele generale',
        'level': 'Fundamente',
        'official': 'Hidrocarburi: clasificare, formule generale, nesaturare',
        'objectives': ['Să clasifici catenele și familiile',
 'Să aplici formulele generale în domeniul lor',
 'Să calculezi și să interpretezi NE'],
        'body': r"""
## Explicație teoretică

### De la compoziție la familie
Hidrocarburile conțin exclusiv carbon și hidrogen. Carbonul formează patru legături covalente, iar hidrogenul una. Catena poate fi deschisă (aciclică), liniară sau ramificată, ori închisă (ciclică). Ramificarea nu creează singură nesaturare: două catene aciclice saturate cu același număr de atomi de carbon au același număr de atomi de hidrogen.
Alcanii sunt aciclici și au numai legături simple. Cicloalcanii monociclici sunt saturați, dar închiderea ciclului elimină formal doi atomi de hidrogen față de alcanul aciclic. Alchenele aciclice cu o singură legătură dublă au aceeași formulă generală ca acești cicloalcani; formula moleculară singură nu îi distinge.
### Ce numără nesaturarea echivalentă
O legătură dublă sau un ciclu contribuie cu o unitate; o legătură triplă contribuie cu două. Alchinele aciclice cu o triplă și alcadienele aciclice cu două duble au aceeași formulă generală. O arenă mononucleară cu catenă laterală saturată are un nucleu benzenic: un ciclu și trei legături π formal localizate în reprezentarea Kekulé, deci patru unități de nesaturare.
NE este un bilanț formal, nu dovada existenței unei anumite grupe. Pentru o hidrocarbură neutră obișnuită, cu înveliș închis, trebuie să fie întreg și nenegativ. O formulă care trece acest test nu este automat stabilă și nici unic determinată structural. Naftalina are două nuclee condensate și nu se introduce în formula arenelor mononucleare.
### Domenii de aplicare
În formulele generale, n este numărul atomilor de carbon, nu cantitatea de substanță. Alcanii încep cu metanul; alchenele și alchinele cu doi atomi de carbon, cicloalcanii cu trei, alcadienele cu trei, iar seria benzenului cu șase. Când se cere identificarea familiei trebuie precizate informații suplimentare: catenă deschisă, tipul legăturilor sau comportarea chimică. Testele de adiție sunt utile pentru nesaturările obișnuite, dar benzenul nu se comportă ca o trienă aciclică.

## Definiții și concepte importante

- **Hidrocarbură**: compus alcătuit numai din C și H.
- **Omologi**: compuși ai aceleiași serii care diferă prin una sau mai multe grupe CH₂.
- **Izomeri**: compuși diferiți cu aceeași formulă moleculară.
- **NE**: număr formal de cicluri și de legături π, o triplă valorând două.

## Formule și relații

$$\mathrm{C_nH_{2n+2};\quad C_nH_{2n};\quad C_nH_{2n-2};\quad C_nH_{2n-6}}$$
În ordine: alcani; cicloalcani monociclici sau monoalchene aciclice; monoalchine sau alcadiene aciclice; arene mononucleare cu substituenți alchil. n este număr întreg de atomi, fără unitate; indicii arată numere de atomi din moleculă.

$$NE=\frac{2n_C+2-n_H}{2}$$
Aici n_C și n_H sunt numerele atomilor de C și H dintr-o moleculă de hidrocarbură; NE este adimensional. Formula nu se aplică nemodificată compușilor cu azot sau halogeni.

## Exemple rezolvate pas cu pas

### Exemplul 1 – Formula C₆H₁₀
1. Calculăm referința saturată: pentru șase atomi de carbon, numărul maxim aciclic de H este 2·6+2 = 14.
2. Deficitul este 14−10 = 4 atomi de H; împărțirea la 2 dă NE = 2.
3. Rezultat: sunt posibile o triplă, două duble, două cicluri ori un ciclu și o dublă. Nu identificăm automat o alchină.

### Exemplul 2 – Masa unui omolog al benzenului
1. Pentru o arenă mononucleară cu opt atomi de carbon și substituenți alchil, formula este C₈H₁₀, deoarece 2·8−6 = 10.
2. Cu mase atomice C=12 și H=1, masa molară este 8·12+10·1 = 106 g/mol.
3. Verificăm NE = (16+2−10)/2 = 4. Toluenul nu este răspunsul: el are șapte atomi de carbon; sunt posibili etilbenzenul și xilenii.

## Interpretarea rezultatelor

Același NE poate proveni din combinații structurale diferite. Masa molară și analiza elementală stabilesc formula moleculară, nu întotdeauna structura. În rezolvări, se scriu întâi ipotezele seriei: „aciclică, o singură dublă”, nu doar formula abreviată. Controlul valenței fiecărui carbon elimină formulele de structură imposibile. Pentru benzen NE este patru, deși nu reacționează ca trei alchene independente; stabilitatea aromatică trebuie tratată separat.
""",
        'mistakes': ['Greșeala: a identifica familia numai din formulă → Cum o eviți: enumeri structurile compatibile.',
 'Greșeala: a număra tripla ca o unitate → Cum o eviți: numeri cele două legături π.',
 'Greșeala: a aplica formula arenelor naftalinei → Cum o eviți: verifici numărul nucleelor.'],
        'takeaways': ['Hidrocarburile conțin numai C și H.',
 'Ramificarea nu modifică formula unui alcan.',
 'Un ciclu contribuie cu NE=1.',
 'O triplă contribuie cu NE=2.',
 'Benzenul are NE=4.'],
        'connections': ['Lecția 7.4 – dubla legătură și izomeria.',
 'Lecția 7.8 – aromaticitatea explică limitele analogiei cu alchenele.'],
    },
    {
        'id': 'hydro_lesson_02',
        'number': '7.2',
        'title': '7.2. Alcani: structură, nomenclatură, izomerie și proprietăți',
        'level': 'Fundamente',
        'official': 'Alcani: nomenclatură IUPAC, izomerie de catenă, proprietăți fizice',
        'objectives': ['Să denumești alcani ramificați simpli',
 'Să enumeri fără duplicate izomerii C₄–C₆',
 'Să explici fierberea și solubilitatea'],
        'body': r"""
## Explicație teoretică

### Structură și denumire
În alcani carbonul este hibridizat sp³, cu geometrie locală tetraedrică și unghiuri apropiate de 109,5°. Legăturile C–C și C–H sunt σ. Rotația în jurul unei legături simple produce conformații; nu transformă n-butanul în izobutan, deoarece conectivitatea atomilor rămâne aceeași.
Denumirea IUPAC începe cu alegerea celei mai lungi catene continue, nu a celei desenate orizontal. Se numerotează din capătul care dă cea mai mică succesiune de locanți la primul punct de diferență. Se identifică substituenții alchil și pozițiile lor. Grupele identice primesc prefixele di-, tri-, tetra-; substituenții diferiți se ordonează alfabetic, fără a lua în considerare aceste prefixe multiplicative. Cratimele separă cifrele de cuvinte și virgulele separă cifrele între ele.
### Izomeria de catenă
Se păstrează formula moleculară, dar se modifică scheletul de carbon. Pentru C₄H₁₀ există butan și 2-metilpropan. Pentru C₅H₁₂ există pentan, 2-metilbutan și 2,2-dimetilpropan. Pentru C₆H₁₄ există exact cinci schelete: hexan, 2-metilpentan, 3-metilpentan, 2,2-dimetilbutan și 2,3-dimetilbutan. O desenare inversată sau o rotire nu creează un izomer nou. Nu confundăm numărul izomerilor alcanului cu numărul derivaților lui monoclorurați: aceștia depind de pozițiile neechivalente ale hidrogenilor.
### Proprietăți și explicații microscopice
Alcanii sunt practic nepolari, insolubili în apă și solubili în solvenți nepolari. Nu formează legături de hidrogen cu apa. Densitățile alcanilor lichizi sunt, în general, mai mici decât densitatea apei; insolubilitatea nu înseamnă însă absența oricărei interacțiuni moleculare.
La presiune obișnuită și în jur de 20 °C, primii patru n-alcani sunt gaze, n-alcanii C₅–C₁₆ sunt lichizi, iar de la C₁₇ sunt solizi. Această delimitare este orientativă și nu se transferă automat tuturor izomerilor ramificați. În seria normală, creșterea masei și polarizabilității întărește forțele de dispersie și ridică temperatura de fierbere. Între izomeri, ramificarea reduce de regulă suprafața de contact și scade fierberea. Topirea depinde puternic și de simetrie și împachetare: nu urmează obligatoriu aceeași ordine.

## Definiții și concepte importante

- **Catenă principală**: cea mai lungă succesiune continuă de atomi de carbon, aleasă după regulile IUPAC.
- **Locant**: număr care indică poziția unui substituent.
- **Izomerie de catenă**: conectivități diferite ale scheletului carbonic.
- **Conformație**: aranjare spațială obținută prin rotație în jurul legăturilor simple.

## Formule și relații

$$\mathrm{C_nH_{2n+2}}\qquad M=14n+2\;\mathrm{g\,mol^{-1}}$$
n este numărul atomilor de C, întreg pozitiv; M este masa molară, calculată cu C=12 și H=1. Numărul de H este 2n+2, fără unitate. Relația pentru M este specifică acestor mase atomice.

$$NE=0$$
NE este nesaturarea echivalentă, adimensională, pentru orice alcan aciclic, indiferent de ramificare.

## Exemple rezolvate pas cu pas

### Exemplul 1 – Identificare după masă
1. Un alcan are M=72 g/mol, cu C=12 și H=1. Scriem 14n+2=72.
2. Rezultă n=(72−2)/14=5; formula este C₅H₁₂.
3. Enumerarea scheletelor dă pentan, 2-metilbutan și 2,2-dimetilpropan: trei izomeri, nu cinci. Toți au aceeași masă molară.

### Exemplul 2 – Denumire și fierbere
1. Pentru CH₃–CH(CH₃)–CH₂–CH₃, catena maximă are patru atomi, nu cinci.
2. Numerotarea dinspre ramificație dă locantul 2; numele este 2-metilbutan, nu 3-metilbutan.
3. Comparat cu pentanul, are aceeași formulă C₅H₁₂, dar este mai compact: fierbe la temperatură mai mică. Nu deducem de aici ordinea punctelor de topire.

## Interpretarea rezultatelor

Denumirea trebuie să permită reconstruirea unei singure conectivități. Dacă două denumiri se reduc la același schelet prin renumerotare, nu avem izomeri diferiți. Verificarea formulei se face completând valența patru a fiecărui carbon. Proprietățile fizice se compară la aceeași presiune; altfel, o temperatură de fierbere izolată nu permite o comparație corectă. Numărul atomilor de carbon explică tendința în serie, iar ramificarea explică diferențe între izomeri.
""",
        'mistakes': ['Greșeala: alegerea catenei desenate drept → Cum o eviți: cauți toate traseele continue.',
 'Greșeala: numărarea rotațiilor ca izomeri → Cum o eviți: compari conectivitatea.',
 'Greșeala: confundarea topirii cu fierberea → Cum o eviți: analizezi separat împachetarea.'],
        'takeaways': ['Carbonul alcanic este sp³.',
 'C₄H₁₀ are doi izomeri.',
 'C₅H₁₂ are trei izomeri.',
 'C₆H₁₄ are cinci izomeri.',
 'Ramificarea scade în general fierberea între izomeri.'],
        'connections': ['Lecția 7.1 – formula generală.', 'Lecția 7.3 – hidrogeni echivalenți și substituție.'],
    },
    {
        'id': 'hydro_lesson_03',
        'number': '7.3',
        'title': '7.3. Reacțiile alcanilor',
        'level': 'Intermediar',
        'official': 'Substituție radicalică, combustie, cracare, dehidrogenare, izomerizare',
        'objectives': ['Să explici cele trei etape ale lanțului radicalic',
 'Să diferențiezi mono- și polisubstituția',
 'Să deosebești cracarea de dehidrogenare și izomerizare'],
        'body': r"""
## Explicație teoretică

### Halogenarea: reacție în lanț
O legătură C–H este înlocuită cu C–X, iar hidrogenul eliminat formează HX. Clorurarea necesită inițiere fotochimică sau termică; nu se confundă cu adiția clorului la o legătură dublă. Un radical este o specie cu electron nepereche. Radicalii se regenerează în propagare, ceea ce permite multor molecule să reacționeze după un singur eveniment de inițiere.
Inițierea este ruperea homolitică a legăturii Cl–Cl: fiecare atom păstrează un electron. În propagare, radicalul clor extrage un H din metan, rezultând HCl și radical metil; acesta atacă o altă moleculă de clor, formează clorometan și regenerează radicalul clor. Întreruperea consumă doi radicali: doi atomi de clor se reunesc, radicalul metil se combină cu un radical clor sau doi radicali metil dau etan. Radicalul este notat prin punct, nu prin semnul sarcinii electrice.
### Selectivitate și polisubstituție
Clorometanul conține încă hidrogeni și poate fi clorurat succesiv până la diclorometan, triclorometan și tetraclorură de carbon. Excesul de metan favorizează statistic monosubstituția, fără a garanta un singur produs pur. La alcani nesimetrici apar și izomeri de poziție. Numărul lor se stabilește prin echivalența pozițiilor, nu prin numărul total al hidrogenilor. Proporțiile nu sunt în general egale: depind de numărul și reactivitatea tipurilor de H. Bromurarea este mai selectivă decât clorurarea.
### Transformări termice și catalitice
La ardere completă, în exces suficient de oxigen, rezultă dioxid de carbon și apă. Cu oxigen insuficient pot apărea CO și funingine. Cracarea rupe catene C–C și poate produce un alcan și o alchenă mai mici; ecuația dată mai jos este o cale posibilă, nu un produs unic al procesului industrial. Dehidrogenarea elimină H₂ și creează o nesaturare fără schimbarea numărului de atomi de C. Izomerizarea rearanjează scheletul, de exemplu butanul în 2-metilpropan, sub cataliză și condiții adecvate; nu modifică formula moleculară.

## Definiții și concepte importante

- **Substituție**: înlocuirea unui atom sau grup cu alt atom sau grup.
- **Homoliză**: rupere cu împărțirea egală a perechii de electroni.
- **Propagare**: etape care consumă și regenerează radicali.
- **Cracare**: fragmentare termică sau catalitică a catenei.

## Formule și relații

Pentru metan, în lumină:

$$\mathrm{CH_4+Cl_2\rightarrow CH_3Cl+HCl}$$

$$\mathrm{CH_3Cl+Cl_2\rightarrow CH_2Cl_2+HCl}$$

$$\mathrm{CH_2Cl_2+Cl_2\rightarrow CHCl_3+HCl}$$

$$\mathrm{CHCl_3+Cl_2\rightarrow CCl_4+HCl}$$
Coeficienții reprezintă raporturi de cantități în mol. Fiecare substituție consumă un mol Cl₂ pe mol de H înlocuit.

$$\mathrm{CH_4+2O_2\rightarrow CO_2+2H_2O}$$

$$\mathrm{C_4H_{10}\rightarrow C_2H_6+C_2H_4}$$

$$\mathrm{C_2H_6\rightarrow C_2H_4+H_2}$$
Ultimele două relații exemplifică o cracare, respectiv o dehidrogenare la temperatură ridicată; dehidrogenarea este favorizată de catalizatori adecvați.

## Exemple rezolvate pas cu pas

### Exemplul 1 – Monoclorurarea propanului
1. Scriem catena CH₃–CH₂–CH₃. Cei doi atomi terminali sunt echivalenți prin simetrie.
2. Înlocuirea unui H terminal dă 1-cloropropan; înlocuirea unui H central dă 2-cloropropan.
3. Rezultat: doi derivați de constituție. Nu rezultă trei numai fiindcă sunt trei atomi de carbon. Distribuția cantitativă cere date cinetice suplimentare.

### Exemplul 2 – Consumul la polisubstituție
1. Obținerea idealizată a unui mol de CH₂Cl₂ din CH₄ înlocuiește doi H.
2. Se adună primele două ecuații: un mol de metan consumă 2 mol Cl₂ și produce 2 mol HCl.
3. Pentru 0,25 mol metan transformați exclusiv astfel, consumul este 0,50 mol Cl₂. Cu Cl=35,5, masa este 0,50·71=35,5 g. În practică, amestecul de produși impune separare.

## Interpretarea rezultatelor

În mecanism, suma etapelor de propagare trebuie să elimine radicalii intermediari și să redea ecuația globală. Inițierea nu apare în bilanțul fiecărui ciclu propagativ. Cracarea păstrează totalul atomilor, dar nu obligatoriu numărul de molecule. Izomerizarea nu produce hidrogen, spre deosebire de dehidrogenare. Ecuațiile globale nu descriu randamentul și nu implică absența reacțiilor secundare.
""",
        'mistakes': ['Greșeala: scrierea radicalului ca ion → Cum o eviți: folosești punctul pentru electronul nepereche.',
 'Greșeala: presupunerea unui produs pur → Cum o eviți: iei în calcul substituțiile succesive.',
 'Greșeala: confundarea cracării cu izomerizarea → Cum o eviți: compari scheletele și formulele.'],
        'takeaways': ['Lumina poate iniția homoliza clorului.',
 'Propagarea regenerează radicali.',
 'Întreruperea consumă radicali.',
 'Monoclorurarea poate da izomeri.',
 'Cracarea și dehidrogenarea sunt procese diferite.'],
        'connections': ['Lecția 7.2 – simetria scheletului.', 'Lecția 7.10 – bilanțuri de combustie.'],
    },
    {
        'id': 'hydro_lesson_04',
        'number': '7.4',
        'title': '7.4. Alchene: structură, nomenclatură și izomerie',
        'level': 'Fundamente',
        'official': 'Alchene: legătura dublă, izomerie, proprietăți fizice',
        'objectives': ['Să descrii componentele σ și π',
 'Să denumești monoalchene simple',
 'Să numeri separat constituțiile și formele geometrice'],
        'body': r"""
## Explicație teoretică

### Dubla legătură nu este o legătură simplă dublată
La fiecare carbon al dublei legături, hibridizarea sp² dă trei direcții coplanare, cu unghiuri apropiate de 120°. Legătura C=C conține o componentă σ, prin suprapunere frontală, și o componentă π, prin suprapunere laterală a orbitalilor p nehibridizați. Densitatea π se află deasupra și dedesubtul planului local. Rotația liberă ar distruge suprapunerea π, deci este împiedicată; această restricție explică izomeria geometrică.
### Nomenclatura și tipurile de izomerie
Se alege o catenă principală care conține dubla, apoi se numerotează astfel încât dubla să primească locant minim. Pentru exemplele simple se folosesc numele but-1-enă, but-2-enă, 2-metilprop-1-enă (uzual 2-metilpropenă). Nu se privilegiază o ramificație în detrimentul locantului dublei.
Izomeria de poziție mută dubla în același schelet, ca între but-1-enă și but-2-enă. Izomeria de catenă schimbă scheletul, ca între but-1-enă și 2-metilpropenă. Izomeria geometrică păstrează conectivitatea și cere ca fiecare carbon al dublei să fie legat de doi substituenți diferiți. În but-2-enă, grupele metil de aceeași parte dau cis, iar de părți opuse dau trans. Dacă unul dintre atomi are doi H, condiția nu este îndeplinită. Pentru substituenți mai complecși, nomenclatura generală este E/Z; cis/trans se folosește aici doar când comparația este neambiguă.
### Proprietăți fizice și numărare corectă
Alchenele sunt în general slab polare, practic insolubile în apă și solubile în solvenți organici nepolari. Primele membre sunt gaze în condiții ambiante, apoi apar lichide și solide pe măsura creșterii catenei. Temperaturile de fierbere cresc în general cu masa molară; geometria poate modifica polaritatea și împachetarea. Nu se deduce automat ordinea punctelor de topire din simpla ramificare.
La C₄H₈ aciclic există trei izomeri de constituție. But-2-ena are două forme geometrice, ceilalți doi nu. Numărul total al formelor distincte, incluzând geometria, este patru; nu sunt patru izomeri de constituție și nici patru perechi cis/trans. Dacă se admit și cicloalcanii, lista de structuri trebuie extinsă; restricția „aciclic” este esențială.

## Definiții și concepte importante

- **Legătură π**: suprapunere laterală de orbitali, mai accesibilă reactivilor decât componenta σ.
- **Izomerie de poziție**: localizări diferite ale dublei pe același schelet.
- **Izomerie geometrică**: aranjări spațiale distincte din cauza rotației împiedicate.
- **cis/trans**: substituenți de referință de aceeași parte, respectiv de părți opuse.

## Formule și relații

$$\mathrm{C_nH_{2n}}\qquad NE=1\qquad M=14n\;\mathrm{g\,mol^{-1}}$$
n este numărul atomilor de carbon, cel puțin 2 pentru o monoalchenă aciclică; NE este adimensional; M este masa molară pentru C=12 și H=1. Formula nu exclude un cicloalcan dacă nu se precizează structura.

$$N_{\mathrm{forme}}=N_{\mathrm{fără\ geometrie}}+2N_{\mathrm{cu\ o\ pereche\ cis/trans}}$$
N reprezintă numere de structuri, fără unitate; relația se folosește aici numai pentru monoalchene simple cu cel mult o pereche cis/trans.

## Exemple rezolvate pas cu pas

### Exemplul 1 – Inventarul C₄H₈ aciclic
1. Scheletul neramificat dă but-1-enă și but-2-enă; numerotarea inversă nu adaugă but-3-enă.
2. Scheletul ramificat dă 2-metilpropenă. Avem trei constituții.
3. Numai but-2-ena îndeplinește condiția geometrică. Totalul formelor este 1+2+1=4: but-1-enă, cis-but-2-enă, trans-but-2-enă și 2-metilpropenă.

### Exemplul 2 – Masă și structură
1. O monoalchenă aciclică are M=70 g/mol, cu C=12, H=1. Din 14n=70 rezultă n=5, deci C₅H₁₀.
2. Pent-2-ena are la fiecare carbon al dublei câte un H și câte un substituent carbonic diferit de H; admite cis/trans.
3. Pent-1-ena are carbon terminal CH₂ și nu admite cis/trans. Aceeași formulă și aceeași masă nu garantează același comportament stereochimic.

## Interpretarea rezultatelor

Într-un desen cis/trans nu se schimbă poziția dublei și nu se rupe scheletul: se schimbă geometria relativă. Verificarea se face local, separat la fiecare carbon sp². Patru substituenți global diferiți nu sunt obligatorii, însă cei doi legați de același carbon trebuie să difere. Formula C₄H₈ are NE=1 indiferent dacă este alchenă sau cicloalcan; informația geometrică nu se recuperează din formula brută.
""",
        'mistakes': ['Greșeala: atribuirea cis/trans but-1-enei → Cum o eviți: verifici carbonul CH₂.',
 'Greșeala: numărarea but-3-enei separat → Cum o eviți: renumerotezi catena.',
 'Greșeala: omiterea restricției aciclice → Cum o eviți: citești toate ipotezele.'],
        'takeaways': ['Carbonii dublei sunt sp².',
 'Dubla conține σ+π.',
 'Rotația liberă este împiedicată.',
 'C₄H₈ aciclic are trei constituții.',
 'Cu geometria inclusă se obțin patru forme.'],
        'connections': ['Lecția 7.1 – formule comune mai multor familii.', 'Lecția 7.5 – reactivitatea electronilor π.'],
    },
    {
        'id': 'hydro_lesson_05',
        'number': '7.5',
        'title': '7.5. Reacțiile alchenelor',
        'level': 'Intermediar',
        'official': 'Adiție electrofilă, regula lui Markovnikov, oxidare blândă',
        'objectives': ['Să explici orientarea adiției HX',
 'Să interpretezi testele cu brom și permanganat',
 'Să calculezi consumuri pentru o dublă'],
        'body': r"""
## Explicație teoretică

### De ce predomină adiția
Componenta π este accesibilă și relativ ușor de consumat. La adiție se pierde componenta π și se formează legături σ noi, fără ruperea scheletului C–C. Hidrogenarea catalitică, de exemplu pe Ni, transformă o monoalchenă în alcan. Halogenarea cu brom consumă culoarea bromului; în modelul școlar se scrie dibromura vicinală. În apă pot apărea și bromohidrine, astfel încât ecuația dibromurii este modelul simplificat folosit în probleme. Decolorarea singură nu dovedește exclusiv o alchenă, fiind posibilă și la alte substanțe reactive.
### Adiția electrofilă și orientarea
În adiția ionică a HBr, norul π atacă protonul electrofil. Protonarea care dă carbocationul mai stabil este favorizată. Carbocationii alchilici secundari sunt, în exemple simple, mai stabili decât cei primari, prin efectele donatoare ale grupelor alchil și hiperconjugare. Ionul bromură atacă apoi carbocationul. La propenă, protonul se leagă preferențial de carbonul terminal, iar sarcina pozitivă apare pe carbonul secundar: se obține predominant 2-bromopropan.
Aceasta justifică regula lui Markovnikov pentru alchene nesimetrice simple: H se fixează preferențial la carbonul dublei care are deja mai mulți H. Regula nu spune că orice adiție trece prin carbocation liber. Adiția Br₂ implică de regulă un intermediar bromoniu. Hidrogenarea este un proces de suprafață catalitică. Pentru HBr în prezența peroxizilor poate apărea orientare radicalică anti-Markovnikov; aici toate exemplele HX sunt fără peroxizi și fără rearanjări.
### Hidratare, oxidare și combustie
În mediu acid, hidratarea urmează orientarea justificată prin protonare; după atacul apei și pierderea unui proton se obține alcoolul și se regenerează catalizatorul acid. Propena dă propan-2-ol. Permanganatul diluat, rece, în mediu neutru sau slab bazic oxidează dubla la diol vicinal: violetul dispare și poate apărea precipitat brun de MnO₂. Testul Baeyer este nespecific pentru alchene; nu se confundă cu oxidarea energică, ce poate rupe catena. Combustia completă formează CO₂ și apă, dar nu este test selectiv pentru dubla legătură.

## Definiții și concepte importante

- **Electrofil**: specie care acceptă o pereche de electroni.
- **Carbocation**: intermediar cu carbon pozitiv, electronodeficitar.
- **Diol vicinal**: compus cu două grupe OH pe atomi de carbon vecini.
- **Regula lui Markovnikov**: orientare predominantă în adiții ionice la alchene nesimetrice simple.

## Formule și relații

$$\mathrm{C_2H_4+H_2\rightarrow C_2H_6}$$

$$\mathrm{C_2H_4+Br_2\rightarrow C_2H_4Br_2}$$

$$\mathrm{C_3H_6+HBr\rightarrow C_3H_7Br}$$

$$\mathrm{C_3H_6+H_2O\rightarrow C_3H_8O}$$
Ultimele două produse sunt predominant 2-bromopropan și propan-2-ol în condițiile precizate; hidratarea necesită cataliză acidă. Coeficienții indică moli. Pentru o dublă obișnuită, un mol alchenă consumă un mol H₂ sau Br₂.

$$\mathrm{C_3H_6+\frac{9}{2}O_2\rightarrow 3CO_2+3H_2O}$$
Fracția reprezintă raport molar, nu jumătate de moleculă într-un eveniment individual.

## Exemple rezolvate pas cu pas

### Exemplul 1 – Brom consumat
1. Avem 5,6 g etenă, C=12, H=1 și Br=80. Masa molară a etenei este 28 g/mol.
2. Cantitatea este 5,6/28=0,20 mol. Raportul etenă:Br₂ este 1:1.
3. Se consumă 0,20 mol brom, adică 0,20·160=32 g. Masa dibromurii, dacă reacția este cantitativă în modelul simplificat, este 5,6+32=37,6 g.

### Exemplul 2 – Orientarea hidratării
1. La propenă, CH₂=CH–CH₃, protonarea carbonului terminal produce un carbocation secundar pe carbonul central.
2. Apa atacă acest centru, apoi se elimină un proton; catalizatorul acid este regenerat.
3. Produsul predominant este CH₃–CH(OH)–CH₃, propan-2-ol, nu propan-1-ol. Pentru 0,10 mol propenă la conversie totală și selectivitate ideală se obțin 0,10 mol alcool, adică 6,0 g pentru M=60 g/mol (C=12, H=1, O=16).

## Interpretarea rezultatelor

Dispariția culorii indică un consum de reactiv, nu o identificare structurală completă. Pentru calcule cantitative trebuie precizate mediul și modelul de reacție. La adiții se verifică atât numărul atomilor, cât și locul legării: formula C₃H₇Br nu distinge cei doi izomeri. Regula empirică trebuie însoțită de argumentul stabilității intermediarului, nu învățată ca simplă inversare mecanică a indicilor.
""",
        'mistakes': ['Greșeala: folosirea Markovnikov la H₂ → Cum o eviți: identifici mecanismul.',
 'Greșeala: identificarea sigură prin decolorare → Cum o eviți: amintești nespecificitatea testului.',
 'Greșeala: confundarea oxidării blânde cu ruperea catenei → Cum o eviți: precizezi condițiile.'],
        'takeaways': ['Adiția consumă componenta π.',
 'Hidrogenarea necesită catalizator.',
 'HX ionic favorizează carbocationul mai stabil.',
 'Hidratarea acidă produce alcool.',
 'Testul Baeyer este calitativ și nespecific.'],
        'connections': ['Lecția 7.4 – structura dublei.', 'Lecția 7.9 – adiție versus substituție aromatică.'],
    },
    {
        'id': 'hydro_lesson_06',
        'number': '7.6',
        'title': '7.6. Polimerizarea alchenelor și calcule',
        'level': 'Intermediar – calcule',
        'official': 'Monomeri, polimeri, grad de polimerizare și materiale uzuale',
        'objectives': ['Să reconstruiești monomerul din unitatea de repetare',
 'Să asociezi PE, PP, PVC, PS, PTFE și PAN cu monomerii',
 'Să calculezi gradul și randamentul fără a le confunda'],
        'body': r"""
## Explicație teoretică

### Cum se formează macromolecula
În polimerizarea prin adiție, moleculele mici de monomer se leagă succesiv; componenta π a dublei se consumă, iar componentele σ formează scheletul macromolecular. Nu se elimină o moleculă mică precum apa. Unitatea de repetare are aceeași compoziție elementală ca monomerul, dar altă conectivitate. Capetele de lanț provin din inițiator și din terminare; contribuția lor la masă este neglijată în modelul școlar.
Într-o descriere radicalică introductivă, un radical inițiator atacă dubla și creează un nou radical la capătul catenei. În propagare, capătul activ adaugă alte molecule. În terminare, centrii activi dispar prin procese precum combinarea. Nu toate polimerizările industriale sunt radicalice: pentru multe polialchene se folosesc catalizatori de coordonare. Condițiile influențează ramificarea, masa și organizarea lanțurilor, deci proprietățile materialului.
### Șase exemple importante
Etena, CH₂=CH₂, dă polietilenă (PE), cu unitatea –CH₂–CH₂–. Propena, CH₂=CH–CH₃, dă polipropilenă (PP), cu unitatea –CH₂–CH(CH₃)–. Clorura de vinil, CH₂=CHCl, dă policlorură de vinil (PVC), –CH₂–CHCl–; clorul rămâne în unitatea de repetare. Stirenul, CH₂=CH–C₆H₅, dă polistiren (PS), –CH₂–CH(C₆H₅)–: se consumă dubla vinilică, nu aromaticitatea nucleului.
Tetrafluoroetena, CF₂=CF₂, dă politetrafluoroetilenă (PTFE), –CF₂–CF₂–. Acrilonitrilul, CH₂=CH–CN, dă poliacrilonitril (PAN), –CH₂–CH(CN)–. Monomerii PVC, PTFE și PAN nu sunt hidrocarburi, dar sunt derivați nesaturați studiați aici pentru aceeași idee de polimerizare. În PAN, grupa nitril rămâne laterală în modelul uzual.
### De la raport molar la aplicații
PE se folosește la ambalaje și recipiente, PP la fibre și obiecte rezistente, PVC la țevi și izolații, PS la ambalaje și spume, PTFE la suprafețe cu frecare mică, PAN la fibre și precursori pentru fibre de carbon. Aditivii modifică proprietățile; nu identificăm materialul doar după un singur obiect.
Un eșantion real conține lanțuri de lungimi diferite. Masa molară medie și gradul mediu trebuie să fie de același tip, de exemplu medii numerice, când se aplică raportul maselor. Randamentul în masă al polimerizării nu este același lucru cu gradul de polimerizare: primul descrie cât material se obține, al doilea câte unități conține un lanț.

## Definiții și concepte importante

- **Monomer**: moleculă capabilă să formeze unități ale macromoleculei.
- **Unitate de repetare**: fragmentul structural repetat de-a lungul lanțului.
- **Grad de polimerizare**: număr de unități de monomer per lanț, sau valoare medie pentru un eșantion.
- **Polimerizare prin adiție**: unire fără eliminare de produs molecular mic.

## Formule și relații

$$n=\frac{M_{\mathrm{polimer}}}{M_{\mathrm{monomer}}}$$
n este gradul de polimerizare, fără unitate; cele două mase molare M sunt în g/mol. Relația neglijează grupele terminale; pentru un amestec se folosesc medii compatibile. Litera n nu desemnează aici cantitatea în mol.

$$m_{\mathrm{polimer}}=\eta\,m_{\mathrm{monomer}}$$
m sunt mase în g sau kg, în aceeași unitate; η este randamentul masic ca fracție între 0 și 1, în modelul fără pierderi suplimentare. Pentru procente se împarte valoarea procentuală la 100.

## Exemple rezolvate pas cu pas

### Exemplul 1 – Gradul pentru PE
1. Cu C=12 și H=1, monomerul C₂H₄ are M=28 g/mol.
2. Pentru un lanț idealizat cu M=140000 g/mol, n=140000/28=5000.
3. Lanțul conține 5000 unități de repetare și 10000 atomi de carbon proveniți din monomer. Nu conține 5000 mol de etenă: n este un număr pe lanț.

### Exemplul 2 – PVC și randament
1. Cu C=12, H=1, Cl=35,5, monomerul C₂H₃Cl are M=24+3+35,5=62,5 g/mol.
2. La M al polimerului de 125000 g/mol, n=125000/62,5=2000, neglijând capetele.
3. Din 250 kg monomer la randament masic de 80 %, se obțin 0,80·250=200 kg PVC. Masa obținută nu determină singură n: aceeași masă poate conține mai multe lanțuri scurte sau mai puține lanțuri lungi.

## Interpretarea rezultatelor

Controlul de masă este deosebit de simplu la polimerizarea prin adiție: compoziția unității rămâne cea a monomerului. Nu se scade apă ca la unele policondensări. Dacă raportul maselor dă o valoare neîntreagă pentru un eșantion, nu este automat o eroare: un grad mediu nu trebuie să fie întreg. Pentru o singură macromoleculă idealizată, numărul de unități este întreg. Separarea noțiunilor de masă a probei și masă molară previne confuzii de multe ordine de mărime.
""",
        'mistakes': ['Greșeala: scăderea apei la adiție → Cum o eviți: urmărești atomii monomerului.',
 'Greșeala: folosirea masei probei în raportul pentru n → Cum o eviți: verifici unitățile g/mol.',
 'Greșeala: consumarea nucleului aromatic la PS → Cum o eviți: identifici dubla vinilică.'],
        'takeaways': ['Dubla vinilică se consumă la polimerizare.',
 'Nu se elimină apă în modelul de adiție.',
 'n este adimensional.',
 'Masele medii trebuie să fie compatibile.',
 'Randamentul nu este grad de polimerizare.'],
        'connections': ['Lecția 7.4 – dubla legătură.', 'Lecția 7.8 – nucleul aromatic din stiren.'],
    },
    {
        'id': 'hydro_lesson_07',
        'number': '7.7',
        'title': '7.7. Alchine și acetilenă',
        'level': 'Intermediar',
        'official': 'Alchine: structură, obținere, adiții, acetiluri și combustie',
        'objectives': ['Să explici structura sp și lipsa cis/trans la triplă',
 'Să calculezi obținerea și adițiile acetilenei',
 'Să distingi hidratarea, tautomeria și formarea acetilurilor'],
        'body': r"""
## Explicație teoretică

### Structură și izomerie
Cei doi atomi de carbon ai triplei sunt hibridizați sp. Direcțiile legăturilor σ sunt coliniare, cu unghi local de 180°. Tripla conține o componentă σ și două componente π, provenite din două perechi de orbitali p perpendiculari. Nu se atribuie cis/trans triplei, fiindcă geometria locală este liniară. Catena principală conține tripla și se numerotează pentru locant minim: but-1-ină și but-2-ină sunt izomeri de poziție. De la catene suficient de mari apare și izomerie de catenă; 3-metilbut-1-ina și pent-1-ina au aceeași formulă C₅H₈. Alcadiènele aciclice sunt izomeri de funcțiune cu alchinele corespunzătoare.
### Obținere și adiții succesive
Acetilena (etina) se obține prin hidroliza carburii de calciu. Procesul degajă căldură și produce hidroxid de calciu. Este o reacție de obținere, nu o hidratare a triplei. O triplă poate adăuga doi echivalenți de hidrogen sau halogen. Hidrogenarea completă duce la alcan; un catalizator parțial dezactivat de tip Lindlar, Pd cu compuși ai Pb²⁺ pe suport, permite oprirea la alchenă. Pentru alchine interne această hidrogenare parțială favorizează alchena cis. Simpla folosire a unui mol de H₂ pe un catalizator foarte activ nu garantează selectivitatea.
Adiția unui echivalent HBr la acetilenă dă bromoetenă; al doilea echivalent dă predominant 1,1-dibromoetan, în condiții ionice obișnuite. La alchine nesimetrice simple se discută orientarea Markovnikov, fără a extinde mecanic toate detaliile mecanismului alchenelor.
### Kucerov și aciditate slabă
În prezență de Hg²⁺ și acid sulfuric, hidratarea acetilenei produce inițial enolul CH₂=CHOH, care se transformă în etanal, CH₃–CHO. Aceasta este tautomerie enol–carbonil: se mută un proton și o legătură dublă. Nu sunt doar două formule de rezonanță; se schimbă poziția unui atom. Etanalul este produsul stabil predominant. Celelalte alchine dau cetone prin hidratare în condițiile reacției Kucerov; alchinele interne nesimetrice pot da amestecuri de cetone. Nu generalizăm etanalul la orice alchină.
Hidrogenul legat direct de carbonul sp al unei alchine terminale are caracter slab acid, mai pronunțat decât H alchenic sau alcanic. Alchinele nu sunt acizi tari în apă și nu colorează indicatorii ca HCl. Cu baze suficient de tari ori prin formare de precipitate cu reactivi amoniacali ai Ag(I) și Cu(I) se pot obține acetiluri. But-2-ina nu are H acetilenic. Acetilurile de argint și cupru pot fi explozive la uscare: descrierea este teoretică, nu o instrucțiune de lucru.

## Definiții și concepte importante

- **Alchină terminală**: are fragmentul –C≡CH.
- **Enol**: compus cu OH legat de carbonul unei duble.
- **Tautomerie**: echilibru între structuri care diferă prin poziția unui proton și a unei legături π.
- **Acetilură**: derivat rezultat formal prin înlocuirea H acetilenic cu metal.

## Formule și relații

$$\mathrm{CaC_2+2H_2O\rightarrow C_2H_2+Ca(OH)_2}$$

$$\mathrm{C_2H_2+H_2\rightarrow C_2H_4}\qquad
\mathrm{C_2H_2+2H_2\rightarrow C_2H_6}$$
Prima hidrogenare este selectivă cu Pd/Pb²⁺ în condițiile descrise.

$$\mathrm{C_2H_2+2Br_2\rightarrow C_2H_2Br_4}$$

$$\mathrm{C_2H_2+HBr\rightarrow C_2H_3Br}\qquad
\mathrm{C_2H_3Br+HBr\rightarrow C_2H_4Br_2}$$

$$\mathrm{C_2H_2+H_2O\rightarrow CH_3CHO}$$
Ultima ecuație este bilanțul Kucerov, catalizat de Hg²⁺ în mediu acid.

$$\mathrm{2C_2H_2+5O_2\rightarrow 4CO_2+2H_2O}$$
Coeficienții exprimă raporturi molare; M(CaC₂)=64 g/mol și M(C₂H₂)=26 g/mol pentru Ca=40, C=12, H=1.

## Exemple rezolvate pas cu pas

### Exemplul 1 – Acetilenă din carbură
1. O probă de 80 g carbură tehnică are puritate masică 80 %. Masa CaC₂ pur este 80·0,80=64 g; impuritățile sunt presupuse inerte.
2. Cu Ca=40 și C=12, cantitatea este 64/64=1 mol CaC₂. Apa este în exces, iar randamentul este 100 %.
3. Se formează 1 mol acetilenă, deci 22,4 L la c.n., folosind 22,4 L/mol. Nu se aplică încă o dată factorul de puritate.

### Exemplul 2 – Hidrogenare totală
1. Pentru 2,6 g acetilenă, cu C=12 și H=1, cantitatea este 2,6/26=0,10 mol.
2. Tripla consumă 2 mol H₂ per mol acetilenă până la etan, deci 0,20 mol H₂.
3. La c.n. volumul este 0,20·22,4=4,48 L. Pentru hidrogenare parțială selectivă s-ar consuma numai 2,24 L, însă produsul ar fi etenă.

## Interpretarea rezultatelor

Bilanțul hidrolizei cere doi moli de apă, nu unul. La adiții se precizează dacă reacția este parțială sau totală; aceeași cantitate de alchină poate consuma cantități diferite de reactiv. Aciditatea H acetilenic este legată de poziția lui direct pe carbonul sp, nu de orice H din moleculă. În Kucerov atomii de C se conservă, astfel că etina dă un produs carbonilic cu doi atomi de carbon.
""",
        'mistakes': ['Greșeala: un mol H₂ pentru saturare totală → Cum o eviți: numeri două componente π.',
 'Greșeala: considerarea oricărui H drept acetilenic → Cum o eviți: verifici legarea directă de sp.',
 'Greșeala: confundarea enolului cu etanolul → Cum o eviți: urmărești formula C₂H₄O.'],
        'takeaways': ['Tripla are σ+2π.',
 'Geometria locală este liniară.',
 'CaC₂ produce acetilenă cu apă.',
 'Kucerov transformă etina în etanal.',
 'Numai alchinele terminale au H acetilenic.'],
        'connections': ['Lecția 7.5 – comparația adițiilor.', 'Lecția 7.10 – arderea acetilenei.'],
    },
    {
        'id': 'hydro_lesson_08',
        'number': '7.8',
        'title': '7.8. Arene: structura benzenului și omologi',
        'level': 'Intermediar',
        'official': 'Benzen: aromaticitate, proprietăți fizice; toluen, xileni, naftalină',
        'objectives': ['Să explici sextetul aromatic și rezonanța',
 'Să diferențiezi toluenul, xilenii și etilbenzenul',
 'Să recunoști limitele formulei mononucleare'],
        'body': r"""
## Explicație teoretică

### Kekulé și modelul electronic
Benzenul are formula C₆H₆ și un inel hexagonal plan. Fiecare carbon este sp² și formează trei legături σ; orbitalul p rămas participă la sistemul π comun. Cele două reprezentări Kekulé cu duble alternante sunt structuri-limită de rezonanță. Molecula nu oscilează între două structuri cu legături scurte și lungi și nu reprezintă un amestec de doi izomeri. Cei șase electroni π sunt delocalizați pe întregul ciclu; cercul înscris în hexagon simbolizează sextetul aromatic.
Toate legăturile C–C din benzen sunt egale, de aproximativ 1,39 Å, intermediare între o legătură simplă și una dublă obișnuită. Unghiurile inelului sunt de 120°. Aceste date sunt compatibile cu delocalizarea și simetria moleculei, nu cu trei duble independente. Stabilizarea aromatică face adițiile mult mai dificile decât la alchene, deoarece adiția ar întrerupe delocalizarea.
### Proprietăți fizice și securitate
Benzenul este un lichid incolor, volatil și inflamabil, practic insolubil în apă, dar miscibil cu mulți solvenți organici. Densitatea sa este mai mică decât a apei. Este toxic și cancerigen: mirosul nu se verifică direct și nu se propun experiențe casnice. Hidrocarburile aromatice nu se definesc printr-un miros plăcut; termenul are sens structural și electronic.
Toluenul, metilbenzenul, are formula C₇H₈. Xilenii, dimetilbenzenii C₈H₁₀, există ca trei izomeri de poziție: 1,2- (orto), 1,3- (meta) și 1,4- (para). Etilbenzenul are tot formula C₈H₁₀, dar nu este xilen: are un singur substituent etil. Toți aceștia sunt arene mononucleare cu substituenți saturați.
### Două inele nu înseamnă două benzenuri izolate
Naftalina, C₁₀H₈, conține două inele condensate care au în comun doi atomi de carbon și o latură. Nu se adună pur și simplu două formule C₆H₆. Este solidă la temperatura ambiantă și sublimează; vaporii pot fi nocivi, deci utilizările istorice nu reprezintă recomandări de manipulare. Sistemul aromatic este comun, iar toate legăturile sale nu sunt identice ca în benzen. Formula generală a arenelor mononucleare nu se aplică naftalinei.
Recunoașterea aromaticității în acest capitol se bazează pe exemplele studiate, nu pe simplul calcul NE. Un compus cu NE=4 poate avea alte structuri; numai cunoașterea conectivității și a sistemului electronic justifică numele de arenă.

## Definiții și concepte importante

- **Arenă**: hidrocarbură cu sistem aromatic de tipul celor studiate.
- **Delocalizare**: distribuirea electronilor π pe mai mulți atomi ai sistemului conjugat.
- **Rezonanță**: descriere prin structuri-limită, fără schimbarea pozițiilor nucleelor.
- **Inele condensate**: inele care au o latură comună.

## Formule și relații

$$\mathrm{C_nH_{2n-6}}\qquad NE=4$$
n este numărul atomilor de carbon, cel puțin 6; formula se referă la arene mononucleare cu substituenți alchil. NE nu are unitate.

$$d_{\mathrm{C-C}}\approx1{,}39\;\text{Å}=0{,}139\;\mathrm{nm}$$
d este lungimea legăturii C–C în benzen; Å este ångströmul, egal cu 10⁻¹⁰ m, iar nm este nanometrul, 10⁻⁹ m. Unghiul C–C–C de 120° este măsurat în grade, nu în radiani.

## Exemple rezolvate pas cu pas

### Exemplul 1 – Izomerii cu opt atomi de carbon
1. Pentru C₈H₁₀, într-o arenă mononucleară cu substituenți alchil rămân doi atomi de C în afara nucleului.
2. Ei pot forma un etil (etilbenzen) ori doi metili (xileni).
3. Doi metili admit trei poziții relative: 1,2; 1,3; 1,4. Totalul este patru arene, dintre care trei xileni. Pozițiile 1,5 și 1,6 se renumerotează în 1,3 și 1,2.

### Exemplul 2 – Comparația NE
1. Pentru benzen C₆H₆, NE=(2·6+2−6)/2=4.
2. Pentru naftalină C₁₀H₈, NE=(20+2−8)/2=7: două cicluri și cinci legături π în reprezentarea formală.
3. Formula mononucleară la zece atomi ar da H=14, nu 8. Rezultatul arată că naftalina este în afara seriei, nu că are o formulă greșită.

## Interpretarea rezultatelor

Distanțele egale din benzen sunt un argument structural puternic împotriva modelului cu legături strict alternante. Numărarea izomerilor de poziție cere simetria hexagonului, nu șase etichete fixe pe un desen. NE exprimă deficitul de hidrogen, dar nu măsoară direct stabilizarea aromatică. În descrierea naftalinei evităm să transferăm fără justificare egalitatea tuturor legăturilor specifică benzenului.
""",
        'mistakes': ['Greșeala: două forme Kekulé ca doi izomeri → Cum o eviți: distingi rezonanța de izomerie.',
 'Greșeala: patru xileni → Cum o eviți: separi etilbenzenul.',
 'Greșeala: aplicarea lungimilor egale întregii naftaline → Cum o eviți: nu generalizezi simetria '
 'benzenului.'],
        'takeaways': ['Benzenul este plan.',
 'Unghiurile sunt de 120°.',
 'Legăturile C–C sunt egale, aproximativ 1,39 Å.',
 'Există trei xileni.',
 'Naftalina este o arenă cu inele condensate.'],
        'connections': ['Lecția 7.1 – NE.', 'Lecția 7.9 – refacerea aromaticității în substituție.'],
    },
    {
        'id': 'hydro_lesson_09',
        'number': '7.9',
        'title': '7.9. Reacțiile benzenului și ale catenei laterale',
        'level': 'Intermediar',
        'official': 'Substituție electrofilă aromatică, adiții dificile, oxidarea toluenului',
        'objectives': ['Să explici etapele substituției electrofile',
 'Să asociezi condițiile cu produsul corect',
 'Să diferențiezi oxidarea catenei și transformările nucleului'],
        'body': r"""
## Explicație teoretică

### De ce substituție, nu adiție ușoară
Norul π aromatic poate ataca un electrofil, dar pierderea stabilizării aromatice costă energie. Mecanismul general al substituției electrofile are trei idei: generarea electrofilului cu ajutorul mediului sau catalizatorului; atacul inelului și formarea unui complex σ cationic, temporar nearomatic; pierderea protonului de pe carbonul atacat, cu refacerea sistemului aromatic. Produsul final păstrează inelul aromatic, spre deosebire de produsul unei adiții. Complexul σ este un intermediar, nu produsul izolat obișnuit.
### Patru substituții reprezentative
Clorurarea sau bromurarea inelului necesită de obicei un acid Lewis, FeCl₃ sau FeBr₃. Catalizatorul polarizează halogenul, făcându-l suficient de electrofil; nu este necesară postularea unui ion halogen pozitiv liber în soluție. Se înlocuiește un H și se formează HX. În absența catalizatorului și a condițiilor speciale, benzenul nu decolorează rapid bromul ca o alchenă.
Nitrarea folosește amestec sulfonitric, HNO₃ concentrat și H₂SO₄ concentrat. Acidul sulfuric favorizează formarea ionului nitroniu NO₂⁺, electrofilul atacant; nitrobenzenul nu este un nitrit sau nitrat organic. Sulfonarea cu SO₃ în mediu sulfuric introduce grupa –SO₃H; procesul este reversibil în funcție de condiții. Alchilarea Friedel–Crafts cu un halogenoalcan și AlCl₃ introduce o grupă alchil, de exemplu metil. Pot apărea polialchilare și rearanjări pentru unii reactanți, deci ecuația simplă este introductivă, nu o metodă universal perfect selectivă.
### Adiția dificilă și reactivitatea toluenului
Hidrogenarea benzenului necesită Ni, temperatură și presiune și formează ciclohexan; consumă trei moli H₂ pe mol benzen. Adiția fotochimică a clorului dă hexaclorociclohexan, C₆H₆Cl₆, amestec de stereoizomeri. Acesta nu este hexaclorobenzenul C₆Cl₆, care ar fi produs de substituție exhaustivă.
La toluen, catena laterală se poate oxida energic cu permanganat, la cald, până la grupă carboxil, cu obținerea acidului benzoic după acidificare. Este necesar H benzilic pentru oxidarea uzuală a unei catene alchilice. Nu se oxidează ușor nucleul în aceleași condiții. Halogenarea catenei radicalic, sub lumină, nu trebuie confundată cu substituția inelului în prezență de FeX₃; condițiile sunt parte esențială a identificării reacției.

## Definiții și concepte importante

- **Complex σ**: intermediar cationic de atac electrofil, cu aromaticitate temporar pierdută.
- **Acid Lewis**: acceptor de pereche electronică, precum FeCl₃ sau AlCl₃.
- **Poziție benzilică**: carbon saturat legat direct de nucleul aromatic.
- **Amestec sulfonitric**: amestec de acizi azotic și sulfuric concentrați.

## Formule și relații

$$\mathrm{C_6H_6+Cl_2\rightarrow C_6H_5Cl+HCl}$$
FeCl₃ catalizează substituția.

$$\mathrm{C_6H_6+HNO_3\rightarrow C_6H_5NO_2+H_2O}$$
H₂SO₄ este mediul catalitic al nitrării.

$$\mathrm{C_6H_6+SO_3\rightarrow C_6H_6SO_3}$$
Produsul este acid benzensulfonic, C₆H₅–SO₃H.

$$\mathrm{C_6H_6+CH_3Cl\rightarrow C_7H_8+HCl}$$
AlCl₃ este catalizatorul Friedel–Crafts.

$$\mathrm{C_6H_6+3H_2\rightarrow C_6H_{12}}\qquad
\mathrm{C_6H_6+3Cl_2\rightarrow C_6H_6Cl_6}$$
Condițiile sunt Ni, temperatură și presiune, respectiv lumină. Coeficienții sunt raporturi molare, fără unitate.

$$\mathrm{C_7H_8+3[O]\rightarrow C_7H_6O_2+H_2O}$$
[O] reprezintă un echivalent formal de atom de oxigen furnizat de oxidant, nu oxigen atomic izolat în soluție; aceasta este o schemă de bilanț organic.

## Exemple rezolvate pas cu pas

### Exemplul 1 – Nitrare idealizată
1. Cu C=12, H=1, N=14, O=16, M(benzen)=78 g/mol și M(nitrobenzen)=123 g/mol.
2. Din 15,6 g benzen avem 15,6/78=0,20 mol. HNO₃ este în exces, raportul molar este 1:1.
3. Masa teoretică este 0,20·123=24,6 g. La randament de 75 %, masa izolată este 24,6·0,75=18,45 g.

### Exemplul 2 – Substituție versus adiție
1. Pentru 0,10 mol benzen, monoclorurarea catalitică ar consuma 0,10 mol Cl₂ și ar da 0,10 mol HCl.
2. Adiția fotochimică totală consumă în schimb 0,30 mol Cl₂ și nu elimină HCl.
3. Cu Cl=35,5, consumurile sunt 7,1 g, respectiv 21,3 g clor. Formulele produselor sunt C₆H₅Cl și C₆H₆Cl₆, nu același compus.

## Interpretarea rezultatelor

O ecuație fără condiții poate fi ambiguă: benzenul și clorul au comportări diferite în lumină față de cataliză Lewis. La nitrare se conservă șase atomi de carbon, iar grupa introdusă este NO₂. La oxidarea toluenului carbonul metilului devine carbonul carboxilic, astfel încât produsul are tot șapte atomi de carbon. Refacerea aromaticității explică eliminarea protonului în ultima etapă a substituției.
""",
        'mistakes': ['Greșeala: adiție în loc de substituție la FeCl₃ → Cum o eviți: verifici eliminarea HCl.',
 'Greșeala: confundarea C₆H₆Cl₆ cu C₆Cl₆ → Cum o eviți: numeri hidrogenii.',
 'Greșeala: numirea NO₃⁻ drept electrofil al nitrării → Cum o eviți: identifici NO₂⁺.'],
        'takeaways': ['Substituția reface aromaticitatea.',
 'FeX₃ activează halogenul.',
 'Nitrarea folosește NO₂⁺.',
 'Hidrogenarea benzenului consumă trei H₂.',
 'Toluenul se oxidează la acid benzoic.'],
        'connections': ['Lecția 7.3 – halogenare radicalică.', 'Lecția 7.8 – stabilitatea aromatică.'],
    },
    {
        'id': 'hydro_lesson_10',
        'number': '7.10',
        'title': '7.10. Combustia hidrocarburilor și combustibili',
        'level': 'Intermediar – calcule',
        'official': 'Combustie, aer, putere calorică, combustibili și impact',
        'objectives': ['Să egalezi ecuațiile de combustie și să calculezi volume',
 'Să utilizezi corect convenția aerului și excesul',
 'Să explici puterea calorică, cifra octanică și riscurile'],
        'body': r"""
## Explicație teoretică

### Bilanțul arderii complete
La ardere completă, fiecare atom de carbon ajunge într-o moleculă de CO₂, iar câte doi atomi de hidrogen formează o moleculă de apă. Se echilibrează întâi C și H, apoi O. Coeficientul oxigenului rezultă adunând oxigenul necesar celor două produse. Oxigenul în exces nu schimbă cantitatea teoretică de CO₂, ci rămâne în gazele finale dacă arderea este completă.
În acest capitol folosim explicit convenția de calcul: aer uscat cu 20 % O₂ în volume, restul fiind considerat inert în bilanțul simplificat. Nu este valoarea exactă a atmosferei reale, care are circa 21 % O₂. La aceeași temperatură și presiune, raporturile volumelor gazelor ideale sunt raporturile molare. Nu aplicăm aceste raporturi între volume de gaz și volume de lichid sau solid. La c.n., apa produsă este în mare parte condensată; dacă se cere volumul gazelor uscate, apa nu se include.
### Energie și aplicații
Puterea calorică reprezintă energia eliberată prin arderea completă a unității de masă sau de volum de combustibil, de exemplu MJ/kg ori MJ/m³. Nu este o putere mecanică în wați, în pofida denumirii uzuale. Valoarea superioară include căldura recuperată prin condensarea apei, iar cea inferioară nu o include. Pentru o comparație trebuie specificată aceeași bază și aceeași convenție.
GPL este un amestec dominat de propan și butani, lichefiat sub presiune; nu este metan pur. Benzina este un amestec de hidrocarburi, nu octan pur. Cifra octanică măsoară rezistența la detonație, raportată la o scară de referință cu izooctan (2,2,4-trimetilpentan) 100 și n-heptan 0. O benzină cu cifra octanică 95 nu este obligatoriu un amestec care conține efectiv 95 % izooctan și nu eliberează neapărat mai multă energie pe kilogram decât una cu cifra 90.
### Produși nedoriți
CO₂ contribuie la efectul de seră; arderea completă elimină CO, dar nu elimină impactul climatic al carbonului fosil. În lipsă de oxigen sau la amestecare insuficientă poate apărea CO, foarte toxic deoarece afectează transportul oxigenului prin hemoglobină. Funinginea conține particule bogate în carbon și afectează sănătatea și mediul. Arderea reală poate genera și NOₓ din aer la temperatură înaltă, fenomen necuprins în bilanțul simplificat O₂/inert. Un aparat care arde combustibil necesită evacuare și aerisire adecvate; absența fumului vizibil nu garantează absența CO.

## Definiții și concepte importante

- **Ardere completă**: oxidare a C la CO₂ și a H la apă.
- **Aer teoretic**: cantitatea minimă calculată pentru arderea completă ideală.
- **Exces de aer**: aer furnizat peste cantitatea teoretică.
- **Cifră octanică**: indicator al rezistenței benzinei la detonație.

## Formule și relații

$$\mathrm{C_xH_y}+\left(x+\frac y4\right)\mathrm{O_2}\rightarrow x\mathrm{CO_2}+\frac y2\mathrm{H_2O}$$
x și y sunt numerele atomilor C și H din moleculă, fără unitate; coeficienții sunt raporturi molare. Pentru alcani coeficientul O₂ este (3x+1)/2, pentru monoalchene 3x/2, pentru monoalchine (3x−1)/2, iar pentru arene mononucleare (3x−3)/2.

$$V_{\mathrm{aer}}=\frac{V_{\mathrm{O_2}}}{0{,}20}=5V_{\mathrm{O_2}}\qquad Q=mq$$
V sunt volume la aceeași temperatură și presiune, în L sau m³; 0,20 este fracția volumică convenită de O₂. Q este energia eliberată în MJ, m masa în kg și q puterea calorică masică în MJ/kg. Nu se confundă q cu un debit energetic.

## Exemple rezolvate pas cu pas

### Exemplul 1 – Propan și aer
1. Ecuația este C₃H₈ + 5O₂ → 3CO₂ + 4H₂O. Pentru 4,48 L propan la c.n., cantitatea este 4,48/22,4=0,20 mol.
2. Se cer 1,00 mol O₂, deci 22,4 L la c.n.; aerul teoretic cu 20 % O₂ este 22,4/0,20=112 L.
3. Se formează 0,60 mol CO₂, adică 13,44 L la c.n., și 0,80 mol apă, adică 14,4 g cu H=1 și O=16. Apa nu se numără ca gaz ideal la c.n.

### Exemplul 2 – Exces de aer și energie
1. Pentru același propan se furnizează 25 % exces față de 112 L aer teoretic: 112·1,25=140 L.
2. Aerul aduce 28 L O₂; după ardere completă rămân 28−22,4=5,6 L O₂, toate volumele raportate la c.n.
3. Dacă 2 kg combustibil au q=46 MJ/kg, energia este 2·46=92 MJ. Aceasta este energia chimică eliberată; la randament util de 80 %, energia utilă ar fi 73,6 MJ.

## Interpretarea rezultatelor

Volumul de aer este de cinci ori cel de oxigen numai sub convenția explicită de 20 %. În gazele uscate finale se pot afla CO₂, inertul aerului și O₂ neconsumat, nu doar CO₂. La calculul masei de apă nu contează dacă ea condensează, însă la volumul amestecului contează. Controlul carbonului este rapid: numărul de moli de CO₂ trebuie să egaleze numărul de moli de atomi de C introduși.
""",
        'mistakes': ['Greșeala: folosirea a 20 L aer pentru 20 L O₂ → Cum o eviți: împarți la 0,20.',
 'Greșeala: includerea apei în gaze uscate → Cum o eviți: citești condițiile.',
 'Greșeala: echivalarea cifrei octanice cu energia → Cum o eviți: reții definiția rezistenței la detonație.'],
        'takeaways': ['Aerul de calcul are 20 % O₂ în volume.',
 'Raporturile de volume cer aceeași temperatură și presiune.',
 'Apa se exclude din gazele uscate.',
 'GPL conține mai ales propan și butani.',
 'CO este toxic, CO₂ are impact climatic.'],
        'connections': ['Lecția 7.1 – formule generale.', 'Lecția 7.11 – probleme inverse de combustie.'],
    },
    {
        'id': 'hydro_lesson_11',
        'number': '7.11',
        'title': '7.11. Recapitulare și probleme de nivel concurs',
        'level': 'Concurs',
        'official': 'Probleme integrate de structură, reactivitate și bilanțuri',
        'objectives': ['Să combini date de ardere și masă molară',
 'Să rezolvi bilanțuri de amestecuri',
 'Să numeri produșii precizând nivelul constituțional sau stereochimic'],
        'body': r"""
## Explicație teoretică

### Strategia unei probleme integrate
Se separă trei niveluri: formula moleculară, conectivitatea și geometria. Analiza de combustie dă compoziția; o masă molară stabilește multiplicatorul formulei empirice; testele și consumurile de reactiv restrâng structurile. O formulă cu NE=1 nu dovedește o alchenă, iar o formulă cu NE=4 nu dovedește un nucleu benzenic. O concluzie structurală se sprijină pe toate ipotezele explicite.
Se scriu întâi necunoscutele ca numere de moli și se traduc observațiile în ecuații independente. Pentru amestecuri gazoase la aceeași temperatură și presiune, fracțiile de volum sunt fracții molare. În bilanțurile masice se includ doar substanțele care participă conform ipotezelor. Impuritățile inerte, randamentul și excesul sunt factori diferiți și se aplică o singură dată la etapa potrivită.
### Alegerea transformării diagnostice
Bromul consumat cantitativ în modelul de adiție poate indica numărul de componente π alifatice reactive. Etena consumă un mol Br₂, iar acetilena doi la adiție totală. Benzenul nu intră în această comparație ca trei alchene. Hidrogenarea completă poate consuma un mol H₂ la alchenă, doi la alchină sau trei la nucleul benzenic, dar condițiile și selectivitatea trebuie precizate. Un test negativ nu este mereu dovada absenței unei grupe dacă mediul sau timpul sunt nepotrivite.
La numărarea derivaților monoclorurați se pornește de la pozițiile neechivalente prin simetrie. Neopentanul are un singur tip de H și un singur produs de constituție, n-pentanul trei, iar 2-metilbutanul patru. Dacă se cere și stereochimia, un produs chiral poate exista ca doi enantiomeri: enunțul trebuie să spună ce se numără. Pentru butan sunt doi derivați de constituție; 2-clorobutanul este chiral, astfel că incluzând enantiomerii numărul formelor individuale este trei.
### Controlul soluției și originalitatea antrenamentului
După calcul se verifică negația distractorilor: o valoare poate părea plauzibilă, dar să folosească masa molară greșită ori să includă apă în gaze uscate. Fracțiile unui amestec trebuie să fie între zero și unu, numerele atomilor să fie întregi, iar sumele maselor să respecte conservarea. Dacă datele nu disting izomerii, se spune explicit acest lucru; nu se inventează o structură unică. Problemele și întrebările acestui capitol sunt materiale originale de antrenament, nu subiecte oficiale ale unui concurs. Scopul nivelului concurs este combinarea raționamentelor, nu extinderea nejustificată a regulilor simple.

## Definiții și concepte importante

- **Formulă empirică**: cel mai simplu raport întreg al atomilor.
- **Bilanț independent**: relație care aduce informație nouă despre necunoscute.
- **Poziții echivalente**: poziții care duc la aceeași constituție prin simetrie.
- **Selectivitate**: preferință pentru un produs dintre mai mulți posibili.

## Formule și relații

$$n(\mathrm C)=n(\mathrm{CO_2})\qquad n(\mathrm H)=2n(\mathrm{H_2O})$$
n(C) și n(H) sunt cantitățile atomilor în mol; celelalte n sunt cantități moleculare în mol. Relațiile presupun ardere completă a unei hidrocarburi, fără alte surse de C sau H.

$$a+b=n_{\mathrm{amestec}}\qquad 2a+3b=n_{\mathrm{CO_2}}$$
a și b sunt moli de etenă și propan; n sunt cantități în mol. Coeficienții 2 și 3 sunt numerele de C per moleculă. Aceste ecuații nu se transferă altui amestec fără schimbarea coeficienților.

## Exemple rezolvate pas cu pas

### Exemplul 1 – Identificare prin combustie
1. O probă de 2,8 g hidrocarbură cu M=56 g/mol dă 8,8 g CO₂ și 3,6 g apă. Cu C=12, H=1, O=16, avem 8,8/44=0,20 mol C și 2·3,6/18=0,40 mol H.
2. Raportul C:H este 1:2, deci formula empirică CH₂, de masă 14 g/mol. Multiplicatorul este 56/14=4: formula C₄H₈.
3. Verificăm masa atomilor: 0,20·12+0,40·1=2,8 g. NE=1; fără alte date nu distingem alchenele de cicloalcani.

### Exemplul 2 – Amestec etenă–propan
1. Un amestec de 0,50 mol etenă și propan produce 1,20 mol CO₂ la ardere completă. Notăm cantitățile a și b: a+b=0,50 și 2a+3b=1,20.
2. Scădem de două ori prima relație: b=1,20−1,00=0,20 mol, apoi a=0,30 mol. Fracția molară a etenei este 0,30/0,50=0,60, adică 60 %.
3. Etena cere 3 mol O₂/mol, propanul 5 mol/mol: total 0,30·3+0,20·5=1,90 mol O₂. Cu 20 % O₂ în volume, aerul teoretic este 9,50 mol, adică 212,8 L la c.n. folosind 22,4 L/mol.

## Interpretarea rezultatelor

În primul exemplu, formula este sigură în cadrul datelor, dar structura nu este unică. În al doilea, rezultatul are ambele cantități pozitive și fracții de 60 % și 40 %, a căror sumă este 100 %. Consumul mediu de O₂ este 1,90/0,50=3,8 mol/mol, între valorile pure 3 și 5: o verificare rapidă a plauzibilității. Într-o rezolvare de concurs, controlul final nu înlocuiește demonstrația, dar poate detecta imediat o eroare de semn ori de coeficient.
""",
        'mistakes': ['Greșeala: declararea unei structuri unice din formulă → Cum o eviți: verifici toate familiile admise.',
 'Greșeala: dublarea factorului de puritate → Cum o eviți: marchezi masa deja corectată.',
 'Greșeala: amestecarea constituțiilor cu enantiomerii → Cum o eviți: precizezi convenția de numărare.'],
        'takeaways': ['Formula empirică nu este obligatoriu cea moleculară.',
 'Bilanțurile trebuie să fie independente.',
 'Fracțiile fizice sunt între zero și unu.',
 'Simetria reduce numărul produșilor.',
 'Condițiile stabilesc reacția relevantă.'],
        'connections': ['Lecția 7.3 – monoclorurare.', 'Lecția 7.5 – adiție cantitativă.', 'Lecția 7.10 – combustie și aer.'],
    },
]

CHAPTER7_QUESTIONS = [{'id': 'hydro7_001',
  'domain': 'Hidrocarburi',
  'lesson': '7.1',
  'topic': 'Familii',
  'level': 'Fundamente',
  'type': 'teorie',
  'question': 'Ce pereche poate avea aceeași formulă generală, în ipotezele uzuale ale seriilor simple?',
  'options': ['A. Monoalchenă aciclică și cicloalcan monociclic',
              'B. Alcan și monoalchină',
              'C. Alcan și arenă mononucleară',
              'D. Monoalchenă și monoalchină',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'A. Monoalchenă aciclică și cicloalcan monociclic',
  'explanation': 'Monoalchenele aciclice și cicloalcanii monociclici au formula CₙH₂ₙ. O dublă sau un ciclu '
                 'înseamnă câte o unitate NE.',
  'option_explanations': {'B': 'Alcanul are patru H în plus față de alchina cu același n.',
                          'C': 'Alcanul are opt H în plus față de arena cu același n.',
                          'D': 'Alchina are doi H mai puțin decât alchena.',
                          'E': 'Varianta A este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_002',
  'domain': 'Hidrocarburi',
  'lesson': '7.1',
  'topic': 'NE',
  'level': 'Intermediar',
  'type': 'calcul',
  'question': 'Care este NE pentru hidrocarbura C₇H₈?',
  'options': ['A. 1', 'B. 4', 'C. 3', 'D. 7', 'E. Niciuna dintre variantele A–D'],
  'answer': 'B. 4',
  'explanation': 'NE=(2·7+2−8)/2=8/2=4. Rezultatul este compatibil cu toluenul, dar formula și NE nu demonstrează '
                 'singure structura aromatică.',
  'option_explanations': {'A': 'O singură unitate ar corespunde formulei C₇H₁₄.',
                          'C': 'Trei unități ar cere C₇H₁₀.',
                          'D': 'Șapte ar rezulta din numărarea carbonilor, nu din deficitul de H.',
                          'E': 'Varianta B este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_003',
  'domain': 'Hidrocarburi',
  'lesson': '7.1',
  'topic': 'Formula alchinelor',
  'level': 'Intermediar',
  'type': 'interpretare',
  'question': 'O hidrocarbură aciclică are șase atomi de carbon, exact o legătură triplă și nicio legătură dublă. Formula sa este:',
  'options': ['A. C₆H₁₄', 'B. C₆H₁₂', 'C. C₆H₁₀', 'D. C₆H₆', 'E. Niciuna dintre variantele A–D'],
  'answer': 'C. C₆H₁₀',
  'explanation': 'O monoalchină aciclică are formula CₙH₂ₙ₋₂. Pentru n=6 rezultă 10 atomi de H și NE=2.',
  'option_explanations': {'A': 'C₆H₁₄ este formula alcanului.',
                          'B': 'C₆H₁₂ are NE=1, insuficient pentru triplă.',
                          'D': 'C₆H₆ are NE=4, deci nesaturări suplimentare.',
                          'E': 'Varianta C este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_004',
  'domain': 'Hidrocarburi',
  'lesson': '7.2',
  'topic': 'Izomeri de catenă',
  'level': 'Fundamente',
  'type': 'teorie',
  'question': 'Câți izomeri de constituție are C₆H₁₄?',
  'options': ['A. 2', 'B. 3', 'C. 4', 'D. 5', 'E. Niciuna dintre variantele A–D'],
  'answer': 'D. 5',
  'explanation': 'Sunt cinci: hexan, 2-metilpentan, 3-metilpentan, 2,2-dimetilbutan și 2,3-dimetilbutan. Rotirea '
                 'sau inversarea unui desen nu adaugă izomeri.',
  'option_explanations': {'A': 'Doi este numărul pentru C₄H₁₀.',
                          'B': 'Trei este numărul pentru C₅H₁₂.',
                          'C': 'Patru omite un schelet distinct.',
                          'E': 'Varianta D este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_005',
  'domain': 'Hidrocarburi',
  'lesson': '7.2',
  'topic': 'Nomenclatură',
  'level': 'Fundamente',
  'type': 'aplicație',
  'question': 'Cum se numește CH₃–CH(CH₃)–CH₂–CH₃?',
  'options': ['A. 2-metilbutan',
              'B. 3-metilbutan',
              'C. Pentan',
              'D. 2,2-dimetilpropan',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'A. 2-metilbutan',
  'explanation': 'Cea mai lungă catenă are patru atomi de carbon. Numerotarea care minimizează locantul pune '
                 'metilul la 2, deci 2-metilbutan.',
  'option_explanations': {'B': 'Numărarea inversă dă 3, care nu este locantul minim.',
                          'C': 'Pentanul are schelet neramificat, nu conectivitatea dată.',
                          'D': '2,2-dimetilpropanul are un carbon central cu patru vecini carbonici.',
                          'E': 'Varianta A este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_006',
  'domain': 'Hidrocarburi',
  'lesson': '7.2',
  'topic': 'Fierbere',
  'level': 'Intermediar',
  'type': 'interpretare',
  'question': 'La aceeași presiune, care explicație justifică fierberea mai joasă a 2,2-dimetilpropanului față de '
              'pentan?',
  'options': ['A. Are masă molară mai mică.',
              'B. Are suprafață de contact moleculară mai mică.',
              'C. Formează mai multe legături de hidrogen.',
              'D. Are mai mulți atomi de carbon.',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'B. Are suprafață de contact moleculară mai mică.',
  'explanation': 'Izomerii C₅H₁₂ au aceeași masă molară. Forma compactă, foarte ramificată, reduce contactele și '
                 'intensitatea globală a interacțiunilor de dispersie.',
  'option_explanations': {'A': 'Masele molare sunt identice fiind izomeri.',
                          'C': 'Alcanii nu formează între ei legături de hidrogen.',
                          'D': 'Ambii au exact cinci atomi de carbon.',
                          'E': 'Varianta B este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_007',
  'domain': 'Hidrocarburi',
  'lesson': '7.3',
  'topic': 'Mecanism radicalic',
  'level': 'Fundamente',
  'type': 'teorie',
  'question': 'Care eveniment reprezintă inițierea clorurării fotochimice a metanului?',
  'options': ['A. Atacul radicalului metil asupra Cl₂',
              'B. Combinarea a doi radicali metil',
              'C. Homoliza Cl₂ în doi radicali clor',
              'D. Formarea HCl prin atacul radicalului clor asupra metanului',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'C. Homoliza Cl₂ în doi radicali clor',
  'explanation': 'Inițierea creează radicalii inițiali prin absorbția luminii și ruperea homolitică a Cl–Cl. '
                 'Etapele ce regenerează radicali sunt propagare, iar combinarea lor este întrerupere.',
  'option_explanations': {'A': 'Aceasta regenerează radicalul clor și este propagare.',
                          'B': 'Combinarea consumă radicali, deci întrerupe lanțul.',
                          'D': 'Extragerea H formează radical metil și aparține propagării.',
                          'E': 'Varianta C este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_008',
  'domain': 'Hidrocarburi',
  'lesson': '7.3',
  'topic': 'Monoclorurare',
  'level': 'Intermediar',
  'type': 'interpretare',
  'question': 'Câți derivați monoclorurați de constituție are 2,2-dimetilpropanul? Nu se numără conformații.',
  'options': ['A. 2', 'B. 3', 'C. 4', 'D. 5', 'E. Niciuna dintre variantele A–D'],
  'answer': 'E. Niciuna dintre variantele A–D',
  'explanation': 'Toți cei 12 H sunt echivalenți prin simetrie: cele patru grupe metil sunt echivalente. '
                 'Înlocuirea oricărui H conduce la un singur derivat de constituție, valoare absentă din A–D.',
  'option_explanations': {'A': 'Nu există două tipuri neechivalente de H.',
                          'B': 'Trei este numărul pentru n-pentan, nu pentru neopentan.',
                          'C': 'Cele patru grupe metil sunt echivalente, nu dau patru produse.',
                          'D': 'Cei cinci atomi de carbon nu sunt cinci poziții de H; carbonul central nici nu '
                               'are H.'}},
 {'id': 'hydro7_009',
  'domain': 'Hidrocarburi',
  'lesson': '7.3',
  'topic': 'Cracare',
  'level': 'Intermediar',
  'type': 'aplicație',
  'question': 'În schema C₄H₁₀ → C₂H₆ + X, care este X dacă se conservă atomii?',
  'options': ['A. CH₄', 'B. C₂H₂', 'C. H₂', 'D. C₂H₄', 'E. Niciuna dintre variantele A–D'],
  'answer': 'D. C₂H₄',
  'explanation': 'Scădem formula etanului din bilanțul butanului: rămân doi C și patru H, deci etenă C₂H₄. Schema '
                 'este o cale posibilă de cracare.',
  'option_explanations': {'A': 'Ar lipsi un atom de carbon; numărul atomilor de hidrogen ar fi conservat.',
                          'B': 'C₂H₂ ar lăsa doi H necontabilizați.',
                          'C': 'H₂ nu contabilizează ceilalți doi atomi de carbon.',
                          'E': 'Varianta D este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_010',
  'domain': 'Hidrocarburi',
  'lesson': '7.4',
  'topic': 'Geometrie',
  'level': 'Fundamente',
  'type': 'teorie',
  'question': 'Care alchenă admite izomerie cis/trans?',
  'options': ['A. But-2-enă',
              'B. But-1-enă',
              'C. 2-metilpropenă',
              'D. Propenă',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'A. But-2-enă',
  'explanation': 'But-2-ena are pe fiecare carbon sp² un H și un metil, deci doi substituenți diferiți. Dubla '
                 'împiedică rotația liberă și permite două geometrii.',
  'option_explanations': {'B': 'Carbonul terminal CH₂ are doi substituenți H identici.',
                          'C': 'Un capăt este CH₂, iar celălalt are doi metili identici.',
                          'D': 'Carbonul terminal CH₂ exclude izomeria geometrică.',
                          'E': 'Varianta A este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_011',
  'domain': 'Hidrocarburi',
  'lesson': '7.4',
  'topic': 'Numărarea formelor',
  'level': 'Intermediar',
  'type': 'interpretare',
  'question': 'Pentru alchenele aciclice C₄H₈, câte constituții și câte forme totale incluzând cis/trans există, '
              'în această ordine?',
  'options': ['A. 4 și 4', 'B. 3 și 4', 'C. 3 și 6', 'D. 2 și 3', 'E. Niciuna dintre variantele A–D'],
  'answer': 'B. 3 și 4',
  'explanation': 'Constituțiile sunt but-1-enă, but-2-enă și 2-metilpropenă. Numai but-2-ena are două forme '
                 'geometrice, deci totalul este 1+2+1=4.',
  'option_explanations': {'A': 'Cis și trans nu sunt constituții diferite.',
                          'C': 'Nu toate trei constituțiile admit cis/trans.',
                          'D': 'Este omis scheletul ramificat.',
                          'E': 'Varianta B este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_012',
  'domain': 'Hidrocarburi',
  'lesson': '7.4',
  'topic': 'Masa alchenei',
  'level': 'Intermediar',
  'type': 'calcul',
  'question': 'O monoalchenă aciclică are masa molară 84 g/mol. Câți atomi de carbon are? C=12, H=1.',
  'options': ['A. 4', 'B. 5', 'C. 6', 'D. 7', 'E. Niciuna dintre variantele A–D'],
  'answer': 'C. 6',
  'explanation': 'Pentru CₙH₂ₙ, M=12n+2n=14n g/mol. Prin urmare n=84/14=6, iar formula este C₆H₁₂.',
  'option_explanations': {'A': 'Patru ar da M=56 g/mol.',
                          'B': 'Cinci ar da M=70 g/mol.',
                          'D': 'Șapte ar da M=98 g/mol.',
                          'E': 'Varianta C este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_013',
  'domain': 'Hidrocarburi',
  'lesson': '7.5',
  'topic': 'Markovnikov',
  'level': 'Intermediar',
  'type': 'interpretare',
  'question': 'La adiția ionică a HBr la propenă, fără peroxizi, produsul predominant este 2-bromopropan '
              'deoarece:',
  'options': ['A. Se formează preferențial un carbocation primar.',
              'B. Bromura se leagă obligatoriu de carbonul cu mai mulți H.',
              'C. Reacția este o substituție radicalică.',
              'D. Protonarea favorizează carbocationul secundar.',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'D. Protonarea favorizează carbocationul secundar.',
  'explanation': 'H se adaugă preferențial carbonului terminal. Astfel centrul cationic este secundar și mai '
                 'stabil decât alternativa primară; Br⁻ îl atacă și formează 2-bromopropan.',
  'option_explanations': {'A': 'Carbocationul secundar, nu primarul, este favorizat.',
                          'B': 'Această formulare inversează orientarea Markovnikov.',
                          'C': 'În condițiile date este adiție ionică, nu substituție.',
                          'E': 'Varianta D este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_014',
  'domain': 'Hidrocarburi',
  'lesson': '7.5',
  'topic': 'Consum brom',
  'level': 'Intermediar',
  'type': 'calcul',
  'question': 'Ce masă de Br₂ consumă 2,8 g etenă la adiție cantitativă în modelul dibromurii? C=12, H=1, Br=80.',
  'options': ['A. 8 g', 'B. 12 g', 'C. 24 g', 'D. 32 g', 'E. Niciuna dintre variantele A–D'],
  'answer': 'E. Niciuna dintre variantele A–D',
  'explanation': 'M(etenei)=28 g/mol, deci cantitatea este 2,8/28=0,10 mol. Raportul față de Br₂ este 1:1; masa '
                 'bromului este 0,10·160=16 g, absentă din A–D.',
  'option_explanations': {'A': '8 g folosește masa atomică Br, nu masa molară Br₂.',
                          'B': '12 g nu respectă raportul molar și masa molară 160.',
                          'C': '24 g ar cere 0,15 mol Br₂, mai mult decât consumul.',
                          'D': '32 g corespund la 5,6 g etenă, dublul probei.'}},
 {'id': 'hydro7_015',
  'domain': 'Hidrocarburi',
  'lesson': '7.5',
  'topic': 'Baeyer',
  'level': 'Intermediar',
  'type': 'aplicație',
  'question': 'În testul Baeyer cu KMnO₄ diluat, rece, neutru sau slab bazic, o alchenă simplă dă în modelul '
              'școlar:',
  'options': ['A. Un diol vicinal și decolorare, adesea cu MnO₂ brun',
              'B. Obligatoriu CO₂ și apă',
              'C. Un alcan, prin reducere',
              'D. Un compus cu aceeași dublă nemodificată',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'A. Un diol vicinal și decolorare, adesea cu MnO₂ brun',
  'explanation': 'Oxidarea blândă introduce două grupe OH pe atomii dublei. Permanganatul se reduce, ceea ce '
                 'explică dispariția violetului și posibilul precipitat brun; testul nu este exclusiv al '
                 'alchenelor.',
  'option_explanations': {'B': 'CO₂ și apa sunt produșii combustiei complete, nu ai oxidării blânde.',
                          'C': 'Transformarea este oxidare la diol, nu hidrogenare la alcan.',
                          'D': 'Dubla este consumată în dihidroxilare.',
                          'E': 'Varianta A este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_016',
  'domain': 'Hidrocarburi',
  'lesson': '7.6',
  'topic': 'Monomeri',
  'level': 'Fundamente',
  'type': 'teorie',
  'question': 'Care monomer produce PTFE prin polimerizare de adiție?',
  'options': ['A. CH₂=CHCl', 'B. CF₂=CF₂', 'C. CH₂=CH–CN', 'D. CH₂=CH–C₆H₅', 'E. Niciuna dintre variantele A–D'],
  'answer': 'B. CF₂=CF₂',
  'explanation': 'PTFE este politetrafluoroetilenă: unitatea sa de repetare este –CF₂–CF₂–. Monomerul '
                 'corespunzător se reconstituie introducând dubla între cei doi atomi de carbon.',
  'option_explanations': {'A': 'Acesta produce PVC.',
                          'C': 'Acesta produce poliacrilonitril.',
                          'D': 'Acesta este stirenul, monomerul PS.',
                          'E': 'Varianta B este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_017',
  'domain': 'Hidrocarburi',
  'lesson': '7.6',
  'topic': 'Grad de polimerizare',
  'level': 'Intermediar',
  'type': 'calcul',
  'question': 'Un PE idealizat are M=84000 g/mol. Care este gradul de polimerizare, neglijând grupele terminale? '
              'C=12, H=1.',
  'options': ['A. 1500', 'B. 2000', 'C. 3000', 'D. 6000', 'E. Niciuna dintre variantele A–D'],
  'answer': 'C. 3000',
  'explanation': 'Monomerul etenă are M=2·12+4·1=28 g/mol. Gradul este raportul maselor molare: 84000/28=3000, '
                 'fără unitate.',
  'option_explanations': {'A': '1500 ar folosi o unitate de masă 56, dublată nejustificat.',
                          'B': '2000 ar folosi masa propenei, 42 g/mol.',
                          'D': '6000 numără atomii de C proveniți din monomer, nu unitățile.',
                          'E': 'Varianta C este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_018',
  'domain': 'Hidrocarburi',
  'lesson': '7.6',
  'topic': 'Randament',
  'level': 'Intermediar',
  'type': 'calcul',
  'question': 'La polimerizarea prin adiție a 125 kg clorură de vinil se izolează PVC cu randament masic 80 %. Ce '
              'masă se obține?',
  'options': ['A. 80 kg', 'B. 125 kg', 'C. 156,25 kg', 'D. 100 kg', 'E. Niciuna dintre variantele A–D'],
  'answer': 'D. 100 kg',
  'explanation': 'În modelul de adiție nu se elimină un produs molecular mic. Masa obținută este masa inițială '
                 'înmulțită cu randamentul fracționar: 125·0,80=100 kg.',
  'option_explanations': {'A': '80 este procentul, nu masa produsului pentru 125 kg.',
                          'B': '125 kg ar reprezenta randament 100 %.',
                          'C': 'Împărțirea la 0,80 calculează o masă necesară, nu produsul din masa dată.',
                          'E': 'Varianta D este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_019',
  'domain': 'Hidrocarburi',
  'lesson': '7.7',
  'topic': 'H acetilenic',
  'level': 'Fundamente',
  'type': 'teorie',
  'question': 'Care compus are H legat direct de un carbon sp și poate forma acetilură în condiții adecvate?',
  'options': ['A. But-1-ină', 'B. But-2-ină', 'C. But-1-enă', 'D. Benzen', 'E. Niciuna dintre variantele A–D'],
  'answer': 'A. But-1-ină',
  'explanation': 'But-1-ina conține capătul HC≡C–. H terminal este slab acid. But-2-ina este internă, iar '
                 'ceilalți compuși nu au H acetilenic.',
  'option_explanations': {'B': 'Tripla internă nu are H legat direct de cei doi atomi sp.',
                          'C': 'H vinilic este legat de sp², nu sp.',
                          'D': 'Carbonul benzenic este sp², nu sp.',
                          'E': 'Varianta A este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_020',
  'domain': 'Hidrocarburi',
  'lesson': '7.7',
  'topic': 'Kucerov',
  'level': 'Intermediar',
  'type': 'interpretare',
  'question': 'Care este produsul carbonilic final predominant al hidratării acetilenei cu Hg²⁺ în mediu '
              'sulfuric?',
  'options': ['A. Etanol', 'B. Etanal', 'C. Propanonă', 'D. Acid etanoic', 'E. Niciuna dintre variantele A–D'],
  'answer': 'B. Etanal',
  'explanation': 'Enolul inițial CH₂=CHOH se tautomerizează la CH₃–CHO, etanal. Se conservă doi atomi de carbon '
                 'și formula globală C₂H₄O.',
  'option_explanations': {'A': 'Etanolul C₂H₆O ar necesita hidrogen suplimentar.',
                          'C': 'Propanona are trei atomi de carbon, imposibil din bilanțul dat.',
                          'D': 'Acidul etanoic are doi O și ar presupune oxidare suplimentară.',
                          'E': 'Varianta B este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_021',
  'domain': 'Hidrocarburi',
  'lesson': '7.7',
  'topic': 'Carbură tehnică',
  'level': 'Intermediar',
  'type': 'calcul',
  'question': 'Ce volum de acetilenă la c.n. se obține din 160 g carbură cu 80 % CaC₂, impurități inerte, apă în '
              'exces și randament 100 %? Ca=40, C=12; Vₘ=22,4 L/mol.',
  'options': ['A. 22,4 L', 'B. 28 L', 'C. 56 L', 'D. 89,6 L', 'E. Niciuna dintre variantele A–D'],
  'answer': 'E. Niciuna dintre variantele A–D',
  'explanation': 'Masa CaC₂ pur este 160·0,80=128 g. M=40+24=64 g/mol, deci 2 mol CaC₂ dau 2 mol C₂H₂ prin '
                 'hidroliză. Volumul corect este 2·22,4=44,8 L, absent din A–D.',
  'option_explanations': {'A': '22,4 L rezultă din înjumătățirea nejustificată a raportului CaC₂:C₂H₂.',
                          'B': '28 L nu respectă masa pură de 128 g și M=64.',
                          'C': '56 L ignoră puritatea și folosește 160/64 mol.',
                          'D': '89,6 L dublează nejustificat produsul din cei 2 mol CaC₂.'}},
 {'id': 'hydro7_022',
  'domain': 'Hidrocarburi',
  'lesson': '7.8',
  'topic': 'Rezonanță',
  'level': 'Fundamente',
  'type': 'teorie',
  'question': 'Care afirmație despre benzen este corectă?',
  'options': ['A. Are trei legături C–C scurte și trei lungi, fixe.',
              'B. Este un amestec de doi izomeri Kekulé.',
              'C. Are șase legături C–C egale și electroni π delocalizați.',
              'D. Are atomi de carbon sp³.',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'C. Are șase legături C–C egale și electroni π delocalizați.',
  'explanation': 'Benzenul are șase atomi sp² coplanari și un sextet π delocalizat. Cele două structuri Kekulé '
                 'sunt reprezentări-limită ale aceleiași molecule, cu legături egale de circa 1,39 Å.',
  'option_explanations': {'A': 'Lungimile egale contrazic alternanța fixă simplă/dublă.',
                          'B': 'Structurile de rezonanță nu sunt izomeri separabili.',
                          'D': 'Geometria plană și orbitalii p corespund hibridizării sp².',
                          'E': 'Varianta C este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_023',
  'domain': 'Hidrocarburi',
  'lesson': '7.8',
  'topic': 'Xileni',
  'level': 'Intermediar',
  'type': 'interpretare',
  'question': 'Câți xileni diferiți de constituție există?',
  'options': ['A. 1', 'B. 2', 'C. 4', 'D. 3', 'E. Niciuna dintre variantele A–D'],
  'answer': 'D. 3',
  'explanation': 'Doi metili pe benzen pot avea pozițiile relative 1,2; 1,3; 1,4. Restul pozițiilor se reduc la '
                 'acestea prin simetrie și renumerotare.',
  'option_explanations': {'A': 'Omite izomeria de poziție.',
                          'B': 'Omite una dintre pozițiile orto, meta, para.',
                          'C': 'Patru include probabil etilbenzenul, care nu este xilen.',
                          'E': 'Varianta D este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_024',
  'domain': 'Hidrocarburi',
  'lesson': '7.8',
  'topic': 'Naftalină',
  'level': 'Intermediar',
  'type': 'aplicație',
  'question': 'Care afirmație caracterizează corect naftalina?',
  'options': ['A. Are formula C₁₀H₈ și două inele condensate.',
              'B. Are formula C₁₂H₁₂, suma a două benzenuri.',
              'C. Este obligatoriu lichidă la 20 °C.',
              'D. Urmează formula CₙH₂ₙ₋₆.',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'A. Are formula C₁₀H₈ și două inele condensate.',
  'explanation': 'Naftalina este C₁₀H₈: cele două inele au o latură comună. Este o arenă polinucleară condensată, '
                 'solidă în condiții ambiante, și poate sublima.',
  'option_explanations': {'B': 'Condensarea implică atomi comuni; nu se adună două molecule separate.',
                          'C': 'Naftalina este solidă în condițiile precizate.',
                          'D': 'La n=10 formula mononucleară ar da C₁₀H₁₄, nu naftalină.',
                          'E': 'Varianta A este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_025',
  'domain': 'Hidrocarburi',
  'lesson': '7.9',
  'topic': 'Electrofil',
  'level': 'Fundamente',
  'type': 'teorie',
  'question': 'Electrofilul caracteristic nitrării benzenului în amestec sulfonitric este:',
  'options': ['A. NO₃⁻', 'B. NO₂⁺', 'C. NH₄⁺', 'D. Cl⁺', 'E. Niciuna dintre variantele A–D'],
  'answer': 'B. NO₂⁺',
  'explanation': 'Acidul sulfuric favorizează formarea ionului nitroniu, NO₂⁺. Inelul atacă acest electrofil, '
                 'formează complexul σ, apoi pierde H⁺ și reface aromaticitatea.',
  'option_explanations': {'A': 'Nitratul este anion, nu electrofilul nitrării.',
                          'C': 'Amoniul nu introduce grupa nitro în acest mecanism.',
                          'D': 'Clorul electrofil ar fi relevant la halogenare, nu la nitrare.',
                          'E': 'Varianta B este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_026',
  'domain': 'Hidrocarburi',
  'lesson': '7.9',
  'topic': 'Adiție fotochimică',
  'level': 'Intermediar',
  'type': 'interpretare',
  'question': 'Ce produs global rezultă prin adiția fotochimică totală a clorului la benzen?',
  'options': ['A. C₆Cl₆', 'B. C₆H₅Cl', 'C. C₆H₆Cl₆', 'D. C₆H₁₂Cl₆', 'E. Niciuna dintre variantele A–D'],
  'answer': 'C. C₆H₆Cl₆',
  'explanation': 'Adiția consumă 3 mol Cl₂ per mol benzen, fără eliminarea H. Rezultă hexaclorociclohexan '
                 'C₆H₆Cl₆, nu hexaclorobenzen C₆Cl₆.',
  'option_explanations': {'A': 'C₆Cl₆ ar corespunde înlocuirii tuturor H, nu adiției.',
                          'B': 'C₆H₅Cl este produs de monosubstituție cu catalizator Lewis.',
                          'D': 'Clorul adăugat nu furnizează încă șase H.',
                          'E': 'Varianta C este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_027',
  'domain': 'Hidrocarburi',
  'lesson': '7.9',
  'topic': 'Nitrare și randament',
  'level': 'Intermediar',
  'type': 'calcul',
  'question': 'Se nitrează 7,8 g benzen cu HNO₃ în exces, obținând exclusiv mononitroderivat cu randament 80 %. '
              'Masa izolată este? C=12, H=1, N=14, O=16.',
  'options': ['A. 7,8 g', 'B. 12,3 g', 'C. 15,375 g', 'D. 9,84 g', 'E. Niciuna dintre variantele A–D'],
  'answer': 'D. 9,84 g',
  'explanation': 'M(benzen)=78 g/mol, deci 0,10 mol. M(nitrobenzen)=123 g/mol; masa teoretică este 12,3 g. La 80 '
                 '%, masa izolată este 12,3·0,80=9,84 g.',
  'option_explanations': {'A': 'Produsul câștigă grupa NO₂ și pierde H; masa nu rămâne cea a benzenului.',
                          'B': '12,3 g este masa teoretică la 100 %.',
                          'C': 'Împărțirea la randament este operația inversă celei necesare.',
                          'E': 'Varianta D este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_028',
  'domain': 'Hidrocarburi',
  'lesson': '7.10',
  'topic': 'Aer teoretic',
  'level': 'Intermediar',
  'type': 'calcul',
  'question': 'Ce volum de aer uscat cu 20 % O₂ în volume arde complet 2 L propan? Toate gazele sunt măsurate la '
              'aceeași temperatură și presiune.',
  'options': ['A. 50 L', 'B. 10 L', 'C. 20 L', 'D. 100 L', 'E. Niciuna dintre variantele A–D'],
  'answer': 'A. 50 L',
  'explanation': 'Un volum de propan cere cinci volume de O₂. Pentru 2 L sunt necesari 10 L O₂; aerul teoretic '
                 'este 10/0,20=50 L.',
  'option_explanations': {'B': '10 L este oxigenul, nu aerul.',
                          'C': '20 L nu conțin cei 10 L O₂ necesari.',
                          'D': '100 L ar fi necesari pentru 4 L propan.',
                          'E': 'Varianta A este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_029',
  'domain': 'Hidrocarburi',
  'lesson': '7.10',
  'topic': 'Cifră octanică',
  'level': 'Intermediar',
  'type': 'aplicație',
  'question': 'Cifra octanică 95 a unei benzine exprimă în primul rând:',
  'options': ['A. Un conținut obligatoriu de 95 % octan.',
              'B. Rezistența la detonație pe scara de referință.',
              'C. O putere calorică de 95 MJ/kg.',
              'D. Procentul de oxigen din combustibil.',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'B. Rezistența la detonație pe scara de referință.',
  'explanation': 'Cifra octanică este un indicator al comportării antidetonante comparate cu combustibili de '
                 'referință. Nu este o analiză a compoziției și nici o măsură directă a energiei.',
  'option_explanations': {'A': 'Benzina reală nu trebuie să conțină efectiv acest procent de octan.',
                          'C': 'Numărul octanic nu are unitatea MJ/kg.',
                          'D': 'Definiția nu implică procentul de oxigen.',
                          'E': 'Varianta B este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_030',
  'domain': 'Hidrocarburi',
  'lesson': '7.10',
  'topic': 'Apă la combustie',
  'level': 'Intermediar',
  'type': 'calcul',
  'question': 'Ce masă de apă produce arderea completă a 0,50 mol butan? H=1, O=16.',
  'options': ['A. 18 g', 'B. 36 g', 'C. 54 g', 'D. 90 g', 'E. Niciuna dintre variantele A–D'],
  'answer': 'E. Niciuna dintre variantele A–D',
  'explanation': 'Un mol C₄H₁₀ dă 5 mol H₂O, deci 0,50 mol dă 2,50 mol apă. Masa este 2,50·18=45 g, valoare '
                 'absentă din A–D.',
  'option_explanations': {'A': '18 g ar însemna numai un mol apă.',
                          'B': '36 g ar proveni din folosirea a patru moli apă per mol butan.',
                          'C': '54 g ar cere șase moli apă per mol butan.',
                          'D': '90 g este masa apei dintr-un mol, nu din jumătate de mol butan.'}},
 {'id': 'hydro7_031',
  'domain': 'Hidrocarburi',
  'lesson': '7.11',
  'topic': 'Amestec gazos',
  'level': 'Concurs',
  'type': 'calcul',
  'question': 'Un amestec de 0,40 mol etenă și propan produce 1,00 mol CO₂ prin ardere completă. Care este '
              'fracția molară a etenei?',
  'options': ['A. 25 %', 'B. 40 %', 'C. 50 %', 'D. 75 %', 'E. Niciuna dintre variantele A–D'],
  'answer': 'C. 50 %',
  'explanation': 'Notăm a mol etenă și b mol propan. Din a+b=0,40 și 2a+3b=1,00, scădem 2(a+b): b=0,20, a=0,20. '
                 'Fracția etenei este 0,20/0,40=0,50, adică 50 %.',
  'option_explanations': {'A': '25 % ar da 1,10 mol CO₂.',
                          'B': '40 % ar da 1,04 mol CO₂.',
                          'D': '75 % ar da 0,90 mol CO₂.',
                          'E': 'Varianta C este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_032',
  'domain': 'Hidrocarburi',
  'lesson': '7.11',
  'topic': 'Constituție și geometrie',
  'level': 'Concurs',
  'type': 'interpretare',
  'question': 'O hidrocarbură aciclică C₄H₈ consumă 1 mol H₂/mol la hidrogenare și admite cis/trans. Ce concluzie '
              'este justificată?',
  'options': ['A. Este exclusiv cis-but-2-enă.',
              'B. Este but-1-enă.',
              'C. Este 2-metilpropenă.',
              'D. Are constituția but-2-enei, dar geometria nu este determinată.',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'D. Are constituția but-2-enei, dar geometria nu este determinată.',
  'explanation': 'Formula și consumul sunt compatibile cu monoalchena. Cerința cis/trans exclude capetele CH₂ și '
                 'selectează but-2-ena. Datele nu disting forma cis de trans, deoarece ambele consumă același H₂.',
  'option_explanations': {'A': 'Datele nu selectează cis în detrimentul trans.',
                          'B': 'But-1-ena nu admite cis/trans.',
                          'C': '2-metilpropena nu admite cis/trans.',
                          'E': 'Varianta D este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}},
 {'id': 'hydro7_033',
  'domain': 'Hidrocarburi',
  'lesson': '7.11',
  'topic': 'Monoclorurare și simetrie',
  'level': 'Concurs',
  'type': 'interpretare',
  'question': 'O hidrocarbură C₅H₁₂ dă un singur derivat monoclorurat de constituție. Care este structura? Se '
              'ignoră conformațiile.',
  'options': ['A. 2,2-dimetilpropan',
              'B. Pentan',
              'C. 2-metilbutan',
              'D. Nu există un asemenea alcan.',
              'E. Niciuna dintre variantele A–D'],
  'answer': 'A. 2,2-dimetilpropan',
  'explanation': 'Cei trei izomeri sunt pentan, 2-metilbutan și 2,2-dimetilpropan. Ei au respectiv trei, patru și '
                 'un tip de poziție de H neechivalentă. Simetria neopentanului face toate cele patru grupe metil '
                 'echivalente.',
  'option_explanations': {'B': 'Pentanul dă derivați 1-, 2- și 3-clorurați: trei constituții.',
                          'C': '2-metilbutanul are patru tipuri de poziții de H și patru derivați de constituție.',
                          'D': 'Neopentanul este exemplul care îndeplinește condiția.',
                          'E': 'Varianta A este corectă, așa cum rezultă din raționamentul detaliat; nu sunt '
                               'toate A–D false.'}}]
