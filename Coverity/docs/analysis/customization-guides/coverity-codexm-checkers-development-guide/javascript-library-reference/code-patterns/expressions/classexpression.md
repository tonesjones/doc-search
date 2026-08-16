---
title: "classExpression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/classexpression.html"
content_id: "F8xDLO2fWukOWrWKhwS43w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:26.510947+00:00"
---

# classExpression

Matches class expressions.

A *classExpression* (as specified in ECMAScript 2015, 14.5) is a way to define a possibly unnamed class.

Note:
This is an expression and not a stand-alone statement.

This pattern only matches nodes of type `expression`.

## Properties

`classExpression` does not expose any new properties.

**Inherits properties from:**

- astnode
- expression

## Example

The `classDefinition` pattern matches the initializer in following case:

[image: JavaScript code follows]

```
    var Rectangle = class {
         constructor(height, width) {
             this.height = height;
             this.width = width;
         }
     };
```

## See also

classDeclaration
