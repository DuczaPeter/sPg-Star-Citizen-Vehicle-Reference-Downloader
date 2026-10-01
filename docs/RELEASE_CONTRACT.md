# Release Contract — V001 GitHub package

**Standard:** V4.2  
**Contract scope:** professional GitHub release package for V001

| Field | Decision |
|---|---|
| PROJECT TYPE | Single-file client-side web application |
| PRIMARY LANGUAGE | Hungarian; equivalent English README required |
| CANONICAL BASELINE | V001 SHA-256 `3bb0b10d5794f36346b0752d05aa3bc5dac90d4b21b4318c6b909834b7e4695b` |
| MAIN ARTIFACT | `sPg_Star_Citizen_Vehicle_Reference_Downloader_V001.html` |
| TARGET VERSION | V001 |
| PUBLIC RELEASE | YES |
| RUNTIME VALIDATION REQUIRED | YES — browser APIs, CORS/media fetching, localStorage and download behavior are core functionality |
| PACKAGE / ZIP REQUIRED | YES |
| REPOSITORY PUBLICATION | MANUAL BY USER |
| LICENSE STATUS | RESOLVED — MIT, matching `DuczaPeter/sPg-salvage-eladasi-ar` license type |
| RELEVANT VISUAL ASSETS | user's own sPg topbar reference; no CIG ship image redistribution |
| RELEASE STANDARD | `docs/RELEASE_STANDARD.md`, byte-identical V4.2 copy |

## Required gates fixed before work

1. Canonical baseline identified.
2. Main artifact identified.
3. Static validation.
4. Credential / secret cleanliness.
5. License status resolved.
6. Version consistency.
7. Baseline byte parity.
8. Single-file parity.
9. Package/inventory/checksum validation.
10. Documentation and HU/EN README parity.
11. Privacy/security documentation.
12. Visual legal cleanliness.
13. Core runtime media → Blob → ZIP evidence.
14. Direct-local browser runtime evidence for the required `file://` product contract.
15. Published repository parity after manual upload.

## Optional / non-blocking evidence

- MOLE E2E;
- Polaris E2E;
- Carrack E2E;
- multi-tab vehicle E2E;
- ground-vehicle E2E;
- dedicated social-preview image;
- V002 changelog endpoint validation.

## Legal/source limitations

- Star Citizen Wiki ship images are not bundled.
- The historical MOLE screenshot is excluded because it contains game imagery.
- Wiki general content licensing and individual-media caveats are documented.
- Public Wiki API developer/fansite/bot use is documented by the source.
- Separate complete API-specific Terms/rate-limit contract remains `UNKNOWN / ATTENTION`.
- RSI fan/trademark disclaimer is included.
- Applicability of RSI site-URL naming guidance to a GitHub repository slug remains `UNKNOWN / ATTENTION`.

## Deviations

- No V001 code modification is allowed for this release.
- No fake or generated UI screenshot is used.
- Repository publication and post-publish parity are explicitly deferred to the user; the published release cannot be READY before fresh-clone verification.
- Social preview is omitted rather than manufacturing a fake V001 UI visual. The repository retains a real user-owned sPg style reference and clear labeling.

Gate classifications in this contract must not be weakened merely to improve the release label.
