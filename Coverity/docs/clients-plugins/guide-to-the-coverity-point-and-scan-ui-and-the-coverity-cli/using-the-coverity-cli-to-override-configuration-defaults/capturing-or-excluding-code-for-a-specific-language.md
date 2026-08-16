---
title: "Capturing or excluding code for a specific language"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/capturing-or-excluding-code-for-a-specific-language.html"
content_id: "joKLldzyO9IsaaJpi4v6aA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:28.331485+00:00"
---

# Capturing or excluding code for a specific language

Use the `--language` or `--exclude-language` options to
specify whether the source code for a specific language should be captured. You can
specify this option multiple times if you want to capture or exclude source for more
than one language.

You can use this option with the `capture` and `scan`
subcommands.

**Syntax**

```
--language lang
```

```
--exclude-language lang
```

The lang argument may be given by the following values:

- `apex`
- `c-family`: C, C++, Objective C, and Objective C++
- `csharp`
- `dart`
- `go`
- `java`: includes JSP
- `javascript`: Javascript and Typescript
- `kotlin`
- `php`
- `python`
- `ruby`
- `scala`
- `sql`
- `swift`
- `vb`
- `configuration`: includes configuration-file formats such as YAML, JSON, TXT, and PLIST
