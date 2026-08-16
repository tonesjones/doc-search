---
title: "zeroInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/zeroinitializer.html"
content_id: "5BESDqhtH80rfXutGQsDZA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:58.463487+00:00"
---

# zeroInitializer

Matches setting the initial value of an object to zero.

`zeroInitializer` reports a match only in the following cases:

1. A named variable with static or thread-local storage duration that is not subject to
   constant initialization (since C++14), before any other initialization.
2. As part of a value-initialization sequence for non-class types, and for members of value-initialized
   class types that have no constructors, including value initialization of elements of aggregates
   for which no initializers are provided.
3. When a character array is initialized with a string literal that is too short,
   and the remainder of the array is zero-initialized.

## Properties

`zeroInitializer` does not expose any new properties.

**Inherits properties from:**

- astnode
- initializer

## Example

The following CodeXM pattern:

  
 [image: CXM code follows]   

```
    node matches zeroInitializer;
```

... matches the right-hand-sides of the declarations shown in the following source code:

  
 [image: C/C++ code follows]   

```
static int x
                
// assuming struct T { int x; }
T t = {};

char c[10] = {};
```
