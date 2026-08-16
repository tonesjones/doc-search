---
title: "forLoop"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/forloop.html"
content_id: "4VZhU9cKck88u841RWvmLQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:56.774586+00:00"
---

# forLoop

Matches both simple and enhanced `for` loops.

To match specific kinds of `for` loops, and to get greater detail about them, refer to
forLoopSimple and
forLoopEnhanced.

This pattern only matches nodes of type `statement`.

## Properties

`forLoop` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `body` | `statement` | The body of the `for` loop |
| `kind` | `enum forLoopKind` | The kind of `for` loop: either `` `simple` `` or `` `enhanced` ``; see ForLoopKind |

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

allLoops
forLoopEnhanced,
forLoopSimple
