---
title: "mapLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/mapliteral.html"
content_id: "JOG_uBG4YrDsPFOtnzv5Iw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:53.604545+00:00"
---

# mapLiteral

Matches literal map expressions.

This pattern only matches nodes of type `expression`.

## Properties

`mapLiteral` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expressions` | `list<dynamicMapping>` | The key/value pairs that comprise the map |

**Inherits properties from:**

- astnode
- expression

## Example

In the following CodeXM code, the pattern `mapWithKeyValue` finds whether a map literal
contains an element that maps the key string `"foo"` to the integer `3`:

[image: CXM code follows]

```
    pattern mapFooTo3 {
        dynamicMapping {
            .propertyName == stringLiteral {
                .valueString == "foo"
            };
            .value == integerLiteral {
                .value == 3
            }
        }
    };

    pattern mapWithKeyValue {
        mapLiteral as mp where (
            exists s in mp.expressions where
                s matches mapFooTo3
        )
    };
```

## See also

dynamicMapping
