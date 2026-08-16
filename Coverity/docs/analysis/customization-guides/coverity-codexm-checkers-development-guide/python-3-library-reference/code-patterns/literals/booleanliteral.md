---
title: "booleanLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/booleanliteral.html"
content_id: "hkUWCEcoIloBrnzNQMAnCQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:49.451801+00:00"
---

# booleanLiteral

Matches Boolean literals: either `true` or `false`
(`True` or `False` as of Python 3).

This pattern only matches nodes of type `expression`.

## Properties

`booleanLiteral` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `value` | `bool` | Either `true` or `false` |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all `True` Boolean literals:

[image: CXM code follows]

```
    pattern trueBooleanLiteral {
        booleanLiteral {
            .value == true
        }
    };
```
