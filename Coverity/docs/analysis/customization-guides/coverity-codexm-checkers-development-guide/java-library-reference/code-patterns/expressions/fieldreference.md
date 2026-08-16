---
title: "fieldReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/fieldreference.html"
content_id: "TZMfCdF_xtrwKuMgaCpVVQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:03.314120+00:00"
---

# fieldReference

Matches where fields are referenced in expressions.

This pattern only matches nodes of type `expression`.

## Properties

`fieldReference` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `fieldSymbol` | `symbol` | The name of the field |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches when the field `example` is referenced:

  
 [image: CXM code follows]   

```
    pattern referringToExample {
        fieldReference {
            .fieldSymbol == symbol { .simpleName == "example"}
        }
    };
```
