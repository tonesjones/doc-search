---
title: "unsafeStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/unsafestatement.html"
content_id: "Hg6dCMmVlVvSJkmzwR1aEA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:09.307948+00:00"
---

# unsafeStatement

Matches `unsafe` blocks.

This pattern only matches nodes of type `statement`.

## Properties

`unsafeStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The body statement contained by `unsafe` |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches `unsafe` statements that are empty:

  
 [image: CXM code follows]   

```
    pattern emptyUnsafe {
        unsafeStatement {
            .bodyStatement == emptyStatement;
        }
    };
```
