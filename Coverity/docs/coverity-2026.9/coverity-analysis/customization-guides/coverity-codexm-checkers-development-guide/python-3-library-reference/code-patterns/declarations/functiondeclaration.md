---
title: "functionDeclaration"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/functiondeclaration.html"
content_id: "eIHyZl6C4X2DLmz61OUcIQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:50.193833+00:00"
---

# functionDeclaration

Matches function declarations.

This pattern only matches nodes of type `statement`.

## Properties

`functionDeclaration` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `argumentInfo` | `mapLiteral` | The initialization map for this function |
| `functionSymbol` | `symbol` | The symbol for this function |
| `isAsync` | `bool` | `true` if the function is declared `async` (Python 3) |

**Inherits properties from:**

- astnode
- declaration

## Example

The following CodeXM pattern matches the declaration of a function named `foo`:

[image: CXM code follows]

```
    pattern declarationFoo {
        functionDeclaration {
            functionSymbol == functionSymbol {
                .simpleName == "foo"
            }
        }
    };
```
