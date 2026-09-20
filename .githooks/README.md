# Commit-msg hook — local copy, with two documented patches

`commit-msg` is the Martinez Methods canonical **v11** hook, copied 2026-09-20 from
`mm-claude-canonical/.githooks/commit-msg` (source sha256 `69bcb86e6527d013…`), with two local
patches. It is installed by pointing `core.hooksPath` at this directory.

## Why it is patched

Canonical v11 derives independent-rater enforcement from the audit threshold alone: the rater
checks fire only when `audit_threshold` is 5 or higher, and then require exactly two raters. It
also parses only three keys out of `.asae-policy` — `visibility`, `going-public`, and
`audit_threshold`.

Krystal Martinez's ruling for this repository is **three parent passes and a four-rater
cross-architectural drain panel**. That shape cannot be expressed on a single threshold ladder:
asking for `strict-5` to get raters would force two parent passes her own gate-log audit shows are
nearly always empty, and `strict-3` as shipped enforces no raters at all.

## The two patches

1. **Read a `raters:` key from `.asae-policy`.** Added beside the existing three-key parse.
2. **Drive rater enforcement from that count, at any threshold.** When `raters:` is a positive
   integer, it sets the required count and the rater block runs regardless of threshold. When the
   key is absent, canonical behaviour is preserved exactly: threshold 5 or higher implies two
   raters, below that implies none.

Both patch sites are marked `LOCAL PATCH (edu-python-for-poets, 2026-09-20)` in the hook source.
Nothing else in the 3,037 lines is modified.

## Known drift, recorded rather than silently inherited

The ASAE skill cites a machine-readable aspect reference describing hook **v10** with sha256
`a434adab…32492`. That JSON is intact and its hash verifies, but the live canonical hook is **v11**
and hashes differently. The spec and the enforcement layer have diverged. Krystal Martinez has a
separate seat working on the ASAE skill itself; this note exists so the divergence is on the record
here and is not mistaken for a defect in this repository.

## What v11 changed, precisely

Two of its three changes are loosenings and one is a tightening that cannot fire here.

- **D1 — loosening, with a targeted tightening inside it.** The rater counter previously parsed
  only prose `**Rater verdict:**` and `**Rater agentId:**` lines, a regex that a rater-section
  restructure broke three times in one batch. v11 additionally accepts a structured `raters:`
  frontmatter block and takes the maximum of the two counts, so it adds a way to satisfy and never
  a new way to fail. The tightening: when a structured block is present its agentIds must be
  distinct, and a block claiming N raters with fewer distinct IDs is refused even where the prose
  path would have passed. A duplicate agentId is a fabricated attestation.
- **D2 — a genuine tightening that does not apply here.** The stack-rule-pack tier moved from
  advisory to refuse for detected Tauri, Electron and SvelteKit projects. This repository contains
  no such stack, so the tier never fires.
- **D3 — pure forgiveness.** An empty `step_re_execution: []` no longer triggers the requirement
  for a matching commit trailer. The false trigger had cost a real gate a refusal.

## Installing

```bash
git config core.hooksPath .githooks
```

Verify with `git config --get core.hooksPath`. The hook refuses a commit that lacks a well-formed
gate attestation; that refusal is the point.
