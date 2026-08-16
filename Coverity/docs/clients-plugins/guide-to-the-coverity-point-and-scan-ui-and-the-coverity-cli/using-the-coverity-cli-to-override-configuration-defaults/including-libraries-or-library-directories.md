---
title: "Including libraries or library directories"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/including-libraries-or-library-directories.html"
content_id: "j7D8hQ4pOtV5OL7nr23M9w"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:30.244305+00:00"
---

# Including libraries or library directories

Use the `--library-file`  or `--library-dir` options to
specify a library or library directory to search when looking for dependencies during
capture. You may specify either option multiple times to pull in multiple files or
directories.

You can use this option with the `capture` and `scan`
subcommands.

**Syntax**

```
--library-file file
```

```
--library-dir directory
```
