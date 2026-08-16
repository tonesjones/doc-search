---
title: "switchStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/switchstatement.html"
content_id: "KcKn1v0M4c4UQdz8UQBRYQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:12.940959+00:00"
---

# switchStatement

Matches `switch` statements.

This pattern only matches nodes of type `statement`.

## Properties

`switchStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The body of the `switch` statement. In most cases it is a blockStatement. |
| `caseList` | `list<statement>` | A list of targets of this `switch` statement. The target can either be a caseStatement or a defaultStatement. |
| `conditionExpression` | `expression` | The expression that determines which case is to be taken |

**Inherits properties from:**

- astnode
- statement

## Example

The `switchStatement` pattern matches the following source code:

[image: JavaScript code follows]

```
    switch(i) {
        case 0:
            break;
        default:
            break;
    };
```

In this instance, the `.conditionExpression` property is `i`,
the `.caseList` property is the list containing both `case 0` and `default` cases, and
the `.bodyStatement` property is the blockStatement
that represents the body of the `switch` statement.

## See also

caseStatement.
defaultStatement
