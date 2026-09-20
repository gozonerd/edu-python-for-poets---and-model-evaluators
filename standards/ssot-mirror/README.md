# SSOT mirror — pointers here, copies in Drive

The course cites third-party texts as the single sources of truth for its instructional content.
Those texts are other people's work, so **this repository holds pointers and provenance, never the
bytes.** The retrieved copies live in Krystal Martinez's Google Drive, which is the standing
convention in this workspace for third-party content.

| | |
|---|---|
| Drive location | `nk:Gozo Nerd Universo Archive/edu-python-for-poets---and-model-evaluators/ssot-mirror/` |
| Sources mirrored | 16, retrieved 2026-09-20, 48 files, ~2.0 MB |
| Verified after upload | `rclone check` reported 0 differences, 48 matching files |

## What is in this folder

| Path | What it is |
|---|---|
| `sources.json` | The source list: id, register entry, locator, publisher, licence, what it anchors |
| `records/` | One provenance record per source — retrieval date, content type, byte count, **sha256 of the raw bytes**, the Drive path, and the command to pull it back |
| `mirror_ssots.py` | The tool that retrieved them, and the tool that re-checks them |

Every record's register entry resolves in
`standards/REGISTER_external-quality-anchors_2026-09-20_v01_I.md`. Nothing is mirrored that the
register does not cite.

## Re-verifying before anything ships

The register's own rule is that a locator which moved is a citation that lies. To check every source
against upstream without writing anything:

```bash
python3 standards/ssot-mirror/mirror_ssots.py --verify
```

It re-fetches each URL, hashes it, and reports `UNCHANGED` or `DRIFTED` per source, exiting non-zero
if anything drifted or is unreachable. Run it before the application packet goes out and record the
result.

To pull one source back out of Drive:

```bash
rclone copy "nk:Gozo Nerd Universo Archive/edu-python-for-poets---and-model-evaluators/ssot-mirror/C1d_sre-book-ch12-effective-troubleshooting" ./C1d
```

## How the copies were made, and the rules they follow

- **Raw bytes are stored byte-for-byte.** Each folder holds `raw.html`, `raw.pdf`, `raw.md` or
  `raw.txt` exactly as the server sent it. That file is the artifact of record.
- **Derived text sits beside it, marked derived.** `text.md` is a plain-text rendering for reading
  and searching. It loses structure. **Quote from the raw file, never from the derived text.**
- **No crawling.** Exactly the cited URLs, once each, paced, with a user agent that says who is
  fetching and why.
- **Nothing is modified.** No cleanup, no reformatting, no excerpting of the stored copy.

## Licences, recorded rather than adjudicated

Each record carries the licence as found. Three were corrected by fetching, one is a constraint worth
reading before anyone reuses a copy:

| Source | Licence as found | Consequence |
|---|---|---|
| Site Reliability Engineering, 5 chapters | CC BY-NC-ND 4.0 | Redistribution permitted unmodified, non-commercially, with attribution |
| The Twelve-Factor App | **MIT** (corrected; the site page states no licence, the source repository does) | Permissive |
| OpenTelemetry docs | CC BY 4.0 | Permissive with attribution |
| Strubell et al. 2019 | CC BY 4.0 via the ACL Anthology | Permissive with attribution |
| Luccioni et al. 2024 (arXiv) | **CC BY-SA 4.0** (corrected) | Share-alike |
| **Patterson et al. 2021 (arXiv)** | **arXiv nonexclusive-distrib/1.0 — not an open licence** | arXiv may distribute it; **we may not redistribute**. Personal archival copy only, and only the abstract page was retrieved, deliberately |
| MLflow, Python Packaging Guide, Inspect, lm-evaluation-harness | project licences, some still to confirm | See `sources.json` |

**This is why the copies are in private Drive and not in a public repository.** One entry alone
settles it: a non-open licence in the set means the set cannot be published, and sorting copies by
licence into two homes would be a filing system that fails quietly the first time someone adds a
source without checking. One home, private, is the honest design.

*Built 2026-09-20 by Flaudechamba A.-L. Formative Horizon v01 (Claude Fable 5.1). AIGHVA.*
