---
title: "blockStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/blockstatement.html"
content_id: "93gR8MMt3u3QpSB5Q2X5kA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:24.984566+00:00"
---

# blockStatement

Matches statements contained in curly braces ( `{`  `}` ).

Block statements assemble a sequence of one or more statements, enclosed in curly braces.

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
