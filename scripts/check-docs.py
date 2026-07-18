#!/usr/bin/env python3
"""Validate the docs/ knowledge system.

Checks:
  1. Every docs/**/*.md has frontmatter `title` and `description`.
  2. Every Markdown link in docs/ resolves:
     - internal links (not http/https) resolve to a file in the repo
       (directory links must contain an index.md); anchors are verified
       against the target file's headings when the target is a .md file.
     - external http(s) links are best-effort HEAD checks (off by default;
       enable with --external) and reported as warnings, not failures.

Exits non-zero on any hard failure. Used by .github/workflows/docs-check.yml.

Run: python3 scripts/check-docs.py [--external]
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

LINK_RE = re.compile(r"\[(?:[^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
HEADING_RE = re.compile(r"^#+\s+(.+?)\s*$", re.MULTILINE)


def parse_frontmatter(text: str) -> dict[str, str] | None:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    fm: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def slugify(heading: str) -> str:
    s = heading.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s]+", "-", s)
    return s


def collect_headings(path: Path) -> set[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return set()
    return {slugify(h) for h in HEADING_RE.findall(text)}


def resolve_internal(link: str, source: Path) -> tuple[bool, str]:
    """Resolve an internal link relative to `source` (a docs/*.md file)."""
    raw = link
    anchor = ""
    if "#" in link:
        link, _, anchor = link.partition("#")
    if link == "":
        # Pure anchor link — resolves within the current file.
        headings = collect_headings(source)
        if anchor and slugify_unchecked(anchor) not in headings:
            return False, f"anchor #{anchor} not found in {source.name}"
        return True, ""
    # Absolute repo path starting with "/" — resolve from repo root.
    if link.startswith("/"):
        target = ROOT / link.lstrip("/")
    else:
        target = (source.parent / link).resolve()
    # Directory link → look for index.md inside.
    if target.is_dir():
        idx = target / "index.md"
        if idx.exists():
            target = idx
        else:
            return False, f"directory {raw} has no index.md"
    if not target.exists():
        return False, f"{raw} -> {target.relative_to(ROOT)} does not exist"
    # Anchor verification for .md targets.
    if anchor and target.suffix == ".md":
        headings = collect_headings(target)
        if slugify_unchecked(anchor) not in headings:
            return False, f"anchor #{anchor} not found in {target.relative_to(ROOT)}"
    return True, ""


def slugify_unchecked(anchor: str) -> str:
    # GitHub-style slug: lower, remove punctuation, spaces -> hyphens.
    return slugify(anchor)


def check_external(url: str, timeout: float = 5.0) -> tuple[bool, str]:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "saas-ideas-docs-check/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            ok = 200 <= r.status < 400
            return ok, f"HTTP {r.status}"
    except urllib.error.HTTPError as e:
        # 405 etc. from servers that disallow HEAD — retry as GET.
        if e.code in (405, 403, 501):
            try:
                req2 = urllib.request.Request(url, headers={"User-Agent": "saas-ideas-docs-check/1.0"})
                with urllib.request.urlopen(req2, timeout=timeout) as r:
                    return (200 <= r.status < 400), f"HTTP {r.status} (GET)"
            except Exception as e2:
                return False, f"{type(e2).__name__}: {e2}"
        return False, f"HTTP {e.code}"
    except Exception as e:
        return False, f"{type(e).__name__}: {e}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--external", action="store_true", help="also HEAD-check external links (best-effort)")
    ap.add_argument("--docs-root", default=str(DOCS))
    args = ap.parse_args()

    docs_root = Path(args.docs_root)
    if not docs_root.is_dir():
        print(f"error: docs root {docs_root} not found", file=sys.stderr)
        return 2

    md_files = sorted(docs_root.rglob("*.md"))
    if not md_files:
        print(f"error: no markdown files under {docs_root}", file=sys.stderr)
        return 2

    errors: list[str] = []
    warnings: list[str] = []

    for f in md_files:
        rel = f.relative_to(ROOT)
        text = f.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{rel}: missing frontmatter (--- ... ---)")
        else:
            if "title" not in fm:
                errors.append(f"{rel}: frontmatter missing 'title'")
            if "description" not in fm:
                errors.append(f"{rel}: frontmatter missing 'description'")
        for m in LINK_RE.finditer(text):
            link = m.group(1)
            if link.startswith(("http://", "https://", "mailto:")):
                if args.external and link.startswith(("http://", "https://")):
                    ok, msg = check_external(link)
                    if not ok:
                        warnings.append(f"{rel}: external link {link} -> {msg}")
                continue
            if link.startswith("data:") or link.startswith("#"):
                continue
            ok, msg = resolve_internal(link, f)
            if not ok:
                errors.append(f"{rel}: broken link {link} ({msg})")

    for w in warnings:
        print(f"WARN: {w}")
    for e in errors:
        print(f"FAIL: {e}")

    print(f"\nChecked {len(md_files)} markdown files. {len(errors)} error(s), {len(warnings)} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
