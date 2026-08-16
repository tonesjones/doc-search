---
title: "The builtin-type"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-builtin-type.html"
content_id: "b~fNUTC1XmkmwJ~ORceHAQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:59.528754+00:00"
---

# The builtin-type

CodeXM has several intrinsic built-in types.

(The `int` and `string` built-in types
correspond to the `int-literal` and `string-literal`
literal-expressions.)

## Syntax

Built-in types are identified by their reserved names.

  
 [image: Syntax diagram, builtin-type]   

```
builtin-type ::=
    'int' | 'bool' | 'string' | 'eventstring'
```

## Details

- `bool`

  A value that equals either `true` or `false`.
- `int`

  The type for an int-literal-expression or an integer variable.
- `string`

  The type for a string-literal-expression or a string variable.
- `eventstring`

  The type of a string value that has been formatted for output.

  For more information, see The eventstring.
