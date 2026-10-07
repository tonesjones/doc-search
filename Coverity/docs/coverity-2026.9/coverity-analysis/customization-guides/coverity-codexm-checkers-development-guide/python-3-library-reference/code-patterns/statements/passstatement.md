---
title: "passStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/passstatement.html"
content_id: "MoGcjx7OVpZr62Zu3ndiZQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:49.811718+00:00"
---

# passStatement

Matches `pass` statements.

This pattern only matches nodes of type `statement`.

## Properties

`passStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `isImplicit` | `bool` | `true` if the statement is compiler-generated |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches `pass` statements in the body of conditionals:

[image: CXM code follows]

```
    pattern passInIf {
        passStatement {
            .parent == ifStatement
        }
    };
```
