---
title: "whileLoop"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/whileloop.html"
content_id: "cr8aMPVhnP4_3QmAkPKSJg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:45.430179+00:00"
---

# whileLoop

Matches `while` loops.

This pattern only matches nodes of type `statement`.

## Properties

`whileLoop` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The statement that the loop iterates. Frequently, this is a blockStatement. |
| `conditionExpression` | `expression` | The condition that causes the loop to terminate |

**Inherits properties from:**

- astnode
- statement

## Example

The `whileLoop` pattern matches the following loop:

[image: JavaScript code follows]

```
    while(true) {
        i++;
    };
```

In this instance, CodeXM sets the `.conditionExpression` property to the literal `true`, and
the `.bodyStatement` property to the statement `{i++;}`.
