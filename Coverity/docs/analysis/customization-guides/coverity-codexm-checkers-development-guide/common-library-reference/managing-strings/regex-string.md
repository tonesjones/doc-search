---
title: "Regex( string )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/regex-string-.html"
content_id: "kcvMxtkLhhC1uyZAy7CNHg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:20.879444+00:00"
---

# Regex( string )

Matches a string that conforms to the specified
[regular expression (regex)](http://perldoc.perl.org/perlre.html),
using the Boost engine.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `string` | `string` | A string that contains the regular expression to match |
| ***return value*** | `pattern` | This pattern matches a string if the string contains a match for the regular expression specified by the `string` argument. |

The `pattern` that `Regex()` returns is a record with two properties:

`captures`
:   `list<string>` — A list of the capture groups in the regular expression

`fullMatch`
:   `string` — The full match

## Example

The following pattern detects cases where a `const` variable identifier in the target code
does not start with `"c"`:

[image: CXM code follows]

```
pattern constVarNoC {
    variableDeclaration {
        .type == typeQualifierConst;
        .identifier != Regex( "^c" );
    }
};
```
