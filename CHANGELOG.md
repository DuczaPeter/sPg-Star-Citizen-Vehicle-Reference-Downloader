# Changelog

All notable project changes are documented here.

## V001 — initial packaged release

### Added

- single-file Star Citizen vehicle reference downloader;
- dynamic vehicle/manufacturer catalog workflow;
- Wiki URL analysis path;
- preview/media detection;
- Original, 2048px, 1280px, Contact Sheet, and source-manifest ZIP output;
- deterministic full-name/view/version image naming;
- local catalog/version/recent/settings storage;
- diagnostic JSON export;
- game-data version and catalog-change tracking;
- professional GitHub release documentation and static release gate.

### Validation

- canonical source hash bound and byte-parity checked;
- real Esperia Prowler Utility runtime manifest preserved under `test-artifacts/`;
- media → Blob → local image processing → ZIP path: runtime PASS for that vehicle;
- exact `file://` protocol and browser/version remain NOT VERIFIED;
- MOLE, Polaris, Carrack, multi-tab vehicle, and ground-vehicle E2E cases remain NOT VERIFIED.

### Known V001 deviations

See `docs/SPECIFICATION.md`, `docs/EXPORT_RULES.md`, `docs/VALIDATION.md`, and `docs/ROADMAP.md`.
