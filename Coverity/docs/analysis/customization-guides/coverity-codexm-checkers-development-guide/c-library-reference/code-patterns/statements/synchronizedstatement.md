---
title: "synchronizedStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/synchronizedstatement.html"
content_id: "ilkDX1PhdjibaY1pUs0PIw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:04.764789+00:00"
---

# synchronizedStatement

Matches `synchronized` blocks.

This pattern only matches nodes of type `statement`.

## Properties

`synchronizedStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The statement block |
| `lockExpression` | `expression` | The monitor object of the statement |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches all `synchronized` blocks that use an expression of type `class MyLock` as the monitor:

  
 [image: CXM code follows]   

```
    pattern myLockSynchronize {
        synchronizedStatement {
            .lockExpression == expression {
                .type == classType { .simpleName == "MyLock" }
            }
        }
    };
```
