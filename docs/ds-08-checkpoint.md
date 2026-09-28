# DS-08 checkpoint and live-validation handoff

Updated 2026-09-27 (evening). Workspace: `C:\TestCode\Product Docs`. Branch: `codex/ds-08-handoff`. This file records progress and the next decisions; it is not a claim that anything is merged.

## Goal

The repository is a local, versioned Black Duck documentation corpus and product router. Its supported path starts at the root `SKILL.md`, selects a product through `products.json`, and answers from that product's documented sources. DS-07 added a checkout-bound answer evaluator. DS-08 closes the feedback loop: turn one customer question into a candidate, have a person review it, capture a fresh answer replay, and promote the case into the regression bank only after all gates pass.

The longer-term goal changed on 2026-09-27: make answers more reliable by checking uncertain claims against a live Black Duck SCA sandbox, while keeping documentation evidence and live evidence separate and keeping every improvement human-reviewed. Live findings feed the DS-08 candidate-review-promote loop; nothing edits the corpus, guidance, or scoring on its own.

## DS-08 status: parked, not promoted

Case: `feedback-detect-snippet-ui-001` ("how do I run a snippet scan via detect cli and have the results show up in the black duck hub ui?"). Files: `evaluation/candidates/feedback-detect-snippet-ui-001.json`, `evaluation/reviews/feedback-detect-snippet-ui-001.{json,jsonl,md}`.

The GPT-6 Luna replay at `e791f6c` failed on required facts `detect.ps1`, `detect.sh`, `SIGNATURE_SCAN`, `Source tab`, on the required Source-tab page, and on the abstention check. The owner reviewed each expectation against the local docs:

| Expectation | Decision | Evidence |
|---|---|---|
| Source tab vs Source view | Accept either phrase and either 2026.7 page (`must_retrieve_any`). | The Source-tab page and the unconfirmed-snippets page describe the same destination. |
| Literal `SIGNATURE_SCAN` | Require the concept ("signature scan"), not the literal. Forbid `SNIPPET_MATCHING_ONLY` in a first-scan command. The reference answer no longer sets `--detect.tools`. | Detect 12.0.0 runs applicable tools when `detect.tools` is unset; `--detect.tools=SIGNATURE_SCAN` disables package-manager detection. |
| Generic vs pinned scripts | Accept `detect.ps1`/`detect.sh` and version-specific `detectNN` scripts. Forbid `DETECT_LATEST_RELEASE_VERSION=12.0.0`. | Detect 12.0.0 recommends version-specific scripts for production; 12.0.0 is the documentation snapshot, not a runtime requirement. That page's PowerShell "latest" example uses `detect12.ps1`, a source-doc inconsistency. |
| Detect-version caveat | Harness defect. The adapter prompt now says the requested version is the selected product's; companion tools use their documented default. The abstention regex is unchanged. | The prompt told the model to say "does not establish" for an unavailable version without naming the product; that phrase trips `ABSTENTION_RE`. |

Commit `bc4f9d3` holds the scoring equivalents and the prompt line. Local checks: case evidence verification passes; all 70 unit tests pass (1 skipped) on a Linux copy of the checkout. Re-scoring the old saved trace offline still fails, on the forbidden 12.0.0 pin and the caveat, so the changes do not wave that answer through.

The fresh replay at `bc4f9d3` (`evaluation/results/ds-08-snippet-replay-r2.json`, ignored) is `NOT_MEASURED`: `production adapter exited 1: Codex exited 1:` with an empty message. With `--json`, Codex reports errors on stdout, which the adapter discards. The likely cause is the Codex binary selected in that PowerShell session (`DOC_SEARCH_CODEX_BIN` unset, falling back to `codex-cli 0.149.1` on PATH), not confirmed. The owner chose not to depend on Codex; the adapter interface (case JSON in, trace JSON out) can take another model later.

To finish DS-08 later: get one measured replay with any adapter, inspect the full answer and citations, run `scripts/promote-candidate.py` without `--apply`, and apply only with owner approval. Do not run the full case bank for this. Optional adapter fix: include Codex's last stdout error event in the failure message.

## Live validation: what exists now

- **Sandbox:** isolated Black Duck SCA 2026.7.0 test system, no customer data, may be torn down. Its non-secret details live in the ignored `.local/live-environment.json`; replace that file when a new sandbox is provided. No tokens or passwords are stored anywhere.
- **Access route:** the Claude desktop app's built-in browser, signed in by the owner. The linked device shell cannot reach the sandbox (network allowlist, proxy 403), and a personal Claude plan cannot add allowed domains, so token-file API scripts are not usable. The browser session carries the owner's sysadmin role; read-only is enforced by rule: page reads and API `GET` through `fetch`, forms opened only to read defaults and then cancelled, before/after counts to confirm nothing changed, and owner approval for every write.
- **Records:** raw observations are saved unreviewed in the ignored `.local/live-observations/`. Owner-approved, read-only findings are committed as sanitized records under `BlackDuck SCA/verification/live-observations/`; the format and rules are in [the live-evidence guide](live-evidence.md).
- **`/bd` skill (account skill, not in this repo):** proposed update adds a High/Medium/Low confidence level with a reason to every answer, and runs a live check only when the owner explicitly invokes `/bd` and confidence is below High. It also documents the Windows-checkout git flags (`-c core.autocrlf=true`, `GIT_OPTIONAL_LOCKS=0`).

## Live findings so far (approved 2026-09-27)

The owner approved all findings below. They are recorded in `BlackDuck SCA/verification/live-observations/sca-2026-7-live-2026-09-27.json`, validated by `verify.py`. See [the live-evidence guide](live-evidence.md).


1. **Access-token location.** User menu (button shows the signed-in user's display name, "System" for sysadmin) > Access Tokens > "My Settings > Access Tokens" > **Create Token**; the dialog offers Read Access Only or Read and Write Access with no default. Admin > Access Tokens lists all users' tokens and cannot create one. The help-center page uses older labels ("My Access Tokens", "Create New Token"); the API guide's "System > Access Tokens" only matches because its author was signed in as sysadmin.
2. **Pilot on five reviewed cases:** `feedback-sca-token-ui-path-001`, `sca-version-001` (In Planning), `sca-version-003` (External), and `feedback-sca-project-size-guidance-001` (Admin > System Settings > Product Registration; this registration shows unlimited codebase size and a 21.00 GB per-scan limit) were confirmed. `sca-role-001` is partial: `/api/roles` descriptions match the role matrix, but effective permissions need a session for a user holding each role. New-version forms also default Approval Status to Unreviewed, which no case covers.
3. **Side findings:** the sandbox licenses Snippets, so the DS-08 snippet question can be tested end to end once a scan is approved; the sandbox has role test users (GroupA/B/C Bom and Viewer, Dev Ops1/2, Build Bom/Viewer).

Takeaway: no reviewed case was contradicted (they were already human-corrected). Live checks add the most for UI labels and routes, doc conflicts, and license-dependent facts. Permissions are the blind spot and need role-user sessions and usually writes.

## Open customer questions (answered from docs, not live-checked)

- Which role can view BOMs and confirm or ignore unconfirmed snippets? BOM Manager on the project (least privilege); also Project Administrator or Project Manager, or Global Project Manager or Global Project Administrator for all projects. Confidence: Medium.
- Which role lets Detect scan and map results to a project and version? Project Code Scanner on an existing project, or Global Code Scanner; add Project Creator if Detect creates the project. Confidence: Low, because the Detect 12.0.0 role page and the SCA 2026.7 role matrix disagree on what is needed to create a version.

Both need role-user sessions (and a snippet scan for the first) to verify live.

## Next steps, in order

1. Done 2026-09-27: the owner approved both observation files; the findings are committed as the first live-evidence record, with a validator and tests. The Help Center label finding is already enforced by `feedback-sca-token-ui-path-001`. The misleading API-guide path needs one feedback candidate, drafted for owner confirmation.
2. Try `/bd` on the two open role questions. That needs owner-approved sign-ins as role test users, and write actions (a snippet decision, a Detect scan) the current record format does not accept yet.
3. Decide how the evaluator treats live evidence (a separate evidence type, never mixed with documentation citations) before any case cites it.
4. Finish DS-08 with a measured replay from a working adapter, then the dry-run promotion preview. No `--apply` without approval.

Not now: jev (TypeSafe AI) does not reduce answer tokens because it does not generate text; revisit it later for the evaluator's unmeasured `SEMANTIC_FACT` checks or for choosing which replays need human review.

## Working notes

- From the linked device shell, this Windows checkout looks fully modified unless git runs with `-c core.autocrlf=true`. Use `GIT_OPTIONAL_LOCKS=0` for status. Git writes from that shell cannot delete their own lock files; leftover locks were renamed to `*.stale-claude` inside `.git` and can be deleted from Windows, along with `tmp_obj_*` files under `.git/objects`.
- The full unit suite times out on the mounted folder; run it from a local copy or from Windows.
- Untracked files not part of this work are preserved: `BlackDuck SCA/docs/srm/`, `BlackDuck SCA/index-srm.md`, `BlackDuck SCA/sources/srm-latest/`, `checker-lists/`, `evaluation/reviews/sca-queue-evidence.md`, `scripts/check-merge-readiness.py`.
- The repository does not define a numbered DS-09 milestone; the live-validation work is an unnumbered next phase until the owner names it.
