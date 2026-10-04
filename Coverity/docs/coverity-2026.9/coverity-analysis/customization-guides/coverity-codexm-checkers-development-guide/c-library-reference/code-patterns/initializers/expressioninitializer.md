---
title: "expressionInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/expressioninitializer.html"
content_id: "2N2CjHtia0ziv01KbtDhKA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:30.499379+00:00"
---

# expressionInitializer

Matches simple expression initializers used to initialize scalar objects.

This pattern only matches nodes of type `initializer`.

## Properties

`expressionInitializer` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression that evaluates to the value that is used to initialize the scalar object |

**Inherits properties from:**

- astnode
- initializer

## Example

The `expressionInitializer` pattern would match the following C# initialization:

  
 [image: C# code follows]   

```
    int a = x + y;
```

The following CodeXM pattern matches all initializations done using binary operations.

  
 [image: CXM code follows]   

```
    pattern binaryOperationInitializer {
        expressionInitializer {
            .expression == binaryOperator;
        }
    };
```
