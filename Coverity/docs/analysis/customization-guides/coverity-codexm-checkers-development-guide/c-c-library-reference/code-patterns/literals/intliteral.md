---
title: "intLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/intliteral.html"
content_id: "nOhKa1d0_EAFYvgmGMZiQQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:36.489687+00:00"
---

# intLiteral

Matches all integer literals, regardless of their sign or base.

This pattern only matches nodes of type `expression`.

## Properties

`intLiteral` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `value` | `int` | The actual value represented by the literal |
| `base` | `enum` | `` `binary` ``, `` `decimal` ``, `` `octal` ``, or `` `hexadecimal` `` |
| `kind` | `enum intKind` | `` `bool` ``, `` `char` ``, `` `short` ``, `` `int` ``, `` `long` ``, or `` `long long` `` (C++ only); see intKind |
| `llzsuffix` | `enum?` | `` `l` `` or `` `ll` `` if the literal has one of these suffixes; `null` otherwise |
| `isLowercaseLSuffix` | `bool` | `true` if the suffix is lower case |
| `hasUSuffix` | `bool` | `true` if the suffix is `U` (for unsigned) |
| `isLowercaseSuffix` | `bool` | `true` if *all* the suffixes are lower case |

**Inherits properties from:**

- astnode
- expression

## Example

Consider the following literal initialization in C or C++:

  
 [image: C/C++ code follows]   

```
long x = 8888l;
```

The value `8888l` produces an integer literal,
so an `intLiteral` pattern matches it.
The `.value` property will be `8888`,
`.kind` will be `` `long` ``,
`.llSuffix` will be `` `L` ``,
and `.isLowercaseLSuffix` will be `true`.

Because the appearance of the lowercase letter L (`l`)
is nearly indistinguishable from the digit *one* (`1`)
in many typefaces and environments, many coding standards require that the suffix always be uppercase
to avoid misinterpretation.
The following CodeXM pattern matches violations of this rule:

  
 [image: CXM code follows]   

```
    pattern intLiteralLowercaseSuffix {
        intLiteral {                      // An integer literal
            .llSuffix != null;            // ... that has a suffix
            .isLowercaseLSuffix == true;  // ... that is lowercase
        }
    };
```
