# Release process

## Local package gate

Run from repository root:

`python tools/check_release.py`

This verifies repository structure, byte-bound artifacts, inventory/checksums, key static invariants, JSON readability, duplicate HTML IDs, single-file markers, secret-pattern checks, and release documentation.

If Node.js is available, the checker additionally extracts the embedded V001 JavaScript to a temporary file and runs `node --check`. Absence of Node does not turn that optional syntax subcheck into runtime evidence.

## Runtime evidence

The static gate does not prove browser behavior.

Current runtime evidence:

- Esperia Prowler Utility media → Blob → resize/contact sheet → ZIP: PASS.
- exact `file://` protocol and browser/version: NOT VERIFIED.

The next normal-use diagnostic export can close those two missing environment facts.

## Manual GitHub publication

Repository publication is `MANUAL BY USER`.

After upload:

1. create a clean directory outside the release-working tree;
2. clone the actually published repository;
3. check out the intended release tag/branch;
4. run `python tools/check_release.py`;
5. verify `CHECKSUMS.sha256`;
6. verify the main artifact hash equals the canonical V001 hash;
7. verify `docs/RELEASE_STANDARD.md` hash;
8. verify dotfiles and `.github/` are present;
9. inspect relative README/docs links;
10. ensure `git status --porcelain` is empty.

Example:

```text
git clone <PUBLISHED_REPOSITORY_URL> spg-vehicle-release-verify
cd spg-vehicle-release-verify
git checkout <V001_TAG_OR_COMMIT>
python tools/check_release.py
git status --porcelain
```

The fresh clone must report the same release-gate results as the package.

## Published status rule

Until manual publication and fresh-clone parity:

- `PUBLISHED REPOSITORY PARITY = NOT VERIFIED / BLOCKED`
- `PUBLISHED RELEASE STATUS = BLOCKED`

Even after parity passes, the release status must be recalculated; the open exact `file://` browser-runtime evidence cannot be silently upgraded by repository parity alone.
