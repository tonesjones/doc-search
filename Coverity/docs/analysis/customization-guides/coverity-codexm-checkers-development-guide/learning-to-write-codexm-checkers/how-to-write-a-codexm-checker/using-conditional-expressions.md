---
title: "Using conditional expressions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-conditional-expressions.html"
content_id: "f3pbGW2JiZ52FbXz0QewSQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:47.006483+00:00"
---

# Using conditional expressions

CodeXM has both a familiar `if` statement, and a *ternary* or *conditional* operator,
`?:`, as in C and some other languages.

The following code fragment uses the conditional operator:

[image: CXM code follows]

```
    let loopStr =
        (code matches whileLoop) ? "is a while loop" : "is not a while loop"
    in
        /* ... Further processing ... */
```

In other words, if `code` matches the `whileLoop` pattern, the conditional returns the string `"is a while loop"`;
otherwise, it returns `"is not a while loop"`.

The conditional operator can be hard to read. We recommend you use it only for brief, one-line tests such as the previous example.
If the test requires more than a single line, and especially if it contains subexpressions, use an `if` statement.

Here is a sample of using an `if` statement to perform the same comparison we performed in the previous example:

[image: CXM code follows]

```
    let loopStr =
        if (code matches whileLoop) then
            "is a while loop"
        else
            "is not a while loop"
        endif
    in
        /* ... Further processing ... */
```

An `if` statement is constructed out of the keywords `if then elsif else endif`, where the `elsif` clauses
(there can be more than one of these) are optional.
