---
title: "imaginaryLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/imaginaryliteral.html"
content_id: "hZIQD5LE9olbInCyCHPAyg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:44.219702+00:00"
---

# imaginaryLiteral

Matches the imaginary part of a complex number.

This pattern only matches nodes of type `expression`.

## Properties

`imaginaryLiteral` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `valueString` | `string` | The value of the imaginary component of the complex number, represented as a string. |

**Inherits properties from:**

- astnode
- expression

## Example

Given the following snippet of Go source:

  
 [image: Go code follows]   

```
    33.14i
```

... the following CodeXM pattern would match it:

  
 [image: CXM code follows]   

```
    f matches imaginaryLiteral { .valueString == "33.14" }
```
