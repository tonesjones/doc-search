---
title: "booleanLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/booleanliteral.html"
content_id: "Ltjv5wJ25RGGkTKqXusCsg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:33.494425+00:00"
---

# booleanLiteral

Matches the Boolean literals `true` and `false`.

This pattern only matches nodes of type `expression`.

## Properties

`booleanLiteral` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isTrue` | `bool` | Matches the value of the literal. |

**Inherits properties from:**

- astnode
- expression

## Example

In the following C++ snippet, the pattern `booleanLiteral` matches
`false` by setting the property `.isTrue`
to `false`:

  
 [image: C++ code follows]   

```
bool flag = false;
```

The following CodeXM pattern matches any `true` Boolean literal.

  
 [image: CXM code follows]   

```
    pattern trueBoolean {
        booleanLiteral { .isTrue == true }
    };
```
