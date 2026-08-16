---
title: "classType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/classtype.html"
content_id: "MzA5_CNzAx1U_dKkwWKdVw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:11.730606+00:00"
---

# classType

Matches `class` (C++), `struct`, and `union` types.

## Properties

`classType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum` | One of `` `class` ``, `` `struct` ``, or `` `union` `` |
| `ownerClassType` | `type?` | The type of the class that owns this one; `null` if there no owner. |
| `isAnonymous` | `bool` | `true` if the object is anonymous |
| `identifier` | `string?` | The string used as an unqualified name for this type; `null` if the object is unnamed |
| `mangledName` | `string?` | The internal "mangled" name used for the class (the mangled name includes type and scope information, to disambiguate this instance of the identifier); `null` if the mangled name is not available |
| `isAlignmentAssigned` | `bool` | `true` if the class is aligned |
| `alignmentInBytes` | `int?` | The alignment of the type, in bytes; `null` if the type is not aligned |
| `isComplete` | `bool` | `true` if the object definition is known at compile time |
| `location` | `sourceloc` | The source-code location of the type definition |
| `scopeList` | `list<string>` | The scopes within which the class is nested |
| `sizeInBytes` | `int?` | The number of bytes required to store a value of this type, if known; `null` if the value is not known |

## Example

In the following source code, the pattern `classType`
matches the type of a local variable, `x`:

  
 [image: C/C++ code follows]   

```
class T { /* ... */ };
                
T x;
```

The following CodeXM pattern matches all expressions that have an anonymous class type:

  
 [image: CXM code follows]   

```
    node matches expression as e
        && e.type matches classType {
            .isAnonymous == true
        };
```

## See also

getClassDefinition()
