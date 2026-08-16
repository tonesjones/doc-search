---
title: "referenceParamType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/referenceparamtype.html"
content_id: "P6slkcnxN27EGea3LLKntQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:23.141421+00:00"
---

# referenceParamType

Matches C# reference (`ref`) parameter types.

Reference types are used when something is passed as a reference (as opposed to by value);
for example, in a function call such as `myFun(ref count)`.

This pattern only matches nodes of type `type`.

## Properties

`referenceParamType` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `toType` | `type` | The type the reference refers to |

## Example

The following CodeXM pattern matches all reference types to a class named `MyClass`:

  
 [image: CXM code follows]   

```
    r matches referenceParamType {
        .toType == classType {
            .simpleName == "MyClass"
        }
    }
```

Here is another example of using `ref`:

  
 [image: C# code follows]   

```
void Method(ref int refArgument) {
    refArgument = refArgument + 44;
};

ref VeryLargeStruct reflocal = ref veryLargeStruct;
```

## See also

referenceType
