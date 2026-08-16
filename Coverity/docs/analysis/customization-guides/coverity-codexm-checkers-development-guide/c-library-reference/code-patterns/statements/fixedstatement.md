---
title: "fixedStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/fixedstatement.html"
content_id: "j9UdoWHFP7grnPA7R7zN7g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:56.030684+00:00"
---

# fixedStatement

Matches `fixed` statements.

This pattern only matches nodes of type `statement`.

## Properties

`fixedStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The contained statement |
| `declarations` | `declaration` | Declaration of the fixed variables |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches `fixed` statements that are empty:

  
 [image: CXM code follows]   

```
    pattern emptyFixed {
        fixedStatement {
            .bodyStatement == emptyStatement;
        }
    };
```
