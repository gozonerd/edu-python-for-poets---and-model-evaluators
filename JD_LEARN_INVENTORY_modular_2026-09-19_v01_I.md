# JD learn inventory — every span Krystal Martinez marked as something to learn, kept modular

**Source posting:** Anthropic, *Research Engineer, Model Evaluations*, Greenhouse 5198255008
(first published 2026-04-28, updated 2026-08-21). Spans below are quoted verbatim from the posting.
**Source of the classes and notes:** her highlighted printout of the posting, read 2026-09-19, and
the legend she typed the same day, which governs:

> pink + orange + purple + green + teal = must learn or review or practice using learning experience
> generator playbook · purple = the above AND must learn conceptually and must put conceptual
> learning into practice · green = have experience at this with humans + need to share these
> experiences · yellow = I got this in spades 😎 · teal = I have a great anecdote for this that
> should probs go in the app somewhere

Yellow spans are excluded here by her legend. Two spans she left unhighlighted are listed at the end.

**Rule for this file:** modules stay distinct. Nothing here says how they integrate; that is the
learning-experience design session. The **verb** column is this seat's proposed reading of her colour
plus her note, marked ⟨proposed⟩ until she ratifies each one. **JD's use** scopes each module to what
the posting actually asks for, so no baseline or lesson drifts into the topic in general.

| Module | JD span (verbatim; her highlight in bold) | Her colour | Her note (verbatim) | Verb ⟨proposed⟩ | JD's use of the topic (scope) | Baseline |
|---|---|---|---|---|---|---|
| **M-PY** · Python for research infrastructure | "**Strong Python programming skills, including production or research infrastructure**" (minimum qualification) | purple | "Python for Poets" | refresh the basics she reads already · learn conceptually the infrastructure patterns · practice by directing | Python as the material of an eval harness: "build and harden the distributed eval execution platform"; "improve the tooling, libraries, and workflows researchers use to implement and iterate on evaluations"; "better retries, better observability, faster feedback"; "implement the scoring", "build the dataset". Not: hand-typed syntax, general-purpose trivia, libraries the posting does not name. | **B01, 2026-09-19** |
| **M-SELF** · Her own programs, taught back to her | (note under *Minimum qualifications*, no span) | purple, by her ruling | "* Have Claude teach me about my python programs, infra architecture + architectural decisions made through SSD interactive artifacts" | learn conceptually, on her own artifacts | The evidence base for M-PY and M-DIST: the programs she has orchestrated are the specimens, and the architectural decisions in them are the content. | folded into B01's specimen choice |
| **M-DIST** · Distributed eval execution | "**Build and harden the distributed eval execution platform so hundreds of evals run reliably against checkpoints throughout production RL training runs**" (the word *distributed* circled) · "**Experience building or operating distributed systems, data pipelines, or other infrastructure that needs to be reliable at scale**" | orange · green | "across machines, cloud environments" · "learning exp. generator" · "capstone = cross machine + local [?] environ" · "+ capstone bonus = across cloud env" · "I have it w/ the people pre-AI version" | learn the machine version · practice as transfer from the human-systems version she has | Many evals, many checkpoints, one platform, reliability under a live training run. Her capstone note sets the shape: cross-machine plus local first, cloud as the bonus. Not: cloud vendor certification, Kubernetes for its own sake. | — |
| **M-DASH** · Model-health dashboards | "Own the dashboards researchers and leadership use to monitor **model health** during training, **improving signal-to-noise, reducing latency, and making regressions impossible to miss**" | orange | "actionable data (formative evals) ↓ Δ of Δ occurring & Δ' appearing on dashboard" | refresh (she has used dashboards heavily, not recently) · learn the during-training context | A dashboard as a formative instrument: the change in the change, surfaced fast enough to act on, with regressions impossible to miss. Not: BI tooling in general. | — |
| **M-OBS** · Observability, monitoring, experiment tracking | "Experience with **observability, monitoring, or experiment-tracking systems**" | orange | — | learn | What the platform records about itself so that "a flaky distributed eval pipeline" can be made "boring" and so two runs can be compared a week later. | — |
| **M-TRN** · ML training infrastructure | "**Experience running or supporting ML training infrastructure**" | orange | — | learn | Enough of the training loop, checkpoints and RL runs to know what the evals are running against and when. Not: training models. | — |
| **M-DIAG** · Model change or infrastructure issue | "determine whether the cause is a model **change or an infrastructure issue**" · representative project two: "determine within hours whether it's the model, the harness, the data, or the infrastructure" | pink | — | learn, then practice inside the project loops | A four-way differential diagnosis under time pressure, communicated clearly. Not: general debugging. | — |
| **M-TOOL** · Tooling researchers iterate with | "**Improve the tooling, libraries, and workflows researchers use to implement and iterate on evaluations**" | green | — | practice as transfer from the human version · share the experience | Tools whose users are researchers iterating on evals; the CLI-package gift belongs here. | — |
| **M-PAIR** · Pair programming | "**Enjoy pair programming — we love to pair**" | purple | — | learn conceptually · practice | Pairing as the posting means it: two people, one problem, live. Every Say-See-Do session is a rehearsal. | — |
| **M-VIZ** · Visualizations legible to decision-makers | "**produce visualizations that make the results legible to researchers and decision-makers**" · representative project one: "ship a dashboard that makes the result legible" | teal | — | share the anecdote · practice on the trajectory visual | Legibility to a named reader, not chart-making. | — |

## Spans she left unhighlighted

| JD span (verbatim) | Status |
|---|---|
| "Design and run new evaluations of Claude's capabilities — reasoning, agentic behavior, knowledge, safety properties" | not highlighted; the benchmark-design work already under way covers it |
| "Comfort operating in an on-call or production-support capacity when training runs are live" | not highlighted; resolved in conversation the same day: yes |

## Counts

Ten modules from eight highlighted spans plus one handwritten note. Four orange, one pink, three
purple (two spans and the note), two green, one teal. Two of the ten (M-DIST, M-TOOL) carry her
statement that the human-systems version of the experience already exists.

*Compiled 2026-09-19 by Flaudechamba A.-L. Formative Horizon v01 (Claude Fable 5.1) from the posting
and her highlighted copy. Verbs are proposed, not ratified. AIGHVA.*
