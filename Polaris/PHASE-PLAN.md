# Polaris corpus — phased scrape plan

**Scope:** Current Polaris Platform documentation. Polaris CI material is reused from the completed Bridge corpus at `C:\TestCode\BlackDuck SCA`.  
**Source mode:** Mutable `latest` documentation; capture timestamps and content hashes.

## Phase 0 — Scaffold and source discovery

- [x] Create local corpus structure and generic tooling.
- [x] Add RAG rules, durable checkpoint, phase plan, and validation.
- [x] Verify the Polaris Platform map ID (`5MMaMfDebQ2sCji2eI3ezg`).
- [x] Initialize the Platform TOC (182 topics).
- [x] Smoke-scrape representative content (tables, code, nested pages).

## Phase 1 — Foundation and onboarding

- Product overview and data model
- UI overview, roles, subscriptions, and access
- Getting-started content by user role
- Terminology and support information

**Status:** complete.

## Phase 2 — Testing workflows

- SAST and Rapid Scan Static
- SCA package, signature, and binary analysis
- DAST, fAST Dynamic, and secure tunnels
- Test artifacts, tool versions, and troubleshooting

**Status:** complete.

## Phase 3 — Findings and governance

- Issues, triage, approvals, and policy types
- Components, licenses, and copyright management
- Dashboards, reports, SBOMs, and risk scoring

**Status:** complete.

## Phase 4 — Administration and platform integrations

- SSO, groups, custom roles, service accounts
- SCM integrations and test automation
- Jira, Azure DevOps, Code Sight, Secure Code Warrior
- Black Duck SCA synchronization and Issue Management MCP

**Status:** complete.

## Phase 5 — Reference and freshness work

- Release notes, change log, IP ranges, API references, and migrations
- Refresh changed content; retry errors; resolve skipped pages

**Status:** initial scrape complete. Converter now preserves permission Yes/No marks, source hashes, and section outlines. Refresh when requested.

## Completion criteria

- No unexpected pending/error topics in the Polaris manifest.
- Every `done` topic has valid front matter (including `content_hash`) and a matching local file.
- Generated indexes, `index.md`, and hub agree with manifest statistics.
- Retrieval smoke tests pass for platform, scanning, policy, roles, MCP, and CI routing (`python scripts/smoke-retrieval.py`).
