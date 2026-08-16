---
title: "fieldReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/fieldreference.html"
content_id: "8VEdxLEupmGsWqNR7Uvgbw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:37.300110+00:00"
---

# fieldReference

Matches expressions that reference fields.

This pattern only matches nodes of type `expression`.

## Properties

`fieldReference` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `fieldSymbol` | `symbol` | The field symbol |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches when a field `example` is referenced:

  
 [image: CXM code follows]   

```
    pattern referringToExample {
        fieldReference {
            .fieldSymbol == symbol { .simpleName == "example" }
        }
    };
```
