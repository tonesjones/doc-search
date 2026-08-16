---
title: "simpleStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/simplestatement.html"
content_id: "emdzI0vqZjYf2cRRl9VBLA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:03.604625+00:00"
---

# simpleStatement

Matches individual executable statements.

In this context, the term *simple* means that such statements do not affect the flow of control.
Simple statements include assignments and function calls.
They do not include variable declarations: See variableDeclaration.

## Properties

`simpleStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression, such as a function call or an assignment, that makes up the statement |

**Inherits properties from:**

- astnode
- statement

## Example

The target expression `x = x + 5;` matches the following CodeXM pattern:

  
 [image: CXM code follows]   

```
    simpleStatement {
        .expression == assignmentOperator
    };
```

Similarly, a statement with the `callLocalFcn();`
function call matches the following CodeXM pattern:

  
 [image: CXM code follows]   

```
    simpleStatement{
        .expression == functionCall
    };
```

To find all function calls in simple statements, you could use the following CodeXM pattern:

  
 [image: CXM code follows]   

```
    for c in codes {
        where c matches simpleStatement {
            .expression == functionCall
        }
    };
```
