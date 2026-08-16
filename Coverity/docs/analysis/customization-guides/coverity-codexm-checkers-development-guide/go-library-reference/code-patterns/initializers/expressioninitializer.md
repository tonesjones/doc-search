---
title: "expressionInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/expressioninitializer.html"
content_id: "i5xlNSXtNjq3ijErLXfbqg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:56.532943+00:00"
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

This pattern would match the following Go initialization:

  
 [image: Go code follows]   

```
    var a = x + y
```

The following CodeXM pattern matches all initializations done using binary operations:

  
 [image: CXM code follows]   

```
    pattern binaryOperationInitializer {
        expressionInitializer {
            .expression == binaryOperator;
        }
    };
```
