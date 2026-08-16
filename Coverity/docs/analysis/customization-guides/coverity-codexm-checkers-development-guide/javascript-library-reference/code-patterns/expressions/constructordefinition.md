---
title: "constructorDefinition"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/constructordefinition.html"
content_id: "tV~oBaHvbNPHxuwtk41RiA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:27.902319+00:00"
---

# constructorDefinition

Matches closure expressions that represent class constructor definitions.

This pattern only matches nodes of type `expression`.

## Properties

`constructorDefinition` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `functionSymbol` | `symbol` | The symbol that represents the defined constructor |

**Inherits properties from:**

- astnode
- expression

## Example

The `constructorDefinition` pattern matches the constructor definition in the following case:

[image: JavaScript code follows]

```
    class Base {
        constructor() {
            this.baseField = 21;
        }
    };
```

In this instance, the `.functionSymbol` property is the symbol that represents the constructor.
