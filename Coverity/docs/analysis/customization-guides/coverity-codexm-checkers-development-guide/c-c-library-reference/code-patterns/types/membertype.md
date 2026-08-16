---
title: "memberType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/membertype.html"
content_id: "JfS4DsaasnSo21s0GYpn6g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:16.298999+00:00"
---

# memberType

(C++) Matches members of classes.

## Properties

`memberType` produces a record that has the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `classType` | `classType` | The type of the class that owns the member |
| `memberType` | `type` | The type of the member itself |

## Example

Consider the following source code:

  
 [image: C/C++ code follows]   

```
class Bird {
    public:
        int mN;
};

int Bird::*pN = &Bird::mN;
```

The following CodeXM fragment would match both these members of `Bird`:
the pointer `pN`
and the pointer target `&Bird::mN`:

  
 [image: CXM code follows]   

```
    pointerType {
        .pointerToType == memberType
    };
```
