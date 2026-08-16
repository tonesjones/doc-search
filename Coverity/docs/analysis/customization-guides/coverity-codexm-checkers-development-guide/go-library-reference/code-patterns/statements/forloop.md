---
title: "forLoop"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/forloop.html"
content_id: "8vzFO1tDXmQ9HQty7lReBg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:11.951751+00:00"
---

# forLoop

This pattern matches both simple and enhanced `for` loops.

The condition of a simple for loop is a *for clause;* for example,
`i := 0; i < 10; i++`.

The condition of an enhanced for loop is either a Boolean expression, or it is a *range clause*
that tells the loop to iterate over all the entries in an object such as an array, a string, a map, and so on.

This pattern only matches nodes of type `statement`.

## Properties

`forLoop` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `body` | `statement` | The body of the `for` loop |
| `kind` | `enum ForLoopKind` | The kind of `for` loop: either `` `simple` `` or `` `enhanced` ``. See ForLoopKind. |

**Inherits properties from:**

- astnode
- statement

## Example

Matches any simple `for` loop:

  
 [image: CXM code follows]   

```
    pattern anySimpleForLoop {
        forLoop { .kind == `simple` }
    };
```

## See also

allLoops,
forLoopSimple
