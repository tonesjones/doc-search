---
title: "C# and Visual Basic side-effect and utility primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/c-and-visual-basic-side-effect-and-utility-primitives.html"
content_id: "660nSfcnN35SGGUxQnitLg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:48.689217+00:00"
---

# C# and Visual Basic side-effect and utility primitives

These primitives handle the treatment of side effects and indeterminate
circumstances.

## `SideEffect.SideEffectFree()`

Any method calling this primitive is assumed to have no useful side effects outside
of its return value.

## `SideEffect.SideEffectOnlyThis()`

Any method calling this primitive is assumed to have no useful side effects outside
of modifying its receiver (*this)* and possibly returning a value. The analysis
currently interprets this exactly as `SideEffects`, but in the future
that might change, to help in finding more USELESS_CALL defects.

## `SideEffect.SideEffects()`

Any method calling this primitive is assumed to have potential side effects outside
of its return value. Instead, calling `SideEffectOnlyThis` is
preferred when it applies. Calling this primitive is not strictly necessary, as any
method definition given to `cov-make-library` is presumed to
have side effects in the absence of one of these primitives. However, calling one
such primitive in each custom model for non-void methods is recommended, even if it
is `SideEffects`, to indicate that the most appropriate one was
selected.

## `Util.KillPath()`

Indicates that the remainder of the path is infeasible (a *killpath)*.

## `Util.Nondet()`

Represents some nondeterministic condition impacting the behavior of the method, the
precise characteristics of which are unimportant to analysis, expressed as a
Boolean. The analysis treats the value returned as it would the return value from an
unknown, unimplemented, or native method.

Calling `Nondet` is considered evidence that both
`true` and `false` are possible each time it is
called, and generally you would want to use this. Under rare circumstances, you
might want an unknown Boolean (that is, no specific evidence that both
`true` and `false` are possible). In this case,
cast the result of `Util.Unknown` to `bool` and use
that. Doing so causes subtly different behavior in analysis, and in most cases is
not necessary.

**See also:**
`Util.Unknown()`

## `Util.Unknown()`

Represents some unknown object, handled by the modeled method, the exact
characteristics of which are unimportant to the modeled behavior. You cam cast,
dereference, or make assertions on the returned object as necessary.

`Unknown`, like an externally implemented function, returns a value
that may or may not be correlated with other states in the program, so a call to
`Unknown` by itself is not considered evidence that any
particular return values are possible. Casting, dereferencing, or making assertions
about the result of `Unknown` is useful for guiding analysis, because
in the absence of evidence that they can fail, the analysis will assume the only
interesting behaviors of the program are when they succeed. For example, having the
model compare the result of `Unknown` to `null` hints
at that possibility, which is reflected in analysis.

**See also:**
`Util.Nondet()`
