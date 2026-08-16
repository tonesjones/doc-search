---
title: "arrayOf( typePattern )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/arrayof-typepattern-.html"
content_id: "0Ny9f60YNsNp7OKPnERIHg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:45.967853+00:00"
---

# arrayOf( typePattern )

Generates a pattern to match arrays of a particular type.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `typePattern` | `pattern` | A pattern matching a type |
| ***return value*** | `pattern` | A pattern matching an array type |

## Example

The following CodeXM snippet returns a pattern, `intArray`, that matches arrays of type `int`:

  
 [image: CXM code follows]   

```
    let intArray = arrayOf(pattern integralType { .kind == `int` }) in
        for code in globalset allFunctionCode where code matches intArray 
            // ...
```

## See also

arrayType
