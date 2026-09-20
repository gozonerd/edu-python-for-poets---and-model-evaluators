# B01 — Baseline: Python as research infrastructure, scoped to the posting

**Module:** M-PY (with M-SELF as the specimen principle). **Instrument:**
`BASELINE_B01_2026-09-19_v01_I.md`. **Key:** held outside this repo so a re-take stays honest.

## Why this module gets the first baseline

- It is the only **minimum** qualification she marked as a gap, and every orange module (distributed
  execution, dashboards, observability, training infra) is built out of it.
- Her purple carries two different needs at once: *refresh the basics* (her own words, 2026-09-19:
  "needs a refresher on basics") and *learn conceptually* the infrastructure patterns. A baseline that
  separates those two bands decides the sequence of the whole Python strand. A baseline on a module
  she has never touched (training infrastructure) would floor out and decide nothing.
- It can be taken tonight, from a phone, on a real program, with no machines to set up.

## Scope, taken from the posting and nothing wider

**In:** "Strong Python programming skills, including production or research infrastructure" as it
shows up in the responsibilities: building and hardening a platform that runs many evals reliably;
"the tooling, libraries, and workflows researchers use to implement and iterate on evaluations";
"better retries, better observability, faster feedback to researchers"; "implement the scoring",
"build the dataset"; and the knobs of "prompting, sampling, and scaffolding" experiments.

**Out:** hand-typed syntax fluency (she directs and reads; the posting's verbs are build, harden,
improve, run, not type); general computer-science trivia; libraries the posting does not name
(no pandas, no torch, no notebooks); distributed-systems theory beyond what one harness shows (M-DIST);
dashboards (M-DASH); the training loop itself (M-TRN).

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

## Scoring: a profile, not a grade

Each item scores **0 · 1 · 2** against indicators in the key (not evidenced · partly · evidenced).
The result is a **16-bar profile**, one bar per concept, plus two band totals (A out of 14, B out of
18). The profile is what gets compared at the end of the strand, bar by bar. No single number is
reported as "the score", because a single number hides exactly the band split this baseline exists
to find.

## Calibration, built in

Every item asks for a **confidence rating (1–4) before the answer**. The gap between confidence and
score, per item, is the calibration profile. Confidence ahead of score on Band B is the expected
shape for a learner who has orchestrated these patterns without having them named; if it shows, the
lessons name the patterns first.

## Re-administration: the parallel form

The same 16 concepts, posed on a **different specimen** (candidate: the Paper B census harness, once
she rules it public, or a sibling tool built inside the course), item for item at the same Bloom's
level. Form B is written only after Form A is scored, so its items are not tuned to her Form-A answers.

## How to take it

Open the specimen on any screen. Answer in prose, one to four sentences an item, in chat or in a copy
of the instrument. No code is written. **No AI assistance**: the baseline measures the learner, and her
own rule for the API-call structure is that it gets learned without AI help. Skipping an item is
allowed and is recorded as 0 with a note, never hidden. Time is hers to note or not.

*Designed 2026-09-19 by Flaudechamba A.-L. Formative Horizon v01 (Claude Fable 5.1). AIGHVA.*
