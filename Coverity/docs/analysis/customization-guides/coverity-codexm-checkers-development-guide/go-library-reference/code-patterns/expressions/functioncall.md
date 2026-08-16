---
title: "functionCall"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functioncall.html"
content_id: "CcHJ_eRRxhpUOJX9ISl9sA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:38.024854+00:00"
---

# functionCall

Matches calls to functions.

This pattern only matches nodes of type `expression`.

## Properties

`functionCall` a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `argumentList` | `list<expression>` | A list of the arguments passed to the function |
| `calledExpression` | `expression` | The expression of the function being called |
| `calledFunction` | `functionSymbol` | The symbol of the function being called |
| `isNonStaticMethod` | `bool` | `true` if the function being called is a non-static method |
| `resolvedCallees` | `list<symbol>` | A list of the callees |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern finds function calls whose arguments are *not* variable references:

  
 [image: CXM code follows]   

```
    pattern nonReferenceArgument {
        functionCall as fn where
            exists a in fn.argumentList where
                ! (a matches variableReference)
    };
```

## See also

functionReference
