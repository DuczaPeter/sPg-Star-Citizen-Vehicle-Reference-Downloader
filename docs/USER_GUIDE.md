# User guide

## Start

Open the V001 HTML in a browser. The intended product requirement is direct local use without a local server, Python, Node.js, installation, or build step.

The successful Prowler runtime evidence did not capture whether that run was actually `file://`, so exact protocol compatibility is still an open release evidence item.

## Top bar

The application presents:

- language selector (`Magyar` in V001);
- **Adatok frissítése**;
- **Log mentése**;
- **Cache törlése**;
- status badges for Wiki/API/version/catalog/network behavior.

## Selecting a vehicle

### By dropdown

1. Choose **Mind**, **Hajók**, or **Földi járművek**.
2. Choose the manufacturer.
3. Choose the vehicle.
4. V001 resolves the vehicle and loads its media metadata/previews.

`Mind` never means bulk download.

### By Wiki URL

Paste a Star Citizen Wiki URL and use the analysis action. The URL path and dropdown path feed the same internal selected-vehicle/media flow.

Known V001 deviation: selecting from dropdown does not fully back-populate the visible Wiki URL field as originally planned. This is V002 item **b**.

## Preview

The preferred large preview is Isometric when available; otherwise V001 can use another found view.

The page shows detected media/view cards. V001 normalizes known names such as `Port` to `Port-side`.

Known V001 deviation: explicit X/Y count and estimated ZIP size are still planned for V002.

## Export

Available options in V001:

- Original;
- 2048px;
- 1280px;
- Contact Sheet;
- source manifest.

Original files retain source bytes/format. 2048px and 1280px variants are PNG in V001 and are generated directly from Original.

The source manifest V001 filename differs from the planned `_source.json`; this is V002 item **a**.

## Diagnostics

Use **Log mentése** after a problem or useful validation run.

V001 names diagnostic files in a form similar to:

`sPg SC Vehicle Reference Downloader - <Vehicle> - Diagnostic - <timestamp>.json`

The next normal-use diagnostic should be retained so the currently UNKNOWN exact protocol and browser/version can be proven without a separate dedicated test.

## Cache

**Cache törlése** removes the app's local catalog/version/recent/settings state. It does not delete browser-downloaded ZIPs.

## Current test coverage

Verified runtime vehicle:

- Esperia Prowler Utility — PASS for six In-space views and media→Blob→ZIP.

Not yet E2E verified:

- MOLE;
- Polaris;
- Carrack;
- multi-tab vehicle page;
- ground vehicle.
