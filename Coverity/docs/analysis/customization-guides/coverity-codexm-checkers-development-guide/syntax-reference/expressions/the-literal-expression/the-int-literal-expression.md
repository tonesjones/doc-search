---
title: "The int-literal-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-int-literal-expression.html"
content_id: "5eAYagyeZI3jF9XdhV3dNA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:45.306825+00:00"
---

# The int-literal-expression

An integer literal is a positive 64-bit value. You can express integers in decimal, hexadecimal, or binary notation.

## Syntax

```
int-literal-expression ::=
      [0-9]+
    | '0x' [0-9a-fA-F]+
    | '0b' [0-1]+                // White space is not allowed.
```

A positive integer value can range from 0 to 263–1.

You might recognize that this range implies that integers use a two's complement representation.
In other words, there is no "sign bit" in the CodeXM representation of integers.
CodeXM *does* allow you to work with negative values, but the minus sign ( `-` )
is always treated as a unary operator, and not as part of the literal itself.
