---
title: "The comparison-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-comparison-expression.html"
content_id: "pY~zrw0UGBuMiaeAvDT0OQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:26.276709+00:00"
---

# The comparison-expression

The `comparison-expression` uses common operators to perform
tests for equality or inequality, and relations such as greater-than or less-than.

## Syntax

  
 [image: Syntax diagram, comparison-expression]   

```
comparison-expression ::=
    expression ( '==' | '!=' | '<' | '<=' | '>' | '>=' | '<=>' ) expression
```

The operator `<=>` is the three-way comparison:
Rather than a Boolean value, its result is –1 for less-than, 0 for equals, and +1 for greater-than.

CAUTION:

The character-combination `<>` is not a valid operator, as it is in some languages.
To compare for inequality, use the `!=` operator.

## Details

In general, you can compare expressions of various types, as described here.

The `astnode` and other node types
:   Two nodes are equal only if they are exactly the same node in the syntax tree.
    Equality and inequality are the only valid comparisons.

symbol
:   Two symbols are equal if they represent the same entity; for example, the same variable.
    Equality and inequality are the only valid comparisons.

type
:   Two types are equal only if they represent the same type.
    Equality and inequality are the only valid comparisons.

    Type comparison does acknowledge `typedef` aliasing in target code;
    for example, after the statement `typedef int Integer`
    the `int` type will equal the `Integer` type.

    However, a qualifier such as `const` changes the fundamental type
    (in this case, from a variable to a constant).
    So the pointer type `const int *` does *not* equal the pointer type
    `int *`.

`int`
:   All the comparisons are available, including relational comparisons such as `>`
    or `>=`.

`string`
:   A string comparison depends on the target language and its file format.
    You can use relational comparisons on strings.
    If the string contains Roman letters, the relation is based on alphabetical order;
    for example, `"l" > "c"`.
    If the string uses non-Roman characters such as Unicode, the result of a comparison is not well defined.

`enum`
:   It is an error to compare two enum values if the types to which they belong have no values in common.
    Otherwise, normal comparisons as per strings apply.

A nullable type
:   You can compare nullable types.
    The value `null` is equal to itself and
    different from—specifically, less than—any non-null value.

Note:
If the two values being compared are not of the same type, CodeXM uses
[*unification*](https://en.wikipedia.org/wiki/Unification_(computer_science))
to find a substitution that makes the two types comparable, if that is possible.
Unification is an operation that is similar to
[*casting*](https://en.wikipedia.org/wiki/Type_conversion) (also known as *type conversion)*.
