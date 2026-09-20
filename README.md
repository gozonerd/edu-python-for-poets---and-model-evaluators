# edu-python-for-poets---and-model-evaluators

Python taught the way Columbia teaches *Physics for Poets*: every foundational and major supporting
concept, conceptually, for a learner whose working mode is **orchestrating AI-assisted coding**:
reading, directing, and QAing Python, and hand-coding the basic, frequently used commands and
functions herself. The learner is Krystal Martinez; the course is scoped to how Python appears in one job description,
Anthropic's *Research Engineer, Model Evaluations* posting, because that is the work she is preparing
for and a curriculum with a real destination learns faster than one without.

**Stood up 2026-09-19**, the day after she found the posting.

## How this course is built

1. **A modular gap inventory from the job description first.** She read the posting with five
   highlighter colours; each colour is a learning verb (learn, learn conceptually, refresh, practice,
   share). `JD_LEARN_INVENTORY_modular_2026-09-19_v01_I.md` keeps every module distinct until the
   learning experience is designed. Integration is a design decision made later, on purpose.
2. **A baseline before any instruction.** Every well-designed curriculum that wants to make progress
   visible starts with a baseline. `baselines/` holds one instrument per module, each scoped to the
   posting's own use of that topic, each built to be re-administered as a parallel form later so the
   before-and-after is a measurement rather than a feeling. Each instrument's key sits beside it,
   written against the built instrument.
3. **Say-See-Do lessons after that**, generated with the `/say-see-do` skill: one standard, one
   objective at a target Bloom's level, three to six Say-See-Do cycles on her real work, independent
   at-bats, and a formative exit ticket that climbs Bloom's and carries a stretch item. Exit tickets
   get a diagnostic call per item and one learning decision, never a number. That grading shape is
   the one she used with her own seventh-graders: ramped items, a marginal diagnosis in purple ink, a
   circle for a missed direction that costs nothing when the science is sound, and a self-rating
   row whose gap from the diagnosis is the calibration signal.
4. **A ledger by learning standard.** Standards are the four AI-Fluency strands (Delegation,
   Description, Discernment, Diligence) until the AI-work standards set she is deriving lands.

## Layout

```
JD_LEARN_INVENTORY_modular_2026-09-19_v01_I.md   the modules, one per highlighted span, kept apart
standards/                                        the register of external quality anchors, the
                                                  framework, and the mastery standards by core idea
standards/ssot-mirror/                            pointers + hashes for the cited third-party texts;
                                                  the copies themselves live in Drive, not in git
baselines/B01_python-for-research-infrastructure/ the first baseline: design note + instrument + key
specimens/                                        real programs the instruments and lessons read from
Decisions/Decision Logs/claude/                   one entry per non-deterministic action
```

## Build order

Standards → evidence plan → **build** the instrument → write its key or rubric **against the built
instrument** → build the lesson that leads to it. A rubric is never written against a plan. Baseline
B01 was built before the standards existed, which is the wrong order; it is kept, and the CI-PY
standards file carries the coverage check that resulted, findings and all.

## ASAE

No `.asae-policy` at the root, so the gate does not bind and a commit here is a save. The standards
set is flagged for **ASAE strict-5 with three independent raters** after its improvement pass;
nothing in this repository has passed a gate.

## Provenance and rights

Course apparatus, instruments and lessons are authored by the seat persona **Flaudechamba A.-L.
Formative Horizon v01 (Claude Fable 5.1)** and committed under that name. Her answers, notes and
rulings are hers and are quoted, never paraphrased into someone else's voice. AI Generated, Human
Verified Always.

No license has been chosen yet, so the GitHub default applies: all rights reserved. A license is an
open decision for the owner.
