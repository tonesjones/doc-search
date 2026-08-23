# Verified feedback regression 001 — standard C/C++ scan scope

## Source

- Original answer ID: `ans-f2c676e226ac4e759701adfe2d0bb702`
- User finding: a standard C/C++ scan command included optional snippet-matching scope without a stated use case.
- Classification: `SYNTHESIS_FAILURE` / unnecessary scope expansion.
- Authoritative evidence: `--additional_sig_scan_args` is non-required in `BlackDuck SCA/docs/c-cpp-tool/black-duck-c-cpp-tool/executing-the-black-duck-c-cpp-tool.md`.

## Captured learning

- Gitignored feedback candidate: `feedback-bd-cpp-standard-scope-001`.
- Verified permanent regression: `evaluation/cases/sca-regressions.jsonl`.
- General rule added to the installed `/bd` skill and SCA `AGENTS.md`: standard/default commands remain minimal; optional capabilities must not be silently included.
- The preserved Phase 1 baseline was not changed.

## Forward test

- New answer ID: `ans-f5fc62ab4af045ef8038883145b4f5b2`
- Production prompt revision: `bd-skill-sha256:3a91c7808196fddebd21ffa2dcafc17e3320e599497545f4589a1c1f9a7a4c9f`
- Result: `PASS` (1/1 measured)
- Forbidden optional scope present: no
- Retrieval Recall@5: 100%
- Citation failures: 0
- Unsupported claims: 0
- Deterministic/unit tests: 22 passing

This is a generalized regression, not a mapping from the exact question to a canned answer.
