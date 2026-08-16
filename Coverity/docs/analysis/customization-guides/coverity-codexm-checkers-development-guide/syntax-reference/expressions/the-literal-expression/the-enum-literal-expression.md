---
title: "The enum-literal-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-enum-literal-expression.html"
content_id: "Hy~LkatJMfkwK5JhAd4wjw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:44.655499+00:00"
---

# The enum-literal-expression

An *enum* literal is similar to a string literal, but it is enclosed by backticks ( `` ` `` ) rather than double quotes.

## Syntax

```
enum-literal-expression ::=
    '`'
        ( [0-9_a-zA-Z] | [^`\] | '\`' | '\\' )*
        '`'                                     // An enum literal can contain white space.
```

As with string literals, any embedded backticks need to be escaped by a preceding backslash ( `` \` `` )
in order to not be parsed as an end-of-enum marker.

The following literal uses correct syntax to include backticks:

`` `Including the \`backtick\` mark` ``
