---
title: "enumDefinition"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enumdefinition.html"
content_id: "Uwwr0fpAqozk1FxAOA_O2A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:31.680589+00:00"
---

# enumDefinition

Describes the definition of a target-language `enum`.

## Properties

`enumDefinition` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `declaredType` | `enumType` | The type name of this `enum` |
| `enumeratorList` | `list<enumerators>` | A list of the literal values this type enumerates |
| `underlyingType` | `type` | The underlying type of the enumerators |
| `hasExplicitEnumBase` | `bool` | `true` if the underlying type is explicitly declared |
| `isScoped` | `bool` | `true` if the `enum` has a class scope |
| `location` | `sourceloc` | The source-code location of the `enum` definition |

## Example

For the following code snippet, `enumDefinition`
matches the definition of `enum E`:

  
 [image: C/C++ code follows]   

```
enum E { A1, A2 };
```
