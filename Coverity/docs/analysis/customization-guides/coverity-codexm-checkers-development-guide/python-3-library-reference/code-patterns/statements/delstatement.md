---
title: "delStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/delstatement.html"
content_id: "R1zAPy4J8J~Y9G13ZzL6zw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:22.000293+00:00"
---

# delStatement

Matches `del` statements.

This pattern only matches nodes of type `statement`.

## Properties

`delStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression to be deleted |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches `del` statements applied to global variables:

[image: CXM code follows]

```
    pattern delGlobalVariable {
        delStatement {
            .expression == variableReference {
                .scope == `global`
            }
        }
    };
```
