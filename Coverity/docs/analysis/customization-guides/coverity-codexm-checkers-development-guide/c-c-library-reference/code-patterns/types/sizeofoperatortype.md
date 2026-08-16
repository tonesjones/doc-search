---
title: "sizeofOperatorType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sizeofoperatortype.html"
content_id: "m43aPKKyDV1cBn2FK9qZOg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:20.023720+00:00"
---

# sizeofOperatorType

Matches instances of the `sizeof()` operator applied to types;
for example, `sizeof( int )`.

## Properties

`sizeofOperatorType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `operandType` | `type` | The type being evaluated |
| `vlaExpressions` | `list<expression>?` | The expression being evaluated to find the size of a variable-length array; `null` if there is no expression |

## Example

The `sizeofOperatorType` pattern matches the use of `sizeof()` in the following source code:

  
 [image: C/C++ code follows]   

```
    int var = /* something */;
    int size = sizeof(int[var]);
```

In this case, the pattern has an `.operandType` indicating that the argument is an array,
and `.vlaExpressions` refers to `var`.

The following CodeXM pattern matches any `sizeof()` operator applied to a variable-length array:

  
 [image: CXM code follows]   

```
    pattern sizeofVLA {
        sizeofOperatorType {
            .operandType == arrayType;
            .vlaExpressions != null;
        }
    };
```
