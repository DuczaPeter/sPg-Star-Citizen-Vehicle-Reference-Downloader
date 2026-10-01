# Security policy

## Supported version

The current supported release in this package is V001.

## Reporting

Please report security-sensitive issues privately to the repository owner before publishing exploit details. Do not post secrets, tokens, private diagnostic logs, or personally identifying information in a public issue.

## Relevant security boundaries

V001 is a local single-file browser tool that performs cross-origin reads from public Wiki/API/media endpoints and writes downloadable ZIP/JSON artifacts through browser APIs.

Security-relevant areas include:

- unsafe handling of remote API/media content;
- filename/path traversal in generated ZIP entries;
- unexpected HTML/script injection from external data;
- credential or token leakage into diagnostics;
- dependency/source-domain substitution;
- malicious or misleading external URLs;
- release package tampering or baseline hash mismatch.

## Secrets

The project does not require API keys or credentials for the documented Wiki endpoints. The release gate scans for common secret patterns, but this is not a substitute for human review.

## Integrity

The canonical V001 main artifact is hash-bound. See `STATUS.md` and `CHECKSUMS.sha256`.

A main-artifact SHA-256 mismatch must be treated as a release failure, not automatically accepted as a harmless formatting change.
