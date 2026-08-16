---
title: "tupleLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tupleliteral.html"
content_id: "J3_KyIJJZERu4v9cBe2T5Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:56.260998+00:00"
---

# tupleLiteral

Matches literal tuple expressions.

This pattern only matches nodes of type `expression`.

## Properties

`tupleLiteral` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expressions` | `list<expression>` | The expressions that comprise the tuple |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern finds tuple literals that contain three elements;
for example, `(1,2,3)`:

[image: CXM code follows]

```
    pattern tripleTuple {
        tupleLiteral as tup where tup.expressions.length == 3
    };
```
