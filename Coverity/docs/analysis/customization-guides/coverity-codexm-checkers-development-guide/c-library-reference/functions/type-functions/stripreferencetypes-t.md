---
title: "stripReferenceTypes( t )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/stripreferencetypes-t-.html"
content_id: "PqWGhZq9ubx4WJz9IVpEwA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:37.930608+00:00"
---

# stripReferenceTypes( t )

A function that removes the reference types around a base type.

It is sometimes useful to strip away the reference types to inspect what the reference is pointing to.
If a type other than a `referenceType` is passed, that same type is returned.

## Parameters and return values

| Name | Type | Description |
| --- | --- | --- |
| `t` | `type` | The type to strip reference types from This does not itself necessarily need to be a `referenceType`. |
| ***return value*** | `type` | The type, stripped of any reference types |

## Example

For the following C# code:

  
 [image: C# code follows]   

```
    void myExampleFunction(ExampleClass c) {
        // ...
    };
```

... the parameter `c` can be passed as a `referenceType`. To inspect the type being referenced, you can use the following CodeXM pattern:

  
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
