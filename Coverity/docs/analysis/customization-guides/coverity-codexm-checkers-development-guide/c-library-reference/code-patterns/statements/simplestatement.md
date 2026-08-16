---
title: "simpleStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/simplestatement.html"
content_id: "R~gma_ZY8BfplPn4KHKrkQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:03.000946+00:00"
---

# simpleStatement

Matches individual executable statements.

The term *simple*—as opposed to *compound*—means that the these statements are not flow-of-control statements.
Simple statements include assignments, function calls, and function returns.
Variable declarations (variableDeclaration) are not considered statements.

This pattern only matches nodes of type `statement`.

## Properties

`simpleStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression to match, such as a function call or an assignment |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches a function call:

  
 [image: CXM code follows]   

```
    pattern simpleStatementFunctionCall {
        simpleStatement {
            .expression == functionCall
        }
    };
```
