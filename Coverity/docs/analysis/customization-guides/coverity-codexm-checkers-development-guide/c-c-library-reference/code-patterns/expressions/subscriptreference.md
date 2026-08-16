---
title: "subscriptReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/subscriptreference.html"
content_id: "edLVa~VvdyMluKvdTpKqAw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:31.366703+00:00"
---

# subscriptReference

Matches subscript references, such as `p[i]`.

CAUTION:

This pattern does not match the logical equivalent, `*( p + i )`,
and it does not match C++ subscript operator overloads (which are method calls rather than actual operators).

See also arrayOf for a function that specifically looks for an array of the type you indicate.

## Properties

`subscriptReference` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `arrayExpression` | `expression` | The array being referenced |
| `indexExpression` | `expression` | The indexing expression |

**Inherits properties from:**

- astnode
- expression

## Example

The `subscriptReference` pattern matches the two instances in the following C/C++ source code:

  
 [image: C/C++ code follows]   

```
    x = arr[3];
    arr[5] = 1;
```

In both cases, `.arrayExpression` refers to a
`variableReference` of `arr`,
and in both cases the `.indexExpression` is an integer literal:
The values will be `3` and `5`, respectively.
