# FINAL REPORT — sPg Star Citizen Vehicle Reference Downloader V001

## RELEASE VERSION

`V001`

## STANDARD VERSION

`V4.2`

Canonical project copy:

`docs/RELEASE_STANDARD.md`

SHA-256:

`f3b1358844a9f04da5ea8bfd6fe87b3051bd052e753bd8451991b39f894972b2`

## CANONICAL BASELINE

Expected SHA-256:

`3bb0b10d5794f36346b0752d05aa3bc5dac90d4b21b4318c6b909834b7e4695b`

## MAIN ARTIFACT

`sPg_Star_Citizen_Vehicle_Reference_Downloader_V001.html`

Packaged SHA-256:

`3bb0b10d5794f36346b0752d05aa3bc5dac90d4b21b4318c6b909834b7e4695b`

**MATCH: YES**

The release packaging does not modify the V001 program.

## RELEASE CONTRACT

See `docs/RELEASE_CONTRACT.md`.

Repository publication:

`MANUAL BY USER`

## EVIDENCE

**Source:** `SOURCE VERIFIED`

**Static:** `STATIC VERIFIED`

**Runtime:** `RUNTIME VERIFIED` for the proven Esperia Prowler Utility media → Blob → local processing → ZIP scope; `NOT VERIFIED` for the exact `file://` protocol and browser/version.

**Integration:** `NOT VERIFIED` as a separate evidence class. The available Prowler evidence is intentionally not upgraded beyond the user's stated runtime proof.

## TEST RESULT SUMMARY

**PASS**

- canonical baseline hash;
- main-artifact byte parity;
- single-file static structure;
- JavaScript static syntax check in the release build environment;
- credential/secret cleanliness heuristic;
- MIT project-license resolution;
- version consistency;
- release-standard byte parity;
- Prowler evidence-manifest byte parity;
- Prowler 6-view metadata;
- Prowler media → Blob → ZIP runtime chain;
- Prowler `Port` → `Port-side` normalization;
- public package visual-IP exclusion;
- inventory/checksum parity.

**EMPTY:** none.

**UNKNOWN**

- exact protocol used in the successful Prowler run (`file://` not proven);
- browser name/version used in that run;
- separate complete Star Citizen Wiki API-specific Terms/rate-limit contract;
- exact applicability of RSI fan-site URL/domain naming guidance to a GitHub repository slug.

**ATTENTION**

- Prowler PNG derivatives represented about 84.9% of the observed unpacked payload bytes;
- Wiki API public developer/fansite/bot usage documentation was found, but no separate full API-specific Terms/rate-limit contract was independently located.

**FAIL:** none.

**ERROR:** none.

## GATE SUMMARY — PACKAGE SCOPE

**REQUIRED DONE:** 13

**REQUIRED N/A:** 0

**REQUIRED BLOCKED:** 1

Blocked package gate:

`DIRECT file:// BROWSER RUNTIME EVIDENCE`

Reason: the real Prowler run proves the media → Blob → ZIP path, but its exact protocol and browser/version were not captured.

**OPTIONAL DONE:** 0

**OPTIONAL N/A:** 0

**OPTIONAL BLOCKED:** 3

- additional E2E vehicles;
- dedicated API-specific Terms/rate-limit contract;
- dedicated social-preview asset.

## PACKAGE STATUS

`STATICALLY VERIFIED ONLY`

`BLOCKED subtype: missing required runtime/browser evidence`

This status is deterministic under the V4.2 release standard because the only REQUIRED local-package blocker is the missing exact browser/runtime environment proof.

## PUBLISHED REPOSITORY PARITY

**Evidence:** `NOT VERIFIED`

**Gate status:** `BLOCKED`

**Reason:** manual GitHub publication has not happened yet.

## PUBLISHED RELEASE STATUS

`BLOCKED`

Manual publication and post-publish fresh-clone parity are pending. In addition, the exact `file://` browser/runtime evidence remains open and must be resolved before a clean READY classification is possible.

## Known limitations

- `file://` protocol and browser/version remain unproven for the successful Prowler run.
- MOLE, Polaris, Carrack, multi-tab vehicle, and ground-vehicle E2E cases are not verified.
- V001 generates PNG derivatives that can be much larger than source JPGs; JPEG/PNG selection remains a V002 decision.
- V001 has documented deviations in manifest naming, URL back-population, explicit Original-unavailable state, version-badge separation, X/Y/ZIP-size display, periodic checks, changelog use, and strict media exclusion.
- Separate complete Wiki API-specific Terms/rate-limit contract remains UNKNOWN/ATTENTION.

## DEVIATIONS

- V001 code was explicitly kept byte-identical.
- The historical MOLE screenshot was excluded because it contains Star Citizen/CIG visual material.
- No fake/mock V001 screenshot was generated.
- A dedicated social preview was omitted instead of presenting a mockup as product evidence.
- Repository publication is manual, so published parity cannot be completed inside this package-generation run.

## Important changes in this release package

The application itself did not change. Added around it:

- full Hungarian and equivalent English README;
- release contract and current status;
- architecture, user, data-source/legal, validation, roadmap, and handoff documentation;
- MIT license and legal/privacy/security notices;
- GitHub issue/PR templates and static CI release gate;
- package manifest, inventory, checksums, and deterministic line-ending/byte-exact policy;
- real Prowler runtime manifest under `test-artifacts/`;
- user-owned sPg topbar screenshot as a clearly labelled design reference.

## Documentation status

Complete for the V001 package scope. The original 00–05 restart-package knowledge is mapped into the repository without maintaining duplicate legacy documents. See `docs/ORIGINAL_RESTART_PACKAGE_MAP.md`.

## Visual artifacts

Included:

`assets/ui-topbar-style-reference.png`

Classification: user-owned sPg design reference; not V001 runtime evidence.

Excluded:

`08_IMAGE_01_MOLE_views.png`

Reason: contains Star Citizen/CIG ship imagery. A text description remains in documentation.

## License status

`RESOLVED — MIT`

The license type matches `DuczaPeter/sPg-salvage-eladasi-ar`.

## Third-party status

- Star Citizen Wiki general content license: source-verified CC BY-SA 4.0 statement.
- Individual Wiki media: file-specific licensing can include additional Star Citizen IP restrictions; not redistributed here.
- Wiki API: public use documentation source-verified; separate complete API-specific Terms/rate-limit contract UNKNOWN/ATTENTION.
- Google Fonts: runtime external dependency for Orbitron/Roboto; no font files redistributed.
- CIG/RSI: unofficial fan/trademark disclaimer included; downloaded game imagery excluded.

## Repository publication and post-publish verification

After manual upload, use a clean directory:

```text
git clone <PUBLISHED_REPOSITORY_URL> spg-vehicle-release-verify
cd spg-vehicle-release-verify
git checkout <V001_TAG_OR_COMMIT>
python tools/check_release.py
git status --porcelain
```

Then confirm:

1. release gate PASS for all static/package checks;
2. main artifact SHA-256 equals `3bb0b10d5794f36346b0752d05aa3bc5dac90d4b21b4318c6b909834b7e4695b`;
3. `docs/RELEASE_STANDARD.md` SHA-256 equals `f3b1358844a9f04da5ea8bfd6fe87b3051bd052e753bd8451991b39f894972b2`;
4. inventory/checksum parity passes;
5. `.github/`, `.gitattributes`, `.gitignore` are present;
6. README/docs relative links resolve;
7. fresh-clone working tree is clean.

Only after this should `PUBLISHED REPOSITORY PARITY` be recalculated.

## CHECKSUM

Repository file checksums are in:

`CHECKSUMS.sha256`

The GitHub release ZIP SHA-256 is generated only after the ZIP itself is created and is reported in the external handoff copy of this Final Report, because a ZIP cannot contain a stable hash of itself.

## ZIP / PACKAGE

The repository package is generated as:

`sPg_Star_Citizen_Vehicle_Reference_Downloader_V001_GitHub_Release.zip`
