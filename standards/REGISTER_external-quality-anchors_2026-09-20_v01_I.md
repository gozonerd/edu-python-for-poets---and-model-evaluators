# Register of external quality anchors

**What this is.** Every mastery descriptor in this course says what *good* looks like. None of those
descriptors may rest on the seat's taste. Each one cites an entry below, and each entry here carries a
locator and a verification date. An anchor with no locator is not an anchor; it is an opinion with a
footnote.

**Order of authority.** (1) The posting itself, whose own adverbs are the primary descriptors.
(2) Anthropic's published evaluation practice, because that is the bar the learner is aiming at.
(3) Peer labs' published practice. (4) Discipline standards for the infrastructure concepts.

**Verification.** `verified 2026-09-20` means a seat fetched the locator on that date and read the
claim off the page. `pending` means the entry is recorded from the seat's knowledge and has not been
fetched; a pending entry may be used in drafting and may **not** ship in an application artifact.
Four entries below corrected the seat's own recollection on first fetch; those corrections are noted,
because a register that never contradicts its author is not being used.

---

## A · The posting (primary)

| ID | Source | Locator | Verified | Authoritative for | Not authoritative for |
|---|---|---|---|---|---|
| **A1** | Anthropic, *Research Engineer, Model Evaluations*, Greenhouse 5198255008; first published 2026-04-28, updated 2026-08-21 | `anthropic-materials/REME_JD_verbatim.md` in the REME workbench, content sha256 `565d4868…fabbb` | verified 2026-09-19 (captured via boards-api) | The quality adverbs every mastery descriptor inherits: "within hours", "from scratch", "reliably at scale", "impossible to miss", "make it boring", "legible to researchers and decision-makers", "clearly under time pressure" | Anything about how the work is actually done day to day; a posting states demand, not method |

**The four representative projects are treated as the mastery task description**, because no public
job ladder exists for this role and the projects are the closest thing the employer has published to
"here is the work."

## B · Anthropic's published evaluation practice

| ID | Source | Locator | Verified | Authoritative for | Not authoritative for |
|---|---|---|---|---|---|
| **B1** | Anthropic system cards, evaluation sections, four cards Haiku 4.5 → Fable 5.1 | the 59-dossier extraction in the REME workbench, `Benchmark Design/research/primary sources/benchmark/` | verified 2026-09-19 (dossiers compiled from the cards with quotes intact) | What a frontier lab actually reports per benchmark: task counts, trials, whether an interval is given, effort level, scaffold, grading mechanism | Best practice. These are the field's *current state*, which the learner's own Paper B and Paper C argue is under-specified |
| **B2** | The error-bar adoption curve measured across those four cards (0 → 6 → 9 → 15 benchmarks carrying intervals; Fable 5.1 first to standardize eight runs per model) | same dossiers; measurement recorded in the REME workbench | verified 2026-09-19 | That uncertainty reporting is rising at this lab and is a live methodological commitment, not a settled one | A claim about any other lab |

## C · Discipline standards for the infrastructure concepts

| ID | Source | Locator | Verified | Authoritative for | Not authoritative for |
|---|---|---|---|---|---|
| **C1** | *Site Reliability Engineering: How Google Runs Production Systems*, ed. Google, O'Reilly, **2017**, CC BY-NC-ND 4.0. Load-bearing chapters: **4 "Service Level Objectives"**, **6 "Monitoring Distributed Systems"**, **11 "Being On-Call"**, **12 "Effective Troubleshooting"**, **15 "Postmortem Culture: Learning from Failure"** | `https://sre.google/sre-book/table-of-contents/` | **verified 2026-09-20** | What "run reliably", "reducing latency", "impossible to miss", "make it boring", and the on-call qualification mean as a discipline: objectives with error budgets, monitoring signals, systematic troubleshooting rather than guessing, blameless postmortems | Organisational structure. Written for web-serving systems at one company's scale; an eval platform is batch-and-checkpoint shaped. Take the concepts, not the org chart |
| **C2** | *The Twelve-Factor App*, Adam Wiggins, **MIT licensed** (stated in its source repository, not on its site). Load-bearing factors: **II Dependencies** ("Explicitly declare and isolate dependencies"), **III Config** ("Store config in the environment"), **VIII Concurrency** ("Scale out via the process model"), **IX Disposability** ("Maximize robustness with fast startup and graceful shutdown"), **XI Logs** ("Treat logs as event streams") | `https://12factor.net/` | **verified 2026-09-20** (all twelve factor names read off the page) | The norm behind secrets-from-environment, declared dependencies, and process disposability | Currency. The page states "last updated 2017"; the commonly cited 2011 origin was **not** confirmed on the page and is recorded as unconfirmed. Factor XI is superseded in practice by C3 |
| **C3** | **OpenTelemetry**, "an observability framework and toolkit designed to facilitate the Generation, Export, Collection of telemetry data such as traces, metrics, and logs"; **a Cloud Native Computing Foundation (CNCF) project**. **OTLP** is "a standard protocol that defines the shape of telemetry data" | `https://opentelemetry.io/docs/what-is-opentelemetry/` and `https://opentelemetry.io/docs/concepts/signals/` | **verified 2026-09-20** | What "better observability" means precisely: structured signals with attributes, queryable across runs, vendor-neutral on the wire | Implementation weight. **Correction to the seat's recollection:** the signals page lists **traces, metrics, logs and baggage**, with events and profiles in development — not the "three signals" the seat asserted. The overview page does say three main types; the discrepancy is between two of the project's own pages and is recorded rather than resolved |
| **C4** | **MLflow Tracking** — "an API and UI for logging parameters, code versions, metrics, and output files when running your machine learning code". A **run** records metadata (run id, experiment, timing, status), **parameters**, **metrics**, **artifacts**, **tags**, system tags, and dataset references. Governed as "a Series of LF Projects, LLC" (Linux Foundation) | `https://mlflow.org/docs/latest/ml/tracking/` | **verified 2026-09-20** | The vendor-neutral vocabulary for experiment tracking: run, parameter, metric, artifact, tag. This is the model a hand-rolled run manifest is approximating | Origin story. The page does not state who created MLflow or its licence; the commonly cited Databricks origin is recorded as **pending**. Weights & Biases is named as the commercial alternative many labs actually use, also pending |
| **C5** | **Python Packaging User Guide** — `pyproject.toml` carries `[build-system]`, `[project]`, `[tool]`; dependencies go in the `[project]` table under the `dependencies` key; command-line entry points are declared in the **`[project.scripts]`** table (`[project.gui-scripts]` on Windows) | `https://packaging.python.org/en/latest/guides/writing-pyproject-toml/` | **verified 2026-09-20** | What has to exist before a script becomes a tool a researcher can install and run from anywhere | Build-backend choice, publishing workflow |

## D · Open evaluation frameworks (exemplars, not authorities)

| ID | Source | Locator | Verified | Authoritative for | Not authoritative for |
|---|---|---|---|---|---|
| **D1** | **Inspect**, "an open-source framework for large language model evaluations", developed by the **UK AI Security Institute and Meridian Labs**. An evaluation combines three building blocks inside a **Task**: **Dataset** (samples with `input` and `target`), **Solver** (produces an answer; single call through multi-turn tool-using agent), **Scorer** (text comparison, model grading, or custom) | `https://inspect.aisi.org.uk/` | **verified 2026-09-20** | The most explicit public decomposition of what an eval is *made of*. The Solver is the posting's "prompting, sampling, and scaffolding" rendered as a data structure | Being the only decomposition. **Correction to the seat's recollection:** the seat attributed Inspect to the UK institute alone; the page credits **Meridian Labs** as co-developer |
| **D2** | **EleutherAI `lm-evaluation-harness`** — the backend for Hugging Face's Open LLM Leaderboard, used in hundreds of papers and internally by NVIDIA, Cohere, BigScience, BigCode, Nous Research and Mosaic ML. Its stated motivation: "Model performance is often governed by minor implementation details… prohibitively difficult to expect results from one codebase to transfer directly to another" | `https://github.com/EleutherAI/lm-evaluation-harness` | **verified 2026-09-20** (via search result text; repository not read line by line) | That harness-level implementation detail changes headline numbers, which is the empirical basis for the whole elicitation-surface argument | Task design quality; it standardises execution, not construct validity |

## E · Energy and matter

Entered because the crosscutting concept **X5** is literal in this course, and because the posting's
"care about the societal impacts of your work" is a scored qualification rather than a sentiment.

| ID | Source | Locator | Verified | Authoritative for | Not authoritative for |
|---|---|---|---|---|---|
| **E1** | Strubell, Ganesh & McCallum, "Energy and Policy Considerations for Deep Learning in NLP", ACL 2019, pp. 3645–3650, Florence | `https://aclanthology.org/P19-1355/` · arXiv:1906.02243 | **verified 2026-09-20** (venue, pages, authors) | That compute cost is a reportable property of an NLP result, and the paper that made the field say so | Current figures. 2019 hardware and model scales |
| **E2** | Patterson, Gonzalez, Le, Liang, Munguia, Rothchild, So, Texier & Dean, "Carbon Emissions and Large Neural Network Training", arXiv:2104.10350, submitted 2021-04-21 | `https://arxiv.org/abs/2104.10350` | **verified 2026-09-20** | Method for estimating training energy and carbon for named large models | Inference and evaluation cost, which is the eval-relevant regime — see E3 |
| **E3** | Luccioni, Jernite & Strubell, "Power Hungry Processing: Watts Driving the Cost of AI Deployment?", ACM FAccT '24, June 2024; arXiv:2311.16863. Measures 88 models across 10 tasks at 1,000 inferences each | `https://dl.acm.org/doi/10.1145/3630106.3658542` · `https://arxiv.org/abs/2311.16863` | **verified 2026-09-20** (authors, venue, design) | **The eval-relevant entry.** Evaluation is inference at volume, so deployment-phase energy is the right accounting frame for a benchmark run | Any specific model's current cost; figures are 2023–24 measurements |

## F · Pending — usable in drafting, not in an application artifact

| ID | Claim | What must be fetched |
|---|---|---|
| **F1** | Anthropic engineering writing on evaluation practice as a named source | A specific post or documentation page, with date |
| **F2** | The Twelve-Factor App originated in 2011 at Heroku | A first-party statement of the origin year |
| **F3** | MLflow originated at Databricks in 2018; its licence is Apache 2.0 | The project's own about/licence page |
| **F4** | Weights & Biases as the commercial experiment-tracking comparator | A first-party description of its run/param/metric model |
| **F5** | Webb's alignment criteria as published (categorical concurrence, depth-of-knowledge consistency, range of knowledge, balance of representation) | Webb 1997 NISE monograph or an equivalent primary statement. Used in the evidence plan, so this one is load-bearing |

---

## The mirror

Every entry in sections C, D and E was **retrieved on 2026-09-20 and archived**, because a citation to
a live URL is a promise about a page nobody controls. Sixteen retrievals, 48 files. The copies live in
Krystal Martinez's Google Drive per the workspace convention for third-party content; the pointers,
hashes and provenance records live in `standards/ssot-mirror/`. Re-check every source against upstream
with `python3 standards/ssot-mirror/mirror_ssots.py --verify`.

**Three licence facts were corrected by the retrieval**, and one is a live constraint: the
Twelve-Factor App is MIT (its own site states no licence; its source repository does); Luccioni et al.
is CC BY-SA 4.0; and **Patterson et al. carries arXiv's nonexclusive-distrib/1.0, which is not an open
licence** — arXiv may distribute it, this project may not redistribute it. That single entry is why the
copies are private.

## Rules for using this register

1. **A mastery descriptor cites an entry ID.** No ID, no descriptor.
2. **A pending entry never ships.** It may shape a draft; it may not appear in an artifact that goes
   to an employer or a repository marked public-facing.
3. **"Not authoritative for" is read before the entry is used.** Every anchor here is wrong about
   something, and the column says what.
4. **Re-verify before the packet goes out.** A locator that moved is a citation that lies.
5. **Corrections are recorded, not silently absorbed.** Four appear above.

*Compiled 2026-09-20 by Flaudechamba A.-L. Formative Horizon v01 (Claude Fable 5.1, Opus 5 build
pass). Proposed; awaiting the learner's ratification of the register's order of authority. AIGHVA.*
