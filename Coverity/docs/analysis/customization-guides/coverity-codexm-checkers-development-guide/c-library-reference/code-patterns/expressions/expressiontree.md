---
title: "expressionTree"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/expressiontree.html"
content_id: "wocMO6mmz5bDc3vouBvH5A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:36.672239+00:00"
---

# expressionTree

Matches all expression trees.

This pattern only matches nodes of type `expression`.

## Properties

`expressionTree` does not expose any new properties.

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches only expression trees whose root is a binary operator:

  
 [image: CXM code follows]   

```
    pattern binaryExpressionTree {
        expressionTree {
            .expr == binaryOperator
        }
    };
```
