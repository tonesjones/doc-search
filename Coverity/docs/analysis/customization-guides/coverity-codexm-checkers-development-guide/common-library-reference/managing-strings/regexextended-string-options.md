---
title: "RegexExtended( string, options )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/regexextended-string-options-.html"
content_id: "FT5E3rJYijp9cMK4CPa2pg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:21.557627+00:00"
---

# RegexExtended( string, options )

Matches a string that conforms to the specified
[regular expression (regex)](http://perldoc.perl.org/perlre.html),
using the Boost engine.
This version allows you to specify additional conditions for how the matching is carried out.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `string` | `string` | A string that contains the regular expression to match |
| `options` | `record` | Several fields that control the behavior of the search. |
| ***return value*** | `pattern` | This pattern matches a string if the string contains a match for the regular expression specified by the `string` argument. |

The `pattern` that `RegexExtended()` returns is a record with two properties:

`captures`
:   `list<string>` — A list of the capture groups in the regular expression

`fullMatch`
:   `string` — The full match

## Option fields

| Name | Type | Description |
| --- | --- | --- |
| `caseInsensitive` | `bool` | Set this to `true` if you want the match to ignore character case. |
| `exactMatch` | `bool` | Set this to `true` if you want the match to be exact. |
| `multiLine` | `bool` | Allows the string to include line breaks. When `multiLine` is `true`, then the `\n` (newline) character introduces a line break: `$` matches the end of the string that precedes the newline, and `^` matches the beginning of the string that follows it.  When `multiLine` is `false`, then `^` and `$` match only the beginning and the end of the entire string, respectively.  **Default**: `true` |
| `replace` | `string` | If `replace` is specified, the `fullMatch` property of the yield record contains the original string with matched substrings replaced according to the value of the `replace` option. The `replace` option uses the algorithm specified for ECMA-262: See the description of "String.prototype.replace" in the [EcmaScript® Language Specification](https://www.ecma-international.org/ecma-262/5.1/). In particular, `"$1"` represents the first matched subgroup. |
| `singleLine` | `bool` | When `singleLine` is `true`, then `.` will match `\n`. Otherwise, it will not match. **Default**: `true` |

The `multiLine` and `singleLine` settings are independent of each other.
