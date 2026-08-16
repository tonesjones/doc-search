---
title: "The enum-type"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-enum-type.html"
content_id: "Zczrby1vVoy2QElAWcUJ5g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:02.441825+00:00"
---

# The enum-type

The `enum-type` is similar to a set, except that each member is an
enum-literal-expression; that is, a character sequence enclosed by backticks
( `` ` `` ) rather than quotation marks.

Note:
The values in an `enum` are not considered to be ordered.

## Syntax

  
 [image: Syntax diagram, enum type]   

```
enum-type ::=
    'enum' '{'
        ( enum-literal-expression (',' enum-literal-expression)* )?
    '}'
```

## Details

Unlike some other languages, where the members of an enumeration are merely identifiers,
in CodeXM the value of an `enum` member can be nearly any string-like value.
For example, an `enum` describing operators might define
its contents by using familiar symbols such as
`` `+` ``, `` `-` ``, `` `*` ``, `` `/` ``,
and so on.

The value of an `enum` is not required to be unique among all
the `enum` types in your CodeXM source file.
In fact, an `enum` literal that is not unique is considered to belong to
any `enum` type that contains the same literal.
For example, the literal `` `X` `` is assumed to be of the type
`` enum{ `X` } ``, which is shared among all enums in the source file that include this same member.

For example, suppose your checker declares the following two enumerations:

[image: CXM code follows]

```
typedef E1 = enum {`A`, `Y`};
typedef E2 = enum {`X`, `Y` };
```

... then a variable of either type can be compared with a variable of the other.
