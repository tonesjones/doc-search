---
title: "integerLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/integerliteral.html"
content_id: "7~YgWP~b2cQ5yVRFgsivmw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:52.303743+00:00"
---

# integerLiteral

Matches literal integer values.

The Python library does not distinguish between integers of type `int` or `long`.

This pattern only matches nodes of type `expression`.

## Properties

`integerLiteral` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `base` | `enum` | Either `` `binary` ``, `` `decimal` ``, `` `octal` ``, or `` `hexadecimal` `` |
| `value` | `int` | The value of the integer |

**Inherits properties from:**

- astnode
- expression

## Example

The following source pattern:

[image: Python code follows]

```
    f = 44;
```

... could be matched by the following CodeXM code:

[image: CXM code follows]

```
    f matches integerLiteral { .valueString == "44" };
```
