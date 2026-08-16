---
title: "imaginaryLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/imaginaryliteral.html"
content_id: "BlKky9oohmsSenk8K1pjMA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:51.569644+00:00"
---

# imaginaryLiteral

Matches the imaginary part of literal complex-number values.

This pattern only matches nodes of type `expression`.

## Properties

`imaginaryLiteral` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `valueString` | `string` | The complex component of the imaginary value, represented as a string |

**Inherits properties from:**

- astnode
- expression

## Example

The following source pattern:

[image: Python code follows]

```
    33.14j;
```

... could be matched by the following CodeXM code:

[image: CXM code follows]

```
    f matches imaginaryLiteral { .valueString == "33.14" };
```
