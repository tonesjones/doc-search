---
title: "variableDeclaration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/variabledeclaration.html"
content_id: "kxgA9M_0DOfM0rN8kVRnAQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:19.549548+00:00"
---

# variableDeclaration

Matches variable declarations.

This pattern only matches nodes of type `statement`.

## Properties

`variableDeclaration` does not expose any new properties.

**Inherits properties from:**

- astnode
- declaration

## Example

Matches the declaration of the variable `a` in the following function:

[image: JavaScript code follows]

```
    function f() {
        var a = 0;
    };
```

In this instance, the `.variable` property is the symbol representing `a`,
and the `.initializer` property is the initializer `0`.
