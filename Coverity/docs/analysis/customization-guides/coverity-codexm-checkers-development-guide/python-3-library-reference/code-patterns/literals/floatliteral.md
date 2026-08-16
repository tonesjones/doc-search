---
title: "floatLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/floatliteral.html"
content_id: "DividDTAhaVeK025IQcvtg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:50.830266+00:00"
---

# floatLiteral

Matches literal floating-point values.

The Python library does not distinguish between floating-point values of type `float` or `complex`.
However, you *can* search for the imaginary component of a complex value:
See imaginaryLiteral.

This pattern only matches nodes of type `expression`.

## Properties

`floatLiteral` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `valueString` | `string` | The floating-point value, represented as a string |

**Inherits properties from:**

- astnode
- expression

## Example

The following source pattern:

[image: Python code follows]

```
    2.5;
```

... could be matched by the following CodeXM code:

[image: CXM code follows]

```
    f matches floatLiteral { .valueString == "2.5" };
```
