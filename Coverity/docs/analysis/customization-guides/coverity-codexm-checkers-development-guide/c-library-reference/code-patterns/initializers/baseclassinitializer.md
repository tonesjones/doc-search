---
title: "baseClassInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/baseclassinitializer.html"
content_id: "82VcWjdfLHGmgcAKxNagyQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:19.050796+00:00"
---

# baseClassInitializer

Matches initialization calls to the C# `super()` function.

This pattern only matches nodes of type constructorInitializer.

## Properties

`baseClassInitializer` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `baseClass` | `type` | The `classType` of the base type being called |

**Inherits properties from:**

- astnode
- initializer

## Example

Given the following CodeXM pattern:

  
 [image: CXM code follows]   

```
    pattern baseExampleSuper {
        baseClassInitializer {
            .baseClass == classType { .simpleName == "BaseExample" }
        }
    };
```

... it would match the call to `super()` in the following C# code:

  
 [image: C# code follows]   

```
    class Example extends BaseExample {
        public Example() {
            super();
        }
    };
```
