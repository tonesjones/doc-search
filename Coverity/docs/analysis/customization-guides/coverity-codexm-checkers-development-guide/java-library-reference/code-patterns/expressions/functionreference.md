---
title: "functionReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functionreference.html"
content_id: "8dLz_wUaVQaFL5i9VsxlyQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:04.716970+00:00"
---

# functionReference

Matches where expressions reference a function.

This pattern only matches nodes of type `expression`.

## Properties

`functionReference` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `functionSymbol` | `symbol` | The symbol representing the function |

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
                .functionSymbol == functionSymbol { .simpleName == "example" }
            }
        }
    };
```

## See also

functionCall
