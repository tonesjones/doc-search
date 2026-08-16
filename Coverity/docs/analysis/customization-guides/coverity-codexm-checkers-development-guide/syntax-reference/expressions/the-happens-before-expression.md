---
title: "The happens-before-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-happens-before-expression.html"
content_id: "WO3Jr_lUfJpsW1vQLYS4WQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:35.991404+00:00"
---

# The happens-before-expression

The `happens-before-expression` takes two operands, and performs a Boolean test on
the sequence in which those operations are invoked in the target code.

## Syntax

  
 [image: Syntax diagram, happens-before-expression]   

```
happens-before-expression ::=
    [!] path-pattern-expression ( '>=>' [!] path-pattern-expression )+
```

Each `path-pattern-expression` is a CodeXM pattern to match a statement or other executable code in the target language.

CAUTION:

This expression is valid only when it is used as an argument to the `sequence()` function.
It is not allowed in other locations in the CodeXM source.

The two patterns do not have to be consecutive: There can be other executable code between them.

You can think of the `sequence()` function as a special kind of pattern that understands paths.
For example, `sequence(pattern_1 >=> pattern_2)`
returns `true` if `pattern_1` executes in the target code
before `pattern_2` does, `false` otherwise.
