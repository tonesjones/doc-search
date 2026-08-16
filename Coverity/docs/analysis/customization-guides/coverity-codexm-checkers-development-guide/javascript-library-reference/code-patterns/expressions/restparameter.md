---
title: "restParameter"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/restparameter.html"
content_id: "Cx16stirnA9glUqOHeG7VQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:39.032693+00:00"
---

# restParameter

Matches rest parameter declarations that use the prefix `...`.

This pattern only matches nodes of type `expression`.

## Properties

`restParamter` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `parameter` | `expression` | The reference to the parameter |

**Inherits properties from:**

- astnode
- expression

## Example

The `restParameter` pattern matches the declaration of `j` in the following case:

[image: JavaScript code follows]

```
    function f(i, ...j) {
        // ...
    };
```

In this instance, the `.parameter` property is the reference to parameter `j`.
