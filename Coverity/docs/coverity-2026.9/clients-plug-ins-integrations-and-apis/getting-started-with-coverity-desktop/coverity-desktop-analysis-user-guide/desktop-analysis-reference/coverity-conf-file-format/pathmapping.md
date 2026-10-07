---
title: "PathMapping"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/pathmapping.html"
content_id: "FatROjnome_qkA5GYOWwag"
version: "2026.9"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-10-04T23:35:09.103983+00:00"
---

# PathMapping

The `PathMapping` settings are used by the Coverity Desktop Analysis
plugins to map any code defects (retrieved from Coverity Connect) to local files. The
following `PathMapping` settings can be configured:

strip_paths?: string
:   Paths that are listed under this setting are stripped from the front of a defect's file
    path. This setting tries to resolve the path to a local file location.

search_paths?: string
:   Paths that are listed under this setting are added to the search locations of local files
    that contain remote issues.
