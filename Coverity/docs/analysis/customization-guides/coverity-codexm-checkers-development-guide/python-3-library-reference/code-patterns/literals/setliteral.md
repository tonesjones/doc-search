---
title: "setLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setliteral.html"
content_id: "7NQnBSMYiNEzQ1rC2L6Vtg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:54.895517+00:00"
---

# setLiteral

Matches literal set expressions.

This pattern only matches nodes of type `expression`.

## Properties

`setLiteral` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expressions` | `list<expression>` | The expressions that comprise the set |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern finds set literals that contain three elements;
for example, `{1,2,3}`:

[image: CXM code follows]

```
    pattern tripleSet {
        setLiteral as s where s.expressions.length == 3
    };
```

## See also

dynamicMapping
