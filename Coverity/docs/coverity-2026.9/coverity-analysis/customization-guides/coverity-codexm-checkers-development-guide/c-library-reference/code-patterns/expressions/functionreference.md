---
title: "functionReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/functionreference.html"
content_id: "V_46zqzo4rgwkSA2SDWq4A"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:27.848356+00:00"
---

# functionReference

Matches expressions that reference functions.

This pattern only matches nodes of type `expression`.

## Properties

`functionReference` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `functionSymbol` | `symbol` | The symbol that represents the function |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches calls to a function named `example()`:

  
 [image: CXM code follows]   

```
    pattern callToExample {
        functionCall {
            .calledExpression == functionReference {
                .functionSymbol
                    == functionSymbol {
                        .simpleName ==  "example"
                       }
                                 }
        }
    };
```

## See also

functionCall
