#!/usr/bin/env python3
"""mirror_ssots.py — retrieve the third-party texts listed in sources.json, bank the raw bytes,
hash them, and write a provenance record for each. Standard library only.

  python3 tools/mirror_ssots.py                 # fetch anything not yet mirrored
  python3 tools/mirror_ssots.py --refetch       # fetch everything again, even if present
  python3 tools/mirror_ssots.py --verify        # re-fetch to a temp buffer and report hash drift
  python3 tools/mirror_ssots.py --only C1d,E3   # restrict to these ids

WHY THIS EXISTS. The course's register of quality anchors says "a locator that moved is a citation
that lies." A citation to a live URL is a promise about a page nobody controls. This tool turns each
citation into a retrieved artifact with a date and a hash, so a claim in a lesson can be checked
against the text as it stood when the claim was made, and so `--verify` can say out loud when the
upstream page has changed.

IT IS ALSO A TEACHING SPECIMEN. It is deliberately built with the same infrastructure patterns as
`audit_against_ssots.py` in the course repo — configuration from flags, retries with backoff, raw
bytes banked before any parsing, a manifest with hashes, one paced request at a time — so it can
serve as the second specimen for Baseline B01 Form B without either form tipping the other.

WHAT IT DOES NOT DO. It does not crawl. It fetches exactly the URLs named in sources.json, once
each, paced. It does not modify what it retrieves: raw bytes are stored byte-for-byte, and any text
extraction is written to a separate file beside them, clearly marked as derived.

Written 2026-09-20 for Krystal Martinez's python-for-poets course by Flaudechamba A.-L. Formative
Horizon v01 (Claude Fable 5.1).
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
import time
from html.parser import HTMLParser
from pathlib import Path
from urllib import error, request

HERE = Path(__file__).resolve().parent.parent
SOURCES = HERE / "sources.json"
OUT = HERE / "sources"

# An honest user agent: who is fetching, why, and where to complain.
UA = ("krystal-martinez-course-ssot-mirror/1.0 "
      "(archival copies of cited texts for a private study repository; one request per cited page)")


# ── fetch ────────────────────────────────────────────────────────────────────────────────────────
class Unavailable(Exception):
    """The server said try later, and it kept saying it."""


def fetch(url: str, tries: int = 3, timeout: int = 120) -> tuple[bytes, dict]:
    """Return (raw bytes, response headers). Retries the retryable codes with capped backoff."""
    for i in range(tries):
        try:
            req = request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
            with request.urlopen(req, timeout=timeout) as r:
                return r.read(), dict(r.headers)
        except error.HTTPError as e:
            body = " ".join(e.read().decode(errors="replace").split())[:200]
            if e.code in (429, 500, 502, 503, 504) and i < tries - 1:
                wait = min(30, 2 ** i * 5)
                print(f"    HTTP {e.code} → retry in {wait}s :: {body}", file=sys.stderr)
                time.sleep(wait)
                continue
            if e.code in (429, 500, 502, 503, 504):
                raise Unavailable(f"HTTP {e.code} persisted through {tries} tries :: {body}")
            raise RuntimeError(f"HTTP {e.code}: {body}")
        except (error.URLError, TimeoutError) as e:
            if i < tries - 1:
                time.sleep(min(60, 2 ** i * 5))
                continue
            raise Unavailable(f"network: {e}")
    raise RuntimeError("unreachable")


# ── derive readable text (a separate file; the raw bytes are never touched) ──────────────────────
class _Text(HTMLParser):
    SKIP = {"script", "style", "noscript", "svg"}

    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1
        elif tag in ("p", "div", "li", "tr", "br", "h1", "h2", "h3", "h4", "h5", "h6", "pre"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip and data.strip():
            self.parts.append(data)


def to_text(raw: bytes, content_type: str, pdf_path: Path | None = None) -> str | None:
    """HTML → plain text via the standard library. PDF → pdftotext if it is installed."""
    if "pdf" in content_type.lower() or (pdf_path and pdf_path.suffix == ".pdf"):
        if pdf_path is None:
            return None
        try:
            out = subprocess.run(["pdftotext", "-layout", str(pdf_path), "-"],
                                 capture_output=True, timeout=120)
            return out.stdout.decode("utf-8", errors="replace") if out.returncode == 0 else None
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return None
    if "html" not in content_type.lower() and not raw.lstrip()[:15].lower().startswith(b"<!doctype"):
        try:
            return raw.decode("utf-8")          # markdown, plain text
        except UnicodeDecodeError:
            return None
    p = _Text()
    try:
        p.feed(raw.decode("utf-8", errors="replace"))
    except Exception:
        return None
    return re.sub(r"\n{3,}", "\n\n", " ".join(p.parts).replace(" \n ", "\n")).strip()


def ext_for(content_type: str, url: str) -> str:
    ct = content_type.lower()
    if "pdf" in ct or url.endswith(".pdf"):
        return "pdf"
    if "html" in ct:
        return "html"
    if url.endswith(".md") or "markdown" in ct:
        return "md"
    return "txt"


# ── the provenance record ────────────────────────────────────────────────────────────────────────
def write_source_md(d: Path, s: dict, meta: dict) -> None:
    (d / "SOURCE.md").write_text(f"""# {s['title']}

**Mirror id:** `{s['id']}` · **Register entry:** `{s['register_id']}` in the course repo's
`standards/REGISTER_external-quality-anchors_2026-09-20_v01_I.md`

| Field | Value |
|---|---|
| Locator | <{s['url']}> |
| Publisher | {s['publisher']} |
| Licence as recorded | {s['licence']} |
| Retrieved (UTC) | {meta['retrieved_utc']} |
| HTTP content type | `{meta['content_type']}` |
| Bytes | {meta['bytes']:,} |
| sha256 of raw | `{meta['sha256']}` |
| Upstream last-modified | {meta.get('last_modified') or 'not sent'} |
| Upstream etag | {meta.get('etag') or 'not sent'} |

**What this anchors in the course:** {s['anchors']}

## Files

- `{meta['raw_name']}` — the retrieved bytes, unmodified. This is the artifact of record.
- {'`text.md` — plain text derived from the raw bytes by this repository’s tool, for reading and searching only. Derived, not authoritative; quote from the raw file.' if meta.get('text_written') else '_No derived text: extraction was not possible for this content type._'}

## Reading rules

1. **Quote from `{meta['raw_name']}`, never from `text.md`.** The derived text loses structure and
   may lose characters.
2. **This copy is dated.** If the claim being supported is time-sensitive, run
   `python3 tools/mirror_ssots.py --verify --only {s['id']}` and record the result before citing.
3. **The licence line above is as recorded, not as adjudicated.** See `LICENCE_NOTES.md`.

*Retrieved by `tools/mirror_ssots.py`.*
""", encoding="utf-8")


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def load_existing(d: Path) -> str | None:
    """The sha256 recorded for an already-mirrored source, if there is one."""
    f = d / "SOURCE.md"
    if not f.is_file():
        return None
    m = re.search(r"sha256 of raw \| `([0-9a-f]{64})`", f.read_text(encoding="utf-8"))
    return m.group(1) if m else None


# ── main ─────────────────────────────────────────────────────────────────────────────────────────
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--refetch", action="store_true", help="fetch even if already mirrored")
    ap.add_argument("--verify", action="store_true", help="re-fetch and report hash drift; writes nothing")
    ap.add_argument("--only", default=None, help="comma-separated source ids")
    ap.add_argument("--pace", type=float, default=2.0, help="seconds between requests (default 2)")
    a = ap.parse_args()

    srcs = json.loads(SOURCES.read_text(encoding="utf-8"))["sources"]
    if a.only:
        want = {x.strip() for x in a.only.split(",")}
        srcs = [s for s in srcs if s["id"] in want]
        missing = want - {s["id"] for s in srcs}
        if missing:
            sys.exit(f"FATAL: no such source id(s): {', '.join(sorted(missing))}")

    OUT.mkdir(exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    done, skipped, drift, failed = [], [], [], []

    for s in srcs:
        d = OUT / f"{s['id']}_{s['slug']}"
        prior = load_existing(d)
        if prior and not (a.refetch or a.verify):
            skipped.append(s["id"])
            print(f"·  {s['id']:4} already mirrored")
            continue

        print(f"→  {s['id']:4} {s['url']}", file=sys.stderr)
        try:
            raw, hdrs = fetch(s["url"])
        except (Unavailable, RuntimeError) as e:
            failed.append((s["id"], str(e)[:160]))
            print(f"   FAILED {s['id']}: {str(e)[:160]}", file=sys.stderr)
            time.sleep(a.pace)
            continue

        h = sha256(raw)
        if a.verify:
            if prior is None:
                print(f"   {s['id']}: not mirrored yet, nothing to verify")
            elif prior == h:
                print(f"   {s['id']}: UNCHANGED")
            else:
                drift.append((s["id"], prior, h))
                print(f"   {s['id']}: **DRIFTED**  mirrored {prior[:12]}…  upstream {h[:12]}…")
            time.sleep(a.pace)
            continue

        ct = hdrs.get("Content-Type", "")
        d.mkdir(parents=True, exist_ok=True)
        raw_name = f"raw.{ext_for(ct, s['url'])}"
        (d / raw_name).write_bytes(raw)                       # bank before anything is parsed
        text = to_text(raw, ct, d / raw_name)
        if text:
            (d / "text.md").write_text(
                f"<!-- DERIVED from {raw_name} by tools/mirror_ssots.py on {stamp}. "
                f"Not authoritative; quote from {raw_name}. -->\n\n{text}\n", encoding="utf-8")
        write_source_md(d, s, {"retrieved_utc": stamp, "content_type": ct or "not sent",
                               "bytes": len(raw), "sha256": h, "raw_name": raw_name,
                               "text_written": bool(text),
                               "last_modified": hdrs.get("Last-Modified"), "etag": hdrs.get("ETag")})
        done.append((s["id"], len(raw), h))
        print(f"   ok  {len(raw):>9,} bytes  {h[:12]}…  {'text' if text else 'no text'}")
        time.sleep(a.pace)

    if a.verify:
        print(f"\n=== verify {stamp} · {len(drift)} drifted · {len(failed)} unreachable ===")
        for i, p, n in drift:
            print(f"  DRIFT {i}: {p} → {n}")
        for i, e in failed:
            print(f"  FAIL  {i}: {e}")
        return 1 if (drift or failed) else 0

    # manifest
    rows = []
    for d in sorted(OUT.iterdir()):
        if not (d / "SOURCE.md").is_file():
            continue
        t = (d / "SOURCE.md").read_text(encoding="utf-8")
        g = lambda p: (re.search(p, t).group(1) if re.search(p, t) else "—")
        rows.append((d.name.split("_")[0], t.splitlines()[0][2:], g(r"Retrieved \(UTC\) \| (.+?) \|"),
                     g(r"sha256 of raw \| `([0-9a-f]{64})`"), g(r"Licence as recorded \| (.+?) \|"), d.name))
    (HERE / "MANIFEST.md").write_text(
        "# Manifest — what is mirrored here\n\n"
        f"Written by `tools/mirror_ssots.py` at {stamp}. {len(rows)} sources.\n\n"
        "| id | Title | Retrieved | sha256 (first 12) | Licence as recorded | Folder |\n"
        "|---|---|---|---|---|---|\n"
        + "".join(f"| `{i}` | {ti} | {r} | `{h[:12]}` | {lic} | `sources/{f}` |\n"
                 for i, ti, r, h, lic, f in rows)
        + "\n*Run `python3 tools/mirror_ssots.py --verify` to check every entry against upstream.*\n",
        encoding="utf-8")

    print(f"\n=== done · {len(done)} fetched · {len(skipped)} already present · {len(failed)} failed ===")
    for i, e in failed:
        print(f"  FAIL {i}: {e}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
