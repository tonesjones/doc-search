---
title: "expressionStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/expressionstatement.html"
content_id: "VniY2ECQhR6BrbELxgVXDA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:22.711087+00:00"
---

# expressionStatement

Matches individual executable expressions.

This pattern only matches nodes of type `statement`.

## Properties

`expressionStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression itself |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches a function call:

[image: CXM code follows]

```
    pattern expressionStatementFunctionCall {
        expressionStatement {
            .expression == functionCall
        }
    };
```
