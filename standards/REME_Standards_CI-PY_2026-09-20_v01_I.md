# REME mastery standards — CI-PY · Python as research infrastructure

**Core idea.** Python as the material an evaluation harness is made of. Scoped by the posting's use of
it and by nothing wider: `JD_LEARN_INVENTORY_modular_2026-09-19_v01_I.md`, module M-PY.

**Grammar, fields, complexity tags and standing assessment boundaries:**
`REME_Learning_Standards_Framework_2026-09-20_v01_I.md`. **Quality anchors cited by ID:**
`REGISTER_external-quality-anchors_2026-09-20_v01_I.md`.

**Why five.** Not chosen. The posting names one minimum qualification here, "Strong Python
programming skills, including production or research infrastructure," and then spends four
responsibility bullets and two representative projects saying what that qualification is *for*:
reading an unfamiliar harness, hardening one, diagnosing one mid-run, making runs comparable, and
handing the result to another researcher. Those are five distinct doings with five distinct evidence
shapes. PY.5 sits on the CI-PY / CI-TOOL boundary and says so.

**Status: proposed.** Every statement, level and descriptor below awaits the learner's ratification.

---

## REME-PY.1 · Account for an unfamiliar harness from its source

> **Statement.** Read the source of an evaluation harness you did not write and account for its
> architecture: name each part, say what it carries, and state the decision each part encodes.

| | |
|---|---|
| **Complexity** | Bloom's **analyze** · Webb's **DOK 3** |
| **Dimensions** | P6 · CI-PY · **X6** structure and function |
| **Clarification** | "Strong Python programming skills, including production or research infrastructure" · "Improve the tooling, libraries, and workflows researchers use to implement and iterate on evaluations" |
| **Assessment boundary** | Single-file or small-package harnesses; cross-machine architecture is CI-DIST. Reading and accounting, not modification, which is PY.2. Standing boundaries 1–4 apply: no syntax reproduced from memory, no evaluative cue inside the content, no clock, no required field term |
| **Mastery descriptor** | The account is *systematic rather than narrative*: it proceeds by part, distinguishes what a part does from why it is there, and separates what the source states from what the reader inferred. The standard for systematic-over-guessing is **C1** ch. 12 "Effective Troubleshooting". A mastery account also names the harness's three evaluation organs where they exist — what supplies the samples, what produces the answer, what grades it — the decomposition **D1** makes explicit |
| **Evidence statement** | Given a harness the learner has not read: (a) every top-level part is named and its cargo stated; (b) at least three parts have their encoded decision stated, not merely their behaviour; (c) at least one inference is marked as an inference; (d) no claim contradicts the source. Adjudicable by a rater holding the source |
| **Traceability** | Minimum qualification 1 · responsibility bullet 5 · representative project 3 |

**Objectives**

- **PY.1.a** I can name every top-level part of a harness I did not write and say what each one
  carries. *(understand · DOK 2)*
- **PY.1.b** I can trace one request from the flag that configures it to the file that records its
  answer. *(apply · DOK 2)*
- **PY.1.c** I can state, for a part of a harness, the decision its author encoded there and what the
  alternative would have cost. *(analyze · DOK 3)*
- **PY.1.d** I can separate, in my own account of a harness, what the source says from what I
  inferred. *(analyze · DOK 3)*

*Rungs skipped: remember. Nothing in this standard is evidenced by recall of syntax or API names.*

---

## REME-PY.2 · Direct a hardening change, and state its cost

> **Statement.** Direct a change to a harness that removes a named failure mode without introducing
> another, and state what the change costs in time, compute and energy.

| | |
|---|---|
| **Complexity** | Bloom's **create** (via evaluate) · Webb's **DOK 3** |
| **Dimensions** | P3 · CI-PY · **X7** stability and change · **X5** energy and matter |
| **Clarification** | "Build and harden the distributed eval execution platform so hundreds of evals run reliably" · "Take a flaky distributed eval pipeline and make it boring — better retries, better observability, faster feedback to researchers" |
| **Assessment boundary** | Single-process hardening: retries, backoff, timeouts, fallback ladders, configuration, disposability. Multi-machine coordination is CI-DIST. The learner directs the change and states its consequence; producing the diff is not required and is not evidence either way |
| **Mastery descriptor** | "Boring" is the target and it is a defined state, not a mood: failures are handled by policy rather than by attention, and the policy is stated. **C1** ch. 4 supplies the frame that reliability is a chosen objective with a budget, not a maximum. **C2** III and IX supply the norms for configuration and disposability. The cost half of the standard is anchored at **E3**: evaluation is inference at volume, so a run's energy is a reportable property of it, and energy spent on a rejected request is spent |
| **Evidence statement** | Given a harness and a named failure mode: (a) the change is stated precisely enough for another person to implement it; (b) the failure mode it removes is named; (c) at least one failure mode the change could introduce is named and addressed or accepted out loud; (d) the cost is stated in a unit that can be checked — wall-clock, requests, tokens, or energy — rather than as "cheap" or "expensive" |
| **Traceability** | Responsibility bullet 2 · representative project 3 |

**Objectives**

- **PY.2.a** I can say what makes a request safe to retry, and name one that is not. *(understand ·
  DOK 2)*
- **PY.2.b** I can read a backoff schedule off its code and say what it will do in the first minute
  of an outage. *(apply · DOK 2)*
- **PY.2.c** I can choose between pacing a harness and running it concurrently by naming the property
  of the provider that decides it. *(evaluate · DOK 3)*
- **PY.2.d** I can direct a hardening change and name the failure mode it might introduce. *(create ·
  DOK 3)*
- **PY.2.e** I can state what a proposed eval run will consume and justify or reduce it. *(evaluate ·
  DOK 3)*

*Rungs skipped: remember. Analyze is folded into 2.c, where choosing requires the comparison.*

---

## REME-PY.3 · Diagnose a failed run from its own records

> **Statement.** Diagnose, from a failed run's own records, whether the cause sits in the request's
> configuration, the provider, or the handling of the response, and direct the one change that
> addresses the cause rather than the symptom.

| | |
|---|---|
| **Complexity** | Bloom's **analyze** into **evaluate** · Webb's **DOK 3** |
| **Dimensions** | P5 · CI-PY · **X2** cause and effect |
| **Clarification** | "Debug anomalous eval results mid-training-run, determine whether the cause is a model change or an infrastructure issue, and communicate the answer clearly under time pressure" |
| **Assessment boundary** | Single-process causes. The posting's full four-way differential — model, harness, data, infrastructure — belongs to **CI-DIAG**; this standard is its harness-local prerequisite. **This is the one standard family whose instruments may be time-bound**, because the posting says "within hours"; the time bound is disclosed on the instrument in advance and is never a surprise |
| **Mastery descriptor** | The diagnosis names the *originating* part, not the part where the failure surfaced, and cites the record line that distinguishes them. **C1** ch. 12 is the anchor: a systematic method beats a plausible story, and the difference is whether the evidence could have come out otherwise. A mastery diagnosis also names what was recorded *before* the failure that made the diagnosis possible at all |
| **Evidence statement** | Given a run directory containing a log, a raw response and a manifest: (a) the originating part is named; (b) the specific record line that shows it is quoted; (c) the symptom location is distinguished from the cause location where they differ; (d) one change is directed, and it addresses the cause; (e) where the records are insufficient to decide, that is said rather than guessed |
| **Traceability** | Responsibility bullet 4 · representative project 2 |

**Objectives**

- **PY.3.a** I can say which files a harness has already written by the time it crashes, and why.
  *(understand · DOK 2)*
- **PY.3.b** I can read a traceback and name the part of the call it failed inside. *(apply · DOK 2)*
- **PY.3.c** I can tell a failure's symptom from its cause when they sit in different parts, and cite
  the line that separates them. *(analyze · DOK 3)*
- **PY.3.d** I can say when a run's records are not sufficient to decide the cause, and name what
  would have to have been recorded. *(evaluate · DOK 3)*

*Rungs skipped: remember, create. Directing the fix is the tail of 3.c and 3.d, not a separate build.*

---

## REME-PY.4 · Specify what a run must record to be comparable later

> **Statement.** Specify what a harness must record about a run so that two runs can be compared
> weeks later and the comparison can be defended.

| | |
|---|---|
| **Complexity** | Bloom's **create** · Webb's **DOK 4** |
| **Dimensions** | P8 · CI-PY · **X4** systems and system models · **X1** patterns |
| **Clarification** | "Run experiments to characterize how prompting, sampling, and scaffolding choices affect results on internal and industry benchmarks" · "validate against known signals" · "Experience with observability, monitoring, or experiment-tracking systems" |
| **Assessment boundary** | What must be *recorded* and why, not which tool records it; tool selection is CI-OBS. Statistical treatment of the resulting comparison is out: that is the learner's own Paper B territory and is parked by her ruling. DOK 4 because the specification has to survive a case the learner constructs against it |
| **Mastery descriptor** | The specification covers the whole surface that can move a number, not only the settings the harness happens to expose. **C4** supplies the vendor-neutral vocabulary a run record is approximating — run, parameter, metric, artifact, tag — and **C3** supplies the standard for structured, queryable signals rather than prose logs. **D2** supplies the empirical reason this matters: harness-level implementation detail changes headline numbers, which is why "same model, same benchmark" is not a specification. A mastery specification also names at least one thing that can still differ between two runs whose records match |
| **Evidence statement** | Given a harness and a comparison someone wants to make: (a) the record specification names the model identity, the elicitation surface (prompt, sampling settings, scaffold), the input identity, and the outcome; (b) each field is justified by what it would let a reader rule out; (c) at least one residual source of difference is named and accepted; (d) the specification is checked against an actual past run and any field that run could not supply is flagged |
| **Traceability** | Responsibility bullet 7 · preferred qualification 4 · representative project 1 |

**Objectives**

- **PY.4.a** I can list what a harness already records about a run without being told where to look.
  *(understand · DOK 2)*
- **PY.4.b** I can say, for a recorded field, which question it lets a later reader answer. *(analyze
  · DOK 3)*
- **PY.4.c** I can specify the record a run needs so that a later comparison is defensible, and name
  what could still differ. *(create · DOK 4)*

*Rungs skipped: remember, apply, evaluate. The evaluation is inside 4.c, where the specification has
to be argued against a residual case.*

---

## REME-PY.5 · Shape a working program into a tool another researcher can use

> **Statement.** Shape a working program into a tool another researcher can install and run from
> anywhere, and say what the shaping buys that correctness alone does not.

| | |
|---|---|
| **Complexity** | Bloom's **create** · Webb's **DOK 3** |
| **Dimensions** | P6 · CI-PY / **CI-TOOL** · **X6** structure and function |
| **Clarification** | "Improve the tooling, libraries, and workflows researchers use to implement and iterate on evaluations" · "faster feedback to researchers" |
| **Assessment boundary** | Local installability and interface shape. Publishing, release process and distribution are out. **Boundary note:** this standard sits on the CI-PY / CI-TOOL line. It is written here because Baseline B01 already measures it (concept B8) and a measured concept with no standard is a categorical-concurrence failure. When CI-TOOL is derived, ownership is reconciled and this note is the marker |
| **Mastery descriptor** | The artefact declares what it needs and how it is invoked, rather than relying on the runner's knowledge of a folder. **C5** is the concrete anchor: `[project]` with a `dependencies` key, `[project.scripts]` for the command, `[build-system]` for the backend. **C2** II supplies the norm — dependencies declared and isolated. Mastery includes the *why*: a tool that must be run from one directory with a long path is a workflow tax, and the posting's clause is about what researchers iterate with |
| **Evidence statement** | Given a working script: (a) the two things that must exist for it to install as a command are named; (b) the invocation a researcher would type is written; (c) the dependency situation is stated accurately, including "none beyond the standard library" where true; (d) the benefit is argued in terms of another person's iteration, not the author's tidiness |
| **Traceability** | Responsibility bullet 5 · representative project 3 |

**Objectives**

- **PY.5.a** I can say what makes a script a tool rather than a file. *(understand · DOK 2)*
- **PY.5.b** I can name what has to exist for a program to be installed and run as a command. *(apply
  · DOK 2)*
- **PY.5.c** I can specify the interface a researcher would meet, and defend it against the way I
  would use the tool myself. *(create · DOK 3)*

*Rungs skipped: remember, analyze, evaluate.*

---

## Coverage check against Baseline B01

B01 was built before these standards existed, which is the wrong order and is recorded as such in
`Decisions/Decision Logs/claude/D-20260919-02…`. It is kept because it was built from the same
posting scope, and it now serves as the check on whether these standards describe something an
instrument can actually reach.

| B01 concept | Standard | Note |
|---|---|---|
| A1 modules and imports | PY.1 | |
| A2 entry point and arguments | PY.1, PY.5 | the entry-point item does double duty |
| A3 functions and return values | PY.1 | |
| A4 nested data structures | PY.1 | |
| A5 loops and early exit | PY.1 | |
| A6 files, paths and encodings | PY.1 | |
| A7 reading a traceback | PY.3 | |
| B1 configuration and secrets | PY.1, PY.2 | structure in PY.1, the norm in PY.2 |
| B2 exceptions as routing | PY.1, PY.3 | |
| B3 retries and backoff | PY.2 | |
| B4 bank before parse | PY.2, PY.3 | it is what makes PY.3 possible at all |
| B5 observability from inside | PY.4 | |
| B6 sequential versus concurrent | PY.2 | carries the X5 energy content |
| B7 process lifecycle | PY.2, PY.3 | |
| B8 package and CLI shape | PY.5 | the reason PY.5 is written here |
| B9 reproducibility knobs | PY.4 | |

**Findings from the check, stated rather than smoothed:**

1. **Every B01 concept maps to a standard.** Categorical concurrence holds in that direction.
2. **PY.1 carries seven of sixteen items.** That is a balance-of-representation warning: Band A is
   over-weighted relative to its share of the mastery construct. B01 measures reading more heavily
   than the standards value it. This is defensible for a *baseline*, whose job is to decide where the
   strand starts, and it must not be repeated in the strand's exit instruments.
3. **PY.4 is a DOK 4 standard measured by two DOK 2–3 items.** Depth-of-knowledge consistency fails
   here. B01 cannot evidence PY.4 at mastery, and no scoring of B01 should be read as doing so. The
   performance task is where PY.4 gets evidenced.
4. **No B01 item touches the cost half of PY.2.** Item B6 names the concurrency decision but asks for
   the provider property, not the consumption. The parallel form should carry it.
5. **PY.5's home is unresolved** until CI-TOOL is derived.

Findings 2, 3 and 4 are inputs to the evidence plan, not defects to be patched by editing B01 now.

*Standards proposed 2026-09-20 by Flaudechamba A.-L. Formative Horizon v01 (Claude Fable 5.1, Opus 5
build pass). Derived anchors-first from the posting, checked against Baseline B01, every mastery
descriptor citing a verified register entry. Awaiting the learner's ratification of each statement,
level and descriptor. AIGHVA.*
