---
title: "classDeclaration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/classdeclaration.html"
content_id: "g2tJhYw~6I6xp_UQJwQ2dA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:17.315658+00:00"
---

# classDeclaration

Matches class declaration statements.

A *classDeclaration* (as specified in ECMAScript 2015, 14.5) is a statement that defines a class.
In JavaScript, all source code is in the body of the top-level function.
So a stand-alone class declaration is also a statement of the top-level function.
This is also the case for functionDeclaration.

This pattern only matches nodes of type `statement`.

## Properties

`classDeclaration` does not expose any new properties.

**Inherits properties from:**

- astnode
- declaration

## Example

The `classDeclaration` pattern matches the following case:

[image: JavaScript code follows]

```
    class Base {
        constructor() {
            this.baseField = 21;
        }
    };
```

## See also

classExpression
