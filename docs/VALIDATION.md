# 05 – AKTUÁLIS ÁLLAPOT ÉS ROADMAP

## 1. Baseline

Aktuális elkészült forrás:

`../sPg_Star_Citizen_Vehicle_Reference_Downloader_V001.html`

Alkalmazás belső verziója:

`V001`

A forrás teljes, nem rövidített. Ebben a dokumentációfrissítésben **nem történt kódmódosítás**.

A restart csomagban rögzített forrás SHA-256:

`3bb0b10d5794f36346b0752d05aa3bc5dac90d4b21b4318c6b909834b7e4695b`

Közös `style.css` SHA-256:

`197a12af11e14f5404ff191cfc1de4a82cc4b67419e3185e35ee1f9039f5621f`

Referencia képek SHA-256:

- `08_IMAGE_01_MOLE_views.png` (historical reference; excluded from public repository because it contains Star Citizen/CIG imagery): `683a4af0af3f219db47d2b849876d3e7cb6b41281d1414b31ac7ffb276f5886f`
- `../assets/ui-topbar-style-reference.png`: `503ca894ab54706cfbd8bd497e57004507c7f4b050083f9f666cd4c9f55fb05a`

## 2. Korábban lokálisan ellenőrzött technikai alapok

### PASS – JavaScript szintaxis

A V001 `<script>` tartalma Node.js `--check` ellenőrzésen hibamentesen átment a csomag készítésekor.

Használt ellenőrző runtime:

`Node v22.16.0`

Ez szintaktikai ellenőrzés volt, nem böngészős E2E teszt.

### PASS – HTML alapszerkezet

A forrásban:

- 1 db `<style>...</style>` blokk;
- 1 db `<script>...</script>` blokk;
- a V001 egyetlen önálló HTML-fájl.

### PASS – beágyazott ZIP-író alapteszt

A saját `ZipBuilder` külön helyi fixture tesztben szabványos, olvasható ZIP-et hozott létre. `unzip -t` hibát nem jelzett.

Ez a korai fixture csak a ZIP-konténer logikát bizonyította; a valós Star Citizen Wiki médiaútvonalat a későbbi Prowler Utility teszt bizonyította.

## 3. Ami V001-ben implementálva van

- egyetlen HTML;
- közös sPg CSS beágyazva;
- `Mind / Hajók / Földi járművek` típusválasztó;
- dinamikus gyártólista a katalógusból;
- dinamikus járműlista;
- vegyes listában `Hajó` / `Földi jármű` jelölés;
- `is_spaceship` / `is_vehicle` / `is_gravlev` alapú típuslogika;
- Wiki URL feldolgozás;
- MediaWiki Action API `origin=*` használat;
- Wiki oldal címfeloldás és keresés;
- wikitext/images parse;
- nézetfelismerés;
- `In space / Landed / Exterior` csoportfelismerés;
- Wiki thumbnail előnézetek;
- teljes Original letöltés csak ZIP-kor;
- Original export;
- 2048px PNG downscale;
- 1280px PNG downscale;
- Contact Sheet PNG;
- saját beágyazott ZIP writer;
- forrásmanifest;
- localStorage katalógus-cache;
- verzióelőzmény;
- legutóbbi 5 jármű;
- kézi frissítés;
- cache törlés;
- háttérben gyűjtött diagnosztika;
- egykattintásos diagnosztikai JSON mentés;
- ablakhiba és unhandled rejection logolás;
- kötelező teljes exportfájl-nevek nagy része implementálva.

## 4. Valós böngészős E2E teszt – Esperia Prowler Utility

### PASS – valós Reference Pack elkészült

A V001-gyel saját böngészős használatban sikeresen elkészült:

`Esperia Prowler Utility - Reference Pack.zip`

A tényleges ZIP-et később külön is megvizsgáltuk. 20 fájlt tartalmaz, a kicsomagolt fájlok összmérete `19 368 597` byte, maga a ZIP kb. 19 MB.

### PASS – 6/6 In space nézet

A csomagban mind a 6 várt `In space` nézet megtalálható:

- `Isometric`
- `Above`
- `Port-side`
- `Front`
- `Rear`
- `Below`

### PASS – Original képek

Mind a hat Original:

- `3840×2160`;
- JPEG;
- közvetlen Star Citizen Wiki `media.starcitizen.tools` URL-ről származik;
- a fájlnév tartalmazza a teljes járműnevet, a nézetet és az `Original` képverziót.

Példa:

`Original/Esperia Prowler Utility - Port-side - Original.jpg`

### PASS – nézetnév-normalizálás

A Wiki eredeti fájlneve:

`Prowler_Utility_in_space_-_Port.jpg`

A program helyesen ezt az exportnézetet képezte:

`Port-side`

Ez bizonyítja a `Port → Port-side` normalizálást ezen a valós teszteseten.

### PASS – 2048px származékok

Mind a hat generált 2048px kép:

- `2048×1152`;
- PNG;
- a V001 helyben generálta az Originalból.

### PASS – 1280px származékok

Mind a hat generált 1280px kép:

- `1280×720`;
- PNG;
- a V001 helyben generálta az Originalból.

### PASS – Contact Sheet

A Contact Sheet:

- `2048×908`;
- PNG;
- fájlnév: `Esperia Prowler Utility - All Views - Contact Sheet 2048px.png`.

### PASS – kötelező fájlnév-logika

A tesztelt képfájlok megfelelnek a kötelező sémának:

`<Teljes gyártó> <Jármű> - <Nézet> - <Képverzió>.<ext>`

Példák:

- `Esperia Prowler Utility - Isometric - Original.jpg`
- `Esperia Prowler Utility - Port-side - 2048px.png`
- `Esperia Prowler Utility - Rear - 1280px.png`

### PASS – rögzített game-data verzió

A generált manifestben:

`game_data_version: 4.10.1-LIVE.12660092`

### [ELTÉR A TERVTŐL] – manifest fájlnév

A V001 ebben a valós csomagban ezt készítette:

`Esperia Prowler Utility - All Views - Source Manifest.json`

A normatív cél továbbra is:

`_source.json`

Ez a V002 első javítási pontja.

## 5. CORS proof-of-concept – frissített állapot

### PASS – media CORS + Blob + ZIP lánc

A korábbi bizonytalanság ezen része lezárható.

A Prowler Utility valós teszt bizonyítja, hogy a V001 képes volt:

1. a Star Citizen Wiki média-metaadatból eljutni az eredeti `media.starcitizen.tools` URL-ekhez;
2. mind a 6 eredeti `3840×2160` JPEG-et böngészőből lekérni;
3. azokat Blobként feldolgozni;
4. helyben 2048px és 1280px PNG-változatokat készíteni;
5. Contact Sheetet készíteni;
6. a teljes csomagot ZIP-be írni.

**Következtetés:** a `media.starcitizen.tools` → böngészős CORS/fetch → Blob → ZIP lánc a gyakorlatban működik legalább az Esperia Prowler Utility V001 tesztesetben.

### [BIZONYTALAN] – pontos futási környezet

A teszthez nem maradt meg bizonyító adat arról, hogy:

- a HTML pontosan `file://` protokollról futott-e;
- Chrome, Edge vagy más böngésző futtatta-e;
- mi volt a böngésző pontos verziója.

Ezért **nem szabad** ebből azt állítani, hogy a `file:// + Chrome/Edge adott verzió` kombináció külön bizonyított. A média-CORS + Blob + ZIP lánc viszont bizonyított.

A `file://` + böngésző kérdés lezárásához **nem kell külön tesztet szervezni**. A felhasználó következő normál V001/V002 használatakor a diagnosztikai logból lezárható, feltéve hogy a log ténylegesen megőrzi a futási protokollt és a böngészőazonosítót. Addig ez a rész továbbra is **[BIZONYTALAN]**.

A következő normál használat diagnosztikai logjában meg kell őrizni és utólag ellenőrizni:

- `location.protocol`;
- `navigator.userAgent`;
- a releváns fetch státuszokat/időket.

## 6. Még teszteletlen kötelező regressziós járművek

A következő valós tesztek ebben a sorrendben javasoltak:

1. **MOLE** – a projekt eredeti referenciaesete, 6 klasszikus In space nézettel;
2. **Polaris** – nagy hajó, más Wiki médiaanyaggal;
3. **Carrack** – újabb külön hajóteszt;
4. **egy többtabos/szokatlan Wiki-oldalú hajó** – a médiafelismerés robusztusságára;
5. **egy földi jármű** – annak bizonyítására, hogy nem kényszerítjük rá a hajós 6 nézetet.

Ezekre jelenleg nincs valós E2E bizonyíték. Nem szabad sikeres tesztként feltüntetni őket.

## 7. Nyitott döntés – PNG származékok mérete

A Prowler Utility valós ZIP-je fontos új megfigyelést adott.

A kicsomagolt csomag méretmegoszlása:

- 6 Original JPEG együtt: `2 915 714` byte;
- generált PNG-k együtt, beleértve a Contact Sheetet: `16 446 733` byte;
- teljes kicsomagolt tartalom: `19 368 597` byte.

A generált PNG-k a teljes tartalom kb. **84,9%**-át adják. Gyakorlatban ez megfelel annak a megfigyelésnek, hogy a PNG származékok gyakran **3–4× nagyobbak**, mint az azonos nézet Original JPG-jei.

### Nyitott V002 döntés

Két elfogadható irány van:

**A – PNG marad fixen**

- nincs új JPEG-veszteségi kör a származékokon;
- egyszerűbb, determinisztikusabb működés;
- viszont lényegesen nagyobb csomagok.

**B – JPEG / PNG választó V002-ben**

- a felhasználó dönthet a kisebb ZIP és a veszteségmentes export között;
- JPEG esetén külön rögzíteni kell a quality értéket és az exportkontraktust;
- az Original továbbra is bájtra érintetlen marad.

**Döntés még nincs.** V001 baseline: 2048px és 1280px = PNG.

## 8. Ismert V001 eltérések a kívánt tervtől

### 8.1 Manifest fájlnév

**[ELTÉR A TERVTŐL]**

Cél:

`_source.json`

V001:

`<Vehicle> - All Views - Source Manifest.json`

### 8.2 Wiki URL kétirányú sync

**[ELTÉR A TERVTŐL]**

URL → dropdown működik.

Dropdown → belső Wiki link működik, de a látható URL input nem frissül vissza.

### 8.3 Original unavailable

**[ELTÉR A TERVTŐL]**

Nincs külön, felhasználónak látható `Original unavailable` állapot.

### 8.4 Külön LIVE / Wiki adatverzió / PTU-EPTU

**[ELTÉR A TERVTŐL]**

V001 egyetlen `gameVersion` értéket kezel és azt LIVE badge-ként mutatja. A három állapot nincs külön modellezve.

### 8.5 Utolsó ellenőrzés badge

**[ELTÉR A TERVTŐL]**

A kívánt külön `Utolsó ellenőrzés` státusz nincs teljesen megvalósítva a felső állapotsor tervezett formájában.

### 8.6 X / Y nézetszám

**[ELTÉR A TERVTŐL]**

V001 pl. `6 nézet`, nem `6 / 6`.

### 8.7 Becsült ZIP-méret

**[ELTÉR A TERVTŐL]**

Nincs implementálva.

### 8.8 30–60 perces automatikus verzióellenőrzés

**[ELTÉR A TERVTŐL]**

Nincs timer. Induláskor és kézi frissítéskor ellenőriz.

### 8.9 Changelog

**[ELTÉR A TERVTŐL]**

V001 nem hív validált changelog endpointot; fingerprint diffet használ NEW/UPDATED jelöléshez.

### 8.10 Médiafelismerés

**[ELTÉR A TERVTŐL]**

A cél a pontos `Ship profile → Exterior → In space / In-space` struktúra felismerése.

V001 heurisztikus wikitext/fájlnév-pontozást használ.

### 8.11 Tiltott média abszolút kizárása

**[ELTÉR A TERVTŐL]**

Paint/livery/concept/interior/logo/icon jelenleg negatív pontot kap, nem abszolút kizárást.

### 8.12 Diagnosztikai fájlnév

**[ELTÉR A TERVTŐL]**

Cél:

`sPg_SC_Ship_Downloader_Diagnostic_ÉÉÉÉHHNN_ÓÓPPMM.json`

V001 járműnevet és ISO-jellegű időbélyeget használ.

### 8.13 Külön CORS hibakategória

**[ELTÉR A TERVTŐL]**

A fetch hiba logolva van, de nincs biztos, külön `CORS_ERROR` osztályozás.

### 8.14 Katalógus háttérfrissítés

**[ELTÉR A TERVTŐL]**

Cache-ről gyorsan renderel, majd szükség esetén az init folyamat frissít, de nincs külön background worker vagy időzített katalógus-refresh.

## 9. Javasolt V002 implementációs sorrend

A következő körben az alábbi sorrendet kell követni. Ez prioritási sorrend, nem csak ötletlista.

### a) Manifest átnevezése `_source.json`-ra

A jelenlegi hosszú manifestnév helyett pontosan:

`_source.json`

A manifest tartalma maradhat kompatibilis, csak a névkontraktus javítandó.

### b) Látható Wiki URL mező visszatöltése legördülős választáskor

A dropdown → canonical Wiki URL → látható URL input kétirányú szinkront teljesen be kell fejezni.

### c) `Original unavailable` állapot

Ha az original URL hiányzik vagy az eredeti fájl nem tölthető le, a UI egyértelműen jelezze:

`Original unavailable`

Thumbnail nem lehet csendes fallback.

### d) LIVE / Wiki adatverzió / PTU-EPTU szétválasztása + `Utolsó ellenőrzés` badge

A három verzióállapot külön mező és külön badge legyen. Eltérésnél jelenjen meg a `frissítésre vár` állapot. Kerüljön külön `Utolsó ellenőrzés` badge is.

### e) `X / Y` nézetszám és becsült ZIP-méret

A felhasználó lássa a talált/elvárt nézetarányt, ahol az elvárt szám bizonyítható, valamint még letöltés előtt kapjon ésszerű ZIP-méretbecslést.

### f) 30–60 perces ellenőrzés nyitott oldalnál

Az oldal nyitva tartása alatt fusson időszakos verzió/metaadat-ellenőrzés. Bezárt oldalnál továbbra sincs háttérfigyelés.

### g) Changelog endpoint validálása, utána NEW/UPDATED arra átállítva

Előbb a Wiki aktuális API-ján bizonyítani kell a changelog endpoint és séma működését. Csak ezután váltsa le a NEW/UPDATED elsődleges forrását. A katalógus fingerprint diff maradhat fallback/diagnosztika.

### h) Szigorúbb `In space` tab-felismerés

A cél a tényleges `Ship profile → Exterior → In space / In-space` struktúra felismerése. A nem oda tartozó media ne pusztán pontlevonást kapjon, hanem bizonyítottan rossz kategória esetén legyen kizárva.

## 10. V002 utáni további technikai adósság

A fenti a–h sorrend után kezelendő:

- diagnosztikai fájlnév a normatív sémára;
- külön `CORS_ERROR` osztályozás;
- a futási protokoll és böngészőverzió egyértelmű rögzítése a diagnosztikai evidence-ben;
- szükség esetén memóriaterhelési teszt nagyobb járműveknél;
- PNG/JPEG származékformátum döntés implementálása, ha a nyitott döntés lezárul.

## 11. Ismert technikai kockázatok

1. **Pontos `file://` regresszió még nincs dokumentálva.** A média-CORS lánc bizonyított, de a futási protokoll/böngésző nincs megőrizve.
2. Wiki sablon/wikitext szerkezet változása.
3. Heurisztikus médiafelismerés hamis pozitívja.
4. Jármű API mezőstruktúra változása.
5. Nagy képcsomagnál böngészőmemória: a V001 a teljes ZIP-et memóriában építi fel.
6. Saját ZIP writer STORE módban nem tömörít; a ZIP mérete közel a tartalom összmérete lesz.
7. A PNG származékok jelentősen növelik a csomagméretet.
8. Google Fonts import hálózati hiba esetén fallback font jelenik meg.

## 12. Későbbi tervek

### Landed / Mindkettő képcsoport

A belső modell már részben támogatja, de a későbbi stabil változatban struktúra-alapú felismeréssel és regressziós teszttel kell véglegesíteni.

### Kereshető járműlista

A jelenlegi dropdown később searchable comboboxszá alakítható, ha a katalógus mérete miatt szükséges.

### „Csak hiányzó képek” manifest alapján

Később egy korábbi manifest betöltésével össze lehet hasonlítani a meglévő nézeteket, és csak az új/hiányzó fájlokat exportálni.

Nem szabad azt feltételezni, hogy a böngésző automatikusan átvizsgálhat tetszőleges helyi mappát; a felhasználó által explicit megadott manifest vagy külön, engedélyezett File System Access út szükséges.

## 13. Következő valós tesztcsomag

A V002 kódmódosítás előtt vagy közben megismételhető a V001 baseline-on:

1. MOLE;
2. Polaris;
3. Carrack;
4. többtabos hajó;
5. földi jármű.

Minden tesztnél rögzítendő:

- futási protokoll (`file:` / `http:` / `https:`);
- böngésző és verzió;
- game-data verzió;
- felismert képcsoport;
- nézetlista;
- original MIME/felbontás;
- original URL origin;
- ZIP fájllista;
- exportált méretek;
- diagnosztikai log.

## 14. Új AI számára fontos lezárás

A V001 már nem csak szintaktikailag létező prototípus: **van valós, sikeres Prowler Utility referencia-csomag bizonyíték**.

Bizonyított:

- 6/6 In space Original;
- `media.starcitizen.tools` eredeti JPG-k;
- böngészős media fetch/CORS;
- Blob-feldolgozás;
- 2048/1280 helyi downscale;
- Contact Sheet;
- ZIP-generálás;
- kötelező kép-fájlnév logika;
- `Port → Port-side` normalizálás;
- `game_data_version: 4.10.1-LIVE.12660092`.

**[BIZONYTALAN]:** a sikeres teszt pontos futási protokollja és böngészője nincs dokumentálva.

**Még nem tesztelt:** MOLE, Polaris, Carrack, többtabos hajó, földi jármű.

A következő AI ne írjon át kódot csak azért, hogy „rendet tegyen”. Először a fenti evidence-t és a V002 prioritási sorrendet vegye alapul.


## 15. GitHub release-package validation overlay

The GitHub packaging work did **not modify** the V001 application bytes.

Canonical main artifact SHA-256:

`3bb0b10d5794f36346b0752d05aa3bc5dac90d4b21b4318c6b909834b7e4695b`

The packaged root artifact is required to match that hash exactly.

The public repository intentionally excludes all Wiki-downloaded Star Citizen ship images and the historical MOLE screenshot reference. Runtime evidence is preserved as metadata in:

`../test-artifacts/09_TEST_Prowler_Utility_manifest.json`

The exact `file://` + browser/version question remains the only release-required browser evidence blocker for the package scope. It should be resolved from the next normal-use diagnostic JSON; no dedicated extra run is required.
