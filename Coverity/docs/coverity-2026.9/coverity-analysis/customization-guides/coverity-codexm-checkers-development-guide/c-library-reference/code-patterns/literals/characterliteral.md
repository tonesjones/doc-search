---
title: "characterLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/characterliteral.html"
content_id: "p2Pwu4lE84932hXo4G_tcA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:28.944984+00:00"
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

The following CodeXM pattern matches all '`a`' characters:

  
 [image: CXM code follows]   

```
    pattern lowercaseA {
        characterLiteral {
            .value == 'a'
        }
    };
```
