---
title: "generatorReturnValue"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/generatorreturnvalue.html"
content_id: "nqyZc4FQmdV1jd7m5ALJig"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:46.509309+00:00"
---

# generatorReturnValue

This pattern, together with a generatorReturnStatement,
matches non-void returns in generator-function bodies.

A `valueExpression` property holds the return value.

This pattern only matches nodes of type `statement`.

## Properties

`generatorReturnValue` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `valueExpression` | `expression` | The expression that generates the return value |

**Inherits properties from:**

- astnode
- expression

## Example

The `generatorReturnValue` pattern matches the following case:

[image: JavaScript code follows]

```
    function* gen(x) {
        yield 1;
        return x;
    };
```

In this instance, the `.valueExpression` property is the expression `"x"`.

## See also

generatorReturnStatement
