# Development / AI handoff

This file replaces the restart package's old `00_START_HERE.md` role inside the GitHub repository.

## Read order

1. `README.md` (or `README.en.md`)
2. `AGENTS.md`
3. `STATUS.md`
4. `docs/SPECIFICATION.md`
5. `docs/EXPORT_RULES.md`
6. `docs/DECISIONS.md`
7. `docs/ARCHITECTURE.md`
8. `docs/VALIDATION.md`
9. `docs/ROADMAP.md`
10. `docs/DATA_SOURCES_AND_LEGAL.md`
11. `test-artifacts/09_TEST_Prowler_Utility_manifest.json`
12. `sPg_Star_Citizen_Vehicle_Reference_Downloader_V001.html` only after the documentation establishes the contract

For full GitHub release work also read:

`docs/RELEASE_STANDARD.md`

## Canonical facts

- Project: sPg Star Citizen Vehicle Reference Downloader
- Version: V001
- Main artifact: `sPg_Star_Citizen_Vehicle_Reference_Downloader_V001.html`
- Canonical SHA-256: `3bb0b10d5794f36346b0752d05aa3bc5dac90d4b21b4318c6b909834b7e4695b`
- Architecture: single-file HTML
- Runtime code may not be split merely for repository aesthetics.
- Current package status: `STATICALLY VERIFIED ONLY`
- Current published release status before manual publication/parity: `BLOCKED`


## Source priority

If sources conflict:

1. **Actual V001 behavior:** `sPg_Star_Citizen_Vehicle_Reference_Downloader_V001.html` is the primary code evidence.
2. **Actual V001 export output:** `test-artifacts/09_TEST_Prowler_Utility_manifest.json` is real Prowler runtime/export evidence, not a synthetic example.
3. **Desired target behavior:** `docs/SPECIFICATION.md` and `docs/EXPORT_RULES.md`.
4. **Visual target:** `docs/DESIGN.md` plus `assets/ui-topbar-style-reference.png`; historical CSS is embedded in the main artifact.
5. **Accepted engineering decisions:** `docs/DECISIONS.md`.
6. **Next work:** `STATUS.md` and `docs/VALIDATION.md` / `docs/ROADMAP.md`.

`[ELTÉR A TERVTŐL]` and `[BIZONYTALAN]` labels are deliberate. Do not erase them by assumption.

## Continuation prompt

Copy/paste this into a new AI session:

> You are continuing the sPg Star Citizen Vehicle Reference Downloader project from an existing repository with no prior conversation context. First read README.md, AGENTS.md, STATUS.md, docs/SPECIFICATION.md, docs/EXPORT_RULES.md, docs/DECISIONS.md, docs/ARCHITECTURE.md, docs/VALIDATION.md, docs/ROADMAP.md, docs/DATA_SOURCES_AND_LEGAL.md, and test-artifacts/09_TEST_Prowler_Utility_manifest.json. The canonical V001 main artifact is `sPg_Star_Citizen_Vehicle_Reference_Downloader_V001.html` and its required SHA-256 is `3bb0b10d5794f36346b0752d05aa3bc5dac90d4b21b4318c6b909834b7e4695b`. Do not modify, reformat, split, or renormalize the V001 HTML unless the requested task explicitly changes the program. Preserve the single-file architecture. Treat the Prowler manifest as real runtime evidence for media→Blob→ZIP, but do not claim the exact file:// protocol or browser/version is verified until a diagnostic log proves it. Do not add downloaded Star Citizen Wiki ship images to the repository without a separate legal review. For full release/package work, read and apply docs/RELEASE_STANDARD.md. Before changing code, state scope, do-not-touch items, required gates, acceptance criteria, targeted tests, and stop condition. Continue from STATUS.md and docs/ROADMAP.md rather than inventing missing project history. On first intake, do not modify code: briefly reconstruct the program goal, what V001 actually proves, known deviations, and the safest next step, then wait for the user's concrete implementation instruction.
