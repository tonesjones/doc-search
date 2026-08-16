---
title: "codeAttribute"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/codeattribute.html"
content_id: "3ZoPVVydb6HzR5U0JWSgWg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:32.547058+00:00"
---

# codeAttribute

Represents a code attribute. Attributes can be placed on classes, class variables, or methods.

## Properties

`codeAttribute` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `attributeType` | `classType` | The attribute type |
| `arguments` | `list<attributeArgument>` | The arguments to the attribute |

## Example

This type can be used to inspect attributes such as the `[Obsolete]` attribute in the following sample C# code:

  
 [image: C# code follows]   

```
    class Example {
        [Obsolete]
        void myfunction() {
            }
    };
```

## See also

classDefinition,
fieldSymbol
functionSymbol,
staticVariableSymbol,
