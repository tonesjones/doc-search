---
title: "enumType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enumtype.html"
content_id: "y4i8k1wIDYtsq_7hd78DcQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:13.235548+00:00"
---

# enumType

Matches `enum` types.

## Properties

`enumType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `identifier` | `string` | The string used as an unqualified name for the `enum` |
| `ownerClassType` | `type?` | The type of the `enum` that this one belongs to; `null` if there no owner. |
| `mangledName` | `string?` | The internal "mangled" name used for the `enum` (the mangled name includes type and scope information, to disambiguate this instance of the identifier); `null` if the mangled name is not available |
| `location` | `sourceloc` | The source-code location of the `enum` definition |
| `isAlignmentAssigned` | `bool` | `true` if the `enum` is aligned |
| `alignmentInBytes` | `int?` | The alignment of the type, in bytes; `null` if the type is not aligned |
| `scopeList` | `list<string>` | The scopes within which the `enum` is nested |
| `sizeInBytes` | `int` | The number of bytes required to store a value of this type |

## Example

In the following target source, the code pattern `enumType`
matches the type of a local variable, `x`:

  
 [image: C/C++ code follows]   

```
enum testEnum { bar, baz };

testEnum x = bar;
```

The following CodeXM pattern matches all expressions with type `enum testEnum`:

  
 [image: CXM code follows]   

```
   node matches expression as e
        && e.type matches enumType {
            .identifier == "FOO"
        };
```

## See also

getEnumDefinition()
