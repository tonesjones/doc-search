---
title: "Issues Materialized Table (IMT) overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/issues-materialized-table-imt-overview.html"
content_id: "w3pEt43cCl7uPf1_Md7UvQ"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:07.370333+00:00"
---

# Issues Materialized Table (IMT) overview

The Issues Materialized Table (IMT) is a performance feature that pre-materializes
snapshot-pinned issue data into an indexed PostgreSQL table, significantly reducing Issue View
query latency in large Coverity Connect deployments.

## What IMT does

In large Coverity Connect deployments, Issue View previously executed a complex multi-join
SQL query per page load, resulting in 5–18 second response times on large databases. IMT
pre-materializes this data into a partitioned PostgreSQL table
(`issues_materialized`) so that Issue View queries join a small indexed
table instead of traversing the full snapshot/defect join tree.

IMT is enabled by default starting in the 2026.9.0 release. Operators can disable it via
configuration as a temporary guardrail if unexpected behavior occurs, but IMT is the
recommended path for all production deployments.

## Scope of IMT

IMT applies only to the following:

- Issue View queries against the **latest snapshot** of a stream.

IMT does **not** apply to:

- Issue View for older (non-latest) snapshots, which continue to use the legacy query
  path.
- Issue View All in Projects, which is not affected.
- Show Occurrences, which always uses the legacy path.
- Range snapshot comparisons or historical snapshot views.

## What does not change

IMT changes only the internal query path. The following behaviors remain unchanged:

- **Issue View results** — The same issues, filters, and sort options are
  displayed.
- **Triage, classification, severity, and actions** — These attributes are always
  fetched live. Triage edits are reflected immediately in Issue View regardless of IMT
  state.
- **Standard attributes** — Always fetched live from the database.

## Automatic fallback for stale or missing data

If a stream's materialized data is missing or behind the latest commit, Issue View
automatically falls back to the legacy query for that stream. Users always see correct,
up-to-date results. The only difference is that Issue View for that stream will be slower
(legacy query speed) until the stream is refreshed.

After a refresh completes, subsequent Issue View requests for that stream use the fast IMT
path automatically.

## Component map changes

When component map file rules are modified, all streams using that component map are
automatically marked stale. Issue View immediately falls back to the legacy query path to
display correct component assignments. The nightly prefill job or a manual API refresh will
refresh these streams, after which the fast IMT path resumes.
