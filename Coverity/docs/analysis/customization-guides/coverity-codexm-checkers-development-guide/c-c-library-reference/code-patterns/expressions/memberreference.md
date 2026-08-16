---
title: "memberReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/memberreference.html"
content_id: "HNqIyHwbFWaUFToiBR1nqw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:29.082432+00:00"
---

# memberReference

Matches references to member fields of structures or classes (C++ only).

## Properties

`memberReference` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `objectExpression` | `expression` | The structure or class object whose member is being accessed |
| `field` | `type` | The member field |

**Inherits properties from:**

- astnode
- expression

## Example

The pattern `memberReference` matches references to members of a
`struct` or a `class`.
Consider the following C++ code:

  
 [image: C++ code follows]   

```
typedef struct {
    int   i;
    float f;
} ST;
                
ST st;
```

In this case, `memberReference` matches two instances, one on each line shown below:

  
 [image: C++ code follows]   

```
int my_i = st.i;
st.f = 42.0f;
```

On the first line, the `.objectExpression` property is `st` and the
`.field` property refers to field `i`.

On the second line the pattern is almost the same, but the
`.field` property refers to field `f`.
