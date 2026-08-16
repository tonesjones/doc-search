---
title: "fieldSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/fieldsymbol.html"
content_id: "qxxp49RFxD~LhrwQSKTP0A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:01.439650+00:00"
---

# fieldSymbol

Matches fields of a `class` (C++ only), `struct`, or `union`.

## Production

`fieldSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `access` | `enum` | The access kind of the field; can be `` `AK_NONE` ``, `` `fileprivate` ``, `` `internal` ``, `` `open` ``, `` `private` ``, `` `protected` ``, `` `protected internal` ``, `` `protected private` ``, or `` `public` `` |
| `isBitField` | `bool` | `true` if the field is declared as a bit-field |
| `isSignedBitField` | `bool` | `true` if the field is declared as a signed bit-field |
| `hasInitializer` | `bool` | `true` if the field has an initializer in its declaration |
| `isAnonymous` | `bool` | `true` if the bit-field was declared without a name |
| `bitWidth` | `int` | The bit-width of the field |
| `offset` | `int` | The offset from the start of the struct |
| `bitOffset` | `int` | The bit-offset from the start of the struct |
| `isClassStatic` | `bool` | `true` if the field is within a static class member |
| `isExplicitLambdaCapture` | `bool` | `true` if the field is an explicit capture in a lambda expression |
| `isVolatile` | `bool` | `true` if the field is within an object declared with the `volatile` specifier |
| `isAlignmentAssigned` | `bool` | `true` if the variable is aligned |
| `alignmentInBytes` | `int?` | The alignment of the type, in bytes; `null` if the type is not aligned |

**Inherits properties from:**

- symbol

## Example

Given the following source-code declaration:

  
 [image: C/C++ code follows]   

```
struct T {
    int m;
};
```

... the `fieldSymbol` pattern matches field `m`
of the `struct t` in the following code snippet:

  
 [image: C/C++ code follows]   

```
void test( struct T t ) {
    t.m++;
};
```

The following example shows one way to express the CodeXM pattern:

  
 [image: CXM code follows]   

```
    node matches variableReference {
        .variable matches fieldSymbol
    };
```
