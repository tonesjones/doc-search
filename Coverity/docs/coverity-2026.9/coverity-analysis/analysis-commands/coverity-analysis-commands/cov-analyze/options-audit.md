---
title: "Options: Audit"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/options-audit.html"
content_id: "8HHaS0tVi1LXRxWA1AerKA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:45.530034+00:00"
---

# Options: Audit

--enable-audit-mode
:   The `--enable-audit-mode` option is the equivalent of using
    both `--enable-audit-checkers` and
    `--enable-audit-dataflow` at the same time.

    Audit scanning can be time-consuming. We recommend that instead of using
    `--enable-audit-mode`, you run a scan using
    `--enable-audit-checkers` alone. Then, if you feel the
    need to see more detail than the audit checkers provide, run a scan using
    only `--enable-audit-dataflow`.

    For more about audit mode, see the "Audit mode"
    section, part of the "Security reference" chapter
    in the Coverity Checker Reference.
