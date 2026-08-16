---
title: "The 'languages' option"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-languages-option.html"
content_id: "lX5rnaXgF8SFXaZvC8YkYg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:53.555030+00:00"
---

# The 'languages' option

The `languages` option lets you include or exclude specific programming languages from the capture process.

## Syntax (YAML format)

Example of using `include`:

```
capture:
    languages:
        include:
            - java
            - csharp
```

Example of using `exclude`:

```
capture:
    languages:
        exclude:
            - javascript
            - python
```

Important:
You can use either `include` or `exclude`, but not both within the same `capture` element
at the same time.

## Supported languages

| Key | Notes |
| --- | --- |
| `apex` |  |
| `c-family` | C, C++, Objective-C, Objective-C++ |
| `configuration` | JSON, YAML, and so on |
| `csharp` |  |
| `dart` |  |
| `go` |  |
| `java` |  |
| `javascript` |  |
| `kotlin` |  |
| `php` |  |
| `python` |  |
| `ruby` |  |
| `scala` |  |
| `sql` | SQL files |
| `swift` |  |
| `vb` |  |

## Examples

To capture only Java and Kotlin files:

```
capture:
    languages:
        include:
            - java
            - kotlin
```

Note:
Java and Kotlin cannot be captured separately. That is, Java and Kotlin will either both be captured or neither will be captured.
To work around this limitation, you can use a `files` exclude pattern.

To exclude JavaScript and Python files:

```
capture:
    languages:
        exclude:
            - javascript
            - python
```
