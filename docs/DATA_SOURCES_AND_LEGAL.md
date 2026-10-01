# Data sources and legal status

## Source precedence

For V001 runtime behavior:

1. Star Citizen Wiki game-data API (`api.star-citizen.wiki/api`) for game-data version and vehicle metadata/catalog.
2. Star Citizen Wiki MediaWiki Action API (`starcitizen.tools/api.php`) for page/title/media discovery.
3. Image URLs returned by Wiki `imageinfo`, normally `media.starcitizen.tools`, for original media bytes.
4. Local V001 cache only as a performance/continuity aid; refresh can replace it with current source data.

No hardcoded manufacturer/vehicle catalog is authoritative.

## Exact V001 endpoints/purposes

### Game-data version

`GET https://api.star-citizen.wiki/api/game-versions/default`

Purpose: detect the Wiki game-data version used for catalog requests.

### Vehicle catalog

Paged request against:

`https://api.star-citizen.wiki/api/vehicles`

V001 supplies the resolved version and paginates the catalog. The exact query construction is documented in `SPECIFICATION.md` and remains authoritative in the V001 source.

Purpose:

- manufacturers;
- vehicles;
- structured vehicle-type information;
- canonical identities used by the selector.

### Search / vehicle details

`https://api.star-citizen.wiki/api/search`

Purpose: resolve vehicle/Wiki records and follow the returned API URL when additional vehicle data is needed.

### MediaWiki Action API

`https://starcitizen.tools/api.php`

V001 uses MediaWiki requests including:

- `action=query` for title/redirect/info resolution;
- `list=search` as a page-resolution fallback;
- `action=parse` with relevant properties for page media discovery;
- `prop=imageinfo` with `iiprop=url|size|mime`;
- `iiurlwidth=640` for preview metadata;
- `format=json`;
- `formatversion=2`;
- `origin=*`.

### Original media

The full-resolution URL returned by `imageinfo` is fetched only when ZIP creation is requested.

## Version tracking

V001 uses `game-versions/default` plus local catalog fingerprint/history logic.

It **does not currently use the Wiki changelog endpoint**. Changelog validation and migration of NEW/UPDATED status to a changelog-backed implementation is a V002 task.

The desired future model separates:

- LIVE game version;
- Wiki data version;
- PTU/EPTU version;
- last checked timestamp.

V001 does not yet fully separate these.

## Verified public policy references

- Star Citizen Wiki general disclaimer: https://starcitizen.tools/Star_Citizen_Wiki:General_disclaimer
- Star Citizen Wiki API overview: https://starcitizen.tools/Star_Citizen_Wiki:Application_programming_interface
- RSI Star Citizen Fankit and Fandom FAQ: https://support.robertsspaceindustries.com/hc/en-us/articles/360006895793-Star-Citizen-Fankit-and-Fandom-FAQ
- RSI Terms of Service: https://robertsspaceindustries.com/tos

## Wiki content license findings

The Star Citizen Wiki general disclaimer states that information from the site is available under CC BY-SA 4.0, while trademarks and other protected material remain with their owners.

Individual Wiki media pages can show CC BY-SA 4.0 for a file but also state that additional restrictions apply when the file contains Star Citizen intellectual property.

Therefore this release does **not** infer a blanket right to redistribute downloaded ship/vehicle images.

## API terms status

The Wiki API documentation explicitly describes APIs as tools used by developers, fansite operators, and bots to retrieve game/Wiki information.

A separate comprehensive API-specific Terms of Service / rate-limit contract was not reliably identified in this release audit.

**Status:** `SOURCE VERIFIED` for public API documentation; `UNKNOWN / ATTENTION` for a separate dedicated API-specific Terms/rate-limit contract.

The project must not invent limits or permissions not stated by the source.

## CIG / RSI fan and trademark status

RSI's current fan guidance requires fan activities to be visibly unofficial and not imply affiliation or endorsement. It also provides an explicit fan-site notice and links to current Terms/Fan Kit guidance.

This repository therefore:

- identifies itself as unofficial;
- does not claim affiliation or endorsement;
- excludes downloaded Star Citizen vehicle images;
- keeps third-party IP outside the MIT project-license scope;
- recommends a neutral GitHub repository slug because RSI guidance warns against official marks in a fan-site URL/domain. Whether that wording applies exactly to GitHub repository slugs remains `UNKNOWN / ATTENTION`.

## Excluded visual asset

Historical restart artifact:

`08_IMAGE_01_MOLE_views.png`

Visual inspection confirms it embeds six Star Citizen MOLE ship renders. It is excluded from the public repository. Its informational purpose is preserved textually in `DESIGN.md`: the reference showed `In space` and `Landed` tabs and six views labelled Isometric, Above, Port-side, Front, Rear, Below.

## Included visual asset

`assets/ui-topbar-style-reference.png`

This is the user's own sPg tool screenshot. It is a design-language reference only and must not be described as a V001 runtime screenshot.

## Project license

Project-owned source/documentation: MIT License.

Third-party trademarks, game content, Wiki content, fonts, and user-generated/downloaded output retain their own rights/licenses.

See `../LICENSE`, `../NOTICE.md`, and `../THIRD_PARTY_NOTICES.md`.
