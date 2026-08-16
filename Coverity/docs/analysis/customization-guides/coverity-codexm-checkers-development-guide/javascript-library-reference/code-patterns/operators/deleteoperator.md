---
title: "deleteOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/deleteoperator.html"
content_id: "4srVAHqnH6gPNzd6moPUbw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:54.933399+00:00"
---

# deleteOperator

Matches a `delete` expression.

The JavaScript `delete` operator removes a property from an object.

Important:
The unaryOperator pattern *does not match*
the `delete` operator.

This pattern only matches nodes of type `expression`.

## Properties

`deleteOperator` does not expose any new properties.

**Inherits properties from:**

- astnode
- expression

## Example

This pattern could match the JavaScript expression `delete c1.a`,
where the property `.operandExpression` is `"c1.a"`.
