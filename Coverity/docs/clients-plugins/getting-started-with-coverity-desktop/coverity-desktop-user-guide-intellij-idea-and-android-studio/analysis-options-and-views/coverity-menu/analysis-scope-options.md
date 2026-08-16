---
title: "Analysis scope options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/analysis-scope-options.html"
content_id: "GVwqSqz374zwQsUJy1_RWA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:48:33.595603+00:00"
---

# Analysis scope options

There are three ways that Coverity Desktop chooses which files to
analyze with Desktop Analysis:

Analyze Current Editor File
:   This option will run Desktop Analysis on the currently
    displayed source file. If there are any unsaved changes, the file will
    be saved when this option is selected.

Analyze Modified Files (SCM)
:   This option will run Desktop Analysis on all of the source
    files that are new or modified, relative to the code version most
    recently checked out from the specified SCM.

    This option is not available if you have not configured an SCM system.
    See SCM.

Analyze Entire Scope
:   This option will run Desktop Analysis on all of the source
    files in your active Analysis Configuration's scope.
