---
title: "fieldReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/fieldreference.html"
content_id: "Y6ysKzxlJ2TeExN7Utterg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:27.758787+00:00"
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
