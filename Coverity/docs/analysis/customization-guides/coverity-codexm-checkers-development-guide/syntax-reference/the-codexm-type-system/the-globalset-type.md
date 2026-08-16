---
title: "The globalset-type"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-globalset-type.html"
content_id: "JyeUW1YiafLAMwaRazQNIQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:04.121054+00:00"
---

# The globalset-type

For every target-language source file, a `globalset` object
contains all the nodes that correspond to the source file's code.

A `globalset` can be used with `exists` and `for` loop expressions.
Many checkers search the entire `globalset`.

Most language libraries include named `globalset` sets that
contain specific kinds of objects; for example, `allFunctionCode`.
You can use these named `globalset` sets to make the scope of a search
more focused, and possibly quicker to run.

## Syntax

  
 [image: Syntax diagram, globalset-type]   

```
globalset-type ::=
    'globalset' '<' type ','
                       '['
                           globalset-domain ( ',' globalset-domain )*
                       ']'
    'gt;'
```

## Details

A few restrictions apply to `globalset` sets, as follows:

- Within an `exists` expression or a
  `for` loop, the
  `globalset` keyword must be used, and
  local variables from outside the expression cannot be referenced.
- If you pass a pattern to the `contains()` test for a
  `globalset`, the pattern must have a constant value.
  (If the `item` argument is a literal value rather than a pattern, then it can be
  either a constant or a variable.)
  For more information about `contains()`,
  see The collection-type.
- A value computed from a `globalset` can depend on another value computed from a `globalset`, but the computed value,
  in turn, *cannot* depend on another `globalset`.

**The type declaration:**
In such a declaration, the `type` is simply
the identifier of the new set, and each `globalset-domain` is one of the following values:

- `functions`
- `globalvars`
- `classes`
- `enums`
- `declarations`

The domains are used for internal bookkeeping and optimization.
There is rarely need for a user-written checker to declare a new `globalset-type`.

## Example

The opening of the following pattern tells CodeXM to search only code within functions:

[image: CXM code follows]

```
    for code in globalset allFunctionCode where code matches // ... further criteria
```
