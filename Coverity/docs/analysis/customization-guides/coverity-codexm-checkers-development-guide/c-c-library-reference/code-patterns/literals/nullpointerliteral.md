---
title: "nullPointerLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/nullpointerliteral.html"
content_id: "b68JDTlrARdVwE9ROxhTKA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:37.232165+00:00"
---

# nullPointerLiteral

Matches null pointers.

The `nullptr` value (as opposed to `NULL`) was introduced in C++11.

This pattern only matches nodes of type `expression`.

## Properties

`nullPointerLiteral` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enumnullKind` | The kind of literal used to encode the null: `` `0` ``, `` `NULL` ``, or `` `nullptr` ``; see nullKind |

**Inherits properties from:**

- astnode
- expression

## Example

The `nullPointerLiteral` pattern matches `NULL`
or `nullptr` or `0` in source code.

For example, the pattern `nullPointerLiteral` matches the following C/C++ snippet and sets the
`.kind` property to `` `NULL` ``:

  
 [image: C/C++ code follows]   

```
int *p_i = NULL;
```

The pattern `nullPointerLiteral` matches the next snippet
by setting `.kind` to
`` `0` ``.

```
int *p_i = 0;
```

The following CodeXM pattern matches the use of `0` as a null pointer:

  
 [image: CXM code follows]   

```
    pattern nullPointerZero {
        nullPointerLiteral {
            .kind == `0`
        }
    };
```
