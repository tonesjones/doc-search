---
title: "CodeXMFiles"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/codexmfiles.html"
content_id: "nYPernrejyu13TLjXZfCQQ"
version: "2026.9"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-10-04T23:35:08.974094+00:00"
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
