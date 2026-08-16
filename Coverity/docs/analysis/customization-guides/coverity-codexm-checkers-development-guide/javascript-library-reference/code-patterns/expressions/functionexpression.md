---
title: "functionExpression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functionexpression.html"
content_id: "GKBW2DANxUq6cXvNhNROWA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:30.731561+00:00"
---

# functionExpression

Matches closure expressions that define a function.

A *functionExpression* (as specified in ECMAScript 2015, 14.1w) is a way to define a possibly unnamed function.

This pattern only matches nodes of type `expression`.

## Properties

`functionExpression` does not expose any new properties.

**Inherits properties from:**

- astnode
- expression

## Example

The `functionExpression` pattern matches the returned unnamed lambda function in the following JavaScript source:

[image: JavaScript code follows]

```
    function f() {
        return function () {return 1;}
    };
```

## See also

functionDeclatation
