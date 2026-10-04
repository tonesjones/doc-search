---
title: "stackAllocation"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/stackallocation.html"
content_id: "bt1LmDoLAxnY1b12xZdcHg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:28.469012+00:00"
---

# stackAllocation

Matches stack allocations made by using the keyword `stackalloc`.

This pattern only matches nodes of type `expression`.

## Properties

`stackAllocation` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `type` | `expression` | The expression being used |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all `stackalloc` allocations of more than 100 objects:

  
 [image: CXM code follows]   

```
    pattern stackAllocMoreThan100 {
        stackAllocation as sa where sa.count > 100
    };
```
