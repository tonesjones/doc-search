---
title: "blockStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/blockstatement.html"
content_id: "qZRij1cAfQEo22HTRK9sbw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:06.161192+00:00"
---

# blockStatement

Matches statements contained in curly braces ( `{ }` ).

Block statements contain one or more statements, enclosed in curly braces.

This pattern only matches nodes of type `statement`.

## Properties

`blockStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `containedStatements` | `list<statement>` | The statements contained in the block |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern finds `blockStatement` entities that contain only the empty statement:

  
 [image: CXM code follows]   

```
    pattern emptyStatementBlock {
        blockStatement {
            .containedStatements == emptyStatement
        }
    };
```

## See also

emptyStatement
