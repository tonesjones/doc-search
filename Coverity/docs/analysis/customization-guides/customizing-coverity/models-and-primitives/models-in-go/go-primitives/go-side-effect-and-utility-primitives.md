---
title: "Go side-effect and utility primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/go-side-effect-and-utility-primitives.html"
content_id: "KM_cCCxszSwG4oE8NyK~ew"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:53.989415+00:00"
---

# Go side-effect and utility primitives

These primitives handle the treatment of side effects and indeterminate
circumstances.

## `NonDet()`

Represents a nondeterministic condition that impacts the behavior of the method. The
precise characteristics of the condition are unimportant to analysis, and the
condition is expressed as a Boolean value. Analysis treats the value returned as it
would the return value from an unknown, unimplemented, or native method.

Calling `NonDet()` is considered evidence that either
`true` or `false` is a possible return value each
time the method is called, and generally you would want to use this primitive when
that is the case.

Under rare circumstances, the return value might be unknown (that is, when there is
no specific evidence that either `true` or `false` is
possible). When this is case, use the `Unknown` primitive and cast
its result to `bool`. This approach causes subtly different behavior
in the analysis, and in most cases is not necessary.

**See Also:**
`Unknown()`

## `Panic()`

Indicates that the remainder of an execution path is infeasible: is a so-called
*killpath*.

## `Unknown()`

Represents an unknown object, handled by the modeled method, the exact
characteristics of which are unimportant to the modeled behavior. You can cast,
dereference, or make assertions on the returned object as necessary.

The `Unknown()` primitive, like an externally implemented function,
returns a value that might or might not be correlated with another state in the
program, so a call to `Unknown` by itself is not considered evidence
that any particular return values are possible. Casting, dereferencing, or making
assertions about the result of `Unknown` can be useful for guiding
analysis, because in the absence of evidence that such operations can fail, the
analysis will assume the only interesting behaviors of the program are when they
succeed.

For example, having the model compare the result of `Unknown()` to
`null`, hints at the possibility that the result *can be*
`null`, and analysis takes this into account.

**See Also:**
`NonDet()`
