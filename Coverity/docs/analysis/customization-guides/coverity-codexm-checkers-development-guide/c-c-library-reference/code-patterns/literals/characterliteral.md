---
title: "characterLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/characterliteral.html"
content_id: "YQ9F6v6DGOcKM793HjsYTA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:34.252393+00:00"
---

# characterLiteral

Matches character literals.

This pattern only matches nodes of type `expression`.

## Properties

`characterLiteral` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `escape` | One of the following: `` `octal` ``, `` `hexadecimal` ``, `` `short UCN` ``, `` `long UCN` ``, `` `none` ``. | Indicates whether an escape sequence was used to specify the character type. The escape sequences and character formats appear as follows: `\0123` for octal, `\xabc` for hexadecimal, `\unnnn` for short UCN (Universal Character Name), `\Unnnnnnnn` for long UCN. |
| `kind` | One of the following: `` `char` ``, `` `char16` ``, `` `char32` ``, `` `u8` ``, `` `wchar` ``. | The type of the character. The character strings are formatted as follows: Character (8-bit): `'a'`, 16-bit character: `u'a'`, 32-bit character: `U'a'`, Unicode (8-bit): `u8'a'`, Wide character (also known as 16-bit Unicode)s: `L'a'`. |
| `value` | `int` | The numeric value of the character |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all '`a`' characters:

  
 [image: CXM code follows]   

```
    pattern lowercaseA {
        characterLiteral {
            .value == 'a'
        }
     };
```
