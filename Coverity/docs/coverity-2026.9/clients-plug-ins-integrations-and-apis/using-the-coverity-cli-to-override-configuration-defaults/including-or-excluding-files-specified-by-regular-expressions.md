---
title: "Including or excluding files specified by regular expressions"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/including-or-excluding-files-specified-by-regular-expressions.html"
content_id: "AfV8iAAQBhT1djD~oO37MQ"
version: "2026.9"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-10-04T23:35:05.425554+00:00"
---

# Including or excluding files specified by regular expressions

Use the `--file-include-regex` or
`--file-exclude-regex` options to specify the regular expression
that determines which files should be included or excluded when capturing files outside
of a build.

You can use this option with the `capture` and `scan`
subcommands.

**Syntax**

```
--file-include-regex regex
```

```
--file-exclude-regex regex
```
