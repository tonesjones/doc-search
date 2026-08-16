---
title: "Writing an A_THEN_B checker"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/writing-an-a_then_b-checker.html"
content_id: "FHP3C6RgzkiaAPSQ1AZKRA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:52.214663+00:00"
---

# Writing an A_THEN_B checker

Writing a checker that detects where one function call is not immediately followed by another
is related to path-sensitive analysis, but is somewhat more subtle to code.

The solution is to locate the function calls within the Abstract Syntax Tree (AST).
Two functions accomplish this:

```
/**
 * Return the index of "n", if any, within "l", starting the search at "startIndex".
**/
function getIndexInListStartingAt(l: list<astnode>, n: astnode, startIndex: int): int? ->
    if startIndex >= l.length then null
    elsif l[startIndex] == n then startIndex
    else  getIndexInListStartingAt(l, n, startIndex + 1)
    endif
;

/**
 * Return the index of "n", if any, within "l"
**/
function getIndexInList(l: list<astnode>, n: astnode): int? ->
    getIndexInListStartingAt(l, n, 0)
;
```

With these two functions in place, the core of the checker is a third function that
employs them to find the A-then-B pattern:

```
/**
 * Return whether "callToA" is immediately followed by a call to "B".
**/
function isFollowedByB(callToA: astnode) ->
    // "A()" must be in a statement on its own, A();
    // That means the parent is a simpleStatement.
    callToA.parent matches simpleStatement as simple
    &&
    // It needs to be immediately followed by another statement in a block. Check for a block.
    simple.parent matches blockStatement as block
    &&
    // Get the index of the statement with the call in the block's statement list.
    // It must be present, but the type system mandates a check.
    getIndexInList(block.containedStatements, simple) matches NonNull as index
    &&
    // Check that the next statement is a call to B().
    // Note that, while containedStatements[index + 1] is optional, we can still match it directly.
    block.containedStatements[index + 1] matches simpleStatement { .expression == functionCall { .calledFunction.identifier == "B" } }
;
```

Once you have coded the `isFollowedByB()` function, the top-level
checker definition is actually quite simple.

Here is the code for the entire checker:

```
// A_THEN_B: A checker that reports if a call to a function called A
// is not immediately followed by a call to a function called B.

include `C/C++`;

/**
 * Return the index of "n", if any, within "l", starting the search at "startIndex".
**/
function getIndexInListStartingAt(l: list<astnode>, n: astnode, startIndex: int): int? ->
    if startIndex >= l.length then null
    elsif l[startIndex] == n then startIndex
    else  getIndexInListStartingAt(l, n, startIndex + 1)
    endif
;

/**
 * Return the index of "n", if any, within "l"
**/
function getIndexInList(l: list<astnode>, n: astnode): int? ->
    getIndexInListStartingAt(l, n, 0)
;

/**
 * Return whether "callToA" is immediately followed by a call to "B".
**/
function isFollowedByB(callToA: astnode) ->
    // "A()" must be in a statement on its own, A();
    // That means the parent is a simpleStatement.
    callToA.parent matches simpleStatement as simple
    &&
    // It needs to be immediately followed by another statement in a block. Check for a block.
    simple.parent matches blockStatement as block
    &&
    // Get the index of the statement with the call in the block's statement list.
    // It must be present, but the type system mandates a check.
    getIndexInList(block.containedStatements, simple) matches NonNull as index
    &&
    // Check that the next statement is a call to B().
    // Note that, while containedStatements[index + 1] is optional, we can still match it directly.
    block.containedStatements[index + 1] matches simpleStatement { .expression == functionCall { .calledFunction.identifier == "B" } }
;

checker {
    name = "A_THEN_B";
    reports = for callToA in globalset allFunctionCode % functionCall { .calledFunction.identifier == "A" } where !isFollowedByB(callToA):
        { events = [
            {
                // Generally you get best results by using
                // "call.calledExpression" in your message. Note that
                // call.calledFunction is optional and cannot be printed
                // directly.
                description = "Call to " + callToA.calledExpression +
                    // This is a good use of "formattedAsCode"
                    "is not followed by a call to " + "B".formattedAsCode + ".";
                location = callToA.location;
            }
          ];
        };
};
```
