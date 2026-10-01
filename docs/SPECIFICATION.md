# 01 – TELJES FUNKCIONÁLIS SPECIFIKÁCIÓ

## 1. Projektcél

Az **sPg Star Citizen Vehicle Reference Downloader** célja egyetlen HTML-fájlban olyan böngészős segédeszközt adni, amely Star Citizen hajók és földi járművek referencia-képeit a Star Citizen Wikiről automatikusan megtalálja, nézetenként egységesen azonosítja, előnézetben megmutatja, majd egy rendezett ZIP-csomagban adja vissza.

Elsődleges használat: képszerkesztéshez, AI-képgenerálási referenciához és vizuális összehasonlításhoz könnyen kezelhető, pontosan elnevezett hajó/jármű nézetcsomag létrehozása.

## 2. Futási modell

Kötelező cél:

- egyetlen `.html` fájl;
- közvetlenül `file://`-ról nyitható;
- nincs helyi szerver;
- nincs Python;
- nincs Node.js;
- nincs telepítő;
- nincs build-folyamat;
- nincs külön runtime CSS- vagy JS-fájl;
- a ZIP-készítéshez szükséges kód a HTML-ben van, nem CDN-ről töltődik.

### V001 tényleges megvalósítása

A V001 teljes CSS-t és JavaScriptet beágyazza a HTML-be. Külső ZIP-könyvtár helyett egy saját, beágyazott `ZipBuilder` osztály ír ZIP-et STORE módban, tehát ZIP-funkcióhoz nincs CDN-függőség.

### V001 valós böngészős E2E bizonyíték

A V001-gyel valós felhasználói böngészős tesztben sikeresen elkészült az:

`Esperia Prowler Utility - Reference Pack.zip`

A teszt bizonyítja, hogy a **Star Citizen Wiki `media.starcitizen.tools` eredeti képe → böngészős CORS/fetch → Blob → lokális átméretezés → ZIP** lánc a gyakorlatban működik a V001-ben legalább az Esperia Prowler Utility esetén.

Bizonyított eredmények:

- 6 darab `In space` nézet: `Isometric`, `Above`, `Port-side`, `Front`, `Rear`, `Below`;
- mind a 6 Original: `3840×2160`, JPEG;
- az Original URL-ek `https://media.starcitizen.tools/...` címek;
- 2048px származékok: `2048×1152`, PNG;
- 1280px származékok: `1280×720`, PNG;
- Contact Sheet: `2048×908`, PNG;
- a Wiki `..._in_space_-_Port.jpg` fájl helyesen `Port-side` nézetnévre normalizálódott;
- a kötelező teljes fájlnév-séma működött;
- a manifestben rögzített `game_data_version`: `4.10.1-LIVE.12660092`.

**[BIZONYTALAN]** A tesztből nincs megőrzött bizonyíték arra, hogy a HTML pontosan `file://` protokollról futott-e, illetve melyik böngésző és verzió futtatta. Ezért a Prowler Utility média-CORS + Blob + ZIP lánc bizonyított, de a kifejezetten `file://` + konkrét böngésző kombináció még nem minősül külön bizonyítottnak. Részletes státusz: `VALIDATION.md`.

Megjegyzés: a közös sPg CSS elején Google Fonts `@import` szerepel az Orbitron és Roboto betűkhöz. Ha ez nem érhető el, a CSS fallback fontokat használ. A program Wiki/API funkciói ettől függetlenek.

## 3. Adatforrások és V001 endpointok

### 3.1 Új Star Citizen Wiki API

Alap URL a V001-ben:

`https://api.star-citizen.wiki/api`

A V001 ténylegesen ezeket használja:

1. **Aktuális alapértelmezett game-data verzió**
   - `GET https://api.star-citizen.wiki/api/game-versions/default`
   - Feladat: az aktuális Wiki game-data verzió felismerése.
   - A V001 ebből egy verziósztringet keres, pl. `4.x.x-LIVE.build` jelleggel.

2. **Járműkatalógus**
   - `GET https://api.star-citizen.wiki/api/vehicles?page={N}&per_page=100&version={VERSION}`
   - Feladat: hajók/földi járművek katalógusának letöltése, max. 30 lapos biztonsági korláttal.
   - A V001 ebből készíti helyben a gyártólistát és a járműlistát.
   - Nincs külön gyártó-endpoint hívás a V001-ben; a gyártószűrés helyben történik.

3. **Keresés Wiki URL → járműrekord párosításhoz**
   - `GET https://api.star-citizen.wiki/api/search?filter[query]={WIKI_CÍM}`
   - Csak akkor kell, ha a beillesztett Wiki-oldalcím nem párosítható közvetlenül a már betöltött katalógushoz.
   - A V001 a `vehicles` típusú találati csoportot keresi.

4. **Jármű részlet URL**
   - A keresési találat `api_url` mezőjét a V001 szükség esetén közvetlenül lekéri.
   - Ezt nem egy hardcoded endpoint építi fel; a keresési válaszból jön.

### 3.2 Star Citizen Wiki MediaWiki Action API

Alap URL:

`https://starcitizen.tools/api.php`

Minden MediaWiki API URL-be bekerül:

- `format=json`
- `formatversion=2`
- `origin=*`

A V001 tényleges hívásai:

1. **Oldalcím/redirect feloldás**
   - `action=query`
   - `titles={TITLE}`
   - `redirects=1`
   - `prop=info`
   - `inprop=url`

2. **Wiki-oldal keresés, ha a közvetlen címjelöltek nem találhatók**
   - `action=query`
   - `list=search`
   - `srsearch={MODELL + GYÁRTÓ}`
   - `srlimit=10`

3. **Wiki oldal parse**
   - `action=parse`
   - `page={TITLE}`
   - `prop=wikitext|images|text`
   - `disablelimitreport=1`
   - Feladat: wikitext, képfájllista és renderelt HTML elérése a médiafelismeréshez.

4. **Képfájl metaadat és preview URL**
   - `action=query`
   - `titles=File:{FILE1}|File:{FILE2}|...`
   - `prop=imageinfo`
   - `iiprop=url|size|mime`
   - `iiurlwidth=640`
   - Feladat: eredeti URL, thumbnail URL, felbontás és MIME megszerzése.

5. **Eredeti médiafájl**
   - A V001 az `imageinfo.url` értékét csak a ZIP készítésekor tölti le közvetlen `fetch(..., {mode:'cors'})` hívással.
   - **V001 valós teszt:** az Esperia Prowler Utility mind a 6 `3840×2160` JPEG Original képe sikeresen letöltődött `media.starcitizen.tools` URL-ről, majd Blobként bekerült a ZIP-folyamatba. Ez a média-CORS/fetch + Blob útvonal működését bizonyítja ennél a tesztesetnél.
   - **[BIZONYTALAN]** A teszt futási protokollja (`file://` vagy más) és a böngésző pontos típusa/verziója nincs dokumentálva.

### 3.3 Changelog

A projektterv szerint a Star Citizen Wiki changelogot is használni kell NEW / UPDATED jelöléshez.

**[ELTÉR A TERVTŐL] V001:** nem hív changelog endpointot. A V001 az előző helyi katalógus és az új katalógus egy kiválasztott mezőkészletből képzett fingerprintjét hasonlítja össze, és ebből képez `[ÚJ]` / `[MÓDOSULT]` jelölést.

**[BIZONYTALAN]** A beszélgetésben korábban vizsgált changelog URL-minta: `https://api.star-citizen.wiki/changelog/{VERSION}?change_type=all&entity_type=vehicle&page=1`. Ezt a jelenlegi készítői környezet hálózati DNS-hibája miatt most nem lehetett újra ellenőrizni. Implementálás előtt a Wiki aktuális API-dokumentációjából validálandó.

## 4. Járműválasztó

A kiválasztási lánc:

**Járműtípus → Gyártó → Jármű**

Járműtípus értékek:

- `Mind`
- `Hajók`
- `Földi járművek`

Kötelező jelentés:

- A `Mind` kizárólag a katalógus megjelenítését jelenti.
- A `Mind` **soha nem jelent összes járműre vagy összes képre indított tömeges letöltést**.
- Vegyes listában a jármű neve mellett legyen típusjelölés: `— Hajó` vagy `— Földi jármű`.

A kategorizálás adatmezőből történjen, nem névből:

- `is_spaceship` igaz → Hajó;
- `is_vehicle` vagy `is_gravlev` igaz → Földi jármű;
- nem bizonyítható típus → ne kerüljön automatikusan a fő katalógusba.

A V001 ezt a logikát implementálja.

## 5. Gyártó- és járműnév

- A gyártókat nem kézi, hardcoded táblából kell fenntartani.
- A gyártólista az aktuális járműkatalógusból készül.
- A jármű teljes exportneve: **teljes gyártónév + modellnév**.
- A program megpróbálja elkerülni a gyártónév duplikálását, ha a jármű neve már tartalmazza.
- Exportnál a Windowsban tiltott fájlnév-karaktereket biztonságos formára kell cserélni; rövidítés tilos.

## 6. Wiki URL mező és kétirányú szinkron

Célviselkedés:

- kézzel beilleszthető pl. `https://starcitizen.tools/MOLE`;
- URL-ből feloldja a járművet;
- automatikusan beállítja a Járműtípus → Gyártó → Jármű mezőket;
- legördülős kiválasztásból automatikusan kitölti/aktualizálja a Wiki URL mezőt;
- mindkét belépési út ugyanazt az egy közös médiafelismerő és exportmotort használja.

**[ELTÉR A TERVTŐL] V001:** URL → legördülők működnek. A legördülőből kiválasztás beállítja a belső canonical Wiki URL-t és a „Wiki oldal megnyitása” linket, de a látható `wikiUrlInput` mezőt nem tölti automatikusan vissza. Ezt külön javítani kell.

## 7. Médiafelismerés

### 7.1 Cél

A képek célcsoportja elsődlegesen:

**Ship profile → Exterior → In space / In-space**

Nem fájlnév-mintából kell kitalálni, hogy „biztosan így hívják a képet”. A Wiki tényleges média-struktúrájából kell azonosítani.

Nem kerülhet a referencia-csomagba tévesen:

- paint/livery;
- concept art;
- belső kép;
- általános gallery-kép;
- schematic;
- logo/icon;
- más képcsoport, ha a felhasználó csak In space csoportot kért.

A médiafeldolgozó belső modellje képcsoport-független legyen, hogy ugyanaz a motor később `Landed` vagy „Mindkettő” csoportot is kezelhessen.

### 7.2 V001 tényleges működés

A V001:

- `action=parse` segítségével lekéri a wikitextet és képlistát;
- a fájlnév körüli wikitext-környezetből keresi a nézet- és csoportkulcsszavakat;
- `In space`, `Landed`, `Exterior` csoportot ismer;
- pontozza a jelölteket;
- a `paint|livery|concept|interior|logo|icon` kifejezésekre pontlevonást ad;
- csoport+nézet páronként a legjobb pontszámú jelöltet tartja meg.

**[ELTÉR A TERVTŐL]:** a V001 nem strukturálisan bizonyítja a `Ship profile → Exterior → In space` tab-hierarchiát. Heurisztikusan végigvizsgálja az oldal képeit/wikitextjét. A tiltott kategóriák jelenleg pontlevonást kapnak, nem abszolút kizárást. Emiatt a felismerés robusztussága még fejlesztendő.

## 8. Nézetnév-normalizálás

Biztosan ismert normalizálások:

- `Isometric` → `Isometric`
- `Above`, `Top view` → `Above`
- `Port`, `Port-side` → `Port-side`
- `Starboard`, `Starboard-side` → `Starboard-side`
- `Front`, `Fore` → `Front`
- `Rear`, `Aft`, `Back` → `Rear`
- `Below`, `Bottom`, `Underside` → `Below`

Normalizálás csak biztos egyezésnél történhet. Ismeretlen nézetet nem szabad önkényesen átnevezni.

Földi járműnél nem szabad erőltetni a hajóknál gyakori 6 nézetet. Csak a ténylegesen talált nézetek jelenjenek meg.

Cél UI: `X / Y` jelzés, ha van értelmezhető elvárt készlet.

**[ELTÉR A TERVTŐL] V001:** jelenleg csak pl. `6 nézet` jelenik meg, nem `6 / 6`. Nincs külön „elvárt nézetszám” modell.

## 9. Háromszintű hálózati működés

Kötelező elv:

### 1. Indulás

Csak:

- verzió/metaadat;
- járműkatalógus;
- helyi cache ellenőrzése.

**Nincs járműkép-letöltés.**

### 2. Konkrét jármű kiválasztása

Csak a kiválasztott jármű:

- Wiki oldalának média-metaadatai;
- kis előnézeti/thumbnail képei.

Más jármű képe nem töltődik le.

### 3. ZIP gomb megnyomása

Csak ekkor:

- a kiválasztott képcsoport teljes felbontású eredeti képei;
- lokális 2048/1280 generálás;
- Contact Sheet, ha kérve van;
- manifest;
- ZIP összeállítás.

A V001 ezt az alapelvet implementálja.

## 10. Előnézet

Előnézeti terület csak jármű kiválasztása után jelenjen meg.

Cél:

- nagy fő preview;
- elsődlegesen `Isometric`;
- ha nincs Isometric, az első ténylegesen talált nézet;
- alatta/mellette az összes felismert nézet;
- nézetnév;
- eredeti felbontás;
- képcsoport;
- elérhetőségi állapot;
- becsült ZIP-méret.

A V001 a nézeteket `Isometric`-tel kezdődő rendezéssel tárolja, ezért ha van Isometric, az lesz az első preview. A preview maga a Wiki által adott `iiurlwidth=640` thumbnail URL-t használja.

**[ELTÉR A TERVTŐL]:** a V001 nem számol és nem mutat becsült ZIP-méretet.

## 11. Original elérhetőség és fallback

Kötelező szabály:

- thumbnail soha nem helyettesítheti csendben az eredetit;
- ha az original URL nincs vagy nem letölthető, a felületen egyértelműen: `Original unavailable`;
- ne készüljön úgy ZIP, hogy a felhasználó azt higgye, teljes eredetit kapott, miközben csak thumbnail került bele.

**[ELTÉR A TERVTŐL] V001:** ha az `imageinfo` hiányzik, a jelölt kiesik és warning log készül. Ha preview URL nincs, kiírja, hogy nincs kis előnézet és az eredetit nem tölti le automatikusan. Külön `Original unavailable` állapotcímke nincs implementálva.

## 12. Képcsoportok

A motor belsőleg ne legyen kizárólag `In space`-re hardcode-olva.

V001 már tartalmazza:

- `Automatikus`
- `In space`
- `Landed`
- `Mindkettő / minden felismert`

Automatikus módban:

- hajónál preferencia: `In space` → `Landed` → `Exterior`;
- földi járműnél preferencia: `Landed` → `Exterior` → `In space`.

Ez előrébb jár az eredeti minimumtervnél, de a felismerés heurisztikussága miatt még validálandó.

## 13. Verziókövetés

### Célmodell

Egymástól külön kezelendő:

1. Star Citizen **LIVE** verzió;
2. Wiki **adatverzió**;
3. PTU/EPTU verzió, ha van.

Nem szabad ezeket egyetlen címkévé összemosni.

Eltérés esetén pl.:

`LIVE 4.x.y — Wiki adat 4.x.x — frissítésre vár`

Követés:

- oldal indulásakor;
- nyitva tartott oldalnál 30–60 percenként;
- kézi `Adatok frissítése` gombbal;
- előző állapot `localStorage`-ban;
- bizonyítható changelog alapján NEW / UPDATED jelölés.

### V001 állapot

**[ELTÉR A TERVTŐL]:**

- egyetlen `gameVersion` mezőt kezel;
- ezt `game-versions/default` válaszból veszi;
- a felső badge-ben `LIVE` címkével mutatja;
- nincs külön Wiki adatverzió;
- nincs külön PTU/EPTU állapot;
- nincs 30–60 perces automatikus időzített ellenőrzés;
- NEW/UPDATED nem changelogból, hanem két katalógus fingerprint összehasonlításából származik.

A helyi verzióelőzmény legfeljebb 12 bejegyzést tárol.

## 14. Katalógus-cache

V001 localStorage kulcsok:

- `spg_sc_vehicle_ref_catalog_v1`
- `spg_sc_vehicle_ref_version_v1`
- `spg_sc_vehicle_ref_version_history_v1`
- `spg_sc_vehicle_ref_recent_v1`
- `spg_sc_vehicle_ref_settings_v1`

Katalógus-cache:

- ha van mentett katalógus, induláskor azonnal megjeleníthető;
- ugyanazon verzió és 24 órán belüli cache esetén V001 nem kér új katalógust;
- más verzió / régi cache / `force` esetén lekéri újra;
- online frissítési hiba esetén, ha van cache, azt megtartja.

Gombok:

- `Adatok frissítése` → verzió + katalógus kényszerített frissítése;
- `Cache törlése` → az alkalmazás saját localStorage kulcsait törli, letöltött ZIP-ekhez nem nyúl.

**[ELTÉR A TERVTŐL]:** nincs külön valódi háttérfrissítő worker/ütemezett cache-refresh; az init folyamat a cache megjelenítése után szinkronban folytatja a hálózati ellenőrzést.

## 15. Legutóbbi 5 jármű

- localStorage alapú;
- maximum 5;
- új választás előre kerül;
- duplikáció nélkül;
- gyorslista a felületen.

A V001 implementálja.

## 16. Rejtett diagnosztika

A felületen nincs állandó logablak.

A háttérben naplózandó minimum:

- programnév és programverzió;
- export időpontja;
- user agent;
- nyelv;
- online/offline állapot;
- `file:` / `http:` futási protokoll;
- oldal URL-je;
- LIVE / Wiki / PTU-EPTU verziók, ha rendelkezésre állnak;
- API endpointok;
- HTTP státuszok;
- válaszidők;
- CORS/fetch hibák;
- kiválasztott jármű;
- canonical Wiki cím/URL;
- felismert nézetek;
- eredeti Wiki fájlnevek;
- thumbnail és original URL-ek;
- MIME;
- felbontás;
- eredeti kép-letöltés eredménye;
- ZIP eredmény;
- cache állapot;
- JavaScript exceptionök stackkel.

Tilos logolni:

- képbájtokat;
- sütiket;
- auth tokeneket;
- secretet.

Cél diagnosztikai fájlnév:

`sPg_SC_Ship_Downloader_Diagnostic_ÉÉÉÉHHNN_ÓÓPPMM.json`

**[ELTÉR A TERVTŐL] V001:** tényleges név:

`sPg SC Vehicle Reference Downloader - <Jármű vagy No Vehicle> - Diagnostic - <ISO timestamp kötőjelekkel>.json`

A V001 a `fetchJSON` hívásoknál URL-t, HTTP státuszt és időt logol siker esetén; hibánál URL-t, hibát és időt. Eredeti média-fetch sikerénél fájlnevet, bájtméretet, MIME-t és időt logol. CORS-hiba nincs külön kategorizálva, általános fetch hiba lesz.

## 17. ZIP és képméretezés

A kötelező export szabályok teljes részletei a `EXPORT_RULES.md` fájlban vannak. Röviden:

- Original bájtra változatlan;
- generált 2048px és 1280px csak lefelé;
- mindkettő közvetlenül az Originalból;
- nincs upscale;
- nincs AI-upscale;
- a V001 generált formátuma **PNG**;
- Contact Sheet PNG;
- az eredeti kép a Wikiről csak egyszer jön le, majd a lokális Blob cache újrahasználható az aktuális választásban.
