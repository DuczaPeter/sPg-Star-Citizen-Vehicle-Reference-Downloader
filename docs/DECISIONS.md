# 04 – DÖNTÉSI NAPLÓ

## 1. Egyfájlos HTML marad

**Döntés:** egyetlen HTML, `file://`, szerver és telepítő nélkül.

**Indok:** egyszerű hordozhatóság; bármely gépen megnyitható; nem kell külön runtime vagy projektkörnyezet.

## 2. Dinamikus gyártó- és járműlista

**Döntés:** nem kézi gyártó/hajótábla.

**Elvetve:** hardcoded lista, pl. `MOLE = ARGO`, `Polaris = RSI`.

**Miért:** hamar elavul; új hajóknál kézi frissítést igényel; a Wiki API már adja a szükséges adatot.

## 3. Típusadatból hajó/földi jármű

**Döntés:** `is_spaceship` / `is_vehicle` / `is_gravlev`-szerű mezők alapján.

**Elvetve:** névből vagy kézi whitelistből találgatás.

**Miért:** adatvezérelt és robusztusabb.

## 4. `Mind` nem tömeges letöltés

**Döntés:** a `Mind` kizárólag a listában engedi mindkét járműtípust.

**Elvetve:** összes gyártó / összes jármű / összes nézet előzetes letöltése.

**Miért:** felesleges hálózati forgalom, memóriahasználat és Wiki-terhelés; felhasználó egyszerre egy járművel dolgozik.

## 5. Háromlépcsős hálózati modell

**Döntés:**

1. indulás → metaadat/katalógus;
2. kiválasztás → csak a konkrét jármű thumbnail/meta;
3. ZIP gomb → teljes felbontású eredetik.

**Miért:** gyorsabb UI, kisebb adatforgalom, tisztább működés.

## 6. Nincs fájlnév-találgatás

**Döntés:** a Wiki oldal tényleges médiaadataiból kell keresni.

**Elvetve:** olyan feltételezés, hogy minden fájl neve biztosan `<Ship> in Space - Isometric.jpg`.

**Miért:** a Wiki oldal- és fájlnév-konvenciói nem minden járműnél azonosak.

**[ELTÉR A TERVTŐL] V001:** bár nem épít fix fájlnevet, a jelenlegi médiafelismerés heurisztikus wikitext/fájlnév pontozás, nem szigorú tabstruktúra-felismerés.

## 7. Egy közös feldolgozómotor

**Döntés:** a Wiki URL-es és a legördülős út ugyanoda fusson be.

**Miért:** ne legyen két eltérő felismerő/exportlogika, amely idővel szétcsúszik.

## 8. Képcsoport-független belső modell

**Döntés:** ne csak In space legyen hardcode-olva.

**Miért:** később Landed és „Mindkettő” ugyanazzal a motorral kezelhető.

A V001 már kínál `Automatikus`, `In space`, `Landed`, `Mindkettő / minden felismert` módot.

## 9. Földi járműveknél nincs kötelező 6 nézet

**Döntés:** csak az legyen, amit ténylegesen találunk.

**Elvetve:** üres vagy kitalált Isometric/Above/Port/Front/Rear/Below helyek kierőltetése.

**Miért:** a Wiki médiakészlete járművenként eltérhet.

## 10. Original érintetlen

**Döntés:** az Original kép bájtjai ne változzanak.

**Miért:** forráshű referencia; később mindig vissza lehet térni a Wiki eredetihez.

## 11. Csak lefelé méretezés

**Döntés:** 2048 és 1280, az Originalból külön-külön.

**Elvetve:** felfelé méretezés.

**Miért:** a felnagyítás nem ad valódi új részletet.

## 12. AI-upscale elvetve

**Döntés:** nincs generatív upscaling.

**Miért:** hajóreferenciánál az AI új panelvonalat, antennát, fegyvert, geometriát vagy feliratot találhat ki; a hitelesség fontosabb.

## 13. SVG-be csomagolt raszter elvetve

**Döntés:** nem próbáljuk a JPG/PNG képet SVG-wrapperrel „korlátlanul nagyíthatóvá” tenni.

**Miért:** egy SVG-be ágyazott raszter továbbra is raszter, a pixelek száma nem nő.

## 14. 512px export elvetve

**Döntés:** nincs külön 512px exportcsomag.

**Miért:** a 2048 és 1280 elég; a felülethez a Wiki thumbnail használható; ne termeljünk fölösleges fájlokat.

## 15. 2048/1280 formátum

A beszélgetésben JPEG és PNG lehetőség is felmerült, de nem született külön explicit lezáró döntés a kód elkészítése előtt.

**V001 as-built döntés:** mindkettő PNG és nem választható.

Ez most baseline-ként kezelendő, amíg a felhasználó kifejezetten másképp nem dönt.

## 16. Kötelező teljes fájlnevek

**Döntés:** minden egyes exportált képfájl nevében legyen:

- teljes gyártó + jármű;
- nézet;
- képverzió.

**Miért:** a felhasználó nem akar egyetlen fájlt sem kézzel átnevezni; egy kimásolt fájl önmagában is azonosítható legyen.

## 17. Contact Sheet

**Döntés:** opcionális, 2048px-es össznézeti referencia.

**Miért:** képgenerálásnál vagy gyors áttekintésnél egyetlen képből látható több nézet.

## 18. `_source.json` / provenance

**Döntés:** a ZIP tartalmazhasson forrásmanifestet.

**Miért:** később visszakövethető legyen, melyik Wiki-oldal, melyik fájlnév és melyik játék/Wiki verzió volt a forrás.

**[ELTÉR A TERVTŐL] V001:** a manifest neve jelenleg hosszú, járműnév-alapú; a normatív cél `_source.json`.

## 19. Látható logfal elvetve

**Döntés:** a felületen ne legyen folyamatos technikai log.

**Miért:** a felhasználói UI maradjon tiszta.

Helyette a program háttérben gyűjt diagnosztikát és egy kattintással JSON-fájlba adja.

## 20. CORS-proxy elvetve

**Döntés:** ne használjunk kétes ingyenes vagy harmadik féltől függő CORS-proxyt.

**Miért:** adatvédelmi, megbízhatósági és rendelkezésre állási kockázat; az eszköz ne épüljön ismeretlen közvetítőre.

### Valós V001 bizonyíték

A V001-gyel felhasználói böngészőben sikeresen elkészült az `Esperia Prowler Utility - Reference Pack.zip`. A csomag mind a 6 `In space` Original képet közvetlen `media.starcitizen.tools` URL-ekről tartalmazza `3840×2160` JPEG formában, és a V001 ezekből helyben előállította a 2048px/1280px PNG-ket és a Contact Sheetet, majd ZIP-be csomagolta őket.

Ez bizonyítja, hogy a **media CORS/fetch → Blob → lokális feldolgozás → ZIP** lánc működik legalább ennél a valós tesztesetnél. Emiatt a jelenlegi működéshez nincs indok CORS-proxy bevezetésére.

**[BIZONYTALAN]** A tesztből nem maradt meg bizonyítható adat arról, hogy a V001 pontosan `file://` protokollról futott-e, illetve melyik böngésző/verzió használta. Ezért a döntés továbbra is az, hogy proxyt nem használunk, de a kifejezetten `file://` + konkrét böngésző kombinációt külön regressziós teszttel kell majd rögzíteni.

## 21. Bezárt oldalnál nincs háttérfigyelés

**Döntés:** az egyfájlos HTML nem ígér működést, amikor be van zárva.

**Miért:** nincs háttérszolgáltatás, nincs service process.

Cél: induláskor, kézzel, illetve nyitott oldalnál időszakosan ellenőrizzen.

**[ELTÉR A TERVTŐL] V001:** automatikus 30–60 perces időzített ellenőrzés még nincs.

## 22. Cache localStorage-ban

**Döntés:** katalógus, verzióelőzmény, legutóbbi 5 jármű és beállítások localStorage-ban.

**Miért:** gyorsabb indulás és nulla külön adatbázis/szerver.

## 23. Changelog előnyben a valódi NEW/UPDATED jelöléshez

**Döntés:** hosszabb távon a Wiki changelog legyen a bizonyító forrás, ha elérhető és stabil.

**[ELTÉR A TERVTŐL] V001:** jelenleg helyi katalógus-diffet használ. Ez hasznos fallback, de nem ugyanaz, mint a hivatalos Wiki changelog.


## Release-packaging decisions

### Star Citizen vehicle images are not repository assets

**Decision:** Wiki-downloaded ship/vehicle images and the historical MOLE visual reference are excluded from the public repository.

**Reason:** the application can fetch source media at runtime, but repository redistribution rights for each game/media asset are not assumed. The package therefore keeps runtime evidence as metadata/manifest only.

### API-specific Terms remain explicit UNKNOWN/ATTENTION

**Decision:** the release documents what the public Wiki API documentation proves, but does not invent a separate API ToS or rate-limit policy.

**Reason:** the API documentation explicitly describes developer/fansite/bot use, but a separate complete API-specific contract was not reliably located in this release audit.

### Exact browser/file protocol evidence is not reconstructed

**Decision:** the successful Prowler runtime test remains PASS for the media → Blob → ZIP chain, while browser identity/version and whether the page ran under `file://` remain NOT VERIFIED / UNKNOWN.

**Reason:** evidence cannot be upgraded after the fact from memory or inference. The next normal-use diagnostic JSON can close this without a dedicated extra test.
