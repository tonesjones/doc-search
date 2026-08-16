---
title: "Running security checkers with cov-run-desktop"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/running-security-checkers-with-cov-run-desktop.html"
content_id: "5v5JE2fhvWvApFxOwcvKdw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:59.663775+00:00"
---

# Running security checkers with cov-run-desktop

By default, Desktop Analysis enables the same set of checkers as `cov-analyze`
(minus any that do not support desktop analysis); in particular, it does not enable most
security checkers by default. You can enable them with the
`--webapp-security` and `--android-security` options
to the `cov-run-desktop` command.

Not all security checkers support Desktop Analysis. Unsupported checkers will be disabled and
have warnings issued to indicate that the checker requires running in
`--whole-program` mode. See Analyzing your whole program with cov-run-desktop for more information.
