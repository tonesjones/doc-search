---
title: "aliasTypeOf( baseType )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/aliastypeof-basetype-.html"
content_id: "Cqrvtq6JI95MjLFvIdQzQA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:39.323664+00:00"
---

# aliasTypeOf( baseType )

This function matches any aliased type (for example, one aliased via a `using` statement) defined in terms of the parameter given.

Use this function to detect not only a specified type, but any other type defined as an alias of that type.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `baseType` | `pattern(type) -> Result` | A pattern based on a specific type |
| ***return value*** | `pattern(type) -> Result` | A pattern similarly matching the desired type, or any alias |

## Example

Assuming that the following type definitions appear in your C# source:

  
 [image: C# code follows]   

```
using myInt = int;
using myNewInt = myInt;
```

... then the use of the following CodeXM pattern:

  
 [image: CXM code follows]   

```
aliasTypeOf(int);
```

... matches the actual type `int` in your source code, as well as any uses of type `myInt`,
and even `myNewInt` (or any other alias based on any of these types).
