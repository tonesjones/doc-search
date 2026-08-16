---
title: "Advanced: Workflow"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/advanced-workflow.html"
content_id: "UB3ttji6_V_6LADgzWbOfw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:48:18.652534+00:00"
---

# Advanced: Workflow

Figure 1. Advanced: Workflow tab
[image: image]

The Workflow tab gives you the option to send analysis results to the
Coverity Connect server: After analysis completes, commit (copy) analysis
results to the Coverity Connect server.

Selecting this box will commit a new snapshot, containing all issues found by local
analysis, to the Coverity Connect server associated with the analysis configuration.
This option will only run by selecting the Analyze Entire Scope
command and only if the When running Analyze Entire Scope, run all enabled
whole program checkers option is enabled on the analysis page.

You can specify a Snapshot Description in the text field, and
click the Advanced Commit Settings button to configure any
additional commit options.

Note: If this option is enabled for an Analysis Configuration, running local analysis with
that Analysis Configuration will not display any CIDs or triage information in the IDE.

Likewise, when you choose this option, analysis is disconnected from the Coverity
Connect snapshot. Therefore, the analysis options included in the reference snapshot
are not used.
