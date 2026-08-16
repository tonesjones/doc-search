---
title: "enumeratorSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enumeratorsymbol.html"
content_id: "X1awG5vi7jcbJKSwa3dFOA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:00.593605+00:00"
---

# enumeratorSymbol

Matches enumeration (`enum`) values.

This pattern only matches nodes of type `symbol`.

## Properties

`enumeratorSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isExplicit` | `bool` | `true` if the enumeration value is declared explicitly. |
| `ownerEnumType` | `record[type]` | Enumerates the identifiers declared in the `enum` base type |
| `value` | `int` | The value of this particular instance of a member of the `enum` |

**Inherits properties from:**

- symbol

## Example

Given the following sample of source code:

  
 [image: C/C++ code follows]   

```
enum myEnum {
    enm1 = 1;
    enm2 = 3;
    specMem
};
```

... the following CodeXM fragment would match the non-explicit value represented by `specMem`:

  
 [image: CXM code follows]   

```
    enumeratorSymbol { .identifier == "specMem" }
```
