---
title: "A note on Git superprojects"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/a-note-on-git-superprojects.html"
content_id: "jz6eLiSOT4Cy9IPLAjaGtg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:08.908175+00:00"
---

# A note on Git superprojects

Git superprojects are unsupported by Desktop Analysis, and will cause errors when used with
`--analyze-scm-modified`.

You might be able to work around this issue by creating a script to access
Git using submodules, and specify that script with the `--scm-tool`
option. This is an advanced use case, and should only be attempted by experienced
users.
