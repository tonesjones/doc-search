---
title: "Analyze files configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/analyze-files-configuration.html"
content_id: "FavtKrcgGJl9pX__3KZEsA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:13.905181+00:00"
---

# Analyze files configuration

Use these keys to specify a subset of source files to analyze.
These options are supported for all languages and all platforms.

Any files that would not be captured due to the capture configuration settings will also be excluded from analysis.

For information about how globs and regexes work, see the configuration file syntax.

| Key | Type | Description |
| --- | --- | --- |
| `exclude-glob` | string | A glob pattern that specifies the set of source files to exclude from analysis. Any include glob patterns and regular expressions are processed prior to handling exclude glob patterns and regular expressions. |
| `exclude-regex` | string | A regular expression that specifies the set of source files to exclude from analysis. Any include glob patterns and regular expressions are processed prior to handling exclude glob patterns and regular expressions. |
| `include-files` | array of strings | Paths of source files to analyze. Include and exclude glob patterns and regular expressions, if specified, are applied to determine which of these files are actually analyzed. |
| `include-glob` | string | A glob pattern that specifies the set of source files to analyze. |
| `include-list-file` | string | A file that contains paths of the source files to analyze, one per line. If include and exclude glob patterns and regular expressions are specified, these are applied to determine which of the files in the list are actually analyzed. |
| `include-regex` | string | A regular expression that specifies the set of source files to analyze. |
