---
title: "typedefType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/typedeftype.html"
content_id: "dKGtiudLaveNhoqa9q7Ikw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:20.781282+00:00"
---

# typedefType

Matches uses of a type defined using a `typedef` declarator.

## Properties

`typedefType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `identifier` | `string` | The string used as an unqualified name for the symbol |
| `mangledName` | `string` | The internal "mangled" name used for the symbol (the mangled name includes type and scope information, to disambiguate this instance of the identifier) |
| `targetType` | `type` | The original, underlying type |
| `scopeList` | `list<string>` | The scopes within which the `typedef` is nested |

## Example

In the following source code, the type of variable pattern `typedefType` matches `i`,
provided `.targetType` is a `typeQualifier` and `.targetType`
specifies an integer type (`intType`):

  
 [image: C/C++ code follows]   

```
typedef const int CInt;
CInt i = 1;
```

The following CodeXM pattern matches nodes whose type is defined as `CInt`:

  
 [image: CXM code follows]   

```
    node matches expression as e
        && e.type matches typedefType {
            .alias == "CInt"
        };
```
