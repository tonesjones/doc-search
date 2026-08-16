---
title: "stringLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/stringliteral.html"
content_id: "LKAfE2wAivHnv4FQsNHeqA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:55.597212+00:00"
---

# stringLiteral

Matches literal strings.

This pattern only matches nodes of type `expression`.

## Properties

`stringLiteral` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `valueString` | `string` | The value of the string |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern finds assignments from the string literal `"Example"`:

[image: CXM code follows]

```
    pattern assignmentsToStringLiterals {
        assignmentOperator {
            .sourceExpression == stringLiteral { .valueString == "Example" }
        }
    };
```
