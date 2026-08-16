---
title: "baseClassInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/baseclassinitializer.html"
content_id: "z773stZRV7_4acgopoPlbQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:27.366664+00:00"
---

# baseClassInitializer

Matches initialization calls to `super()`.

This pattern only matches nodes of type `type`.

## Properties

`baseClassInitializer` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `baseClass` | `type` | The `classType` of the base type being called |

**Inherits properties from:**

- astnode
- initializer

## Example

For the following snippet of Java:

  
 [image: Java code follows]   

```
    Example extends BaseExample {
        public Example() {
            super();
        }
    };
```

... the following CodeXM pattern matches all calls to `super()` for the class `` `BaseExample` ``:

  
 [image: CXM code follows]   

```
    pattern baseExampleSuper {
        baseClassInitializer {
            .baseClass == classType { .simpleName == "BaseExample" }
        }
    };
```
