---
title: "withStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/withstatement.html"
content_id: "f0AezCOO1nSolMbPkeUzcw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:15.917739+00:00"
---

# withStatement

Matches `with` statements.

This pattern only matches nodes of type `statement`.

## Properties

`withStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The statement to be evaluated |
| `objectExpression` | `expression` | The expression to be added to the scope chain used when evaluating the body statement |

**Inherits properties from:**

- astnode
- statement

## Example

The `withStatement` pattern matches the following case:

[image: JavaScript code follows]

```
    var a;
    with (Math) {
        a = PI;
    };
```

In this instance, the `.objectExpression` property is the expression `Math`, and
the `.bodyStatement` property is the statement `{a = PI;}`.
