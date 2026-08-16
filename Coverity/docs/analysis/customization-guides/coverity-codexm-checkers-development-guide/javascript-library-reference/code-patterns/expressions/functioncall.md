---
title: "functionCall"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functioncall.html"
content_id: "NmchjmZ_5bQ0S08xWjfLWw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:29.973001+00:00"
---

# functionCall

Matches function calls.

Note:
The `argumentList` only contains explicit arguments.
It does not include `this` or `new.target`.

This pattern only matches nodes of type `expression`.

## Properties

`functionCall` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `argumentList` | `list<expression>` | The list of explicit arguments |
| `calledExpression` | `expression` | The called expression |
| `calledFunction` | `symbol?` | The symbol of the called function; `null` if there is none |
| `isMethodCall` | `bool` | `true` if this is a method call against an object |

**Inherits properties from:**

- astnode
- expression

## Example

Matches calls to functions; for example, `f(1)`.
