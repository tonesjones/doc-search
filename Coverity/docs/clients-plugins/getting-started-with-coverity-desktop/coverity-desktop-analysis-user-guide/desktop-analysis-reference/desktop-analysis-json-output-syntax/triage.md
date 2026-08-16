---
title: "Triage"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/triage.html"
content_id: "5h3YA6wk2yOvwKkfT1CKUg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:07.804577+00:00"
---

# Triage

This object carries the current values of *built-in* triage attributes for the defect.

classification: string
:   The current issue Classification.

action: string
:   The current Action to be taken on the issue.

fixTarget: string
:   The current Fix Target for the issue.

severity: string
:   The current Severity of the issue.

legacy: string
:   The current Legacy value of the issue.

owner: string
:   The username of the currently assigned owner of the issue, or an empty string if there is
    no assigned owner.

externalReference: string
:   The "external reference" string for the issue.
