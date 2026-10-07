---
title: "instanceofOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/instanceofoperator.html"
content_id: "SzWQwd2WVaI53278z36lNg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:48.053880+00:00"
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
