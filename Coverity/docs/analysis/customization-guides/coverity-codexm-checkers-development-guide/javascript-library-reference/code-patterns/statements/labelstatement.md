---
title: "labelStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/labelstatement.html"
content_id: "c7C9uV8cl0vL59vZHBrnIA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:10.716300+00:00"
---

# labelStatement

Matches `label` statements.

This pattern only matches nodes of type `statement`.

## Properties

`labelStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `nameString` | `string` | The label string |
| `targetStatement` | `statement` | The statement to which this label is assigned |

**Inherits properties from:**

- astnode
- statement

## Example

The `labelStatement` pattern matches the following cases:

[image: JavaScript code follows]

```
    lab: x++;
```

.

In this instance, the `.nameString` property is `"lab"`, and
the `.targetStatement` property is the statement `x++;`.
