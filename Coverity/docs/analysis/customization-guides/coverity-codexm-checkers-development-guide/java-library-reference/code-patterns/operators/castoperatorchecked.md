---
title: "castOperatorChecked"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/castoperatorchecked.html"
content_id: "BnO77LCw2CocQ62~fuVMKA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:19.089165+00:00"
---

# castOperatorChecked

Matches all checked casts in Java.

This pattern only matches nodes of type `expression`.

## Properties

`castOperatorChecked` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum castKind` | Always `` `checkedExplicit` ``; see castKind |
| `operandExpression` | `expression` | The expression being cast |

**Inherits properties from:**

- astnode
- expression

## Example

For the following Java example:

  
 [image: Java code follows]   

```
Object o = "String";
String s = (String) o;        // Checked cast
```

The following CodeXM pattern can be used to find checked casts from `Object`:

  
 [image: CXM code follows]   

```
    pattern checkedCastFromObject {
        castOperatorChecked {
            .operandExpression == expression {
                .type == classType { simpleName == "Object" }
            }
        }
    };
```

## See also

castOperator,
castOperatorExplicit,
castOperatorImplicit
