---
title: "codeAnnotation"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/codeannotation.html"
content_id: "24vUwEPnGEBuS4LrjaCxkg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:39.359625+00:00"
---

# codeAnnotation

Represents a code annotation. Annotations can be placed on classes, class variables, or methods.

## Properties

`codeAnnotation` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `annotationType` | `classType` | The annotation type |
| `elements` | `list<annotationElementValuePair>` | The element-value pairs |

## Example

`codeAnnotatoin` can be used to inspect things like the `@Deprecated` annotation in the following Java code:

  
 [image: Java code follows]   

```
Example {
    @Deprecated
    void myFunction() {
        // ...
    }
};
```

## See also

classDefinition,
fieldSymbol,
functionSymbol,
staticVariableSymbol
