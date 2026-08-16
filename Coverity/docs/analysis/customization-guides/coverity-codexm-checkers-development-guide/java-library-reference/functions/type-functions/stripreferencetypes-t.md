---
title: "stripReferenceTypes( t )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/stripreferencetypes-t-.html"
content_id: "7PnLW~d~f2kZ9m3pr8wLgA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:44.655131+00:00"
---

# stripReferenceTypes( t )

Removes `referenceTypes` around a "base type".

Sometimes it is useful to strip away one or more reference types in order to inspect what the reference is pointing to.
If a type other than a `referenceType` is passed, that same type is returned.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `t` | `type` | The type to strip `referenceTypes` from. This does not itself necessarily need to be a `referenceType`. |
| ***return value*** | `type` | The type, stripped of any `referenceTypes` |

## Example

For the following Java code:

  
 [image: Java code follows]   

```
void myExampleFunction(ExampleClass c) {
    // ...
};
```

... the parameter `c` can be passed as a `referenceType`. To inspect the type being referenced, in CodeXM we can specify:

  
 [image: CXM code follows]   

```
    pattern isReferenceToExampleClass {
        referenceType as t where stripReferenceType(t) matches classType {
            .simpleName == "ExampleClass"
        }
    };
```

## See also

arrayType,
referenceType
