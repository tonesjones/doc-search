---
title: "The string-literal-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/the-string-literal-expression.html"
content_id: "8deZcC_oGetIlWtfsoEjkQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:12.707701+00:00"
---

# The string-literal-expression

A *string* is a sequence of characters enclosed by double quotation marks ( `"` ).

## Syntax

```
string-literal-expression ::=
    '"'
        ( [0-9_a-zA-Z] | [^"\] | '\"' | '\\' | '\n' )*
    '"'                                                // The string can contain white space.
```
