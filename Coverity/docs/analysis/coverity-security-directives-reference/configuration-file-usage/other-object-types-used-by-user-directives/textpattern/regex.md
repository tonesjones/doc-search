---
title: "regex"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/regex.html"
content_id: "xf6UCZOCvCjyz_tvySJs1w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:41.065754+00:00"
---

# regex

A `regex TextPattern` describes a regular expression to match
a string or the text contents of a file.

## Fields

The `regex TextPattern` uses these fields:

`regex`
:   A string value that specifies a Perl-style regular expression.
    For the JSON code to parse correctly,
    any special characters within the string need to be appropriately escaped.

`case_sensitive`
:   (Optional) A Boolean value. If set to `false`, the match
    will be insensitive to case. The default value is `true`.

`line_match`
:   (Optional) A Boolean value. If `true`, the caret (
    `^` ) and dollar-sign ( `$` ) symbols,
    respectively, match the beginning and end of a line. This is equivalent
    to the Perl modifier `//m`. The default value is
    `true`.

`dot_matches_newline`
:   (Optional) A Boolean value. If `true`, the dot (
    `.` ) character matches a newline character. This is
    equivalent to the Perl modifier `//s`. The default value
    is `true`.

## Examples

```
{
    "regex" : "WEB-INF\\/(.+)\\.xml$",
    "case_sensitive" : false
},
```

Note: The `.` (dot) and `/` (slash) characters are regex
metacharacters and so must be backslash-escaped. Since a backslash is a
metacharacter in JSON, it too must be escaped. Hence, when using one of these
characters as a literal in a `regex` context, you need to escape it
by prefixing it with two backslashes (`\\` or `\\/`)
as in the example above.
