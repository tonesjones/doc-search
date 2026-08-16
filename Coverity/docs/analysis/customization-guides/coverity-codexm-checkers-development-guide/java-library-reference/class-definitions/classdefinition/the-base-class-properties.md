---
title: "The base class properties"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-base-class-properties.html"
content_id: "H7VccSYa5~oNq7oR0UpshA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:12.527609+00:00"
---

# The base class properties

This describes how to use base classes.

The function provided by the `findBaseproperty` has this form:

  
 [image: CXM code follows]   

```
function <testType> ( callback:
    function( base: typeof( classType ).producedType ) ->
        testType?
);
```

The function provided by the `findMatchingBaseproperty` has this form:

  
 [image: CXM code follows]   

```
function <testType> ( pattern( typeof( classType ).matchedType ) ->
    testType ) ->
        testType?
;
```

The `findBaseClass` call detects whether a base class is accepted by the callback function.
If the callback returns a non-null value, then `findBaseClass` returns that value (which matches `NonNull`).
If the callback does not return such a non-null value on any base class, `findBaseClass` returns `null`.

The `findMatchingBaseClass` call uses a pattern rather than a callback function,
but it returns either a matching value or `null`,
just as `findBaseClass` does.

Because both these function calls accomplish the same thing, for the most part which one you choose to use is up to you.
The pattern form can be easier, and less lengthy, to code (see the examples that follow);
on the other hand, a callback function can encode tests that a pattern cannot.

The following "Examples" section shows checkers that use these properties.
