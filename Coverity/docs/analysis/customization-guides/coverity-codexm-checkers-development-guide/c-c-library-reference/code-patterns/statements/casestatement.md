---
title: "caseStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/casestatement.html"
content_id: "CL22Qfpaib_NY1xqlEIdBA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:53.783098+00:00"
---

# caseStatement

Matches individual `case` statements within a `switch`.

`caseStatement` does not match the statement in the `default` clause:
See the defaultStatement pattern.

## Properties

`caseStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `valueExpression` | `expression` | The value associated with this case |

**Inherits properties from:**

- astnode
- statement

## Example

Given the same example from `switchStatement`:

  
 [image: C/C++ code follows]   

```
switch( i ) {
    case 1:  return "one";
    case 2:  return "two";
    case 3:  return "three";
    default: return "unknown";
};
```

... we can use `caseStatement` to match the three `case` labels but exclude the `default` statement.
The `valueExpression` is the associated value of the `case` label.

A custom pattern, `matchCaseByValueExpression`, that matches instances of
`case 1:` looks like this:

  
 [image: CXM code follows]   

```
    pattern matchCaseByValueExpression {
        caseStatement {
            .valueExpression == intLiteral {
                .valueInt == 1
            }
        }
    };
```
