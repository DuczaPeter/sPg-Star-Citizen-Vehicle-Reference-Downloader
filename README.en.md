# sPg Star Citizen Vehicle Reference Downloader V001

[Magyar README](README.md)

**sPg Star Citizen Vehicle Reference Downloader** is a single-file, locally run browser utility for collecting reference images of Star Citizen spacecraft and ground vehicles. It uses Star Citizen Wiki data to select a vehicle, detect relevant exterior views, show previews, and package original images plus optional downscaled variants into a consistently named ZIP.

> **V001 release status:** `STATICALLY VERIFIED ONLY` — static, integrity, and documentation gates for the package are complete, and a real Esperia Prowler Utility runtime test passed for the media → Blob → ZIP chain. The exact mandatory `file://` execution mode and browser/version were not captured in that runtime evidence, so the browser/runtime gate remains blocked. The published GitHub repository status remains `BLOCKED` until manual publication and fresh-clone parity verification.

## Main artifact

`sPg_Star_Citizen_Vehicle_Reference_Downloader_V001.html`

The application remains **single-file HTML**: CSS, JavaScript, and the ZIP writer are embedded in the HTML. The GitHub repository structure does not split the runtime application.

Canonical V001 SHA-256:

`3bb0b10d5794f36346b0752d05aa3bc5dac90d4b21b4318c6b909834b7e4695b`

## V001 features

- vehicle type filter: **All / Spacecraft / Ground vehicles**;
- dynamic **Manufacturer → Vehicle** selection from Wiki data;
- manually entered Star Citizen Wiki URL;
- `In space` / compatible media-group detection and view normalization such as `Port` → `Port-side`;
- large preview and individual view cards;
- original image downloads only when ZIP creation is requested;
- `Original`, `2048px`, `1280px`, Contact Sheet, and source-manifest exports;
- consistent full filenames;
- local catalog cache, five recent vehicles, and settings in `localStorage`;
- one-click JSON diagnostic export from a hidden background log;
- game-data version and catalog-change tracking using the V001 implementation.

## Quick start

1. Download `sPg_Star_Citizen_Vehicle_Reference_Downloader_V001.html`.
2. Open it in a browser.
3. Select vehicle type, manufacturer, and vehicle, or provide a Wiki URL.
4. Review the detected views.
5. Select export variants.
6. Press **ZIP download**.
7. If something fails, use **Log mentése / Save log** to export the diagnostic JSON.

The app itself needs no Python, Node.js, local server, installer, or build process. Internet access is required for Wiki/API/media requests and for the embedded Google Fonts import.

## Network model

V001 intentionally avoids pre-downloading all vehicle images.

1. **Startup:** catalog and metadata only.
2. **Vehicle selection:** metadata and previews only for that vehicle.
3. **ZIP request:** full-resolution originals only for the selected vehicle.

`All` affects list filtering only; it never triggers bulk image downloads.

## Export naming

ZIP:

`<Full manufacturer> <Vehicle> - Reference Pack.zip`

Image:

`<Full manufacturer> <Vehicle> - <View> - <Image version>.<ext>`

Example:

`Esperia Prowler Utility - Port-side - Original.jpg`

Original files remain byte-identical to the Wiki response. In V001, 2048px and 1280px derivatives are PNG and are downscaled directly from the original only.

## Real V001 evidence

`test-artifacts/09_TEST_Prowler_Utility_manifest.json` is a real runtime manifest extracted from a successfully created V001 reference pack. For Esperia Prowler Utility it proves:

- all 6 `In space` views: Isometric, Above, Port-side, Front, Rear, Below;
- Original: 3840×2160 JPG;
- 2048px: 2048×1152 PNG;
- 1280px: 1280×720 PNG;
- Contact Sheet: 2048×908 PNG;
- `..._in_space_-_Port.jpg` normalized to `Port-side`;
- `game_data_version = 4.10.1-LIVE.12660092`;
- working `media.starcitizen.tools` → CORS/fetch → Blob → local processing → ZIP chain.

**Not proven by this evidence:** the exact `file://` protocol and browser name/version. V001 E2E tests are also still missing for MOLE, Polaris, Carrack, a multi-tab vehicle page, and a ground vehicle.

## Data sources

V001 uses two Wiki layers:

- `https://api.star-citizen.wiki/api` — game-data version, vehicle catalog, search/vehicle metadata;
- `https://starcitizen.tools/api.php` — MediaWiki Action API for page/media discovery with `origin=*`.

See [docs/SPECIFICATION.md](docs/SPECIFICATION.md) and [docs/DATA_SOURCES_AND_LEGAL.md](docs/DATA_SOURCES_AND_LEGAL.md) for exact endpoints, cache behavior, and limitations.

## Privacy

The app has no project-operated backend, account system, or built-in analytics. V001:

- uses `localStorage` for catalog, version, recent-vehicle, and settings cache;
- connects to Star Citizen Wiki APIs and `media.starcitizen.tools`;
- may contact Google Fonts infrastructure because the embedded CSS imports Google Fonts;
- creates the diagnostic log locally and downloads it only on user action.

Details: [PRIVACY.md](PRIVACY.md).

## License and fan-project status

Project-owned source code is released under the **MIT License**, matching the license type used by `DuczaPeter/sPg-salvage-eladasi-ar`.

This is an **unofficial Star Citizen fan tool**, not affiliated with the Cloud Imperium group of companies and not claiming official approval. Star Citizen, Roberts Space Industries, Cloud Imperium, related names, trademarks, and game assets remain the property of their respective rights holders.

The repository **does not redistribute** ship images downloaded from the Wiki. The earlier MOLE visual reference was excluded because it contains Star Citizen/CIG imagery. `assets/ui-topbar-style-reference.png` is the user's own sPg UI style reference and is **not a V001 runtime screenshot**.

The Wiki generally marks its textual content CC BY-SA 4.0, while individual media files may carry file-specific license information plus additional Star Citizen IP restrictions. Wiki API documentation explicitly describes API access for developers, fansite operators, and bots; a separate complete API-specific ToS/rate-limit contract was not reliably identified for this release, so that remains `UNKNOWN / ATTENTION`. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Visual style reference

![sPg top-bar style reference](assets/ui-topbar-style-reference.png)

This image is a screenshot of another user-owned sPg tool and documents the shared sPg design language only. It is **not a runtime screenshot of Vehicle Reference Downloader V001**.

## Release validation

Static release gate:

`python tools/check_release.py`

This does **not** replace browser runtime validation. See [STATUS.md](STATUS.md), [docs/VALIDATION.md](docs/VALIDATION.md), and [docs/ROADMAP.md](docs/ROADMAP.md).

## Documentation

- [STATUS.md](STATUS.md) — current release state;
- [docs/SPECIFICATION.md](docs/SPECIFICATION.md) — functional specification;
- [docs/EXPORT_RULES.md](docs/EXPORT_RULES.md) — normative export and naming rules;
- [docs/DESIGN.md](docs/DESIGN.md) — sPg visual system;
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — components and data flow;
- [docs/DECISIONS.md](docs/DECISIONS.md) — engineering decisions;
- [docs/DATA_SOURCES_AND_LEGAL.md](docs/DATA_SOURCES_AND_LEGAL.md) — sources and legal status;
- [docs/VALIDATION.md](docs/VALIDATION.md) — evidence and test matrix;
- [docs/ROADMAP.md](docs/ROADMAP.md) — V002 order;
- [docs/DEVELOPMENT_HANDOFF.md](docs/DEVELOPMENT_HANDOFF.md) — continuation guide for developers/AIs;
- [docs/RELEASE_STANDARD.md](docs/RELEASE_STANDARD.md) — canonical V4.2 release standard.
