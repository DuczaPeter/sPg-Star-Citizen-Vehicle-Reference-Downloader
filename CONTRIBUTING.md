# Contributing

## Baseline first

Before changing code, read:

1. `AGENTS.md`
2. `STATUS.md`
3. `docs/SPECIFICATION.md`
4. `docs/EXPORT_RULES.md`
5. `docs/DECISIONS.md`

Canonical V001 artifact:

`sPg_Star_Citizen_Vehicle_Reference_Downloader_V001.html`

Canonical SHA-256:

`3bb0b10d5794f36346b0752d05aa3bc5dac90d4b21b4318c6b909834b7e4695b`

Do not reformat, normalize, split, or rewrite the HTML incidentally. V001 is a single-file application.

## Change scope

Keep changes targeted. Avoid unrelated refactors, file renames, design rewrites, or data-source substitutions.

For code changes:

- state the problem and intended behavior;
- identify affected invariants;
- add or update a targeted regression check;
- update docs that describe changed behavior;
- run `python tools/check_release.py`;
- perform browser/runtime testing when browser behavior, storage, DOM, networking, image processing, or downloads are affected.

## Runtime evidence

Static checks are not runtime proof.

For browser failures, attach the app's diagnostic JSON when safe to do so. Remove personal information before posting publicly.

## External media

Do not commit downloaded Star Citizen Wiki ship/vehicle images unless their redistribution rights have been independently reviewed and explicitly approved for the repository. Current policy is to keep such images out.

## Pull requests

A PR should include:

- scope;
- expected behavior;
- tests performed;
- evidence level;
- known limitations;
- whether the main artifact hash is intentionally changed;
- documentation updates.
