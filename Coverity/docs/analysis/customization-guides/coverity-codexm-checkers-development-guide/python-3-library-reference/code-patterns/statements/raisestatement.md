---
title: "raiseStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/raisestatement.html"
content_id: "Ed1K0P_WjE89wpGzA4oEOw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:26.085791+00:00"
---

# raiseStatement

Matches `raise` statements.

This pattern only matches nodes of type `statement`.

## Properties

`raiseStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The exception that the statement raises |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches `raise` statements that throw `Exception("Error!")`:

[image: CXM code follows]

```
    pattern raiseErrorException {
        raiseStatement {
            .expression == stringLiteral {
                .valueString == "Error!"
            }
        }
    };
```
