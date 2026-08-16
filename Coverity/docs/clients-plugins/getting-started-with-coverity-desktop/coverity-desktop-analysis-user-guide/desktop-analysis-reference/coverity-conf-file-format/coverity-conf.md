---
title: "coverity.conf"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity.conf.html"
content_id: "qObe~1wYv17_13urX5bIjA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:13.910150+00:00"
---

# coverity.conf

The root of the JSON object tree is called coverity.conf because
that is the name of the file, and the file consists of exactly one such object. It has
the following attributes:

type: "Coverity configuration"
:   The `type` must be exactly "Coverity configuration" to label the file's
    contents.

format_version: 1
:   The version must be the number 1. Future releases of the Coverity tools may introduce
    additional permitted version numbers.

format_minor_version: 7
:   The minor version is currently at 7. Future releases of the Coverity tools may introduce
    additional permitted minor version numbers.

variables?: UserDefinedVariables
:   Defines a variable that can be used within the coverity.conf file
    itself using a `variables` property. Each variable is defined
    by a name and a corresponding value.

settings?: Settings
:   Defines the unconditional settings stored in this file.

conditional_settings?: ConditionalSettings[]
:   Defines the conditional settings in this file. Each object has some conditions that must be
    true for the object to take effect. Conditional settings override
    unconditional settings, and earlier conditional settings take precedence
    over later conditional settings (if both are active).
