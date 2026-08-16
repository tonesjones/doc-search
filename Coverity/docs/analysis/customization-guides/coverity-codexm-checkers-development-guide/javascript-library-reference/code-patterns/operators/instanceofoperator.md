---
title: "instanceofOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/instanceofoperator.html"
content_id: "SzWQwd2WVaI53278z36lNg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:56.406265+00:00"
---

# instanceofOperator

Matches binary operations where the operator is `instanceof`.

This pattern only matches nodes of type `expression`.

## Properties

`instanceofOperator` does not expose any new properties.

**Inherits properties from:**

- astnode
- expression

## Example

The `instanceofOperator` pattern matches the following expression:

[image: JavaScript code follows]

```
    car instanceof Car
```

## See also

binaryOperator
