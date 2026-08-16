---
title: "nodejsRequire"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/nodejsrequire.html"
content_id: "a1ts_BwsZzAMEIbR_J6UXQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:35.610383+00:00"
---

# nodejsRequire

Matches `Node.js require` imports.

Unlike ES6 imports, the module specifier can be an expression, not just a string.

This pattern only matches nodes of type `expression`.

## Properties

`nodejsRequire` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `moduleExpression` | `expression` | The module specifier |

**Inherits properties from:**

- astnode
- expression

## Example

The `nodejsRequire` pattern matches the following expression:

[image: JavaScript code follows]

```
    require(module)
```

The resulting `.moduleExpression` property is `"module"`.
