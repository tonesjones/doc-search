# Record reviewed live evidence

Live evidence is what an agent or person observed on a running Black Duck SCA instance. It is separate from documentation evidence. A documentation citation says what the docs state; a live observation says what one instance, version, license, and role showed on one date.

## Where records live

- Raw observations: `.local/live-observations/`. Git ignores this folder. Records start as `UNREVIEWED`.
- Reviewed records: `BlackDuck SCA/verification/live-observations/*.json`. Commit a record only after the owner approves it.
- Sandbox details: `.local/live-environment.json` (URL, expected version, label). Git ignores it. Replace it when a sandbox is replaced.

The repository is public. Committed records name no server, username, token, password, or registration key. The validator rejects secret-bearing keys, bearer values, and `*.poc.*` or `*.customer.*` server URLs.

## Record format

Each committed record has these top-level fields: `schema_version`, `observation_id`, `title`, `product`, `product_version`, `observation_date`, `environment`, `principal`, `method`, `review`, `findings`, and `open_gaps`.

Rules the validator enforces:

- `review.status` is `APPROVED`, with `reviewed_by` and `reviewed_at`.
- `method.mode` is `READ_ONLY`, and `method.mutation_check` says how no change was confirmed.
- `environment.sanitized` is true and `environment.customer_data` is false.
- Each finding has a `statement`, a `surface` (`UI` or `API`), an `outcome` (`OBSERVED`, `PARTIAL`, `NOT_TESTED`), and a `scope`. Use `ENVIRONMENT_SPECIFIC` for license- or configuration-dependent values, such as a registration's scan limit.
- `related_cases` must name existing cases in `evaluation/cases/`.
- Each `documentation` entry names an existing corpus page and a verdict: `CONSISTENT`, `OUTDATED_LABELS`, `MISLEADING`, `CONTRADICTED`, or `NOT_COVERED`.

`python -B "BlackDuck SCA/verification/verify.py"` validates every committed record. The DS-06 RBAC case keeps its own format for role and access scenarios.

## What live evidence does not do

Records are outside the evaluation profile's `instruction_files` and `evidence_roots`, so they do not change measured answers or `instruction_revision`. A record does not correct an answer by itself. When a finding shows a documentation page is wrong or misleading, record a feedback candidate after the owner confirms it, and follow [the promotion guide](ds-08-promotion.md).

Write actions (creating objects, running scans, changing roles, signing in as another user) need owner approval each time. The format does not accept them yet; extend it when the first approved write-based check is recorded.
