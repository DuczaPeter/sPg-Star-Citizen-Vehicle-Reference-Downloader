# Third-party notices

This document records third-party services, content, and legal status relevant to V001. It is documentation, not legal advice.

## Star Citizen Wiki

Verified public references:

- General disclaimer: https://starcitizen.tools/Star_Citizen_Wiki:General_disclaimer
- API overview: https://starcitizen.tools/Star_Citizen_Wiki:Application_programming_interface

**Service:** Star Citizen Wiki / starcitizen.tools  
**Use in V001:** runtime vehicle/media discovery, MediaWiki Action API, links to original media.  
**Bundled data/media:** none, except the user-provided runtime manifest in `test-artifacts/`, which contains source URLs and metadata but no image bytes.

The Wiki's general disclaimer states that Wiki information is made available under the Creative Commons Attribution-ShareAlike 4.0 International license (CC BY-SA 4.0), while trademarks and other protected material remain with their owners. Individual media pages can carry their own license notice and may also state that additional restrictions apply when Star Citizen intellectual property is present.

**Repository decision:** do not redistribute Star Citizen Wiki ship/vehicle media files in this repository.

**API usage:** the Wiki's API documentation explicitly describes APIs as interfaces used by developers, fansite operators, and bots to retrieve game/Wiki information.

**API-specific Terms/rate-limit status:** `UNKNOWN / ATTENTION`. A separate, complete, authoritative API-specific Terms of Service/rate-limit contract was not identified during this release audit. The repository therefore does not claim broader permission or guarantees beyond the public API documentation actually located.

## Cloud Imperium / Roberts Space Industries / Star Citizen

Verified public references:

- Fan kit and fandom FAQ: https://support.robertsspaceindustries.com/hc/en-us/articles/360006895793-Star-Citizen-Fankit-and-Fandom-FAQ
- Terms of Service: https://robertsspaceindustries.com/tos

This is an unofficial fan tool. RSI's current fan guidance requires fan activities to avoid implying official affiliation or endorsement and provides a specific notice for fan sites. The repository therefore includes prominent unofficial/fan notices and does not redistribute the downloaded ship images used at runtime.

Because the project name contains “Star Citizen”, repository/domain naming should be reviewed before publication. RSI's fan-site guidance warns against using official brands/marks in a site URL/domain. Whether that guidance applies identically to a GitHub repository slug is `UNKNOWN`; a neutral repository slug such as `spg-vehicle-reference-downloader` is the conservative choice while retaining the descriptive project title in the README.

## Google Fonts

The embedded CSS requests:

- Orbitron
- Roboto

from `fonts.googleapis.com` / Google Fonts when network access is available.

Google Fonts metadata identifies the families as OFL-licensed fonts. No font files are redistributed in this repository; they are requested at runtime by the browser.

Privacy impact is documented in `PRIVACY.md`.

## MIT License source

The project license type was selected to match the existing repository:

`DuczaPeter/sPg-salvage-eladasi-ar`

Its `LICENSE` file is MIT. This project uses the same MIT license terms with a project-specific copyright line.
