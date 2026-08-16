---
title: "Language configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/language-configuration.html"
content_id: "JW4TQnELxmN45QmGWXRToA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:04.638726+00:00"
---

# Language configuration

Use one of the following keys to specify which languages to include or exclude from capture.
You may not specify both keys.

Language strings can be the following:

- `apex`
- `c-family`: C, C++, Objective C, and Objective C++
- `csharp`
- `dart`
- `go`
- `java`: includes JSP and android config files
- `javascript`: JavaScript and TypeScript
- `kotlin`
- `php`
- `python`
- `ruby`
- `scala`
- `sql`
- `swift`
- `vb`
- `configuration`: includes configuration-file formats such as YAML, JSON, TXT, and PLIST

Note: The following languages are not supported by the Coverity CLI:

- `CUDA`
- `Fortran`

| Key | Type | Description |
| --- | --- | --- |
| `include` | array of strings | Specifies the languages for which the source code should be included in the capture. This key is mutually exclusive with the `exclude` key.  Default: All languages are included. |
| `exclude` | array of strings | Specifies the languages for which the source code should be excluded in the capture. This key is mutually exclusive with the `include` key.  Default: No languages are excluded. |
