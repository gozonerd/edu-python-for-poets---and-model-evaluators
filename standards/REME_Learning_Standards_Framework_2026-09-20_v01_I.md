# REME learning standards — the framework

**What a standard in this course is.** A statement of *cognitive complexity × specific concept ×
specific observable behaviour*, written as a doing. That formulation is the learner's, 2026-09-20:
*"We backwards plan from external standards enumerating the cognitive complexity indicated to
interact with what specific learning concept by executing what specific observable behavior?"* It is
also, independently, the grammar of an NGSS performance expectation and of her own benchmark-design
note on bullet-journal p. 176: *"The model can x capability at y quality, demonstrated by a(b, and c)
observable actions."* Swap the model for the learner and the sentence is a mastery standard.

**Every standard here is a mastery standard.** Her ruling, 2026-09-20: *"every standard is a mastery
standard. What does the industry genuinely consider mastery of its concepts and practices? Then
learning standards are decomposed into the individual learning objectives whose mastery directly
supports the mastery of the standard the learning objective was backwards planned from."* So the
count of standards is not chosen; it falls out of the anchors. There is no target number in this
document, on purpose.

**Derivation route: anchors-first.** Of the two flagship routes in her own standards-derivation
research, CCSS wrote college-and-career-readiness anchors first and back-mapped, NGSS built a
research framework first and wrote standards from it. This course goes anchors-first, because the
anchor set already exists, is external, is employer-authored, and is frozen with a content hash: the
posting (register **A1**). Its responsibility bullets are the anchors; its representative projects
are the performance tasks; its qualifications name the content.

**The evidentiary chain.** Messick's construct-centred framework operationalised through
Evidence-Centred Design, as her research report records it: define the construct first, let it drive
task selection and rubric development. Here the **proficiency model** is what mastery of each anchor
looks like at the bar the register sets; the **evidence model** is the observable behaviours in each
standard's evidence statement; the **task model** is the baselines, exit tickets and performance
tasks. The chain has to be walkable from an observed behaviour back to an inference about capability,
and back down again.

---

## Dimension P · Practices

Nine practices from the posting's eight key-responsibility bullets. Bullet one splits, because the
learner highlighted its two halves differently: the design-and-run half is unhighlighted, the
visualisation half is teal. Two different relationships to the same sentence is evidence of two
practices, not one.

| Code | Practice | Posting span (verbatim) |
|---|---|---|
| **P1** | Design and run evaluations | "Design and run new evaluations of Claude's capabilities — reasoning, agentic behavior, knowledge, safety properties" |
| **P2** | Make results legible | "produce visualizations that make the results legible to researchers and decision-makers" |
| **P3** | Build and harden execution at scale | "Build and harden the distributed eval execution platform so hundreds of evals run reliably against checkpoints throughout production RL training runs" |
| **P4** | Own model-health monitoring | "Own the dashboards researchers and leadership use to monitor model health during training, improving signal-to-noise, reducing latency, and making regressions impossible to miss" |
| **P5** | Diagnose and communicate under time pressure | "Debug anomalous eval results mid-training-run, determine whether the cause is a model change or an infrastructure issue, and communicate the answer clearly under time pressure" |
| **P6** | Improve what researchers iterate with | "Improve the tooling, libraries, and workflows researchers use to implement and iterate on evaluations" |
| **P7** | Partner to define what to measure | "Partner with research teams across the full lifecycle of a new capability — from defining what to measure to interpreting results as training progresses" |
| **P8** | Characterise elicitation effects | "Run experiments to characterize how prompting, sampling, and scaffolding choices affect results on internal and industry benchmarks" |
| **P9** | Communicate inward and outward | "Communicate evaluations and their results to internal stakeholders and, where appropriate, external audiences" |

## Dimension CI · Core ideas

The content modules, from her highlighted reading of the posting
(`JD_LEARN_INVENTORY_modular_2026-09-19_v01_I.md`). Eight are core ideas. Two entries in that
inventory are not core ideas and are recorded here as what they actually are.

| Code | Core idea | Her colour |
|---|---|---|
| **CI-PY** | Python as research infrastructure | purple |
| **CI-DIST** | Distributed eval execution | orange · green |
| **CI-DASH** | Model-health dashboards | orange |
| **CI-OBS** | Observability, monitoring, experiment tracking | orange |
| **CI-TRN** | ML training infrastructure | orange |
| **CI-DIAG** | Model change versus infrastructure issue | pink |
| **CI-TOOL** | Tooling researchers iterate with | green |
| **CI-VIZ** | Visualisations legible to decision-makers | teal |

**Not core ideas, and why:**

- **M-SELF** (*"Have Claude teach me about my python programs, infra architecture + architectural
  decisions made through SSD interactive artifacts"*) is a **specimen rule** that governs every
  module: wherever a lesson or an instrument needs an artifact, it uses one the learner has
  orchestrated, and the architectural decisions inside it are the content. It is recorded as a rule
  because a specimen rule with a module code would collect standards that belong elsewhere.
- **M-PAIR** (*"Enjoy pair programming — we love to pair"*) is a **delivery mode** that governs every
  lesson: every Say-See-Do or 5E/7E session is a pairing session, and the evidence for it accumulates
  across the course rather than in one module. It will carry standards only if the learner rules that
  pairing itself needs assessing separately from the work done while pairing.

## Dimension X · Crosscutting concepts

The seven NGSS crosscutting concepts, ported. The learner ruled all seven port, correcting this
seat's proposal to swap the fifth for a financial proxy: *"Are you not made of matter? Are you not
consuming so much energy…"* The correction stands as the reason X5 is literal here.

| Code | Concept | In an evaluation platform |
|---|---|---|
| **X1** | Patterns | Anomalous results; a regression's shape; what recurs across runs and across checkpoints |
| **X2** | Cause and effect: mechanism and explanation | Model, harness, data, or infrastructure — the four-way differential the posting names |
| **X3** | Scale, proportion and quantity | Hundreds of evals; signal-to-noise; task count as the uncertainty floor; n of 30–40 for a generalizable claim |
| **X4** | Systems and system models | The eval platform as a system; the harness as a model of a system; what a manifest models about a run |
| **X5** | **Energy and matter: flows, cycles and conservation** | Compute, accelerators, electricity, water and heat flowing through a benchmark run. Energy spent on a rejected request is still spent. Thirty validated items beating three hundred unvalidated ones is an energy claim as much as a validity claim |
| **X6** | Structure and function | Why a harness is shaped the way it is; what each part is for; the dataset / solver / scorer decomposition (register **D1**) |
| **X7** | Stability and change | Regression detection during training; her own note, *"Δ of Δ occurring & Δ' appearing on dashboard"* — the rate of change of the rate of change, surfaced fast enough to act on |

## Cognitive complexity: two tags, not one

Every standard and every objective carries both, at the learner's ruling (*"bloom and webb for sure!"*).

**Bloom's revised** names the *kind* of cognition: remember · understand · apply · analyze ·
evaluate · create. **Webb's depth of knowledge** names the *demand* of the task: DOK 1 recall ·
DOK 2 skill and concept · DOK 3 strategic thinking · DOK 4 extended thinking. They are not the same
axis, which is why both are needed: a *create* task can sit at DOK 2 if the recipe is given, and an
*analyze* task can sit at DOK 4 if it requires sustained investigation across sources.

**Where a standard's level comes from:** the posting's own verb. Build and harden are *create*.
Determine, debug and diagnose are *analyze* into *evaluate*. Characterise is *analyze*. Own is
*evaluate*. Communicate is *understand* into *evaluate*, depending on audience. The mastery standard
sits at the posting's level. The learning progression steps down from it. The baseline sits wherever
the learner actually is, which is a measurement, not an assumption.

---

## The statement grammar

> **[practice verb] + [core idea] + [crosscutting lens]**, in one sentence, describing a doing.

A standard is never "understands X." It is what the learner does, to what, seen through which lens.

### Required fields on every standard

| Field | What it carries |
|---|---|
| **Code** | `REME-<CI>.<n>` |
| **Statement** | One sentence, a doing, per the grammar above |
| **Complexity** | Bloom's level · Webb's DOK level |
| **Dimensions** | The P, CI and X codes it integrates |
| **Clarification** | The posting span it answers to, quoted verbatim (register **A1**) |
| **Assessment boundary** | What is explicitly out of scope, including modality |
| **Evidence statement** | The observable behaviours that count, written so a rater can adjudicate them without interpreting intent |
| **Mastery descriptor** | What good looks like, citing a register entry by ID |
| **Traceability** | Bullet or qualification, plus any representative project |

### Standing assessment boundaries, on every standard in this course

1. **Modality.** The working mode under assessment is **orchestrating AI-assisted coding**: reading,
   directing, verifying, and hand-coding the basic, frequently used commands and functions. No
   standard is evidenced by reproducing syntax from memory, and no instrument requires it.
2. **No evaluative cue inside the content.** No confidence prompt, self-rating, or ability-diagnostic
   framing appears inside or beside a content item on any instrument. Self-assessment is a separate
   item set, administered after the content and before any score is shown. The mechanism the learner
   named is stereotype threat; the rule is therefore about cues, not only about interleaving.
3. **No time pressure unless the standard is time-bound.** One standard family (CI-DIAG) is
   explicitly time-bound because the posting says "within hours"; nowhere else does a clock appear.
4. **Field terms follow constructed concepts.** An instrument may accept a field term; it may never
   require one the course has not yet taught. The learner is a constructivist and has ruled that
   jargon arrives after the concept is built, not before.

### Objectives under a standard

Learning objectives use the Expeditionary Learning **"I can…"** stem, each tagged with Bloom's and
DOK, each tracing to **exactly one** standard, generally climbing the complexity ladder but **not
required to visit every rung** — her ruling, and the same rule governs exit tickets. Where a rung is
skipped the objective set says so, so the progression stays inspectable rather than implied.

### Lesson and instrument rules that follow

- The curriculum runs as **one or more project-based threads**; each lesson teaches and evaluates
  **exactly one objective** and ends in an exit ticket.
- Each lesson is **Say-See-Do** or a **5E/7E** cycle. Where the objective builds a concept, 5E/7E:
  the learner explores the specimen or the failure, constructs and names what is happening in her own
  words, and only then does the Explain phase hand over the field's term. Where the objective is a
  procedure to be seen once and practised, Say-See-Do.
- **The rubric is written against the built instrument**, never against a plan. Her ruling,
  2026-09-20: *"rubric design is done against the built evaluation instrument."* Order: standards →
  evidence plan → build the instrument → write its key or rubric against the built instrument →
  build the lesson that leads to it.
- The **ledger** tracks mastery by standard and carries a two-way glossary: the learner's own name for
  each pattern beside the field's term.

---

## What is not decided here

- **The evidence plan** (which instrument evidences which standard, at what DOK, with what indicator)
  is the next artifact. Webb's four alignment criteria are its check, and Webb is register entry
  **F5**, still pending.
- **Standards for CI-DIST, CI-DASH, CI-OBS, CI-TRN, CI-DIAG, CI-TOOL and CI-VIZ.** CI-PY is written
  first because Baseline B01 already exists to check the standards against.
- **Whether M-PAIR carries standards of its own.**
- **The Claude capability standards** for the application are a separate derivation, from a different
  corpus, and are not in scope here.

*Framework proposed 2026-09-20 by Flaudechamba A.-L. Formative Horizon v01 (Claude Fable 5.1, Opus 5
build pass), from the posting, her highlighted reading of it, her rulings of 2026-09-19 and
2026-09-20, and her own Learning Standards Derivation research. Awaiting her ratification. AIGHVA.*
