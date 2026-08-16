---
title: "Including or excluding files specified by regular expressions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/including-or-excluding-files-specified-by-regular-expressions.html"
content_id: "AfV8iAAQBhT1djD~oO37MQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:28.977663+00:00"
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
