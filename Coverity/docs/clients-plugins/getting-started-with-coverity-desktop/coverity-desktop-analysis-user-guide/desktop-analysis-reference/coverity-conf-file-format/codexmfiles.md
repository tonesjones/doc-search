---
title: "CodeXMFiles"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/codexmfiles.html"
content_id: "nYPernrejyu13TLjXZfCQQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:32.215893+00:00"
---

# CodeXMFiles

The `CodeXMFiles` class allows users to run CodeXM checkers during the
`cov-run-desktop` analysis. It has the following attributes:

directory?: path
:   A directory containing the custom CodeXM checker definitions.

files?: string
:   The names of files that define CodeXM checkers.

Here is an example that shows how to use the codexm_files
property:

```
{
    // other settings...
    "codexm_files": [ 
        {
            "directory": "$(install_dir)/codexm",
            "files": [
                "CODEXM_CHECKER_A.cxm",
                "CODEXM_CHECKER_B.cxm"
            ]
          }
       ]
}
```
