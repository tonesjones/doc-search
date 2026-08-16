---
title: "The 'sequence()' function"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-sequence-function.html"
content_id: "~RtmFs_lNEw9QXfQlZPXvw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:36.646218+00:00"
---

# The 'sequence()' function

The `sequence()` function reports on whether a particular execution sequence
occurs (or does not occur) in the code being analyzed.

The argument to `sequence()` is a `happens-before-expression`.
The function returns `true` if the `happens-before-expression` expression can be matched,
`false` if it cannot.

Typically, `sequence()` is called from within a
matches-expression.

CAUTION:

If the last element in the sequence is a call to a function that might not return (for example, the function throws an exception),
then `sequence()` might not report a match because the analysis notices that the call won't return, and stops before it adds the call to the sequence
(which normally happens after the call's effects).
In situations like this, match an argument to the call instead, by checking for its parent being a call.

It is common for function arguments to be cast, so you might have to check for a cast as well; and also check for a specific argument to avoid multiple matching.

For example, see the sample code that follows.

```
pattern endOfSequence {
    expression {
        .parent == functionCall { .calledFunction.identifier == "sink" } as call
    } as e where e == call.argumentList[2] && stripCasts(e)
          matches variableReference as arg -> {
        key = arg
    }
};
```

For more information about using the `sequence()` function
and the `>=>` operator, see
Path-sensitive analysis.
