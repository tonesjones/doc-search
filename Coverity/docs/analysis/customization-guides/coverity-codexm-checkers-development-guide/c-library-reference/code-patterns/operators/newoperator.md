---
title: "newOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/newoperator.html"
content_id: "FQkRRvbwJ1pPxQ1vZyAozQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:11.009236+00:00"
---

# newOperator

Matches the C# `new` operator.

This pattern only matches nodes of type `expression`.

## Properties

`newOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `initializer` | `initializer` | The expression evaluated to determine the initial condition |
| `objectType` | `type` | The type of the object being created |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all `new` operations that create an object of type `class Example`:

  
 [image: CXM code follows]   

```
    pattern exampleNew {
        newOperator {
            .objectType == classType { .simpleName == "Example" }
        }
    };
```
