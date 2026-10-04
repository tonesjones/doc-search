---
title: "checkedBlock"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/checkedblock.html"
content_id: "LWFBbn7AV8gHCU_O9au36w"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:27.361649+00:00"
---

# checkedBlock

Matches `checked` blocks.

This pattern only matches nodes of type `expression`.

## Properties

`checkedBlock` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The statements contained in the block |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches `checked` statements that are empty:

  
 [image: CXM code follows]   

```
    pattern emptyChecked {
        checkedBlock {
            .bodyStatement == emptyStatement;
        }
    };
```

## See also

checkedexpression,
uncheckedBlock,
uncheckedExpression
