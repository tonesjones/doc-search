---
title: "Returning objects from patterns"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/returning-objects-from-patterns.html"
content_id: "yXt~xRhSY245XzBjCw7pVA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:41.884883+00:00"
---

# Returning objects from patterns

A custom CodeXM pattern can also return a new object. The object can have a different set of properties than the patterns
for which the custom pattern searches.

A returned object can be useful when you want to match multiple related code constructs and then handle information in a uniform way.

**Use case:**
:   Find loops.

    Such a checker might come in handy when you are reviewing a program's flow of control.

The following sample code finds loops of various types:

[image: CXM code follows]

```
pattern allLoops {
    | forLoopRange as loop ->
        {
            body      = loop.bodyStatement;
            condition = null;
            after     = null;
        }
    | forLoopSimple as loop ->
        {
            body      = loop.bodyStatement;
            condition = loop.conditionExpression;
            after     = loop.updateStatement;
        }
    | whileLoop as loop ->
        {
            body      = loop.bodyStatement;
            condition = loop.conditionExpression;
            after     = null;
        }
    | doWhileLoop as loop ->
        {
            body      = loop.bodyStatement;
            condition = loop.conditionExpression;
            after     = null;
        }
};
```

The pattern above matches four different kinds of loops: `while`, `do-while`, and the two kinds of `for` loop.
The C# or Java library patterns that match these (`forLoopRange`, `forLoopSimple`, `whileLoop`,
and `doWhileLoop`) each has its own particular set of properties.
The `loop` variable returned by our new `allLoops` pattern, on the other hand, uses three properties to summarize those different loop types. (The .after property applies only to forLoopSimple: It is the statement that is executed at the end of every iteration.)

As an example of using the custom `allLoops` pattern, suppose we wanted to write a CodeXM checker that inspected the body of each loop in the target code,
without caring what kind of loop contained that body. The following code sample shows how you could set this up:

[image: CXM code follows]

```
    for loop in allFunctionCode % allLoops :
        let body = loop.body in
            /*
                Something that needs to use the information in a loop's body,
                but doesn't care what kind of loop it is.
            */
```

The new pattern provides a generic way to locate loop bodies, greatly simplifying our search condition.

Note:
Some language libraries have a pattern to match all loop types. The C/C++ library and the Python library do not.
