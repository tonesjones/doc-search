---
title: "floatLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/floatliteral.html"
content_id: "wTbFVp8g1VcibaVoNSbENw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:35.734784+00:00"
---

# floatLiteral

Matches all floating-point literals, including both single and double precision
(that is, the types `float`
and `double`).

This pattern only matches nodes of type `expression`.

## Properties

`floatLiteral` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `valueString` | `string` | The string representation of the literal |
| `suffix` | `enum floatSuffix?` | `` `f` `` or `` `l` `` if a suffix is specified in the source (see floatSuffix); `null` if there is no suffix. |
| `isLowercaseSuffix` | `bool` | `true` if the suffix is lower case in the source |
| `isLowercaseLSuffix` | `bool` | `true` if the suffix is a lowercase `l` (ell) |
| `isHexFloat` | `bool` | `true` if the literal is hexadecimal (preceded by `0x` or `0X`) |

**Inherits properties from:**

- astnode
- expression

## Example

In the case of the folllowing target C/C++ code:

  
 [image: C/C++ code follows]   

```
float x = 2.5f;
```

... a `floatLiteral` matches if `.valueString` is set to `"2.5"` and
`.suffix` is set to `` `f` ``.
The property `.isLowercaseSuffix` will be `true`.
