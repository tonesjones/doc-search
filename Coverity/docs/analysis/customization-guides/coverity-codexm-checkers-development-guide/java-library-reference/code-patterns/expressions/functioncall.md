---
title: "functionCall"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functioncall.html"
content_id: "VMRFrrHJLTxLg0Fwix_UHg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:04.037469+00:00"
---

# functionCall

Matches function call locations.

This pattern only matches nodes of type `expression`.

## Properties

`functionCall` produces a record that contains the following properties:

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

The following CodeXM pattern finds function calls that have anything but variable references as their arguments:

  
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
