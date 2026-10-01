# Restart package → GitHub repository map

This map proves where the information from the original 00–09 restart package was integrated, without keeping duplicate legacy documents in the public repository.

| Original restart artifact | Repository destination |
|---|---|
| `00_START_HERE.md` | `README.md`, `AGENTS.md`, `docs/DEVELOPMENT_HANDOFF.md` |
| `01_SPEC.md` | `docs/SPECIFICATION.md` |
| `02_EXPORT_RULES.md` | `docs/EXPORT_RULES.md` |
| `03_DESIGN.md` | `docs/DESIGN.md` |
| `04_DECISIONS.md` | `docs/DECISIONS.md` |
| `05_STATUS_AND_ROADMAP.md` | `docs/VALIDATION.md`, with current summary in `STATUS.md`; `docs/ROADMAP.md` points to the authoritative roadmap section |
| `06_SOURCE_sPg_Star_Citizen_Vehicle_Reference_Downloader_V001.html` | root `sPg_Star_Citizen_Vehicle_Reference_Downloader_V001.html`, byte-identical |
| `07_STYLE.css` | not shipped separately; it is already embedded into the single-file artifact; design variables/hash are documented in `docs/DESIGN.md` |
| `08_IMAGE_01_MOLE_views.png` | excluded for visual-IP cleanliness; textual description retained in `docs/DESIGN.md` and `docs/DATA_SOURCES_AND_LEGAL.md` |
| `08_IMAGE_02_felso_menu_minta.png` | `assets/ui-topbar-style-reference.png`, byte-identical |
| `09_TEST_Prowler_Utility_manifest.json` | `test-artifacts/09_TEST_Prowler_Utility_manifest.json`, byte-identical |

No restart-package content necessary to understand V001 was intentionally discarded.
