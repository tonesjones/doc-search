---
title: "Defining CodeXM functions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/defining-codexm-functions.html"
content_id: "7IZtFG2uQXdkwIQeerAqeQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:48.403726+00:00"
---

# Defining CodeXM functions

In addition to custom patterns, CodeXM allows you to define your own functions.

Defining functions is particularly useful for structuring your CodeXM checker. Functions are even required to perform certain kinds of tests.
This section shows an example of that technique.

**Use case:**
:   Find a `throw` operator outside a `try` statement.

    A `throw` outside a `try` is simply poor logic.

This kind of search requires recursion, and to search recursively you need a function to call.

Here is an example of the code we want to examine:

[image: C++ code follows]

```
void f()
    {
        throw 1;          // Find this one.
    
        try {
            throw 2; 	 // But not this one.
        }
        catch( /*...*/ ) {
            return;
        }
    };
```

We can use the following pattern to check for `throw` operators that are not inside of a `try` statement:

[image: CXM code follows]

```
pattern badThrow {
    throwOperator as t
        where ! insideTry(t)
};
```

... But this example is not complete, because it relies on a call to the function `insideTry()`. Now we need to define that function as well.

CodeXM functions, like functions elsewhere, take arguments and return the value obtained from evaluating their function body.

To satisfy the needs of the pattern we defined above, the implementation of `insideTry()` returns a Boolean value that indicates
whether some ancestor of the function's argument is a `try` statement or not. The code to define the function looks like this:

[image: CXM code follows]

```
function insideTry(n : astnode) : bool ->
    if n.parent matches NonNull as p then   // Check whether parent exists
        switch(p) {
            | tryStatement -> true          // If a try statement, return true
            | default      -> insideTry(p)  // ... else, recursively check parent
        }
    else
        false                               // No more parents: not inside a try
    endif;
```

Examining this example, we see that the function expects an `astnode` argument
and returns a Boolean value.
(An `astnode` is a node in the Abstract Syntax Tree: in effect, any statement or expression.)

First, the function checks whether the node has a parent.

- If the node has no parent, the function returns `false`, since this node is already at the outermost level of the code being analyzed.
- If the node *does* have a parent, the function checks whether the parent is a `try` statement or not:
  It returns `true` when this is the case.
- If neither of the preceding cases apply, the function calls itself to recursively check whether the parent is inside of a `try` statement.

Functions, like patterns, are good for modularizing your code, providing easy-to-maintain reusable elements, or otherwise just giving descriptive names
to complicated logic.
Used together with checkers, they can make CodeXM an effective and powerful language.
