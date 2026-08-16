---
title: "hasBaseType( typeName )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/hasbasetype-typename-.html"
content_id: "GrskSkz5xZiVRUszfMb7JQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:21.664910+00:00"
---

# hasBaseType( typeName )

For `pointerType`, `arrayType`, `typeQualifier`,
`typedefType`, or `deducedType`,
returns the base type of these types;
that is, the type a pointer points to, the type contained in an array, and so on.

This function is applied recursively, so that like the pattern functions,
it can resolve declarations that resolve to `typeName`.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `typeName` | `type` | The type to match |
| ***return value*** | `type` | The base type without pointers, arrays, or qualifiers |

## Example

The following C/C++ code defines the integer type `sideLength`,
and then declares a pointer to the new type:

  
 [image: C/C++ code follows]   

```
typedef int sideLength;
Length *sideLength;
```

The following CodeXM pattern uses `hasBaseType()` to check whether the type passed in
(`ty`) resolves to an integer.
It would match the sample above.

  
 [image: CXM code follows]   

```
    pattern isInteger {
        type as ty where
            ( hasBaseType( ty ) matches intType )
    };
```

The `hasBaseType()` function can also check whether two types are the same,
as in the following CodeXM function declaration shows:

  
 [image: CXM code follows]   

```
    function typeIsTheSame( type1, type2 ) : bool ->
        hasBaseType( type1 ) == hasBaseType( type2 );
```
