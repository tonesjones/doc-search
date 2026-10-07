---
title: "unpackOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/unpackoperator.html"
content_id: "AcPitgl~WBCBE0LV4zRnPQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:53.007358+00:00"
---

# unpackOperator

Matches `unpack` operators (Python 3).

This pattern only matches nodes of type `expression`.

## Properties

`unpackOperator` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression that results from unpacking |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches applying the `*` operator to a list named `args`:

[image: CXM code follows]

```
    pattern unpackArgs {
        unpackOperator {
            .expression == variableReference {
                .simpleName == "args"
            }
        }
    };
```
