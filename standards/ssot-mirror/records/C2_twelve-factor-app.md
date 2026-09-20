# The Twelve-Factor App

**Mirror id:** `C2` · **Register entry:** `C2` in the course repo's
`standards/REGISTER_external-quality-anchors_2026-09-20_v01_I.md`

| Field | Value |
|---|---|
| Locator | <https://12factor.net/> |
| Publisher | Adam Wiggins |
| Licence as recorded | MIT License (github.com/heroku/12factor: "Released under the MIT License") |
| Retrieved (UTC) | 2026-09-20T11:18:00Z |
| HTTP content type | `text/html;charset=utf-8` |
| Bytes | 10,596 |
| sha256 of raw | `69230eae64071cc9ffcdfff6154c00dfb85c0c96d0710c63d189e20879a9dab9` |
| Upstream last-modified | not sent |
| Upstream etag | not sent |

**What this anchors in the course:** Config in the environment (III), declared dependencies (II), disposability (IX), concurrency (VIII), logs as streams (XI).

## Where the copy lives

The retrieved bytes are **not in this repository**. Third-party content is stored in Krystal
Martinez's Google Drive and pointed at from git — the standing convention for this workspace.

| | |
|---|---|
| Drive path | `Gozo Nerd Universo Archive/edu-python-for-poets---and-model-evaluators/ssot-mirror/C2_twelve-factor-app/` |
| rclone remote | `nk:` (also reachable as `kjml:`) |
| Retrieve | `rclone copy "nk:Gozo Nerd Universo Archive/edu-python-for-poets---and-model-evaluators/ssot-mirror/C2_twelve-factor-app" ./C2_twelve-factor-app` |
| Check this record against the copy | `sha256sum C2_twelve-factor-app/raw.*` and compare with the hash above |

## Files in that Drive folder

- `raw.html` — the retrieved bytes, unmodified. This is the artifact of record.
- `text.md` — plain text derived from the raw bytes by this repository’s tool, for reading and searching only. Derived, not authoritative; quote from the raw file.

## Reading rules

1. **Quote from `raw.html`, never from `text.md`.** The derived text loses structure and
   may lose characters.
2. **This copy is dated.** If the claim being supported is time-sensitive, run
   `python3 tools/mirror_ssots.py --verify --only C2` and record the result before citing.
3. **The licence line above is as recorded, not as adjudicated.** See `LICENCE_NOTES.md`.

*Retrieved by `tools/mirror_ssots.py`.*
