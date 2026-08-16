---
title: "expressionInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/expressioninitializer.html"
content_id: "PuA9HNyPvCIYqnuMiHO4yw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:28.880096+00:00"
---

# expressionInitializer

Matches simple expression initializers used to initialize scalar objects.

This pattern only matches nodes of type `initializer`.

## Properties

`expressionInitializer` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression that evaluates to a value used to initialize the object |

**Inherits properties from:**

- astnode
- initializer

## Example

`expressionInitializer` matches the following Java initialization:

  
 [image: Java code follows]   

```
int a = x + y;
```

For example, the following CodeXM pattern matches all initializations done using a binary operation:

  
 [image: CXM code follows]   

```
    pattern binaryOperationInitializer {
        expressionInitializer {
            .expression == binaryOperator;
        }
    };
```
