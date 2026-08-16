---
title: "Using switch statements"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-switch-statements.html"
content_id: "NFfywvEU1sFEGUvZCfmkzQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:46.285946+00:00"
---

# Using switch statements

As many common languages do, CodeXM has a `switch` expression that compares one value to multiple patterns
and returns a value based on the first pattern that matches.

The following sample code shows the overall syntax of a `switch`:

[image: CXM code follows]

```
    switch( /*variable*/ ) {
    | /* a pattern */        -> // What to return if a pattern matches
    | /* another pattern */  -> // What to return if a different pattern matches
    /*
    And so on: as many cases as you need
    */
    | default                ->  // What to return if we get here.
                                 // This clause is optional
                                 // (but strongly recommended).
    }
```

CodeXM only goes through the cases—in the order they are listed—until one of the patterns matches, or the until it reaches the `default` case. In any event, when a match does occur, the `switch` returns the corresponding result. Therefore, the order of your patterns within the `switch` matters.
The `default` case will always match if no case before it has done so.
(The `default` case is optional, but we recommend that you always use it.)

Since you specify a pattern before each arrow, you can also specify an `as variable`.
The variable definition goes after the pattern but before the arrow.
This way, the expression to the right of the arrow can use the local variable to refer to the pattern's result.
A variable specified within a case remains in scope until the next case begins (at the vertical bar).
Because the variable is local to a single case only, you can use the same variable name for several patterns.

The following sample code shows a completed switch statement that uses local, case-by-case variables:

[image: CXM code follows]

```
    let cond =
        switch(code) {
            | ifStatement as c -> [ c.condition ] // A list of one element
            | whileLoop as c   -> [ c.condition ]
            | forLoop as c     -> [ c.condition ]
            | default          -> [ ]             // An empty list
        }
    in
        // An expression using the variable cond, which is of type list<expression>
```

Note:
Strictly speaking, the vertical bar ( `|` ) before the first of the cases is optional, but our recommended style is to use it,
to maintain readability and visual consistency.

To summarize this example, the `switch` checks whether `code` matches one of three statement types:
in order, an `if`, a `while`, or a `for`.
If `code` does match one of these, then `cond` is assigned a one-element list that contains the
matching statement's conditional expression. If `code` does not match (the `default` case),
then `cond` is assigned an empty list.
