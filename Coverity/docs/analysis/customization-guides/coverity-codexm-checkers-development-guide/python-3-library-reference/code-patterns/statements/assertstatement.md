---
title: "assertStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/assertstatement.html"
content_id: "eZjPmPoXa0qpALJpliNW3w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:18.641848+00:00"
---

# assertStatement

Matches `assert` statements.

This pattern only matches nodes of type `statement`.

## Properties

`assertStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `conditionExpression` | `expression` | The condition of the assertion |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches assertions on Boolean literals—that is,
`assert(True)`

[image: CXM code follows]

```
    pattern uselessAssert {
        assertStatement {
            .conditionExpression == booleanLiteral
        }
    };
```
