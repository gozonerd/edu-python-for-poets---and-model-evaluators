## D-20260920-03 — Three rulings applied: PBL threads with one-objective lessons, self-assessment as a separate item set, and the Python framing

**Her rulings, verbatim (2026-09-20, mobile):**

On structure: *"I want you to structure as a or several pbl thread(s) throughout the curriculum and I
want the individual lessons to teach and evaluate exactly one learning objective w an exit ticket.
The lesson should be either say see do or 5/7 e in design. I am a constructivist in just about every
sense of the epistemic concept and thrive when I have to construct knowledge especially if it's
before I have to learn epistemic jargon aka what field specific words feel and read as if I am
taught it without understanding what is means when applied"*

On the ledger: *"self scoring and especially confidence self scoring should be a distinct item set
from the content under eval. answering or even just asking alongside asking for content answers
triggers a whole slew of negative psychological phenomena"*

On the learner profile: *"do *not* put that I do not hand code anywhere near this job app. we frame it
as I orchestrate ai assisted coding. we frame it has me being able to hand code very basic frequently
used commands and functions independently and that doing do comes with significant accessibility
challenges that effectively orchestrating ai assisted coding allows me to overcome w no negative
latency impact on my ability to work w code and programming effectively"*

**Actions (three, one entry each would be the spec's letter; they are recorded together only because
all three are corrections to text already public, applied in one commit, and each is listed with
its own falsifier):**

1. **B01 v02.** Removed the per-item confidence prompt from all sixteen content items; added Part 2,
   a per-concept self-rating on four behaviourally described levels, administered after Part 1 and
   before any score is shown; moved the journal line after it. v01 retired to `deprecated/`. The
   private key moved to v02 with an explicit calibration rule reading Part 2 against Part 1.
2. **Framing.** The README no longer says the learner reads and directs Python "rather than
   hand-typing it." It says her working mode is orchestrating AI-assisted coding: reading, directing,
   QAing, and hand-coding the basic, frequently used commands and functions herself. The B01 design
   note's scope-out paragraph was rewritten on the same construct. The private handoff carries her
   ruling as an appendix; the seat's memory files were corrected.
3. **Structure, recorded for the design session, no files yet.** Curriculum organised as one or more
   project-based threads; every lesson teaches and evaluates exactly one learning objective with an
   exit ticket; each lesson is Say-See-Do or a 5E/7E cycle; field terms are introduced only after the
   learner has constructed the concept.

**Method:** Authored edits by this seat; version-up for the instrument and key per the file-naming
rule, append-only for the handoff and this log. DEFAULT tooling.

**Repetition:** 2 (D-01, D-02 share the Method of this seat authoring course apparatus). New rationale:
these are corrections at her ruling, not new design.

**Alternatives rejected:**
- **Keep per-item confidence and add a note.** Rejected: her ruling names the mechanism (asking
  alongside the content changes the answering), and the literature on the reactivity of judgments of
  learning agrees; a note does not remove the interference.
- **Collect the self-rating before Part 1 instead of after.** Rejected: a pre-rating primes the
  content answering the same way; after Part 1 and before the reveal is the only slot that leaves both
  measures clean.
- **Rewrite D-01's open item (3) to match the new framing.** Rejected: decision entries are records;
  D-01 stays as written and this entry supersedes it.

**Rationale:** each ruling is quoted; nothing here is inferred from it. On the framing, the construct
the course assesses was always read-and-direct; the earlier wording described it as an absence, and an
absence is not a construct.

**Falsifiers:** (1) the calibration reading from Part 2 turns out uninformative because the four
levels do not discriminate, in which case the levels are rewritten, not the separation; (2) any text
in the public repo or application artifacts still carries the "does not hand-code" framing after this
commit, which a grep for "hand-typ" and "hand-cod" should return empty except in this entry and the
handoff appendix; (3) a lesson ships with two objectives or with a field term introduced before its
concept, which the rigor rubric must catch.

Recorded after the edits by Flaudechamba A.-L. Formative Horizon v01 (Claude Fable 5.1), session
20cd8283, 2026-09-20.
