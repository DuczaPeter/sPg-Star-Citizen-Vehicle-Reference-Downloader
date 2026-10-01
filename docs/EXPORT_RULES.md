# 02 – KÖTELEZŐ EXPORT-, ZIP- ÉS FÁJLNÉVSZABÁLYOK

Ez a dokumentum normatív. Ezeket a szabályokat csak kifejezett felhasználói döntéssel szabad megváltoztatni.

## 1. ZIP neve

Kötelező forma:

`<Teljes gyártó> <Jármű> - Reference Pack.zip`

Példa:

`ARGO Astronautics MOLE - Reference Pack.zip`

A teljes gyártónév és a jármű neve nem rövidíthető önkényesen.

## 2. ZIP belső szerkezete

Célstruktúra:

- `Original/`
- `2048px/`
- `1280px/`
- `Contact-Sheet/` – csak ha a Contact Sheet opció be van kapcsolva
- `_source.json` – csak ha a forrásmanifest opció be van kapcsolva

**[ELTÉR A TERVTŐL] V001:** a manifest jelenleg nem `_source.json`, hanem:

`<Teljes gyártó> <Jármű> - All Views - Source Manifest.json`

és a ZIP gyökerébe kerül. Ezt a következő javításkor a normatív `_source.json` névre kell átállítani, hacsak a felhasználó másképp nem dönt.

## 3. Minden képfájl kötelező neve

Minden exportált képfájl neve:

`<Teljes gyártó> <Jármű> - <Nézet> - <Képverzió>.<ext>`

Példák:

- `ARGO Astronautics MOLE - Port-side - Original.jpg`
- `ARGO Astronautics MOLE - Isometric - Original.jpg`
- `ARGO Astronautics MOLE - Front - 2048px.png`
- `ARGO Astronautics MOLE - Rear - 1280px.png`

Kötelező:

- a teljes gyártónév szerepel;
- a jármű neve szerepel;
- a nézet neve szerepel;
- a képverzió szerepel;
- az `Original` szó az Original fájlnévben akkor is szerepel, ha az `Original/` mappában van.

Tilos:

- `front.jpg`
- `isometric.png`
- `image_01.png`
- `MOLE_1.jpg`
- bármilyen név, amelyből önmagában nem derül ki a teljes jármű, nézet és verzió.

## 4. Contact Sheet név

Kötelező forma:

`<Teljes gyártó> <Jármű> - All Views - Contact Sheet 2048px.<ext>`

V001 jelenlegi formátuma: PNG.

Példa:

`ARGO Astronautics MOLE - All Views - Contact Sheet 2048px.png`

## 5. Windows fájlnévbiztonság

A Windowsban tiltott karaktereket biztonságos karakterre/szövegre kell cserélni:

`< > : " / \ | ? *` és kontrollkarakterek.

A V001 ezeket ` - ` jellegű elválasztásra cseréli, a többszörös whitespace-t összevonja és a fájlnév végéről pontot/szóközt eltávolít.

**Rövidíteni tilos.**

Tehát Windows-kompatibilissé tenni szabad, de például `Roberts Space Industries` → `RSI` automatikus rövidítés nem engedélyezett exportnévben.

## 6. Original fájl

Az `Original/` fájl:

- a Wiki eredeti média URL-jéről letöltött bájtokból készül;
- nem méretezhető át;
- nem konvertálható;
- nem újratömöríthető;
- eredeti MIME/formátumban marad;
- a kiterjesztés az eredeti MIME/URL alapján kerül meghatározásra.

V001 megvalósítás: a Blob `arrayBuffer()` bájtjai változtatás nélkül kerülnek a ZIP-be. A saját ZIP-író STORE módban tárolja őket; ez a fájl tartalmát nem módosítja.

## 7. Lefelé méretezés

Csak lefelé méretezés engedélyezett.

Példa egy 3840×2160 forrásnál:

- 2048-as változat: 2048×1152
- 1280-as változat: 1280×720

Mindig oldalarányt kell tartani.

A „2048px” és „1280px” a hosszabbik oldal maximális mérete.

Ha az eredeti hosszabbik oldala már kisebb vagy egyenlő a kért méretnél:

- **nem szabad felnagyítani**;
- az adott generált verziót ki kell hagyni;
- a manifest/log jelezze, hogy upscale tiltás miatt maradt ki.

## 8. Nincs láncolt méretezés

Tilos:

`3840 → 2048 → 1280`

Kötelező:

`Original → 2048`

és külön:

`Original → 1280`

Így a 1280-as változat nem egy már egyszer újraméretezett fájlból készül.

A V001 ezt betartja.

## 9. Nincs upscale és nincs AI-upscale

Nem engedélyezett:

- klasszikus felfelé interpolálás exportként;
- AI-upscale;
- generatív „részletjavítás”;
- bármilyen olyan feldolgozás, amely új hajógeometriát vagy nem létező részletet találhat ki.

Referenciafelhasználásnál a geometriai hitelesség fontosabb, mint a mesterségesen nagy felbontás.

## 10. 512px verzió

Az 512px-es exportváltozat kikerült a végleges tervből.

A program használhat kis Wiki thumbnailt a felület gyors előnézetéhez, de az nem ugyanaz, mint egy kötelező `512px/` exportmappa.

## 11. Generált 2048/1280 formátum – lezárt V001 állapot

A beszélgetés során JPEG és PNG is felmerült, de külön felhasználói döntés nem zárta le ezt a pontot a kód elkészítése előtt.

A **V001 tényleges kódja ezt eldöntötte: a 2048px és 1280px változatok mindig PNG-k**.

- `canvas.toBlob(..., 'image/png')`
- fájlnév: `... - 2048px.png`
- fájlnév: `... - 1280px.png`

Ezért a V001 baseline szempontjából a végleges jelenlegi viselkedés:

**2048px = PNG, 1280px = PNG, nem választható.**

Ha később JPEG/PNG választót akarunk, az új funkció és explicit spec-változás legyen; ne „javításként” változzon meg csendben.

## 12. Helyi méretezés és hálózati forgalom

- A Wikiről az eredeti képet egyszer kell letölteni az aktuális ZIP-generáláshoz.
- A 2048 és 1280 változatokat a böngésző helyben generálja Canvas segítségével.
- Contact Sheet is helyben készül.
- Nem kérjük le a Wikiről ugyanazt a képet külön 2048 és 1280 változatban.
- V001 az eredeti Blobokat a kiválasztott jármű munkamenetén belül `Map`-ben cache-eli.

## 13. Contact Sheet

V001:

- maximum 3 oszlop;
- sötét háttér;
- cián keretes cellák;
- minden cellában a nézet képe és alatta a nézet neve;
- maximum szélesség: 2048 px;
- formátum: PNG.

Ha a felhasználó kikapcsolja a Contact Sheet opciót, a `Contact-Sheet/` elem ne kerüljön a ZIP-be.

## 14. `_source.json` kötelező tartalma

Cél szerinti minimum:

- schema/contract verzió;
- alkalmazásnév és alkalmazásverzió;
- letöltés/generálás időpontja;
- teljes gyártónév;
- járműnév;
- jármű teljes neve;
- járműtípus: Hajó / Földi jármű;
- LIVE verzió;
- Wiki adatverzió;
- canonical Wiki oldal címe;
- canonical Wiki oldal URL-je;
- kiválasztott képcsoport;
- nézetenként:
  - normalizált nézetnév;
  - eredeti Wiki fájlnév;
  - original URL;
  - eredeti szélesség/magasság;
  - eredeti MIME;
  - elkészült exportfájlok és méretek.

**[ELTÉR A TERVTŐL] V001:**

- `game_data_version` mező van, nincs külön LIVE + Wiki adatverzió;
- a manifest fájl neve nem `_source.json`;
- a többi fenti provenance nagy része már benne van.

## 15. Képverzió jelentése

A fájlnév utolsó névrésze mindig azt mondja meg, milyen képverzióról van szó:

- `Original`
- `2048px`
- `1280px`
- Contact Sheet esetén `Contact Sheet 2048px`

Ez azért kötelező, hogy egy ZIP-ből kimásolt önálló fájl is kontextus nélkül azonosítható maradjon.
