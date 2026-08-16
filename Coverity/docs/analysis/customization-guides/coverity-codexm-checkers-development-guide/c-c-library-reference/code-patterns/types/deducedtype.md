---
title: "deducedType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/deducedtype.html"
content_id: "I4JIqRxUg4h41gM5Yn9y8A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:12.473843+00:00"
---

# deducedType

Matches compiler-deduced types specified using the `auto`
or `decltype` declarators.

CAUTION:

This pattern only applies to C++.
With this pattern, the `auto` keyword refers to C++ usage, not to C usage.
It indicates a variable that is declared in a function's stack frame.
Because the C-language use of `auto` is the default,
`auto` in C code is not recorded by analysis, *per se;*
see localVariableSymbol.

## Properties

`deducedType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum deducedTypeKind` | One of `` `auto` ``, `` `decltype` ``, or `` `gnu_auto` ``; see deducedTypeKind. |
| `inferredType` | `type` | The type inferred by a compiler |

## Example

In the following source code, the type of a local variable `a` is declared
using `auto`.
This can be matched by a `deducedType` pattern that specifies
`.inferredType` to be `intType`
(that is, the compiler inferred the type of integer) and `.kind`
to be `` `auto` ``.

  
 [image: C/C++ code follows]   

```
auto i = 1;
```

The following CodeXM pattern matches types that are inferred to be integers:

  
 [image: CXM code follows]   

```
    node matches expression as e
        && e.type matches deducedType {
            .inferredType == intType
        };
```
