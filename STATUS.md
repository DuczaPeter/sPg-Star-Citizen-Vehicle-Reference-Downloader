# Status

**Project:** sPg Star Citizen Vehicle Reference Downloader  
**Current version:** V001  
**Main artifact:** `sPg_Star_Citizen_Vehicle_Reference_Downloader_V001.html`  
**Canonical SHA-256:** `3bb0b10d5794f36346b0752d05aa3bc5dac90d4b21b4318c6b909834b7e4695b`  
**Release standard:** V4.2  
**Repository publication:** MANUAL BY USER

## Current package status

`STATICALLY VERIFIED ONLY`

Meaning: the release package passes its static/integrity/documentation gates and includes a real Prowler Utility runtime PASS for the media → Blob → ZIP path, but the exact required `file://` execution protocol and browser/version are still NOT VERIFIED. Under the project release contract this keeps the browser/runtime gate BLOCKED.

## Published release status

`BLOCKED`

Reason: the repository has not yet been manually published and therefore PUBLISHED REPOSITORY PARITY is NOT VERIFIED/BLOCKED. In addition, the exact `file://` browser evidence remains open.

## Latest runtime evidence

`test-artifacts/09_TEST_Prowler_Utility_manifest.json`

Evidence: RUNTIME VERIFIED + PASS for Esperia Prowler Utility media → Blob → local resize/contact sheet → ZIP.

`game_data_version`: `4.10.1-LIVE.12660092`

## ATTENTION / UNKNOWN

- exact protocol (`file://` or otherwise) used in the successful Prowler run: UNKNOWN;
- browser name/version for that run: UNKNOWN;
- dedicated complete Star Citizen Wiki API-specific ToS/rate-limit contract: UNKNOWN / ATTENTION;
- applicability of RSI's “site URL/domain” naming guidance to a GitHub repository slug: UNKNOWN / ATTENTION;
- PNG derivatives are large: in the observed Prowler package they represented about 84.9% of unpacked payload bytes.

## NOT VERIFIED

- MOLE E2E;
- Polaris E2E;
- Carrack E2E;
- multi-tab vehicle page E2E;
- ground vehicle E2E.

## Next task

Collect the next normal-use diagnostic JSON to close protocol + browser/version evidence, then continue the V002 sequence in `docs/VALIDATION.md` / `docs/ROADMAP.md`.

Tasks that change the V001 code require a new development scope; this release packaging intentionally keeps the application byte-identical.
