---
title: "undefinedLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/undefinedliteral.html"
content_id: "RIfi5WHi1sZGtEaa~JuiwA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:56.920839+00:00"
---

# undefinedLiteral

Matches undefined literals.

The Python language does not support an "undefined literal",
but sometimes one appears in the abstract syntax tree.
Usually this happens when parsing creates a temporary variable whose value later needs to become undefined.

This pattern only matches nodes of type `expression`.

## Properties

`undefinedLiteral` does not expose any new properties.

**Inherits properties from:**

- astnode
- expression

## Example

In the following Python code, at line 4 the variable `a` is set to an undefined literal.
The `undefinedLiteral` pattern would match this occurrence:

[image: Python code follows]

```
def outer():
a = 0
class Cls:
    b = (a + 1 for a in l);
```
