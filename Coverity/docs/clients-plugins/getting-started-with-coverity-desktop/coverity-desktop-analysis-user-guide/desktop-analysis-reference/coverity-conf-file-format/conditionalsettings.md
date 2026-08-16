---
title: "ConditionalSettings"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/conditionalsettings.html"
content_id: "Mt8So2r6ggorw~yyEOqxgw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:15.196309+00:00"
---

# ConditionalSettings

`ConditionalSettings` combines 
`Settings`
 with conditions under which they apply. If the conditions are true in the
environment where the file is being read, then the corresponding settings are active
(and may override settings from elsewhere).

The attributes of this class are:

when: Condition
:   The condition(s) that must be true for the `settings` to be active.

settings: Settings
:   When the conditions specified in the other attributes are satisfied, these settings become
    active, overriding same-named attributes from unconditional settings.
