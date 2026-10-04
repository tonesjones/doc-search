---
title: "The addition-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/the-addition-expression.html"
content_id: "W7FC2I4uC_ax9r1x~ZwMmQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:11.285995+00:00"
---

# The addition-expression

An `addition-expression` adds ( `+` ) or
subtracts ( `-` ) two integer values.

An `addition-expression` has two specialized uses as well:

- The concatenation operator ( `++` ) concatenates two sets or two lists.
- The null-coalescing operator ( `??` ) replaces a null value with a
  usable non-null expression.

**String concatenation:**
You can also use the plus-sign operator ( `+` ) to concatenate strings.
However, the result of this operation is not of type `string`,
but of type eventstring:
so this usage is a special case that is not a true `addition-expression`.
(You can use the `strcat()` function to obtain a string that is a concatenation
of two others: See strcat.)

## Syntax

  
 [image: Syntax diagram, addition-expression]   

```
addition-expression ::=
      ( expression ( '+' | '-' ) expression )
    | ( set-expression '++' expression )
    | ( nullable-expression '??' expression )
```

The `set-expression` evaluates to a set or a list.

The `nullable-expression` evaluates to a nullable type.
