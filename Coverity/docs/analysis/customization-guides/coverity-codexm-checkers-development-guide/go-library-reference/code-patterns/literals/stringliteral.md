---
title: "stringLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/stringliteral.html"
content_id: "dEKSN4T3YNBenu7JAtuYHQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:46.858490+00:00"
---

# stringLiteral

Matches all string literals.

This pattern only matches nodes of type `expression`.

## Properties

`stringLiteral` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `valueString` | `string` | The value of the `string` literal. |

**Inherits properties from:**

- astnode
- expression

## Example

The following pattern finds assignments from the string literal `"Example"`:

  
 [image: CXM code follows]   

```
    pattern assignmentsToStringLiterals {
        assignmentOperator {
            .sourceExpression == stringLiteral { .value == "Example" }
        }
    };
```
