# AGENTS.md

## Project goal

Maintain and improve **sPg Star Citizen Vehicle Reference Downloader** without breaking its single-file architecture or losing evidence/provenance.

## Canonical baseline

- version: V001
- main artifact: `sPg_Star_Citizen_Vehicle_Reference_Downloader_V001.html`
- canonical SHA-256: `3bb0b10d5794f36346b0752d05aa3bc5dac90d4b21b4318c6b909834b7e4695b`

## Authoritative files

Read in this order for normal development:

1. `STATUS.md`
2. `docs/SPECIFICATION.md`
3. `docs/EXPORT_RULES.md`
4. `docs/DECISIONS.md`
5. `docs/ARCHITECTURE.md`
6. `docs/VALIDATION.md`
7. `docs/ROADMAP.md`

For full GitHub release or release-package work, use:

`docs/RELEASE_STANDARD.md`

Do not load or apply the full release workflow during ordinary development tasks.

If a dedicated release skill is available, it may assist execution, but the project-local `docs/RELEASE_STANDARD.md` remains the authoritative persistent release standard unless the user's current instruction explicitly overrides it.

## Critical invariants

- V001 is a single-file HTML app.
- Do not split runtime CSS, JS, data, or ZIP logic into required sidecar files merely for repository aesthetics.
- Do not modify/reformat the canonical V001 artifact unless the task explicitly changes the program.
- Original source images must remain byte-identical in exported `Original/`.
- 2048px/1280px derivatives are downscales from Original, never from each other.
- No upscale or AI-upscale.
- Every exported image filename contains full manufacturer + vehicle + view + image version.
- `Mind` means list filtering only, never bulk image fetch.
- Original media is fetched only for the selected vehicle and only at ZIP time.
- Do not silently substitute thumbnails for unavailable originals.
- Do not invent missing API/media facts.
- Do not commit downloaded Star Citizen ship/vehicle images without explicit legal review/approval.

## Source precedence

See `docs/DATA_SOURCES_AND_LEGAL.md`.

## Storage/cache policy

Browser `localStorage` is used for catalog/version/history/recent/settings. Do not replace dynamic source discovery with hardcoded current values.

## Testing policy

Static checks are not runtime evidence.

Run:

`python tools/check_release.py`

For changes touching DOM, browser storage, network/CORS, image processing, download behavior, or ZIP generation, perform targeted browser/runtime validation and retain non-sensitive evidence.

Current real runtime evidence: `test-artifacts/09_TEST_Prowler_Utility_manifest.json`.

## Release gates

Gate definitions are fixed in `docs/RELEASE_CONTRACT.md`. Do not downgrade a failing/unknown required gate to optional merely to improve the status label.

## Forbidden regressions

- main artifact ceases to be single-file;
- eager all-vehicle image downloading;
- filename guessing replacing Wiki media discovery;
- Original bytes re-encoded;
- chained derivative resizing;
- AI-generated detail/upscale presented as source reference;
- source/media legal uncertainty hidden;
- fake/mock UI image represented as a runtime screenshot;
- runtime PASS claimed from static checks.

## Documentation rule

If behavior changes, update the relevant normative docs, STATUS, validation evidence, and CHANGELOG in the same change.
