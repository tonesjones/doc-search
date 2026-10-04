---
title: "breakStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/breakstatement.html"
content_id: "JxUuWYcpsRk7n1XeknHsoA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:17.055405+00:00"
---

# breakStatement

Matches `break` statements.

## Properties

`breakStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `controlStatement` | `statement` | The flow-of-control statement within which the `break` statement occurs, such as `for`, `while`, or `switch` |

**Inherits properties from:**

- astnode
- statement

## Example

Consider this bit of C or C++ code:

  
 [image: C/C++ code follows]   

```
while ( getMore() ) {
    if ( someCondition() )
        break;
};
```

A `breakStatement` pattern matches the `break` statement in the preceding code fragment.
The pattern's `.controlStatement` property references the
`while` loop itself.

To identify `break` statements specifically within
`switch` statements, use the following pattern:

  
 [image: CXM code follows]   

```
    pattern breakInSwitch {
        breakStatement {
            .controlStatement == switchStatement
        }
    };
```
