---
title: "functionCall"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functioncall.html"
content_id: "PckxK3MO28EsSI_aHR1cDA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:41.402130+00:00"
---

# functionCall

Matches calls to functions.

This pattern only matches nodes of type `expression`.

## Properties

`functionCall` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `argumentList` | `list<expression>` | The arguments passed to the function |
| `calledExpression` | `expression` | The expression of the function being called |
| `calledFunction` | `functionSymbol` | The symbol of the function being called |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern finds function calls being passed arguments that are not variable references:

[image: CXM code follows]

```
    pattern nonReferenceArgument {
        functionCall as fn where
            exists a in fn.argumentList where
                ! ( a matches variableReference )
    };
```
