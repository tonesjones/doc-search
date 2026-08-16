---
title: "functionDeclaration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functiondeclaration.html"
content_id: "zmEmxfa_xaXxrHxq10m~bA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:18.799855+00:00"
---

# functionDeclaration

Matches function declaration statements.

A *functionDeclaration* (as specified in ECMAScript 2015, 14.1) is a statement that defines a function.

This pattern only matches nodes of type `statement`.

## Properties

`functionDeclaration` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `functionSymbol` | `symbol` | The declared function |

**Inherits properties from:**

- astnode
- declaration

## Example

The `functionDeclaration` pattern matches the following case:

[image: JavaScript code follows]

```
    function f() {
    };
```

## See also

functionExpression
