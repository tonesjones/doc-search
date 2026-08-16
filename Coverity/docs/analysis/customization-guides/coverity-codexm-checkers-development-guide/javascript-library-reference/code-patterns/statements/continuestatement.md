---
title: "continueStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/continuestatement.html"
content_id: "zNEjEn~9iaTaZw~xBcuMOA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:02.337051+00:00"
---

# continueStatement

Matches both labeled and unlabeled `continue` statements.

`continueStatement` produces a record that contains the following properties:

## Properties

`continueStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `controlStatement` | `statement` | The flow-of-control statement within which the `continue` statement occurs, such as a `for` loop or `while` loop |
| `target` | `statement?` | The continue target statement; `null` if there is none |

**Inherits properties from:**

- astnode
- statement

## Example

The `continueStatement` pattern matches the following cases:

[image: JavaScript code follows]

```
    label: for (let i = 0; i < 10; ++i) {
        if (maybe) {
            continue label;       // Case 1
        }
    }
    while(true) {
        continue;                 // Case 2
    };
```

In the first case, the `.controlStatement` property is the `for` loop, and
the `.target` property is the labelStatement
`label: ...`.

In the second case, the `.controlStatement` property is the `while` loop, and
the `.target` property is `null`.
