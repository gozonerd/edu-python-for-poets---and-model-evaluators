## D-20260920-06 — Mirror the cited third-party texts to Drive, keep pointers and hashes in git

**Her instruction, verbatim (2026-09-20):** *"i want you to stand up a mirror repo for this python for
poets & model evaluators learning experience to save copies of the 3rd party texts that the learning
experience is using as its ssots for the instructional content"*, corrected mid-build: *"oh oh oh! you
misunderstood and i likely got distracted and wernt off on a tangent before fully saying the mirror is
in my gdrive aka the place that we store 3rd party content with pointers from the repo there"*

**Action:** Retrieve the 16 third-party texts the register cites (sections C, D, E), store the copies
in Google Drive at `nk:Gozo Nerd Universo Archive/edu-python-for-poets---and-model-evaluators/ssot-mirror/`,
and keep the pointer apparatus in this repository at `standards/ssot-mirror/`: the source list, one
provenance record per source carrying the sha256 and the Drive path, and the retrieval tool.

**Method:** `tools/mirror_ssots.py`, written for this purpose: stdlib Python, one paced request per
cited URL, raw bytes banked before any parsing, sha256 per file, derived text written to a separate
marked file. Upload by `rclone copy` to the `nk:` remote; verified by `rclone check --one-way`, which
reported **0 differences, 48 matching files**. Python used under the §9 A1 suspension.

**Repetition:** 5 (D-01 through D-05 share the Method of this seat authoring course apparatus). New
rationale: this is the first entry whose output is *not* authored text but retrieved artifacts, and
the discipline that matters shifted accordingly — from citation to custody. The rut check that applies
here is different too: the tool's `--verify` mode exists so that re-checking is a command rather than
an intention.

**Alternatives rejected:**
- **A standalone GitHub repo holding the texts** — the seat's first reading of her instruction, and
  wrong twice over. Her convention puts third-party content in Drive with pointers from git, and
  independently the licence survey below makes a public repo indefensible. The repo was created before
  her correction arrived; it was never pushed to and is empty. **Open item: it still exists at
  `gozonerd/edu-python-for-poets---and-model-evaluators-ssot-mirror` and needs deleting. The CLI
  refused with HTTP 403 for want of the `delete_repo` scope.**
- **Sorting copies into a public folder by licence and a private one for the rest.** Rejected: one
  non-open licence in the set settles the question for the set, and a filing system that requires a
  licence judgment per addition fails quietly the first time someone skips the check.
- **Storing only the derived text.** Rejected: derived text loses structure and characters, and a
  quote checked against it is a quote checked against a lossy copy. Raw bytes are the artifact of
  record; derived text sits beside them marked derived.
- **Fetching the Patterson PDF.** Rejected on reading its licence — see below.

**Rationale:** the register's own rule is that a locator which moved is a citation that lies. Sixteen
citations are now sixteen dated, hashed artifacts, and `--verify` turns "re-check before the packet
ships" from an intention into one command with a non-zero exit code.

**Licence findings, which changed three register entries:**
- *The Twelve-Factor App* is **MIT**, stated in its source repository though not on its own site.
- Luccioni et al. 2024 is **CC BY-SA 4.0**, stated on the arXiv abstract page.
- **Patterson et al. 2021 carries arXiv's `nonexclusive-distrib/1.0`, which is not an open licence**:
  arXiv may distribute it, this project may not. Only the abstract page was retrieved, deliberately,
  and that single entry is the reason the whole mirror is private rather than public.

**Falsifier:** `--verify` reports drift on a source whose claim a lesson already rests on, and the
lesson's claim does not survive the current text; or a copy in Drive cannot be pulled back by the
command its record prints, which would mean the pointer is decorative.

Recorded after the build by Flaudechamba A.-L. Formative Horizon v01 (Claude Fable 5.1), session
20cd8283, 2026-09-20.
