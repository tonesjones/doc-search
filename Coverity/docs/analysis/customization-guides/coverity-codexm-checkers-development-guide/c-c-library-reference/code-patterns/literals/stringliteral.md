---
title: "stringLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/stringliteral.html"
content_id: "5gMOv_9geHxFY45D64poGw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:37.978280+00:00"
---

# stringLiteral

Matches all character string literals.

This pattern only matches nodes of type `expression`.

## Properties

`stringLiteral` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `valueString` | `string` | The actual string |
| `encodingType` | `enum stringLiteralEncoding` | `` `char` ``, `` `wchar` ``, `` `utf16` ``, or `` `utf32` ``; see stringLiteralEncoding |

**Inherits properties from:**

- astnode
- expression

## Example

Consider the following target-code declaration:

  
 [image: C/C++ code follows]   

```
char str[] = "hello";
```

In this case, the `stringLiteral` pattern matches `"hello"`,
with `.valueString` containing the string itself and
`.encodingType` set to `` `char` ``.

The following CodeXM pattern matches a `stringLiteral` whose encoding type
is `` `char` ``, such as the one in the previous example:

  
 [image: CXM code follows]   

```
    pattern stringPtn {
        stringLiteral {
            .encodingType == `char`
        }
    };
```
