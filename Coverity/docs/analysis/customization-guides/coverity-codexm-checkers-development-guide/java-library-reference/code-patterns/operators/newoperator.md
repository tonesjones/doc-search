---
title: "newOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/newoperator.html"
content_id: "8rDnOQCI5OkIbASPZGQIRg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:23.175368+00:00"
---

# newOperator

Matches the Java `new` operator.

This pattern only matches nodes of type `expression`.

## Properties

`newOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `initializer` | `initializer` | The expression evaluated to determine the initial condition |
| `isImplicit` | `bool` | `true` if the `new` operator is implicitly placed |
| `objectType` | `type` | The type of the object being created |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all `new` operations that create an object of type `Example`:

  
 [image: CXM code follows]   

```
    pattern exampleNew {
        newOperator {
            .objectType == classType { .simpleName == "Example" }
        }
    };
```
