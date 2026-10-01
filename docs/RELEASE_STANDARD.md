UNIVERSAL PROFESSIONAL GITHUB RELEASE MASTER STANDARD

Standard version: V4.2
Standard updated: 2026-09-23
Recommended canonical path: docs/RELEASE_STANDARD.md

Technikai + dokumentációs + vizuális + jogi + validációs +
AI/Codex-folytathatósági szabvány.


==================================================
0. CÉL
==================================================

Ha azt kérem, hogy egy projektből profi GitHub release,
GitHubra feltölthető projektcsomag vagy publikálható repository készüljön,
ezt a szabványt alkalmazd.

Ez a szabvány technológiától és projekttípustól független.

Alkalmazható például:

- webalkalmazásra;
- single-file HTML projektre;
- Python programra;
- CLI eszközre;
- desktop alkalmazásra;
- adatfeldolgozó programra;
- játéksegédre;
- libraryre;
- pluginra;
- modra;
- API kliensre;
- OCR eszközre;
- adatvizualizációra;
- automatizálási eszközre;
- kutatási projektre.

A cél NEM az, hogy minél több fájl készüljön.

A cél egy olyan GitHub projekt létrehozása, amely:

- működő;
- ellenőrizhető;
- jól dokumentált;
- vizuálisan igényes;
- jogilag rendezett;
- regresszióktól védett;
- hosszú távon karbantartható;
- más fejlesztő vagy AI által biztonságosan folytatható.

A repository első megnyitásakor egy idegen felhasználó,
fejlesztő vagy AI gyorsan értse:

- mi ez;
- mire való;
- milyen problémát old meg;
- hogyan használható;
- hogyan működik;
- milyen adatforrásokat használ;
- mi van ténylegesen bizonyítva;
- mi nincs bizonyítva;
- milyen korlátai vannak;
- hogyan teszteljük;
- hogyan fejleszthető tovább;
- hogyan készül belőle release;
- milyen jogi feltételek vonatkoznak rá.


==================================================
1. EZ MINŐSÉGI SZABVÁNY, NEM MEREV FÁJLLISTA
==================================================

A szabvány alkalmazása előtt először értsd meg az adott projektet.

Határozd meg:

- a projekt célját;
- a célközönséget;
- a jelenlegi architektúrát;
- a tényleges main artifactot;
- a canonical baseline-t;
- a kritikus működési invariánsokat;
- a fő regressziós veszélyeket;
- a külső függőségeket;
- a jogi környezetet;
- a projekt vizuális identitását.

Ezután csak a releváns részeket alkalmazd.

Ha egy elem valóban nem releváns:
jelöld indokolt N/A-ként.

Ha valami releváns, de nem sikerült elkészíteni:
ne nevezd N/A-nak.

Ha valami fontos az adott projekthez,
de ez a szabvány nem említi:
add hozzá.

A MINŐSÉGI SZINT legyen állandó,
ne a konkrét fájlok száma.


==================================================
2. RELEASE STANDARD ELHELYEZÉSE
==================================================

Projektlokális canonical hely:

docs/RELEASE_STANDARD.md

A fájl elején mindig szerepeljen:

Standard version: V4.2

és lehetőség szerint:

Standard updated: YYYY-MM-DD

A repository saját RELEASE_STANDARD.md fájlja
szándékosan verziórögzített projektartifact.

A master szabvány későbbi frissítése NEM írja felül automatikusan
a projektben lévő példányt.

Ha egy projektet újabb szabványverzióra migrálnak,
az explicit, ellenőrzött változtatás legyen.

Ugyanaz a szabványverzió-jelölés nem takarhat eltérő szöveget.

Ha több repository ugyanazt a szabványverziót használja,
a projektlokális RELEASE_STANDARD.md példányok
byte-azonosak legyenek.

Ezt SHA-256 összevetéssel kell igazolni,
a publikált repositoryk friss klónján.


==================================================
3. UTASÍTÁSI PRIORITÁS
==================================================

Eltérő utasítások esetén a prioritás:

1. Aktuális, explicit felhasználói utasítás
   - az adott kérésre vonatkozik;
   - a Release Contractban dokumentáld DEVIATION-ként,
     ha eltér a projekt alap release-szabványától.

2. Projektlokális:
   docs/RELEASE_STANDARD.md

3. Az aktuális környezetben elérhető release skill,
   ha létezik és releváns.

4. Általános fallback release-szabályok.

Az explicit felhasználói utasítás nem módosítja
észrevétlenül a projekt tartós szabványát.

Példa:

DEVIATION:
Social preview omitted by explicit user instruction for this release.

Ez csak az aktuális release-re vonatkozik,
kivéve ha a felhasználó kifejezetten
a projekt tartós szabványát is módosítja.


==================================================
4. EXPLICIT FELHASZNÁLÓI ELTÉRÉS ÉS GATE-VÉDELEM
==================================================

Az explicit felhasználói utasítás OPTIONAL elemet
elhagyhat dokumentált DEVIATION-nel.

Egy már REQUIRED-ként rögzített gate kihagyását
a DEVIATION önmagában nem teszi DONE állapotúvá.

Ha egy REQUIRED gate nincs teljesítve:

GATE STATUS = BLOCKED

A release státusz ilyenkor a normál release-status szabályok szerint:

BLOCKED

vagy kizárólag hiányzó kötelező runtime evidence esetén:

STATICALLY VERIFIED ONLY

lehet.

READY WITH LIMITATIONS csak akkor használható,
ha minden REQUIRED gate teljesült.

Projekt-specifikus REQUIRED / OPTIONAL besorolás
a Release Contract létrehozásakor módosítható,
ha az explicit felhasználói utasítás ezt indokolja,
és az eltérés dokumentált.

A FIX MINIMUM RELEASE GATE-ek
publikus release esetén puszta DEVIATION-nel nem kerülhetők meg.

A CREDENTIAL / SECRET CLEANLINESS gate
nem hagyható el és nem írható felül.


==================================================
5. AKTIVÁLÁSI SZABÁLY
==================================================

A teljes release workflow csak akkor aktiválódjon, ha a feladat:

- GitHub release;
- teljes GitHub package;
- release preparation;
- repository publication;
- vagy ezekkel egyértelműen egyenértékű kérés.

Normál:

- fejlesztés;
- hibajavítás;
- kisebb UI-módosítás;
- adatjavítás;
- feature-fejlesztés;

esetén ne töltsd be automatikusan a teljes release-szabványt.

A teljes szabvány ne kerüljön bele az AGENTS.md-be,
mert normál fejlesztésnél fölöslegesen növeli a kontextust.


==================================================
6. AGENTS.md HIVATKOZÁS
==================================================

Az AGENTS.md-be rövid hivatkozás kerüljön:

For full GitHub release or release-package work, use:

docs/RELEASE_STANDARD.md

Do not load or apply the full release workflow during ordinary development tasks.

If a dedicated release skill is available, it may assist execution,
but the project-local docs/RELEASE_STANDARD.md remains
the authoritative persistent project standard unless explicitly
overridden by the user's current instruction.


==================================================
7. RELEASE CONTRACT – MUNKA ELŐTT KÖTELEZŐ
==================================================

Mielőtt release fájlokat módosítasz vagy létrehozol,
rögzíts rövid RELEASE CONTRACT-ot.

Minimum:

PROJECT TYPE
PRIMARY LANGUAGE
CANONICAL BASELINE
MAIN ARTIFACT
TARGET VERSION
PUBLIC RELEASE: YES / NO
RUNTIME VALIDATION REQUIRED: YES / NO + indok
PACKAGE / ZIP REQUIRED: YES / NO
REPOSITORY PUBLICATION: AUTOMATED / MANUAL BY USER / NOT PART OF THIS RELEASE
LICENSE STATUS
REQUIRED GATES
OPTIONAL GATES
RELEVANT VISUAL ASSETS
N/A ELEMENTS + indok
DEVIATIONS

A release gate-eket a munka ELEJÉN kell rögzíteni.

Utólag nem szabad egy hibás vagy nehéz gate-et
„nem kötelezővé” nyilvánítani azért,
hogy a release sikeresnek tűnjön.

Gate-besorolás később csak dokumentált indokkal változhat.

AI/Codex projekt esetén ezt lehetőség szerint
AGENTS.md-ben és/vagy STATUS.md-ben is tükrözni kell.


==================================================
8. FIX MINIMUM RELEASE GATE-EK
==================================================

Minden normál publikus release minimum REQUIRED gate-je:

1. CANONICAL BASELINE IDENTIFIED
2. MAIN ARTIFACT IDENTIFIED
3. STATIC VALIDATION
4. CREDENTIAL / SECRET CLEANLINESS
5. LICENSE STATUS RESOLVED
6. VERSION CONSISTENCY

Ezeket kényelmi okból nem lehet OPTIONAL-ra változtatni.

Ezek a FIX MINIMUM RELEASE GATE-ek
publikus release esetén nem lehetnek N/A.

Tényleges teljesítést igényelnek.

A projekt jellegétől függően további REQUIRED gate lehet:

- runtime validation;
- browser validation;
- integration test;
- regression suite;
- single-file parity;
- data-source validation;
- visual validation;
- package validation;
- platform-specific test;
- API compatibility test.

Ha a repository publikálása a release életciklus része,
a PUBLISHED REPOSITORY PARITY gate is REQUIRED (67. pont).


==================================================
9. CANONICAL BASELINE
==================================================

Mindig a legutolsó ténylegesen működő
és lehetőség szerint runtime-validált verzió legyen
a canonical baseline.

Ne generáld újra feleslegesen.

Ha csak:

- dokumentáció;
- GitHub struktúra;
- grafika;
- release metadata;
- CI;
- licenc;
- manifest;
- csomagolás

változik, a validált alkalmazást
lehetőleg byte-pontosan őrizd meg.

Ne változtass indokolatlanul:

- üzleti logikát;
- algoritmust;
- UI-viselkedést;
- storage/cache rendszert;
- adatforrás-logikát;
- számítási logikát;
- kompatibilitási viselkedést.

Új programverzió csak:

- tényleges programváltozásnál;
- vagy explicit kérésre

készüljön.


==================================================
10. BASELINE BYTE-PARITY
==================================================

Ha a release elkészítése során a main artifactnak
változatlanul kell maradnia,
ezt ne csak feltételezd.

Bizonyítsd hash-összevetéssel.

Példa:

BASELINE SHA-256
PACKAGED ARTIFACT SHA-256
MATCH: YES / NO

Ha byte-identitás elvárt:

NO MATCH = FAIL.

Ha az alkalmazás szándékosan változott:

BYTE PARITY = N/A

indokkal.

Ebben az esetben a byte-parity gate csak akkor lehet N/A,
ha maga a byte-identitás az adott release-ben fogalmilag nem alkalmazható.

Az új artifact kapjon saját végleges SHA-256 hash-t.


==================================================
11. NÉGY KÜLÖN ÁLLAPOTRENDSZER
==================================================

A következő négy fogalmi rendszert SOHA ne keverd össze.


A) EVIDENCE LEVEL
Mit sikerült ténylegesen ellenőrizni?

SOURCE VERIFIED
STATIC VERIFIED
RUNTIME VERIFIED
INTEGRATION VERIFIED
NOT VERIFIED


B) TEST RESULT
Mi lett az adott ellenőrzés eredménye?

PASS
EMPTY
UNKNOWN
ATTENTION
FAIL
ERROR


C) CHECKLIST / GATE STATUS
Elkészült-e az adott release-feladat?

DONE
N/A
BLOCKED


D) RELEASE STATUS
Mi az egész release állapota?

READY
READY WITH LIMITATIONS
STATICALLY VERIFIED ONLY
BLOCKED


Példák:

STATIC VERIFIED + PASS

RUNTIME VERIFIED + PASS

SOURCE VERIFIED + UNKNOWN

NOT VERIFIED + UNKNOWN

A vizuális ellenőrzés nem külön Evidence Level.

VISUAL VERIFIED vagy más új evidence-címke nem használható.

Valódi, futó UI-ról készült screenshot bizonyítéka:
RUNTIME VERIFIED

Vizuális asset (SVG/PNG) megléte, mérete, linkelhetősége:
STATIC VERIFIED

Kézi vizuális átnézés külön teszteredmény lehet,
de nem hoz létre új Evidence Levelt.


==================================================
12. TEST RESULT JELENTÉSEK
==================================================

PASS

Az elvárt működés bizonyítottan megfelelő.


EMPTY

Nincs eredmény,
de ez a specifikáció szerint elfogadott működés.


UNKNOWN

Nincs elég adat megbízható döntéshez.


ATTENTION

A működés nem hibás,
de ismert adat- vagy környezeti korlát van.


FAIL

Egy elvárt invariáns bizonyítottan megsérült.


ERROR

Technikai végrehajtási vagy feldolgozási hiba történt.


==================================================
13. CHECKLIST / GATE STATUS
==================================================

Minden gate rendelkezzen:

REQUIRED: YES / NO

mezővel és külön státusszal:

DONE
N/A
BLOCKED


DONE

Az elem ténylegesen elkészült.


N/A

Csak akkor használható,
ha az elem a projekt természetéből fakadóan
valóban nem alkalmazható.

N/A nem használható azért, mert:

- nehéz volt;
- nincs hozzá eszköz;
- nincs idő;
- nem sikerült;
- túl sok munka lenne;
- a modell el akarja kerülni a BLOCKED állapotot.

Minden N/A rövid indoklást igényel.


BLOCKED

Az elem releváns,
de jelenleg nem teljesíthető.

BLOCKED lehet:

REQUIRED BLOCKED
→ az egész release blokkolt.

OPTIONAL BLOCKED
→ önmagában nem blokkolja a release-t,
  de limitationként dokumentálni kell.


REQUIRED GATE TELJESÜLÉSE

Egy REQUIRED gate akkor számít teljesültnek, ha:

STATUS = DONE

vagy

STATUS = N/A,

de kizárólag akkor,
ha az N/A a projekt természetéből fakadóan
valóban indokolt és dokumentált.

Az indokolt REQUIRED N/A
nem release-hiba.

Példa:

Egy projektben runtime teszt
technikailag és fogalmilag nem alkalmazható.

RUNTIME GATE:
REQUIRED: YES
STATUS: N/A
REASON: Runtime execution is not applicable to this project type.

Ez a gate teljesültnek számít.


FONTOS:

A FIX MINIMUM RELEASE GATE-ek
nem lehetnek N/A:

- CANONICAL BASELINE IDENTIFIED
- MAIN ARTIFACT IDENTIFIED
- STATIC VALIDATION
- CREDENTIAL / SECRET CLEANLINESS
- LICENSE STATUS RESOLVED
- VERSION CONSISTENCY

Ezek publikus release esetén
tényleges teljesítést igényelnek.


==================================================
14. REQUIRED UNKNOWN / NOT VERIFIED
==================================================

Ha egy REQUIRED gate eredménye:

UNKNOWN

vagy az evidence:

NOT VERIFIED

és a bizonyítás szükséges a release-hez,
akkor a release blokkolt.

Kötelező gate esetén:

UNKNOWN
NOT VERIFIED

nem alakítható át pusztán:

READY WITH LIMITATIONS

állapottá.


==================================================
15. RELEASE STATUS SZIGORÚ DEFINÍCIÓJA
==================================================

READY

Csak akkor használható, ha:

- minden REQUIRED gate teljesült;
- vagyis minden REQUIRED gate DONE,
  illetve kizárólag valóban indokolt esetben N/A;
- a FIX MINIMUM RELEASE GATE-ek közül egyik sem N/A;
- minden alkalmazható REQUIRED teszt PASS
  vagy specifikáció szerint elfogadott EMPTY;
- nincs REQUIRED FAIL;
- nincs REQUIRED ERROR;
- nincs REQUIRED UNKNOWN;
- nincs REQUIRED NOT VERIFIED;
- nincs REQUIRED BLOCKED;
- nincs nyitott release-releváns ATTENTION;
- nincs dokumentálandó OPTIONAL BLOCKED;
- nincs egyéb nyitott limitation.

READY = tiszta release.


READY WITH LIMITATIONS

Csak akkor használható, ha:

- minden REQUIRED gate teljesült;
- a FIX MINIMUM RELEASE GATE-ek ténylegesen teljesültek;
- nincs REQUIRED FAIL;
- nincs REQUIRED ERROR;
- nincs REQUIRED UNKNOWN;
- nincs REQUIRED NOT VERIFIED;
- nincs REQUIRED BLOCKED;

de maradt dokumentált,
nem blokkoló:

- ATTENTION;
- opcionális UNKNOWN;
- OPTIONAL BLOCKED;
- külső adatforrási korlát;
- egyéb nem release-kritikus limitation.

Kötelező gate hibája
SOHA nem nevezhető limitationnek.


STATICALLY VERIFIED ONLY

A BLOCKED release státusz speciális,
informatív alesete.

Csak akkor használható, ha:

- minden REQUIRED gate a runtime/runtime-browser
  bizonyításon kívül teljesült;
- nincs más REQUIRED FAIL;
- nincs más REQUIRED ERROR;
- nincs más REQUIRED UNKNOWN;
- nincs más REQUIRED NOT VERIFIED;
- nincs más REQUIRED BLOCKED;
- az EGYETLEN release-blokkoló ok az,
  hogy a kötelező runtime bizonyíték
  nem készült el vagy technikailag nem volt végrehajtható.

Jelentése:

STATICALLY VERIFIED ONLY
= BLOCKED: missing required runtime evidence

Ez NEM publikus release-ready állapot.

Ha a runtime teszt a projekt természetéből fakadóan
eleve nem alkalmazható:

RUNTIME GATE:
REQUIRED: YES
STATUS: N/A
REASON: runtime validation is not applicable to this project type.

Ez teljesült gate-nek számít.

Ebben az esetben a projekt
a többi gate teljesülése alapján lehet READY.

Ha a hiányzó runtime evidence mellett
bármilyen más REQUIRED gate is blokkol:

RELEASE STATUS = BLOCKED.


BLOCKED

Ha bármely REQUIRED gate:

- FAIL;
- ERROR;
- UNKNOWN;
- NOT VERIFIED;
- BLOCKED

állapotú a release-kritikus bizonyítás szempontjából,

és nem teljesül a STATICALLY VERIFIED ONLY
szűk speciális esete.


==================================================
16. FAIL-SAFE ALAPELV
==================================================

Ha valamit nem tudsz biztosan:

ne találd ki.

Használj:

UNKNOWN
ATTENTION
NOT VERIFIED
BLOCKED

állapotot.

Soha ne állíts:

- runtime PASS-t runtime teszt nélkül;
- jogi megfelelést ellenőrzés nélkül;
- licencet feltételezésből;
- mockupot valódi screenshotnak;
- generált képet runtime evidence-nek;
- validált adatot megfelelő forrás nélkül.


==================================================
17. REPOSITORY FELÉPÍTÉS
==================================================

A konkrét struktúrát a projekthez igazítsd.

Lehetséges elemek:

README.md
README.hu.md
README.en.md

CHANGELOG.md
CONTRIBUTING.md
SECURITY.md
PRIVACY.md

LICENSE
NOTICE.md
THIRD_PARTY_NOTICES.md

AGENTS.md
STATUS.md
VERSION.json

/release
/docs
/assets
/tools
/test-artifacts
/.github

Csak valódi funkciójú fájlt készíts.

Ne gyárts:

- üres dokumentumot;
- dísznek készült metadata-fájlt;
- fölösleges mappastruktúrát;
- random másolatokat;
- irreleváns régi buildet.

A ponttal kezdődő fájlok és könyvtárak
(például .github/, .gitignore, .gitattributes, .nojekyll)
a repository teljes értékű részei.

Publikáláskor nem maradhatnak ki csak azért,
mert rejtett / dotfile elemek.


==================================================
18. MAIN ARTIFACT
==================================================

A projekt fő használható artifactja
legyen egyértelműen azonosítható.

Például:

index.html
app.exe
script.py
package
extension
binary
plugin
library

A README nevezze meg egyértelműen.


==================================================
19. SINGLE-FILE PROJEKTEK
==================================================

Ha a projekt követelménye single-file artifact:

maradjon single-file.

Ne bontsd szét:

CSS
JavaScript
template
data
config

külön fájlokra csak azért,
hogy a repository „profibbnak” tűnjön.

A professzionális GitHub-struktúra
a program köré épüljön,
ne bontsa szét annak elfogadott architektúráját.


==================================================
20. README STRATÉGIA
==================================================

A README.md legyen teljes értékű fő landing page
a projekt elsődleges nyelvén.

Ne legyen üres nyelvválasztó oldal.

Ha több nyelv kell:

README.md

+

README.en.md
vagy
README.hu.md

és linkeljenek egymásra.

A README tartalmazza tömören:

- projekt neve;
- mi ez;
- mire való;
- milyen problémát old meg;
- fő funkciók;
- aktuális release;
- main artifact;
- gyors használat;
- követelmények;
- adatforrások;
- validációs állapot;
- ismert korlátok;
- licenc;
- third-party attribution;
- részletes dokumentáció linkjei.


==================================================
21. KÉTNYELVŰ PARITÁS
==================================================

Ha a projekt két vagy több nyelven dokumentált,
a fontos felhasználói dokumentáció
tartalmilag legyen egyenértékű.

Nem elfogadható:

- teljes magyar dokumentáció + félkész angol;
- teljes angol dokumentáció + elavult magyar;
- egyik nyelvből hiányzó fontos limitation;
- eltérő feature-leírás;
- eltérő verzióinformáció;
- eltérő jogi figyelmeztetés.

A nyelvi változatoknak nem kell
szó szerinti másolatnak lenniük,
de ugyanazt a lényegi információt kell hordozniuk.


==================================================
22. TECHNIKAI DOKUMENTÁCIÓ
==================================================

A projekt jellegétől függően
készíts releváns dokumentációt.

Lehetséges:

USER GUIDE
ARCHITECTURE
DATA SOURCES
TESTING
RELEASE
KNOWN LIMITATIONS
ROADMAP
RELEASE NOTES

Ne készíts külön dokumentumot,
ha az csak értelmetlenül megismételné a README-t.


==================================================
23. USER GUIDE
==================================================

Ha releváns, dokumentáld:

- hogyan használható a program;
- főképernyő;
- mezők;
- gombok;
- kapcsolók;
- workflow;
- tipikus példák;
- hibaüzenetek;
- ismert edge case-ek;
- gyakori félreértések.


==================================================
24. ARCHITECTURE
==================================================

Dokumentáld:

- fő komponensek;
- belső rétegek;
- adatfolyam;
- business logic;
- UI;
- storage;
- cache;
- API-k;
- fallback;
- validation;
- diagnostics;
- kritikus invariánsok;
- fontos mérnöki döntések.

Egy új fejlesztőnek vagy AI-nak
értenie kell a rendszer felépítését.


==================================================
25. DATA SOURCES
==================================================

Ha a projekt külső adatforrásokat használ,
dokumentáld minden jelentős forrásnál:

- név;
- hivatalos URL / API / repository;
- mire használjuk;
- milyen adat érkezik;
- source precedence;
- version discovery;
- freshness;
- fallback;
- cache;
- ismert hiányosságok.


==================================================
26. SOURCE PRECEDENCE
==================================================

Ha több adatforrás létezik,
dokumentáld a prioritást.

Példa:

1. Current direct authoritative source
2. Current primary API
3. Current secondary API
4. Versioned repository
5. Verified fallback
6. Community evidence
7. Legacy fallback
8. UNKNOWN

A tényleges sorrendet
mindig az adott projekthez igazítsd.


==================================================
27. DINAMIKUS ADATFORRÁSOK
==================================================

Ha a projekt automatikusan követ:

- játékverziót;
- buildet;
- API verziót;
- adatverziót;
- új rendszereket;
- új locationöket;
- új adatfájlokat;
- source revisiont;

ezt release közben őrizd meg.

Ne cseréld:

dynamic discovery

megoldást

hardcoded current values

megoldásra.

Dokumentáld:

- mit fedez fel automatikusan;
- hogyan;
- fallback;
- schema-break viselkedés;
- mi igényel manuális frissítést.


==================================================
28. KÜLSŐ ADAT ÚJRACSOMAGOLÁSA
==================================================

Ne csomagolj automatikusan újra
harmadik féltől származó teljes adatbázist,
adatdumpot vagy nagy adatkészletet.

Különösen ne tedd,
ha a redisztribúciós jog vagy licenc nem tisztázott.

Ha:

LICENSE STATUS = UNKNOWN

akkor:

- ne másold automatikusan a teljes adatforrást a repositoryba;
- dokumentáld külső függőségként;
- hivatkozz az eredeti forrásra;
- runtime fetch-et is csak akkor használj,
  ha azt a forrás feltételei lehetővé teszik.

Jogilag bizonytalan adatot
ne tegyél a saját projektlicenc alá.


==================================================
29. REGRESSZIÓVÉDELEM
==================================================

Minden fontos hibajavításhoz
és minden kritikus új feature-höz
tartozzon célzott regressziós ellenőrzés.

Ne csak a hibát javítsd.

Bizonyítsd azt is,
hogy ugyanaz a hiba később észrevehető lesz,
ha visszatér.

A diagnosztika fejlődjön együtt a programmal.


==================================================
30. RELEASE GATE AUTOMATIZÁLÁS
==================================================

Ha technikailag lehetséges,
legyen automatikus release-check script.

Például:

tools/check-release.*

Ellenőrizheti:

- main artifact;
- syntax;
- parsing;
- version consistency;
- kritikus invariánsok;
- duplicate IDs;
- single-file követelmény;
- kötelező dokumentáció;
- regressziós marker-ek;
- credential/secret cleanliness;
- manifest;
- releváns vizuális assetek jelenléte.

A gate soha ne nevezzen
statikus ellenőrzést runtime tesztnek.

A release gate script köteles ellenőrizni
az inventory / checksum existence parity-t (69. pont).

Ha a release checksum working-tree szöveges fájlokra is kiterjed,
a gate ellenőrizze a determinisztikus .gitattributes
line-ending policy jelenlétét (70. pont).


==================================================
31. CI / GITHUB ACTIONS
==================================================

Ha a projekthez értelmes,
legyen GitHub Actions workflow.

Lehetséges esemény:

push
pull_request
release

A CI világosan különítse el:

STATIC TEST
RUNTIME TEST
INTEGRATION TEST

Egy grep, syntax-check vagy parser
nem runtime teszt.


==================================================
32. TEST EVIDENCE
==================================================

Ha van tényleges teszt vagy runtime bizonyíték:

test-artifacts/

alatt őrizd meg.

Például:

runtime-log.json
validation-summary.json
release-gate-summary.json
screenshots/

A rövid summary
ne helyettesítse a nyers evidence-et.

A kettő együtt adjon auditálható nyomot.


==================================================
33. CHANGELOG ÉS RELEASE NOTES
==================================================

Verziózott projektnél legyen CHANGELOG.md.

Ajánlott kategóriák:

Added
Changed
Fixed
Removed
Security
Validation

Fontos bugfixnél dokumentáld:

- mi volt a hiba;
- mi okozta;
- hogyan javult;
- milyen regressziós ellenőrzés védi.

Az aktuális release-hez legyen
rövid, érthető release összefoglaló is.


==================================================
34. AGENTS.md
==================================================

AI/Codex által folytatható projektnél
legyen AGENTS.md.

Tartalmazza röviden:

- projekt célja;
- canonical baseline;
- main artifact;
- authoritative files;
- kritikus invariánsok;
- source precedence;
- storage/cache policy;
- required release gates;
- testing policy;
- tiltott regressziók;
- dokumentációfrissítési szabály;
- hivatkozás a docs/RELEASE_STANDARD.md fájlra.

A teljes release-szabványt
ne másold bele az AGENTS.md-be.


==================================================
35. STATUS.md
==================================================

STATUS.md legyen rövid és aktuális.

Tartalmazza:

- current version;
- canonical baseline;
- latest validated artifact;
- latest validation;
- current release status;
- known ATTENTION;
- known UNKNOWN;
- BLOCKED elemek;
- next task;
- NOT STARTED scope;
- külön jóváhagyást igénylő feladatok.

Ne legyen belőle
végtelen történelmi napló.


==================================================
36. AI / CODEX FOLYTATHATÓSÁG
==================================================

Ha az adott környezetben rendelkezésre állnak
projekt-specifikus skillek vagy workflow-eszközök,
használd a relevánsakat.

Codex környezetben, HA ELÉRHETŐ:

$credit-efficient-project-runner

meglévő projekt folytatására.

$uj-projekt

csak valóban új projekt
vagy indokolt inicializálás esetén.

Más környezetben ugyanezeket az elveket
az ott rendelkezésre álló eszközökkel alkalmazd.

A workflow ne függjön kötelezően
egy konkrét skillnévtől.


==================================================
37. AI / CODEX TASK CONTRACT
==================================================

Komoly fejlesztési handoff tartalmazza:

BASELINE
SCOPE
DO NOT TOUCH
REQUIRED GATES
ACCEPTANCE CRITERIA
TARGETED TESTS
STOP CONDITION

Dirty/WIP állapotot őrizd meg.

Külön jóváhagyás nélkül tilos:

reset
force overwrite
unrelated cleanup

Korábbi elfogadott döntést
új bizonyíték nélkül ne nyiss újra.


==================================================
38. LICENC
==================================================

Az AI SOHA ne válasszon önállóan projektlicencet.

Ha van meglévő licenc:
őrizd meg.

Ha a tulajdonos megadja:
azt használd.

Ha nincs eldöntve és a felhasználó elérhető:
kérdezz rá.

Ha autonóm folyamatban nincs kitől megkérdezni:

LICENSE GATE = BLOCKED.

A többi nem destruktív:

- dokumentációs;
- audit;
- validációs;
- vizuális;

munka folytatható.

Publikus release azonban
nem jelenthető READY-nek.

Ne válassz automatikusan:

MIT
GPL
Apache
BSD

vagy más licencet.


==================================================
39. THIRD-PARTY ÉS JOGI DOKUMENTÁCIÓ
==================================================

Ha releváns, legyen:

LICENSE
NOTICE.md
THIRD_PARTY_NOTICES.md
PRIVACY.md
SECURITY.md

Third-party forrásnál dokumentáld:

- név;
- hivatalos forrás;
- mire használjuk;
- licenc vagy Terms;
- attribution;
- redisztribúciós státusz;
- ismert korlátozás.

Ha a licenc nem ismert:

LICENSE STATUS: UNKNOWN


==================================================
40. FAN / TRADEMARK DISCLAIMER
==================================================

Fan project, játéksegéd vagy
harmadik fél trademarkját használó projekt esetén
legyen megfelelő unofficial/fan disclaimer,
ha szükséges.

Ne állíts hivatalos kapcsolatot,
partnerséget vagy jóváhagyást,
ha ilyen nincs.

A disclaimer legyen tárgyilagos,
és ne állítson többet a tényleges jogi helyzetnél.


==================================================
41. VIZUÁLIS JOGTISZTASÁG
==================================================

Ne használj engedély nélkül:

- stock fotót;
- third-party logót;
- proprietary ikonkészletet;
- játékassetet;
- külső illusztrációt;
- jogvédett marketingképet.

Preferáld:

- saját diagramot;
- saját UI screenshotot;
- saját generált projektgrafikát;
- egyértelműen licencelt assetet.

Ha third-party vizuális elem kerül a projektbe,
a jogi státuszát is dokumentáld.


==================================================
42. PRIVACY
==================================================

Csak a tényleges működést dokumentáld.

Ha releváns, térj ki:

- localStorage;
- IndexedDB;
- cookies;
- cache;
- külső API hívások;
- analytics;
- backend;
- login/account;
- feltöltött fájlok;
- helyi adattörlés.

Ha nincs analytics:
ne találj ki.

Ha nincs backend:
ne állíts mást.


==================================================
43. SECURITY
==================================================

Ha releváns, legyen SECURITY.md.

Tartalmazhatja:

- vulnerability reporting;
- milyen probléma számít security issue-nak;
- érzékeny adatkezelés;
- külső függőségek;
- mit ne publikáljanak nyilvános issue-ban.


==================================================
44. CONTRIBUTING
==================================================

Ha a repository fejlesztésre is nyitott,
vagy várható későbbi közreműködés,
legyen használható CONTRIBUTING.md.

Tartalmazza:

- hogyan induljon módosítás;
- scope;
- tesztelés;
- regressziós követelmény;
- dokumentációfrissítés;
- PR elvárások;
- unrelated refactor kerülése;
- canonical baseline tiszteletben tartása.


==================================================
45. ISSUE ÉS PR TEMPLATE
==================================================

Ha releváns, legyen:

.github/ISSUE_TEMPLATE/bug_report.md
.github/ISSUE_TEMPLATE/feature_request.md
.github/pull_request_template.md

Bug report kérjen például:

- app/project version;
- environment;
- reproduce steps;
- expected result;
- actual result;
- screenshot;
- log;
- browser/platform;
- additional context.


==================================================
46. VIZUÁLIS MINŐSÉG
==================================================

Publikus, bemutatásra szánt projekt esetén
a vizuális dokumentáció a release minőségének része.

Csak RELEVÁNS vizuális elemek készüljenek.

Lehetséges:

- social preview / hero;
- architecture diagram;
- workflow diagram;
- data flow diagram;
- validation/status diagram;
- UI screenshot;
- feature preview.

Egyszerű CLI vagy minimális library esetén
több ilyen elem lehet indokolt N/A.


==================================================
47. EGYSÉGES DESIGN LANGUAGE
==================================================

A vizuális dokumentáció legyen egységes.

Igazodjon lehetőség szerint:

- a projekt UI-jához;
- brandjéhez;
- színvilágához;
- célközönségéhez;
- technikai jellegéhez.

Legyen következetes:

- tipográfia;
- szín;
- kontraszt;
- háttér;
- keretek;
- ikonok;
- spacing;
- címhierarchia;
- vizuális ritmus.

Ne használj minden projekthez
ugyanazt a generikus sablont.


==================================================
48. VIZUÁLIS ARTIFACT PRIORITÁS
==================================================

Vizualizációhoz a legjobb ténylegesen
elérhető módszert használd.

Prioritás:

1. valódi UI/browser screenshot;
2. saját projekt-specifikus grafika;
3. SVG;
4. Mermaid;
5. renderelő HTML/script.

Mindig különítsd el:

REAL UI SCREENSHOT
GENERATED PROJECT GRAPHIC
TECHNICAL DIAGRAM
MOCKUP / CONCEPT

Soha ne nevezd:

- mockupot screenshotnak;
- generált képet runtime evidence-nek;
- placeholdert kész artifactnak.


==================================================
49. SVG ÉS MERMAID
==================================================

Technikai diagramoknál
SVG vagy Mermaid előnyös.

Mermaid különösen alkalmas:

- architecture;
- workflow;
- state flow;
- dependency graph;
- release process;
- data flow.

SVG jó:

- standalone assethez;
- precíz vizuális kontrollhoz;
- README képhez;
- PNG exportra;
- skálázható dokumentációhoz.

Social previewhoz vagy UI showcase-hez
ne használj automatikusan Mermaidet.


==================================================
50. DARK / LIGHT MODE
==================================================

Ha egy asset csak dark vagy csak light GitHub témában
olvasható jól,
készíts megfelelő változatot.

README-ben szükség esetén használható:

<picture>

elem megfelelő media / prefers-color-scheme logikával.

Ha egy neutrális asset
mindkét témában jól működik,
ne gyárts fölöslegesen két példányt.


==================================================
51. VIZUÁLIS VALIDÁCIÓ
==================================================

Release előtt ellenőrizd
a releváns vizuális artifactokat.

Minimum:

- nincs levágott szöveg;
- nincs kilógó elem;
- helyesek a feliratok;
- megfelelő a kontraszt;
- GitHubon olvasható;
- mobilon ésszerűen olvasható;
- megfelelő a felbontás;
- nincs indokolatlanul nagy fájlméret;
- nem elavult;
- a jelenlegi projektverziót mutatja.


==================================================
52. VIZUÁLIS FRISSESSÉG
==================================================

A vizuális dokumentáció is verziózott project artifact.

Ha változik:

- UI;
- architecture;
- workflow;
- adatforrás;
- validation;
- fő feature;

ellenőrizd a kapcsolódó képeket és diagramokat.

Régi screenshot vagy diagram
nem maradhat bent úgy,
mintha aktuális lenne.

Historical evidence legyen jelölve:

VERSION
DATE
HISTORICAL


==================================================
53. SOCIAL PREVIEW
==================================================

Ha releváns,
készíts GitHubhoz alkalmas social preview assetet.

Ajánlott arány:

kb. 2:1

például:

1280 × 640

Legyen:

- olvasható;
- projekt-specifikus;
- vizuálisan egységes;
- nem túlzsúfolt;
- nem clickbait;
- nem generikus stock-hatású.

FONTOS:

A repositoryban lévő social preview kép
önmagában nem állítja be
a GitHub repository social previewját.

Ha tényleges beállítás kell,
azt külön GitHub UI/API lépésként jelezd.


==================================================
54. README-BE ÉPÍTETT VIZUALITÁS
==================================================

A vizuális assetek ne csak létezzenek.

Használd őket értelmesen a README-ben.

Például:

Hero
↓
Project summary
↓
Feature overview
↓
Screenshot
↓
Workflow
↓
Architecture
↓
Validation
↓
Documentation / Legal

Ne zsúfold tele a README-t.

Minden vizuális elemnek legyen információs funkciója.


==================================================
55. VERSION, MANIFEST ÉS FILE INVENTORY
==================================================

Ha releváns, használható:

VERSION.json
FILE-INVENTORY.json
PACKAGE-MANIFEST.json

Csak akkor készítsd el,
ha ténylegesen segíti az auditálhatóságot.

Ne készíts manifestet puszta formaságból.


==================================================
56. RELEASE CHECKSUM
==================================================

A hash-eket a végleges release artifactokra generáld.

Preferált:

CHECKSUMS.sha256

vagy CI által generált release checksum artifact.

A checksum fájl ne próbálja
saját magát hash-elni.

Ha commitolt manifest hash-eket tartalmaz,
artifactváltozás után újra kell generálni.

A release-time checksum generálás
előnyben részesíthető.

A cross-platform line-ending stabilitásról
és a byte-exact evidence kezeléséről
a 70–72. pont rendelkezik.


==================================================
57. TÖBBFÁZISÚ KIVITELEZÉS
==================================================

Ha a teljes release túl nagy
egy biztonságos munkalépéshez,
bontsd fázisokra.

Ajánlott:

PHASE A
Baseline + Release Contract

PHASE B
Technical documentation

PHASE C
Legal / governance

PHASE D
Visual documentation

PHASE E
Validation

PHASE F
Final package

A fázisok között:

- canonical baseline ne változzon észrevétlenül;
- gate-besorolás ne változzon opportunista módon;
- már elfogadott döntést ne nyiss újra indok nélkül;
- részleges állapotot ne jelents READY-nek;
- STATUS legyen naprakész.

Ha a munka token- vagy kontextuskorlát miatt több körre bomlik,
csak a szükséges resume-contextet vidd tovább.


==================================================
58. ATOMIKUS RELEASE
==================================================

A végső release
egyetlen konzisztens állapot legyen.

Egyezzen:

- version;
- README;
- STATUS;
- CHANGELOG;
- docs;
- screenshots;
- diagrams;
- test evidence;
- main artifact;
- release artifact;
- checksums;
- manifest.

Régi és új verzió adata
ne keveredjen.

Ha a repository publikálása a release életciklus része,
a konzisztenciát a publikált repository
friss klónján is igazolni kell (67. pont).


==================================================
59. TEST STRATÉGIA
==================================================

Használj célzott teszteket.

TARGETED TEST
FEATURE TEST
REGRESSION TEST

Teljes regresszió akkor indokolt,
ha a változás hatóköre ezt indokolja.

Például:

- core logic;
- architecture;
- storage;
- data pipeline;
- external dependency;
- release infrastructure;
- széles UI-változás.

Ne futtass fölöslegesen teljes regressziót
egy olyan változtatás miatt,
amelyet célzott teszt megfelelően lefed.


==================================================
60. BROWSER / RUNTIME TEST
==================================================

Browser/runtime teszt különösen indokolt,
ha változik:

- UI;
- DOM;
- interaction;
- responsive layout;
- browser storage;
- routing;
- external link behavior;
- browser API használat.

Ha runtime/browser validáció REQUIRED,
de nem végrehajtható:

EVIDENCE = NOT VERIFIED
GATE STATUS = BLOCKED

Ha ez az egyetlen REQUIRED blokkoló ok:

RELEASE STATUS =
STATICALLY VERIFIED ONLY

Jelentése:

BLOCKED: missing required runtime evidence

Ha ezen kívül más REQUIRED gate is blokkol:

RELEASE STATUS = BLOCKED

Ne állíts browser/runtime PASS-t
tényleges runtime teszt nélkül.

FONTOS:

„nem alkalmazható”
nem ugyanaz, mint
„nem tudtam lefuttatni”.

Ha fogalmilag nem alkalmazható:
indokolt N/A lehet.

Ha alkalmazható lenne,
de nem sikerült futtatni:
BLOCKED.


==================================================
61. DOKUMENTÁCIÓ ÉS KÓD SZINKRON
==================================================

Release előtt ellenőrizd,
hogy összhangban vannak-e:

CODE
README
CHANGELOG
STATUS
AGENTS
TESTING
RELEASE NOTES
ARCHITECTURE
VISUALS
VERSION
MANIFEST

Régi dokumentáció nem maradhat
új program mellett.


==================================================
62. ZIP / PACKAGE SZABÁLY
==================================================

Teljes ZIP-et csak akkor készíts,
ha ezt kifejezetten kérem.

Például:

„készíts teljes GitHub csomagot”
„kérek release ZIP-et”
„csomagold GitHubra”

Ha csak egy programfájlt módosítok:

ne készíts automatikusan teljes ZIP-et.


==================================================
63. PACKAGE TISZTASÁG
==================================================

Ne kerüljön publikus package-be:

- temp;
- cache;
- editor backup;
- credential;
- API key;
- token;
- secret;
- személyes fájlút;
- irreleváns régi build;
- scratch;
- fölösleges debug artifact.

A CREDENTIAL / SECRET CLEANLINESS
kötelező minimum release gate.

Ezt nem lehet:

- N/A-ra tenni;
- OPTIONAL-ra minősíteni;
- DEVIATION-nel kihagyni.


==================================================
64. RELEASE CHECKLIST
==================================================

Minden checklist elem rendelkezzen:

REQUIRED: YES / NO
STATUS: DONE / N/A / BLOCKED
INDOK: ha N/A vagy BLOCKED

Minimum ellenőrzés:

[ ] Canonical baseline
[ ] Main artifact
[ ] Baseline byte-parity, ha változatlanság elvárt
[ ] Version consistency
[ ] Static validation
[ ] Runtime validation, ha alkalmazható és REQUIRED
[ ] Integration validation, ha alkalmazható és REQUIRED
[ ] Regression gates
[ ] Credential / secret cleanliness
[ ] License status
[ ] Third-party legal status
[ ] External-data redistribution status
[ ] Documentation
[ ] HU/EN parity, ha többnyelvű
[ ] Privacy/security, ha releváns
[ ] CONTRIBUTING, ha releváns
[ ] Issue/PR templates, ha releváns
[ ] Visual documentation, ha releváns
[ ] Visual validation, ha releváns
[ ] Visual legal cleanliness
[ ] Social preview, ha releváns
[ ] Checksums
[ ] Manifest, ha releváns
[ ] CI/release gate, ha releváns
[ ] Package cleanliness
[ ] Artifact consistency
[ ] Inventory / checksum existence parity
[ ] Line-ending / .gitattributes policy, ha CHECKSUMS szöveges fájlt hash-el
[ ] Published repository parity, ha a publikálás a release része


REQUIRED gate:

DONE
vagy indokolt N/A
→ teljesült.

KIVÉTEL:

A FIX MINIMUM RELEASE GATE-ek
nem lehetnek N/A.


REQUIRED BLOCKED
→ RELEASE BLOCKED.


OPTIONAL BLOCKED
→ limitation,
nem automatikus release block.


==================================================
65. RELEASE STATUS DETERMINISZTIKUS LEVEZETÉSE
==================================================

A release státuszt
ne érzésre válaszd.

A gate-ekből kell következnie.


1. Először ellenőrizd,
hogy minden REQUIRED gate teljesült-e.

Egy REQUIRED gate teljesült, ha:

STATUS = DONE

vagy

STATUS = indokolt N/A,

feltéve, hogy nem FIX MINIMUM RELEASE GATE.


2. Ha bármely alkalmazható REQUIRED gate:

FAIL
ERROR
UNKNOWN
NOT VERIFIED
BLOCKED

és nem kizárólag a runtime evidence hiányzik:

RELEASE STATUS = BLOCKED


3. Ha az egyetlen blokkoló tényező
a kötelező runtime/browser evidence hiánya:

RELEASE STATUS =
STATICALLY VERIFIED ONLY

(BLOCKED subtype: missing required runtime evidence)


4. Ha minden REQUIRED gate teljesült,
de maradt nem blokkoló:

ATTENTION
OPTIONAL UNKNOWN
OPTIONAL BLOCKED
vagy más limitation:

RELEASE STATUS =
READY WITH LIMITATIONS


5. Ha minden REQUIRED gate teljesült
és nincs nyitott limitation:

RELEASE STATUS =
READY

Ha REPOSITORY PUBLICATION = MANUAL BY USER,
a levezetést két külön scope-on kell elvégezni:
PACKAGE STATUS és PUBLISHED RELEASE STATUS (68. pont).


==================================================
66. FINAL REPORT
==================================================

A végén röviden add meg:

RELEASE VERSION

STANDARD VERSION

CANONICAL BASELINE

MAIN ARTIFACT


EVIDENCE

Source:
SOURCE VERIFIED / NOT VERIFIED

Static:
STATIC VERIFIED / NOT VERIFIED

Runtime:
RUNTIME VERIFIED / NOT VERIFIED / N/A

Integration:
INTEGRATION VERIFIED / NOT VERIFIED / N/A


TEST RESULT SUMMARY

PASS:
EMPTY:
UNKNOWN:
ATTENTION:
FAIL:
ERROR:


GATE SUMMARY

REQUIRED DONE:
REQUIRED N/A:
REQUIRED BLOCKED:

OPTIONAL DONE:
OPTIONAL N/A:
OPTIONAL BLOCKED:


RELEASE STATUS

READY

vagy

READY WITH LIMITATIONS

vagy

STATICALLY VERIFIED ONLY
(BLOCKED subtype: missing required runtime evidence)

vagy

BLOCKED


Ha REPOSITORY PUBLICATION = MANUAL BY USER:

PACKAGE STATUS
PUBLISHED RELEASE STATUS

külön-külön, a 68. pont szerint,
valamint a publikálás után futtatandó
pontos ellenőrzési lépések és parancs (67. pont).


Továbbá röviden:

- ismert limitations;
- DEVIATIONS;
- fontos változások;
- dokumentáció állapota;
- vizuális artifactok;
- license status;
- third-party status;
- repository publication módja és published repository parity;
- checksum;
- ZIP/package helye, ha készült.


==================================================
67. PUBLISHED REPOSITORY PARITY
==================================================

Ha a GitHub repository publikálása vagy frissítése
az aktuális release életciklus része,
a publikált repository ellenőrzése kötelező.

A lokálisan vagy ZIP-ben validált release
NEM bizonyítja automatikusan,
hogy a ténylegesen publikált GitHub repository is azonos és helyes.

A Release Contract tartalmazza:

REPOSITORY PUBLICATION:
- AUTOMATED
- MANUAL BY USER
- NOT PART OF THIS RELEASE


Ha:

REPOSITORY PUBLICATION = AUTOMATED

akkor publikálás után:

1. készíts friss klónt a publikált repository cél branchéről;
2. a klón ne a release készítéséhez használt working directory legyen;
3. futtasd újra a projekt release gate-jét;
4. ellenőrizd a manifestet, inventoryt és checksumokat;
5. ellenőrizd a ponttal kezdődő fájlokat és könyvtárakat is;
6. ellenőrizd a relatív linkeket;
7. ellenőrizd a main artifactot;
8. csak sikeres eredmény után jelöld a publikált repositoryt validáltnak.


Ha:

REPOSITORY PUBLICATION = MANUAL BY USER

akkor a PUBLISHED REPOSITORY PARITY
NEM lehet N/A.

Állapota a kézi publikálás után elvégzett ellenőrzésig:

EVIDENCE = NOT VERIFIED
GATE STATUS = BLOCKED
REASON = post-publish verification required

A Final Report tartalmazza a publikálás után
futtatandó pontos ellenőrzési lépéseket és parancsot.

Példa:

1. clone the published repository into a clean directory
2. checkout the published target branch
3. run the project's exact release-gate command
4. verify inventory/checksum parity
5. report the resulting release status

A publikált repository csak ezen ellenőrzés PASS eredménye után
tekinthető validáltnak.


Ha:

REPOSITORY PUBLICATION = NOT PART OF THIS RELEASE

akkor kizárólag ebben az esetben lehet:

PUBLISHED REPOSITORY PARITY = N/A

indokkal:

Repository publication is outside the complete release lifecycle
covered by this task.

Ez a 13. pont N/A-szabályának kifejezett, szűk kivétele:
itt az N/A oka nem a projekt természete,
hanem az, hogy a publikálás a release életciklusán kívül esik.


Ha a package validált,
de a publikált repository eltér tőle:

PUBLISHED REPOSITORY PARITY = FAIL

és ha a gate REQUIRED:

PUBLISHED RELEASE STATUS = BLOCKED

MANUAL BY USER esetén ez nem változtatja meg
a már külön levezetett PACKAGE STATUS értékét.

AUTOMATED esetben ez egyszerűen a publikált release
egészének BLOCKED állapota, tehát:

RELEASE STATUS = BLOCKED


==================================================
68. PACKAGE STATUS ÉS PUBLISHED RELEASE STATUS
==================================================

Ha:

REPOSITORY PUBLICATION = MANUAL BY USER

akkor a Final Report két külön státuszt tartalmazzon.


1. PACKAGE STATUS

A lokálisan elkészített release package állapota.

Ugyanazzal a determinisztikus logikával kell levezetni,
mint a 65. pont RELEASE STATUS szabályait,
de a még végre nem hajtható:

PUBLISHED REPOSITORY PARITY

gate nélkül.

Ez azt mutatja meg, hogy maga az átadott:

- ZIP;
- release directory;
- main artifact;
- documentation;
- manifest;
- checksum;
- test evidence;

kiadásra kész állapotban van-e.


2. PUBLISHED RELEASE STATUS

A ténylegesen GitHubra publikált release állapota.

Ez MINDEN REQUIRED gate-et tartalmaz,
beleértve:

PUBLISHED REPOSITORY PARITY

ellenőrzést is.

Kézi feltöltés előtt vagy a post-publish ellenőrzésig:

PUBLISHED REPOSITORY PARITY:
EVIDENCE = NOT VERIFIED
GATE STATUS = BLOCKED

ezért:

PUBLISHED RELEASE STATUS = BLOCKED


Példa:

PACKAGE STATUS = READY

PUBLISHED RELEASE STATUS = BLOCKED
Reason: manual publication and post-publish verification pending.


FONTOS:

A PACKAGE STATUS = READY
NEM jelenti azt,
hogy a GitHubon publikált repository is READY.

A két státusz két külön scope-ot ír le.

A „READY” szó használatakor mindig egyértelműen jelezni kell,
hogy PACKAGE STATUS-ról
vagy PUBLISHED RELEASE STATUS-ról van szó.

Publikálás és sikeres fresh-clone validáció után
a PUBLISHED RELEASE STATUS újraszámolandó.


==================================================
69. INVENTORY / CHECKSUM EXISTENCE PARITY
==================================================

A release gate script köteles ellenőrizni:

1. A FILE-INVENTORY minden listázott fájlja ténylegesen létezik.

2. A CHECKSUMS minden listázott fájlja ténylegesen létezik.

3. Minden ellenőrizhető checksum egyezik
   a tényleges fájl tartalmával.

4. A manifestben kötelezőként megjelölt artifactok ténylegesen léteznek.

5. A ponttal kezdődő fájlok és könyvtárak
   nem maradhatnak ki csak azért,
   mert hidden/dotfile elemek.

Kiemelten ellenőrizendő, ha a projekt használja:

.github/
.gitignore
.gitattributes
.nojekyll

Ha inventory vagy checksum olyan fájlt sorol fel,
amely nincs jelen:

TEST RESULT = FAIL

Ha ez REQUIRED release gate része:

GATE STATUS = BLOCKED

A release nem lehet READY.


A release gate-et úgy kell megírni,
hogy ugyanaz a script lokális package-en
ÉS friss GitHub-klónon is értelmesen futtatható legyen.

Nem elég azt ellenőrizni,
hogy „a fontos fájlok megvannak”.

A deklarált inventory és a tényleges repository
közötti eltéréseket is fel kell ismernie.


==================================================
70. CROSS-PLATFORM CHECKSUM ÉS LINE-ENDING STABILITÁS
==================================================

Ha a CHECKSUMS vagy más byte-level hash manifest
szöveges fájlokat is tartalmaz,
a repositorynak determinisztikusan rögzítenie kell
a sorvég-kezelést.

Enélkül ugyanaz a Git repository
különböző operációs rendszereken eltérő working-tree byte-okat
eredményezhet.

Például Windows alatt:

core.autocrlf=true

LF → CRLF konverziót okozhat,
ami megváltoztatja a SHA-256 hash-t,
miközben a tartalom logikailag azonos.


Ezért a hash-elt fájlokhoz megfelelő
.gitattributes szabály szükséges.

A .gitattributes policy kialakításakor mindig különítsd el
a normalizálható szöveges forrásfájlokat
és a byte-exact evidence artifactokat.

Preferált normál szöveges forrásfájloknál például:

*.md text eol=lf
*.html text eol=lf
*.js text eol=lf
*.json text eol=lf
*.yml text eol=lf
*.yaml text eol=lf

Így a checkout sorvége
platformtól függetlenül LF marad.


Ha egy fájlt valóban byte-pontosan,
Git text normalization nélkül kell megőrizni,
használható:

path/to/file -text

Ezt csak indokolt,
byte-exact artifactokra használd (71. pont).


Bináris fájlokat explicit binárisként lehet jelölni,
például:

*.png binary
*.jpg binary
*.zip binary


A konkrét .gitattributes szabályokat
a projekt fájltípusaihoz kell igazítani.


REQUIRED CHECK

Ha CHECKSUMS szöveges working-tree fájlokat hash-el:

- .gitattributes jelenléte legyen ellenőrizve;
- a releváns line-ending policy legyen determinisztikus;
- a checksum ellenőrzést clean checkouton is futtasd.

A checksum-stratégia nem támaszkodhat
a fejlesztő helyi core.autocrlf beállítására.


==================================================
71. BYTE-EXACT EVIDENCE ÉS RENORMALIZÁLÁSI SZABÁLY
==================================================

Test evidence és más, hash-sel hivatkozott fájlok
byte-exact artifactok.

Ide tartozhat például:

- runtime log;
- validation evidence;
- ground truth;
- golden fixture;
- snapshot;
- szó szerinti licencszöveg;
- más olyan fájl, amelynek SHA-256 értékére
  dokumentáció, VERSION, STATUS vagy más bizonyíték hivatkozik.

Ezekre ne alkalmazz automatikusan:

text eol=lf

normalizálást.

Használj megfelelő .gitattributes szabályt,
például:

path/to/evidence -text

A cél az eredeti byte-szekvencia megőrzése.

Egy hash-sel kötött evidence artifactot
utólagos line-ending renormalizálás
nem módosíthat észrevétlenül.

Ha egy evidence artifact byte-jai megváltoznak,
a korábbi hash-kötés többé nem érvényes,
és azt új bizonyítékként kell kezelni.


==================================================
72. MEGLÉVŐ REPOSITORY .gitattributes MIGRÁCIÓ
==================================================

Meglévő repositoryba .gitattributes bevezetésekor
a változtatást kontrollált migrációként kezeld.

Ajánlott sorrend:

1. Azonosítsd a hash-sel kötött és byte-exact artifactokat.

2. Először rögzítsd a .gitattributes szabályokat.

3. A byte-exact evidence fájlokat védd -text szabállyal.

4. Csak a normalizálható fájlokra alkalmazz renormalizálást.

5. A renormalizálás után generáld újra
   az érintett CHECKSUMS és manifest adatokat.

6. Ellenőrizd, hogy a hash-kötött evidence fájlok
   byte-pontosan változatlanok maradtak.

7. Futtasd újra a release gate-et.

8. Publikálás után készíts friss klónt,
   és azon is futtasd le ugyanazt a gate-et.

Hash-kötött evidence-t a renormalizálás nem módosíthat.

Ha mégis módosul:

TEST RESULT = FAIL

amíg a bizonyítéklánc nincs szabályosan újralétrehozva.


==================================================
73. ABSZOLÚT ALAPELV
==================================================

Nem az a cél,
hogy minden projekt ugyanazokat a fájlokat,
képeket és diagramokat kapja.

Az a cél,
hogy minden projekt ugyanazt a
PROFESSZIONÁLIS MINŐSÉGI SZINTET kapja.

Ami releváns:
legyen kiváló.

Ami projektjelleg miatt nem releváns:
legyen indokolt N/A.

Ami releváns, de nem sikerült:
legyen BLOCKED.

Ami nincs bizonyítva:
legyen UNKNOWN vagy NOT VERIFIED.

Ami hibás:
legyen FAIL.

Egy REQUIRED gate lehet teljesült
indokolt N/A-val,
de kizárólag akkor,
ha az adott ellenőrzés valóban nem alkalmazható
a projekt természetéből fakadóan.

A FIX MINIMUM RELEASE GATE-ek
nem lehetnek N/A.

Kötelező gate hibáját
nem szabad limitationné átnevezni.

Kötelező gate-et
nem szabad pusztán azért opcionálissá tenni,
mert nehéz teljesíteni.

A credential/secret ellenőrzést
nem szabad kihagyni.

A végső GitHub release legyen:

TECHNIKAILAG KORREKT
VIZUÁLISAN IGÉNYES
JÓL DOKUMENTÁLT
JOGILAG RENDEZETT
ELLENŐRIZHETŐ
FOLYTATHATÓ
REGRESSZIÓKTÓL VÉDETT
ÉS HOSSZÚ TÁVON KARBANTARTHATÓ.


==================================================
74. VÉGSŐ MUNKASZABÁLY
==================================================

Ne mechanikusan gyárts fájlokat.

Először értsd meg a projektet.

Utána készíts olyan GitHub csomagot,
amely az adott projekthez illik,
de legalább ezt a minőségi szintet teljesíti.

Ha valami technikailag nem megoldható:
mondd ki.

Ha valami nincs bizonyítva:
ne állítsd bizonyítottnak.

Ha valami nem releváns:
indokold az N/A-t.

Ha valami releváns, de hiányzik:
ne rejtsd el.

Ha valami fontos,
de ez a szabvány nem említi:
add hozzá.

A cél nem a legtöbb fájl.

A cél a lehető:

LEGJOBB
LEGÉRTHETŐBB
LEGSZEBB
LEGELLENŐRIZHETŐBB
LEGBIZTONSÁGOSABBAN FOLYTATHATÓ

GitHub projekt.
