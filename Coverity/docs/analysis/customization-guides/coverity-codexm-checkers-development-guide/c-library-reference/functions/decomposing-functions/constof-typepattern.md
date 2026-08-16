---
title: "constOf( typePattern )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/constof-typepattern-.html"
content_id: "8Ga6dY4bQ044DE9gTOC1gA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:40.745588+00:00"
---

# constOf( typePattern )

Matches types that have a `const` qualification.

The pattern produced by this function matches various forms of `const` qualification of the type
described by the `typePattern` field, including the following kinds of constants:

- An explicit `const` against a simple type
  (for example, `const int`)
- An alias defined against a `const`-qualified type
  (for example, `using cint = const int;`)

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `typePattern` | `pattern(type) -> Result` | A pattern matching some simple type |
| *return value* | `pattern(type) -> Result` | A pattern that matches a `const`-qualified variation of the given type |

## Example

Assuming that the following type definition appears in your C# source:

  
 [image: C# code follows]   

```
const int ci;
```

... then the use of this CodeXM pattern:

  
 [image: CXM code follows]   

```
constOf(int);
```

... matches the actual type `const int` in your source code.

## See also

cvModifiedType,
cvModifierKind
