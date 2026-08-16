---
title: "functionCall"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functioncall.html"
content_id: "mfeS8F7Ir~8huT7mxSjdKA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:27.691510+00:00"
---

# functionCall

Matches function call sites: places in the current code where a function is invoked.

This pattern only matches actual function call sites.
It *does not* match simple references to the function's identifier.
For example, it would not match the function name's appearance in code that assigned a function pointer to the function.

## Properties

`functionCall` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `calledFunction` | `functionSymbol?` | Information about the function itself; `null` if this is not available |
| `argumentList` | `list<expression>` | The parameters used in the call |
| `isVirtual` | `bool` | `true` if the function is a `virtual` method call (C++ only) |
| `isNonstaticMethod` | `bool` | `true` if the function call is into a class method that is not static (that is, it has a `this` pointer) |
| `isQualified` | `bool` | `true` if the function's return type has a qualifier |

**Inherits properties from:**

- astnode
- expression

## Example

The `functionCall` pattern matches source code that invokes a call to another function;
for example, `sum( i, j+k )`
in the initialization shown by the following target C/C++ code:

  
 [image: C/C++ code follows]   

```
int m = sum( i, j+k );
```

In this example, the `.calledFunction` property refers to the metadata
for the function `sum()`.
The `.argumentList` contains two items:
The first is a `variableReference` to `i`,
and the second is the `binaryOperator` that represents the addition of the variables
`j` and `k`.
