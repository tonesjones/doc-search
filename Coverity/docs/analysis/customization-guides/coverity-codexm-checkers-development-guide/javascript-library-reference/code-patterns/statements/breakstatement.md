---
title: "breakStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/breakstatement.html"
content_id: "HWFzMUyCwrBSmFVEYCd7aw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:00.863761+00:00"
---

# breakStatement

Matches both labeled and unlabeled `break` statements.

This pattern only matches nodes of type `statement`.

## Properties

`breakStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `controlStatement` | `statement` | The flow-of-control statement within which the `break` statement occurs, such as a `for`, `while`, or `switch` |
| `target` | `statement?` | The break target statement; `null` if there is none |

**Inherits properties from:**

- astnode
- statement

## Example

The `breakStatement` pattern matches the following cases:

[image: JavaScript code follows]

```
    label: for (let i = 0; i < 10; ++i) {
        if (maybe) {
            break label;          // Case 1
        }
    }
    switch(i) {
        case 0:
            break;                // Case 2
        default:
    };
```

In the first case, the `.controlStatement` property is the `for` loop, and the
`.target` property is the
labelStatement `label: ...`.

In the second case, the `.controlStatement` property is the `switch` statement, and
the `.target` property is `null`.
