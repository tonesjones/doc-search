---
title: "The string-literal-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-string-literal-expression.html"
content_id: "8deZcC_oGetIlWtfsoEjkQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:45.955031+00:00"
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
