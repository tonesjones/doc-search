---
title: "newOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/newoperator.html"
content_id: "IjofyOLANDqGmIOP_Jphww"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:57.138927+00:00"
---

# newOperator

Matches the JavaScript `new` operator.

A *newExpression* (as specified in ECMAScript 2015 section 12.3) is an expression that creates an object.

This pattern only matches nodes of type `expression`.

## Properties

`newOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `argumentList` | `list<expression>` | The ordered list of explicit parameters |
| `constructor` | `functionSymbol` | The constructor |

**Inherits properties from:**

- astnode
- expression

## Example

In the following JavaScript example:

[image: JavaScript code follows]

```
    function C(a) {
        this.a = a;
    }
    var c1 = new C("Hello");
```

... `newOperator` matches the expression `new C("Hello")`,
where the `.constructor` property is the symbol that represents `C`
and the `.argumentList` property is the list `["Hello"]`.
