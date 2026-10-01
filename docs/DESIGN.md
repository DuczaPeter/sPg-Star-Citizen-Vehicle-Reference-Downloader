# 03 – DESIGN / UI RENDSZER

## 1. Vizuális cél

A program az sPg eszközök megszokott sötét, Star Citizenhez illő, technikai felületét használja:

- nagyon sötét kék-fekete háttér;
- vékony cián keretek;
- visszafogott cián glow;
- borostyán/arany kiemelés elsődleges műveleteknél;
- kompakt státusz badge-ek;
- kerekített panelek és gombok;
- világos, jól olvasható fehér/kékesszürke szöveg;
- Orbitron főcímekhez, Roboto normál UI-szöveghez.

A `historical restart-package 07_STYLE.css` a közös sPg stílus teljes, változtatás nélküli forrása. A V001 ezt a CSS-t beágyazza, majd utána saját „Vehicle Reference Downloader additions” szabályokat ad hozzá.

## 2. Alap sPg CSS – fontos változók

A közös `style.css` fő változói:

- `--assignment-accent: #14d9ff`
- `--assignment-accent-dark: #00acc4`
- `--assignment-success: #4caf50`
- `--assignment-warning: #ffc107`
- `--assignment-danger: #f44336`
- `--text-primary: #e3eaf2`
- `--text-secondary: #90a4ae`
- `--text-muted: #b0bec5`
- `--page-bg: #1a2636`
- `--page-bg-alt: #0f1720`
- `--sc-primary: #ffb300`
- `--sc-primary-700: #c88700`
- `--surface: #162338`
- `--surface-soft: #1a2636`
- `--line: rgba(24, 218, 255, 0.5)`
- `--line-soft: rgba(24, 218, 255, 0.28)`
- `--accent-strong: #fff0c2`
- `--shadow: 0 0 0 1px rgba(24,218,255,.16) inset, 0 14px 34px rgba(0,0,0,.36), 0 0 24px rgba(24,218,255,.14)`

Betűk:

- Orbitron: 400 / 500 / 700 / 800
- Roboto: 300 / 400 / 500 / 700 / 900
- fallback: Arial / Helvetica / sans-serif

A CSS Google Fonts importot használ:

`https://fonts.googleapis.com/css2?family=Orbitron...&family=Roboto...`

## 3. V001-specifikus design változók

A V001 saját kiegészítései:

- `--header-bg: rgba(9, 17, 28, 0.98)`
- `--panel-bg: rgba(20, 34, 53, 0.96)`
- `--cyan: #18daff`
- `--cyan-soft: rgba(24, 218, 255, 0.32)`
- `--gold: #ffb300`

## 4. Felső menü – vizuális referencia szöveges rekonstrukciója

A vizuális mintakép fájlja:

`assets/ui-topbar-style-reference.png`

A kép egy nagyon széles, kb. dashboard-szerű sPg felület tetejét mutatja.

### Első sor

- teljes szélességű, sötét kék-fekete fejléc;
- bal szélen nagyobb, félkövér fehér cím: a referencia képen `sPg salvage eladási ár`;
- jobb szélen egysoros műveleti blokk;
- első elem sötét dropdown: `Magyar`;
- mellette arany/borostyán keretes `Adatok frissítése` gomb;
- utána cián keretes `Log másolása`;
- utána cián keretes `Cache törlése`;
- minden gomb kompakt, kerekített, sötét kitöltésű.

A Downloaderben ennek megfelelően:

- cím: `sPg Star Citizen Vehicle Reference Downloader`;
- `Magyar`;
- `Adatok frissítése`;
- `Log mentése`;
- `Cache törlése`.

### Második sor: státuszsáv

- az első sor alatt vékony határvonallal elválasztott, sötét sáv;
- balra kis, kapitális, kékesszürke `ADATFORRÁSOK` címke;
- utána több kapszula/badge;
- badge-ek vékony cián kerettel, sötét belsővel, kicsi fehér/kék szöveggel;
- az aktív/egészséges státusz zöld pontot/kiemelést kaphat;
- figyelmeztetés borostyán keretet/színt kap.

Downloader cél badge-ek:

- `ADATFORRÁSOK`
- `Star Citizen Wiki API ✓`
- `LIVE ...`
- `Wiki adatverzió ...`
- `Járműkatalógus: N`
- `Utolsó ellenőrzés: ...`
- verzióeltérés / NEW / UPDATED összefoglaló, ha releváns.

**[ELTÉR A TERVTŐL] V001:** külön `Wiki adatverzió` és `Utolsó ellenőrzés` badge jelenleg nincs. Van API badge, egy `LIVE`-nak nevezett gameVersion badge, katalógusszám, változás-badge és hálózati működést magyarázó badge.

## 5. Fő vezérlőpanel

A felső sáv alatt egy nagy, lekerekített, cián keretes panelben:

- Járműtípus;
- Gyártó;
- Jármű;
- Legutóbbi;
- Képcsoport;
- teljes szélességű Wiki URL mező + `Link elemzése` gomb.

Minden mező:

- sötét gradient háttér;
- vékony cián border;
- 11–12 px körüli kompakt UI-szöveg;
- label erősebb fehér;
- helper text szürkés-kék.

## 6. Állapotüzenet

A control panel alatt egy vékony státuszmező:

- muted/info/good/warn/error színezés;
- nincs konzolszerű logfal;
- csak aktuális felhasználói állapotüzenet.

## 7. Üres állapot

Jármű kiválasztása előtt:

- nagy, középre rendezett, szaggatott cián keretes terület;
- rövid cím;
- magyarázat, hogy csak katalógus-metaadat töltődik, képek nem.

## 8. Előnézeti állapot

Kiválasztás után kétoszlopos elrendezés:

### Bal oldal

- nagy preview-kártya;
- sötét checker/technikai háttér;
- a kép `object-fit: contain`;
- alul kis caption: nézet, eredeti felbontás, eredeti Wiki fájlnév.

### Jobb oldal

- `Felismert nézetek` kártya;
- 2 oszlopos kis nézetkártyák;
- mindegyikben thumbnail, nézetnév, felbontás, képcsoport;
- aktív kártya arany kiemelést kap.

## 9. Exportpanel

Külön kártya a preview alatt:

- `Referencia-csomag` cím;
- checkbox kártyák:
  - Eredeti
  - 2048px
  - 1280px
  - Contact Sheet
  - Forrásmanifest
- nagy arany/borostyán elsődleges ZIP gomb;
- mellette progress szöveg és keskeny progress bar;
- progress bar cián → arany gradient.

## 10. Fontos komponensszínek

Tipikus UI jelentések:

- cián `#14d9ff` / `#18daff`: normál aktív technikai keret és fókusz;
- arany `#ffb300`: elsődleges művelet, kiemelt kontroll;
- zöld `#4caf50`: siker / kapcsolódva;
- sárga `#ffc107`: figyelmeztetés / betöltés;
- piros `#f44336`: hiba;
- fő szöveg `#e3eaf2` / `#f3f8ff`;
- másodlagos szöveg `#90a4ae` környéke;
- alap háttér `#0f1720` és `#1a2636`.

## 11. MOLE nézetreferencia

A `08_IMAGE_01_MOLE_views.png [EXCLUDED FROM PUBLIC REPOSITORY]` vizuális célként mutatja, hogyan csoportosítja a Wiki az `In space` nézeteket:

- felső tabok: `In space` aktív, `Landed` inaktív;
- egy lekerekített sötét keretben hat nézet:
  - Isometric
  - Above
  - Port-side
  - Front
  - Rear
  - Below
- minden nézet fölött címke, alatta/benne kis thumbnail.

A Downloader ezt nem pixelpontosan másolja, hanem ugyanazt az információs logikát viszi át az sPg saját UI-stílusába.


## Release-repository asset mapping

- The historical `07_STYLE.css` was used as the common sPg design source while V001 was built. It is **not shipped as a runtime file** in this repository because V001 must remain single-file and the relevant CSS is already embedded in the canonical HTML. Historical CSS SHA-256: `197a12af11e14f5404ff191cfc1de4a82cc4b67419e3185e35ee1f9039f5621f`.
- `assets/ui-topbar-style-reference.png` is included. It is a screenshot of the user's own sPg Salvage Selling Price interface and is a **style reference**, not a V001 runtime screenshot.
- `08_IMAGE_01_MOLE_views.png` is **not included** in the public package. Visual inspection shows six Star Citizen MOLE ship renders embedded in the screenshot (Isometric, Above, Port-side, Front, Rear, Below). Because those are Star Citizen/CIG image assets, the public release keeps only this textual description and does not redistribute the screenshot.
