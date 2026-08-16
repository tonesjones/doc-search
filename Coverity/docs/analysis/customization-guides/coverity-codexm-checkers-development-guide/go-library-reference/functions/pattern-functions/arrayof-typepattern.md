---
title: "arrayOf( typePattern )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/arrayof-typepattern-.html"
content_id: "mx03O3wD_f0gYwO1zWMwRw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:08.544252+00:00"
---

# arrayOf( typePattern )

A function that generates a pattern to match arrays of a particular type.

This can be used to construct patterns that match nested structure.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `typePattern` | `pattern` | A pattern matching a type |
| ***return value*** | `pattern` | A pattern matching an array type |

## Example

The following CodeXM snippet returns a pattern, `intArray`, that matches arrays of type `int`:

  
 [image: CXM code follows]   

```
   let intArray = arrayOf( pattern integertype { .kind == `int` } ) in
        for code in globalset allFunctionCode where code matches intArray {
            // ...
    };
```

## See also

arrayType
