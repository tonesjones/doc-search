---
title: "KnownInstallation"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/knowninstallation.html"
content_id: "D0pSwSAmWzK1YkmvxA3zkQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:26.691574+00:00"
---

# KnownInstallation

A single `KnownInstallation` object records the existence of an
installation of the Coverity Analysis tools. It has the following attributes:

version: string
:   The version number of the Coverity Analysis tools.

platform: string
:   The platform that this installation is intended to run on, as a Coverity platform
    identifier like "`linux64`". See Condition.platform for a complete
    list.

kind: string
:   The kind of tool installed at this location. Currently, the only possible value is
    "`cov-analysis`".

directory: path
:   wAn installation directory for the tools identified by `version` and
    `kind`.
