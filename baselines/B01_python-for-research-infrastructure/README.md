# B01 — Baseline: Python as research infrastructure, scoped to the posting

**Module:** M-PY (with M-SELF as the specimen principle). **Instrument:**
`BASELINE_B01_2026-09-20_v02_I.md` (v01 retired to `deprecated/`, reason at the bottom). **Key:**
`KEY_B01_FormA_2026-09-20_v02_I.md`, beside it, written against the built instrument.

## Why this module gets the first baseline

- It is the only **minimum** qualification she marked as a gap, and every orange module (distributed
  execution, dashboards, observability, training infra) is built out of it.
- Her purple carries two different needs at once: *refresh the basics* (her own words, 2026-09-19:
  "needs a refresher on basics") and *learn conceptually* the infrastructure patterns. A baseline that
  separates those two bands decides the sequence of the whole Python strand. A baseline on a module
  she has never touched (training infrastructure) would floor out and decide nothing.
- It can be taken rested, from a phone, on a real program, with no machines to set up.

## Scope, taken from the posting and nothing wider

**In:** "Strong Python programming skills, including production or research infrastructure" as it
shows up in the responsibilities: building and hardening a platform that runs many evals reliably;
"the tooling, libraries, and workflows researchers use to implement and iterate on evaluations";
"better retries, better observability, faster feedback to researchers"; "implement the scoring",
"build the dataset"; and the knobs of "prompting, sampling, and scaffolding" experiments.

**Out:** reproducing syntax from memory, because the posting's verbs are build, harden, improve and
run, and because the working mode under assessment is orchestrating AI-assisted coding, in which the
engineer reads, directs, verifies, and hand-codes the frequently used pieces; general computer-science
trivia; libraries the posting does not name (no pandas, no torch, no notebooks); distributed-systems
theory beyond what one harness shows (M-DIST); dashboards (M-DASH); the training loop itself (M-TRN).

## The specimen

`specimens/audit_against_ssots.py`, a 250-line standard-library program written 2026-09-19 for this
course: it sends one artifact plus the sources it was generated from to a different LLM and asks for
an audit. It has the shape of an eval harness in miniature: configuration from flags and environment,
a secret read from the environment, a request body assembled from files, retries with backoff, a
quota step-down ladder, raw output banked before parsing, a manifest with hashes. Two concepts the
posting cares about (concurrency, process lifecycle) are not in a single-call program, so those two
items are posed from a real episode of the same day instead of from code.

## Sixteen concepts, two bands

| Band | Concepts | What a low band score means |
|---|---|---|
| **A · reading Python** (refresh candidates) | modules and imports · entry point and arguments · functions and return values · nested data structures · loops and early exit · files, paths and encodings · reading a traceback | the Python for Poets strand starts with a refresher before any infrastructure pattern |
| **B · infrastructure patterns** (conceptual-learning candidates) | configuration and secrets · exceptions as routing · retries and backoff · bank before parse · observability from inside · sequential versus concurrent · process lifecycle · package and CLI shape · reproducibility knobs | the strand's centre of mass is the patterns, and the refresher can be light |

Items in Band B ask for the idea in the learner's own words first; a field term is accepted but never
required, because naming a pattern she has already constructed is the lesson's job, not the baseline's.

## Scoring: a profile, not a grade

Each item scores **0 · 1 · 2** against indicators in the key (not evidenced · partly · evidenced).
The result is a **16-bar profile**, one bar per concept, plus two band totals (A out of 14, B out of
18). The profile is what gets compared at the end of the strand, bar by bar. No single number is
reported as "the score", because a single number hides exactly the band split this baseline exists
to find.

## Self-assessment and calibration: a separate item set, on purpose

Part 2 of the instrument is a per-concept self-rating on four behaviourally described levels, taken
**after all sixteen content answers are in and before any score is shown**. It is kept apart from the
content items by the learner's ruling: asking someone how sure they are while they are answering
changes the answering. The mechanism she named is stereotype threat, not only measurement
reactivity, which widens the rule: no evaluative cue sits inside the content, the instrument is
framed as setting the curriculum's starting point rather than diagnosing ability, and self-assessment
is its own item set afterward. The per-concept gap between the Part 2 self-rating and the Part 1 evidenced
score is the calibration reading. Confidence running ahead of evidence marks where a quiet
misunderstanding sits and tells the next lesson to open with a check. Confidence running behind calls
for encouragement, not drilling. The learner's own line about which band felt like reading and which
like guessing is quoted beside the band totals.

## Re-administration: the parallel form

The same 16 concepts, posed on a **different specimen** (candidate: the Paper B census harness, once
she rules it public, or a sibling tool built inside the course), item for item at the same Bloom's and
Webb's levels, with its own key written against it.

## How to take it

Open the specimen on any screen. Answer Part 1 in prose, one to four sentences an item, in chat or in
a copy of the instrument. No code is written; the format is read-and-direct. **No AI assistance**: the
baseline measures the learner. Skipping an item is allowed and is recorded as 0 with a note, never
hidden. Then Part 2, then the journal line. Time is hers to note or not.

## Version note

v01 (2026-09-19) asked for a confidence rating beside every content item. Retired 2026-09-20 on her
ruling: *"self scoring and especially confidence self scoring should be a distinct item set from the
content under eval. answering or even just asking alongside asking for content answers triggers a
whole slew of negative psychological phenomena."* v02 moves all self-assessment into Part 2.

*Designed 2026-09-19, revised 2026-09-20, by Flaudechamba A.-L. Formative Horizon v01 (Claude Fable
5.1). AIGHVA.*
