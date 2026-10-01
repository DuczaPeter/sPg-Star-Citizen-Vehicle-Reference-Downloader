#!/usr/bin/env python3
"""Static release gate for sPg Star Citizen Vehicle Reference Downloader V001.

This script intentionally performs STATIC/package validation only.
It must never be described as browser/runtime evidence.
"""
from __future__ import annotations

import hashlib
import html.parser
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "sPg_Star_Citizen_Vehicle_Reference_Downloader_V001.html"
STANDARD = ROOT / "docs" / "RELEASE_STANDARD.md"
EVIDENCE = ROOT / "test-artifacts" / "09_TEST_Prowler_Utility_manifest.json"

EXPECTED_MAIN_SHA = "3bb0b10d5794f36346b0752d05aa3bc5dac90d4b21b4318c6b909834b7e4695b"
EXPECTED_STANDARD_SHA = "f3b1358844a9f04da5ea8bfd6fe87b3051bd052e753bd8451991b39f894972b2"
EXPECTED_EVIDENCE_SHA = "8d1e93de466741c4687478b403be85fa1193f771e5ed919023a067ed0611d4f9"
EXPECTED_STYLE_REF_SHA = "503ca894ab54706cfbd8bd497e57004507c7f4b050083f9f666cd4c9f55fb05a"

errors: list[str] = []
warnings: list[str] = []
passes: list[str] = []

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def ok(msg: str) -> None:
    passes.append(msg)

def fail(msg: str) -> None:
    errors.append(msg)

def warn(msg: str) -> None:
    warnings.append(msg)

required = [
    "README.md",
    "README.en.md",
    "AGENTS.md",
    "STATUS.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "PRIVACY.md",
    "LICENSE",
    "NOTICE.md",
    "THIRD_PARTY_NOTICES.md",
    "VERSION.json",
    "PACKAGE-MANIFEST.json",
    "FILE-INVENTORY.json",
    "CHECKSUMS.sha256",
    ".gitattributes",
    ".gitignore",
    "sPg_Star_Citizen_Vehicle_Reference_Downloader_V001.html",
    "docs/RELEASE_STANDARD.md",
    "docs/RELEASE_CONTRACT.md",
    "docs/SPECIFICATION.md",
    "docs/EXPORT_RULES.md",
    "docs/DESIGN.md",
    "docs/DECISIONS.md",
    "docs/ARCHITECTURE.md",
    "docs/DATA_SOURCES_AND_LEGAL.md",
    "docs/USER_GUIDE.md",
    "docs/VALIDATION.md",
    "docs/ROADMAP.md",
    "docs/DEVELOPMENT_HANDOFF.md",
    "docs/RELEASE_PROCESS.md",
    "docs/ORIGINAL_RESTART_PACKAGE_MAP.md",
    "assets/ui-topbar-style-reference.png",
    "assets/README.md",
    "test-artifacts/09_TEST_Prowler_Utility_manifest.json",
    "test-artifacts/README.md",
    "test-artifacts/validation-summary-V001.json",
    "release/RELEASE_NOTES_V001.md",
    "tools/check_release.py",
    ".github/workflows/release-gate.yml",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/feature_request.md",
    ".github/pull_request_template.md",
]
for rel in required:
    if not (ROOT / rel).is_file():
        fail(f"Missing required file: {rel}")
if not errors:
    ok("Required repository file set exists")

# Byte-exact artifacts.
if MAIN.is_file():
    got = sha256(MAIN)
    if got == EXPECTED_MAIN_SHA:
        ok(f"Main artifact byte parity: {got}")
    else:
        fail(f"Main artifact SHA mismatch: {got} != {EXPECTED_MAIN_SHA}")

if STANDARD.is_file():
    got = sha256(STANDARD)
    if got == EXPECTED_STANDARD_SHA:
        ok(f"Release standard byte parity: {got}")
    else:
        fail(f"Release standard SHA mismatch: {got} != {EXPECTED_STANDARD_SHA}")

if EVIDENCE.is_file():
    got = sha256(EVIDENCE)
    if got == EXPECTED_EVIDENCE_SHA:
        ok(f"Prowler runtime manifest byte parity: {got}")
    else:
        fail(f"Prowler evidence SHA mismatch: {got} != {EXPECTED_EVIDENCE_SHA}")

style_ref = ROOT / "assets" / "ui-topbar-style-reference.png"
if style_ref.is_file():
    got = sha256(style_ref)
    if got == EXPECTED_STYLE_REF_SHA:
        ok(f"User-owned style reference byte parity: {got}")
    else:
        fail(f"Style reference SHA mismatch: {got} != {EXPECTED_STYLE_REF_SHA}")

# Excluded third-party/game image reference must not be present.
for p in ROOT.rglob("*"):
    if p.is_file() and "MOLE_views" in p.name:
        fail(f"Excluded MOLE/CIG visual found in public package: {p.relative_to(ROOT)}")
if not any("MOLE_views" in p.name for p in ROOT.rglob("*") if p.is_file()):
    ok("Excluded MOLE/CIG visual is absent")

# Main HTML static structure.
if MAIN.is_file():
    raw = MAIN.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as e:
        fail(f"Main HTML is not UTF-8 decodable: {e}")
        text = ""

    if text:
        if "<!DOCTYPE html>" in text or "<!doctype html>" in text.lower():
            ok("HTML doctype present")
        else:
            fail("HTML doctype missing")

        style_count = len(re.findall(r"<style(?:\s[^>]*)?>", text, flags=re.I))
        script_open = list(re.finditer(r"<script([^>]*)>", text, flags=re.I))
        inline_script_count = sum(1 for m in script_open if not re.search(r"\bsrc\s*=", m.group(1), re.I))
        external_script_count = sum(1 for m in script_open if re.search(r"\bsrc\s*=", m.group(1), re.I))
        if style_count == 1 and inline_script_count == 1 and external_script_count == 0:
            ok("Single-file HTML markers: 1 style, 1 inline script, 0 external scripts")
        else:
            fail(f"Unexpected style/script structure: style={style_count}, inline_script={inline_script_count}, external_script={external_script_count}")

        ids = re.findall(r'\bid=["\']([^"\']+)["\']', text, flags=re.I)
        dupes = sorted({x for x in ids if ids.count(x) > 1})
        if dupes:
            fail("Duplicate HTML IDs: " + ", ".join(dupes))
        else:
            ok(f"HTML IDs unique ({len(ids)} IDs)")

        markers = [
            "sPg Star Citizen Vehicle Reference Downloader",
            "version: 'V001'",
            "https://api.star-citizen.wiki/api",
            "https://starcitizen.tools/api.php",
            "class ZipBuilder",
            "localStorage",
        ]
        missing = [m for m in markers if m not in text]
        if missing:
            fail("Missing main-artifact markers: " + "; ".join(missing))
        else:
            ok("Expected V001 architecture/source markers present")

        # Optional embedded JavaScript syntax check with Node if installed.
        node = shutil.which("node")
        m = re.search(r"<script[^>]*>(.*?)</script>", text, flags=re.I | re.S)
        if node and m:
            with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as tf:
                tf.write(m.group(1))
                temp_js = Path(tf.name)
            try:
                cp = subprocess.run([node, "--check", str(temp_js)], capture_output=True, text=True)
                if cp.returncode == 0:
                    ok("Embedded JavaScript passed node --check")
                else:
                    fail("Embedded JavaScript node --check failed: " + (cp.stderr.strip() or cp.stdout.strip()))
            finally:
                temp_js.unlink(missing_ok=True)
        elif not node:
            warn("Node.js not available; embedded JavaScript syntax subcheck skipped (not runtime evidence)")

# JSON readability.
for p in ROOT.rglob("*.json"):
    try:
        json.loads(p.read_text("utf-8"))
    except Exception as e:
        fail(f"Invalid JSON: {p.relative_to(ROOT)}: {e}")
if not any("Invalid JSON" in e for e in errors):
    ok("Repository JSON files parse")

# Project version consistency markers.
for rel in ["README.md", "README.en.md", "STATUS.md", "CHANGELOG.md", "release/RELEASE_NOTES_V001.md"]:
    p = ROOT / rel
    if p.is_file() and "V001" not in p.read_text("utf-8"):
        fail(f"V001 version marker missing: {rel}")
if not any("version marker missing" in e for e in errors):
    ok("V001 version markers consistent in primary release docs")

# Disclaimer / privacy markers.
for rel, needles in {
    "README.md": ["nem hivatalos", "MIT License", "Google Fonts", "localStorage"],
    "README.en.md": ["unofficial", "MIT License", "Google Fonts", "localStorage"],
    "NOTICE.md": ["unofficial Star Citizen fan tool"],
    "PRIVACY.md": ["localStorage", "fonts.googleapis.com"],
}.items():
    p = ROOT / rel
    if p.is_file():
        t = p.read_text("utf-8")
        for n in needles:
            if n not in t:
                fail(f"Required documentation marker '{n}' missing from {rel}")
if not any("Required documentation marker" in e for e in errors):
    ok("Fan/trademark/privacy documentation markers present")

# Secret/credential heuristic scan.
secret_patterns = [
    ("private key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("GitHub classic token", re.compile(r"\bghp_[A-Za-z0-9]{30,}\b")),
    ("GitHub fine-grained token", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{30,}\b")),
    ("OpenAI-like secret", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("assigned API key", re.compile(r"(?i)\bapi[_-]?key\s*[:=]\s*[\"'][A-Za-z0-9._-]{16,}[\"']")),
]
scan_ext = {".md", ".html", ".json", ".py", ".yml", ".yaml", ".txt", ".sha256"}
secret_hits = []
for p in ROOT.rglob("*"):
    if not p.is_file() or p.suffix.lower() not in scan_ext:
        continue
    try:
        t = p.read_text("utf-8")
    except UnicodeDecodeError:
        continue
    for label, rx in secret_patterns:
        if rx.search(t):
            secret_hits.append(f"{label}: {p.relative_to(ROOT)}")
if secret_hits:
    fail("Potential credential/secret material: " + "; ".join(secret_hits))
else:
    ok("Credential/secret heuristic scan clean")

# Avoid personal absolute Windows user paths.
path_hits = []
rx_path = re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+\\")
for p in ROOT.rglob("*"):
    if p.is_file() and p.suffix.lower() in scan_ext:
        try:
            t = p.read_text("utf-8")
        except UnicodeDecodeError:
            continue
        if rx_path.search(t):
            path_hits.append(str(p.relative_to(ROOT)))
if path_hits:
    fail("Personal Windows user paths found: " + ", ".join(path_hits))
else:
    ok("No personal Windows user paths found")

# .gitattributes byte-exact policy.
ga = ROOT / ".gitattributes"
if ga.is_file():
    t = ga.read_text("utf-8")
    needed = [
        "sPg_Star_Citizen_Vehicle_Reference_Downloader_V001.html -text",
        "docs/RELEASE_STANDARD.md -text",
        "test-artifacts/09_TEST_Prowler_Utility_manifest.json -text",
        "*.md text eol=lf",
    ]
    missing = [x for x in needed if x not in t]
    if missing:
        fail(".gitattributes missing rules: " + "; ".join(missing))
    else:
        ok(".gitattributes protects byte-exact artifacts and normalizes normal text")


# Local Markdown link existence.
import urllib.parse
missing_links = []
for md in ROOT.rglob("*.md"):
    try:
        body = md.read_text("utf-8")
    except UnicodeDecodeError:
        continue
    for match in re.finditer(r'!?\[[^\]]*\]\(([^)]+)\)', body):
        target = match.group(1).strip().split()[0].strip("<>")
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target = target.split("#", 1)[0]
        if not target:
            continue
        resolved = (md.parent / urllib.parse.unquote(target)).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            continue
        if not resolved.exists():
            missing_links.append(f"{md.relative_to(ROOT)} -> {target}")
if missing_links:
    fail("Broken local Markdown links: " + "; ".join(missing_links))
else:
    ok("Local Markdown links resolve")

# Inventory exact-set parity.
inv_path = ROOT / "FILE-INVENTORY.json"
if inv_path.is_file():
    try:
        inv = json.loads(inv_path.read_text("utf-8"))
        declared = set(inv["files"])
        actual = {
            p.relative_to(ROOT).as_posix()
            for p in ROOT.rglob("*")
            if p.is_file()
        }
        if declared != actual:
            missing = sorted(declared - actual)
            extra = sorted(actual - declared)
            fail(f"Inventory parity mismatch; missing={missing}; extra={extra}")
        else:
            ok(f"Inventory exact-set parity ({len(actual)} files)")
    except Exception as e:
        fail(f"Inventory validation error: {e}")

# Checksum existence and hash parity.
checks = ROOT / "CHECKSUMS.sha256"
if checks.is_file():
    listed = {}
    malformed = []
    for ln in checks.read_text("utf-8").splitlines():
        if not ln.strip():
            continue
        m = re.match(r"^([0-9a-f]{64})  (.+)$", ln)
        if not m:
            malformed.append(ln)
            continue
        listed[m.group(2)] = m.group(1)
    if malformed:
        fail("Malformed CHECKSUMS lines: " + repr(malformed[:3]))
    expected_paths = {
        p.relative_to(ROOT).as_posix()
        for p in ROOT.rglob("*")
        if p.is_file() and p.name != "CHECKSUMS.sha256"
    }
    if set(listed) != expected_paths:
        fail(
            "Checksum existence parity mismatch; "
            f"missing={sorted(expected_paths-set(listed))}; "
            f"extra={sorted(set(listed)-expected_paths)}"
        )
    bad = []
    for rel, expected in listed.items():
        p = ROOT / rel
        if p.is_file() and sha256(p) != expected:
            bad.append(rel)
    if bad:
        fail("Checksum mismatch: " + ", ".join(bad))
    if not malformed and set(listed) == expected_paths and not bad:
        ok(f"CHECKSUMS parity and hashes valid ({len(listed)} files)")

print("sPg Vehicle Reference Downloader V001 — STATIC RELEASE GATE")
print("=" * 68)
for x in passes:
    print("[PASS]", x)
for x in warnings:
    print("[ATTENTION]", x)
for x in errors:
    print("[FAIL]", x)
print("-" * 68)
print(f"PASS={len(passes)} ATTENTION={len(warnings)} FAIL={len(errors)}")
print("NOTE: This is STATIC/package validation, not browser/runtime proof.")
sys.exit(1 if errors else 0)
