## D-20260920-07 — Wire the ASAE commit-msg hook, patched so the rater count comes from policy

**Her instruction, verbatim (2026-09-20):** *"i want you to first wire up the hooks in this repo the
way it should be as the asae repo says or if you have more updated and effective instructions run it
by me for approval before using it"*, then after the findings were presented: *"go ahead and proceed
with wiring the hook then roll right into the rest of the asae stages for the first commit bundle"*.

Her ruling on the threshold and roster, same day, which the wiring has to express:

> *"after three parent loops, loops 4 and 5, the number of errors detected dropped very very
> dramatically to nearly 0 for both loops 4 and 5. then, i found that the lever for defect detection
> to pull is on the ind raters. this repo since it's public from jump has one of the more rigorous
> ind rater policies with 2 american and 2 chinese architectures, and 4 distinct architectures total,
> and 2 cheap and smaller models and then followed by 2 less cheap and bigger reasoning models."*

And on the state of the apparatus: *"just follow what i've told you ignore anything on disk that
contradicts."*

**Action:** Copy canonical v11 `commit-msg` into `.githooks/`, apply two marked local patches, write
`.asae-policy` (public, going-public, documentation, strict-3, raters 4), write `.githooks/README.md`
documenting the patches and the known spec-versus-hook drift, and set `core.hooksPath`.

**Method:** Direct file copy and two surgical patches by this seat, verified with `bash -n` and then
by a live refusal test. No model dispatch.

**Repetition:** 6 prior entries share the Method of this seat authoring repository apparatus. New
rationale, and it is the first entry where the artifact is an enforcement mechanism rather than a
document: the correctness criterion is not "reads well" but "refuses what it should refuse," which is
why this entry carries a live negative test rather than a review.

**The problem the patches solve.** Canonical v11 derives rater enforcement from the audit threshold
alone — the rater block fires only at threshold 5 or higher and then demands exactly two raters — and
it parses only three keys from `.asae-policy`. Her ruling is **three parent passes with four raters**.
That shape is not expressible on the shipped ladder: `strict-5` would force two parent passes her own
gate-log audit shows are nearly always empty, and `strict-3` as shipped enforces no raters at all,
which would leave the single highest-value control in the protocol completely unenforced.

**The two patches**, both marked `LOCAL PATCH (edu-python-for-poets, 2026-09-20)` in the source:
1. Parse a `raters:` key from `.asae-policy` beside the existing three.
2. When that key is a positive integer, it sets the required rater count and the rater block runs at
   any threshold. When absent, canonical behaviour is preserved byte-for-byte.

**Alternatives rejected:**
- **Set `strict-5` to obtain rater enforcement.** Rejected: it buys raters by forcing two parent
  passes against her measured finding, and it would still cap the panel at two when she ruled four.
- **Leave the hook unpatched at `strict-3`.** Rejected: it would enforce the axis she found weak and
  ignore the axis she found strong, which inverts the whole point of the wiring.
- **Widen gate-01's scope to include this infrastructure.** Rejected, and the hook itself blocks it:
  Tier 38 refuses a `documentation` domain gate whose staged diff carries code, and the hook is shell.
- **Modify the canonical hook instead of a local copy.** Rejected: canonical propagates to roughly
  eighty consumer repositories and this ruling is specific to this repository.

**Rationale:** her protocol is the requirement and the hook is the backstop. A backstop that enforces
the wrong axis is worse than none, because it produces a green light that means nothing.

**Disclosed deviation — the bootstrap commit uses `--no-verify`.** A commit-msg hook cannot gate its
own installation: the commit that installs it is evaluated by it, and it demands a gate trailer for a
gate that cannot exist yet. This one commit therefore uses the bypass the hook itself documents. It
is recorded here rather than left silent. The infrastructure it installs is not application evidence
and carries no claims; every subsequent commit in this repository passes through the hook for real.

**Verification performed, not asserted:** `bash -n` parses the patched hook clean; `core.hooksPath`
resolves to `.githooks`; and a deliberately malformed commit was **refused** with Rule 2, the refusal
correctly resolving the policy as public / going-public / documentation and requiring strict at
threshold 3 or above. The hook is live.

**Falsifier:** a commit lacking a valid `ASAE-Gate:` trailer is accepted in this repository; or the
`raters:` patch fails to raise the required count, which would show as a gate-01 commit landing with
fewer than four distinct rater agentIds.

Recorded after the wiring by Flaudechamba A.-L. Formative Horizon v01 (Claude Fable 5.1), session
20cd8283, 2026-09-20.
