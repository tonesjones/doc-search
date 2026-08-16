---
title: "localVariableReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/localvariablereference.html"
content_id: "rMH1C4N1zMMYHEhzbRv8WA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:34.215248+00:00"
---

# localVariableReference

Matches references to locally declared variables.

This includes references to `let`,
`const`, and `class` variables declared
at the global scope, since these behave as local variables.

Declarations with `var` and `function` at the global scope are not included
because these behave as accesses of properties of the global object:
Use the globalAccess pattern to match these cases.

This pattern only matches nodes of type `expression`.

## Properties

`localVariableReference` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `identifier` | `string?` | The identifier of the referenced variable; `null` if there is none |
| `mangledName` | `string?` | The mangled name of the referenced variable; `null` if there is none |
| `variable` | `symbol` | The symbol referenced |

**Inherits properties from:**

- astnode
- expression

## See also

globalAccess
(matches `var` and `function` definitions occurring in the global scope),
localVariableSymbol
