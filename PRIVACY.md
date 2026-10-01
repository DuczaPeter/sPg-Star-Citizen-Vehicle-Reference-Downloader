# Privacy

## Summary

V001 is a client-side, single-file browser application. The project does not operate its own backend, login service, analytics service, or telemetry collector.

## Local browser storage

V001 uses `localStorage` for:

- `spg_sc_vehicle_ref_catalog_v1`
- `spg_sc_vehicle_ref_version_v1`
- `spg_sc_vehicle_ref_version_history_v1`
- `spg_sc_vehicle_ref_recent_v1`
- `spg_sc_vehicle_ref_settings_v1`

These values are used for catalog/version caching, recent vehicle selection, and local settings.

The **Cache törlése / Clear cache** action removes this application's local cache keys. It does not delete previously downloaded ZIP files.

## Network requests

While online, V001 may connect to:

- `api.star-citizen.wiki`
- `starcitizen.tools`
- `media.starcitizen.tools`
- `fonts.googleapis.com` and the related Google Fonts delivery infrastructure

The first three are required for live Wiki/API/media functionality. Google Fonts requests are caused by the embedded CSS `@import`.

As with ordinary web requests, those external providers can receive network-level information such as IP address, browser request headers, and request timing under their own policies. This project does not proxy those requests through a project-operated backend.

## Diagnostics

The app keeps an in-memory diagnostic event history and can export a JSON file only when the user presses **Log mentése**.

The diagnostic export is designed to contain:

- app version and timestamp;
- browser user agent, language, online state, protocol, and page URL without fragment;
- game-data/catalog state;
- selected vehicle and Wiki information;
- relevant request/result/error events.

It is not intended to contain image bytes, cookies, authentication tokens, or API keys. Before sharing a diagnostic file publicly, users should still review it because browser/environment information may be personally identifying in some contexts.

## Cookies, accounts, analytics

V001 itself does not intentionally create an account, send project analytics, or use a project-owned cookie/backend system.

Third-party endpoints may have their own browser/network behavior and privacy policies.

## Local files

Generated ZIPs and diagnostic JSON files are downloaded through the browser and remain under the user's control. The project does not upload those generated files to a project backend.
