---
title: "regularExpressionLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/regularexpressionliteral.html"
content_id: "Bg_h9epsE0KsDpiE_nYVLg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:47.280606+00:00"
---

# regularExpressionLiteral

Matches regular expression literals that have the form `/pattern/flags`.

This pattern only matches nodes of type `expression`.

## Properties

`regularExpressionLiteral` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `body` | `string` | The regular expression |
| `flags` | `string` | The flags for advanced searches |

**Inherits properties from:**

- astnode
- expression

## Example

The `regularExpressionLiteral` pattern matches the following initializer of `re`:

[image: JavaScript code follows]

```
    var re = /\w+\s/g;
```

The `.body` property is `"\w+\s"`, and the `.flags` property is `"g"`.
