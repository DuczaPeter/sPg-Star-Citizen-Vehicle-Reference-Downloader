# V001 release notes

## Summary

V001 is the first packaged release of the single-file **sPg Star Citizen Vehicle Reference Downloader**.

Main artifact:

`sPg_Star_Citizen_Vehicle_Reference_Downloader_V001.html`

Canonical SHA-256:

`3bb0b10d5794f36346b0752d05aa3bc5dac90d4b21b4318c6b909834b7e4695b`

## Core capabilities

- dynamic spacecraft/ground-vehicle catalog and manufacturer filtering;
- Wiki URL analysis;
- selected-vehicle-only media discovery and previews;
- original images fetched only when creating the ZIP;
- Original / 2048px / 1280px / Contact Sheet / source manifest export;
- deterministic full manufacturer + vehicle + view + image-version filenames;
- local cache and recent-vehicle state;
- diagnostic JSON export;
- game-data version/catalog change tracking.

## Validation state

**Package status:** `STATICALLY VERIFIED ONLY`

A real Esperia Prowler Utility V001 run is `RUNTIME VERIFIED + PASS` for the media → Blob → ZIP chain. Exact `file://` protocol and browser/version were not captured and remain the required browser/runtime evidence blocker.

The following E2E vehicle classes are not yet verified: MOLE, Polaris, Carrack, multi-tab vehicle page, and ground vehicle.

## Legal/asset policy

No downloaded Star Citizen Wiki ship/vehicle images are bundled. The repository includes only the user's own sPg UI style reference and metadata-only runtime evidence.

## Known V001 deviations

See `docs/VALIDATION.md` and `docs/ROADMAP.md`.

## Publication

Repository publication is manual. The published repository remains `BLOCKED` until clean-clone release-gate and checksum parity verification is completed after upload.
