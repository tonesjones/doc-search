---
title: "Including or excluding files specified by glob patterns"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/including-or-excluding-files-specified-by-glob-patterns.html"
content_id: "mPn5_~rg1gyJyF9fZdWk4g"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:29.613922+00:00"
---

# Including or excluding files specified by glob patterns

Use the `--file-include-glob`  or `--file-exclude-glob` options
to specify the glob patterns that determine which files should be included or excluded
when capturing files outside of a build.

You can use this option with the
`capture` and
`scan` subcommands.

**Syntax**

```
--file-include-glob glob
```

```
--file-exclude-glob glob
```

**Examples**

```
coverity capture --file-include-glob src/*.cpp [-- <build-command>...]
```

```
coverity scan --file-exclude-glob src/*.cpp [-- <build-command>...]
```
