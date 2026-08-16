---
title: "uncheckedBlock"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/uncheckedblock.html"
content_id: "PSi0riBnlW_uvMIud6Yt9g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:52.363865+00:00"
---

# uncheckedBlock

Matches statements in `unchecked` blocks.

This pattern only matches nodes of type `expression`.

## Properties

`uncheckedBlock` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `checked` | `statement` | The statement |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches `unchecked` statements that are empty:

  
 [image: CXM code follows]   

```
    pattern emptyUnchecked {
        uncheckedBlock {
            .bodyStatement == emptyStatement;
        }
    };
```

## See also

checkedBlock,
checkedExpression,
uncheckedExpression
