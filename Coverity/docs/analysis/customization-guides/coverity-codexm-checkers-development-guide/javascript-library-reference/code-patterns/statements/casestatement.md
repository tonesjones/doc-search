---
title: "caseStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/casestatement.html"
content_id: "9LiOXjyuqtFJEqYgk4usmw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:01.603329+00:00"
---

# caseStatement

Matches individual `case` statements within `switch` statements.

This pattern only matches nodes of type `statement`.

## Properties

`caseStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `valueExpression` | `expression` | The value associated with the case |

**Inherits properties from:**

- astnode
- statement

## Example

The `caseStatement` pattern matches the statement `case 0:` in the following source code:

[image: JavaScript code follows]

```
    switch(i) {
        case 0:         // caseStatement
            break;
        default:
            break;
    };
```

In this instance, the `.valueExpression` property is `0`.

## See also

switchStatement
