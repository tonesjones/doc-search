---
title: "referenceType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/referencetype.html"
content_id: "560fIB5ujP8nqiyjs1RXwQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:57.273865+00:00"
---

# referenceType

Matches Java reference types.

Reference types are used to represent when something is passed as a reference; for example, in a function parameter.

This pattern only matches nodes of type `type`.

## Properties

`referenceType` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `toType` | `type` | The type the reference refers to |

## Example

The following CodeXM match pattern:

  
 [image: CXM code follows]   

```
    t matches referenceType { .toType == classType { .simpleName == "MyClass" } };
```

... matches all references to a class named `MyClass`.
