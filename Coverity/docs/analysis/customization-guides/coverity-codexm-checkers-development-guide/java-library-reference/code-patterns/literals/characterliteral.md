---
title: "characterLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/characterliteral.html"
content_id: "ds7KUGbPlJC3QzFlIh6quw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:09.873272+00:00"
---

# characterLiteral

Matches character literals.

This pattern only matches nodes of type `expression`.

## Properties

`characterLiteral` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `value` | `int` | The numeric value of the character |

**Inherits properties from:**

- astnode
- expression

## Example

The following pattern matches all instances of the character literal `'a'`:

  
 [image: CXM code follows]   

```
    pattern lowercaseA {
        characterLiteral {
            .value == 'a'
        }
    };
```
