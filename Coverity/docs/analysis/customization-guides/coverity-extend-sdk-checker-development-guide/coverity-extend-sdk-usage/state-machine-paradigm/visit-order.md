---
title: "Visit order"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/visit-order.html"
content_id: "qIQglv7FqyumQM68bOAbMg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:34.920166+00:00"
---

# Visit order

In addition to the *abstraction*, which was the subject of the Abstract interpretation section, an abstract interpreter also
*interprets*. This means that it simulates execution, modulo the chosen
abstraction.

Consequently, like a real interpreter, an abstract interpreter visits the abstract syntax
statements and expressions in execution order. For example, in the following fragment:

```
x = y + z;
a = foo(b, c*2);
```

the visit order is:

```
y
z
y + z
x = y + z
x
x = y + z;           // statement
b
c
2
c*2
foo(b, c*2)
a = foo(b, c*2)
a
a = foo(b, c*2);     // statement
```

This is called post-order traversal: the children of a given node are visited (recursively) in
order, and then the node itself is visited.

Left-hand sides of assignments are evaluated *after* the assignment, since the
left-hand side becomes the value of the entire assignment expression.

The previous visit order can be seen by running the `hello` checker that
we created in the previously (with the source file at
<HELLO>/hello.c) on
<install_dir>/sdk/hello/test2/hello.test.c.

When the abstract interpreter reaches choice points (such as an `if`
statement), it first follows one path, then later backtracks to follow the other. In
this way, all paths in the function are explored. See Paths for more detail about paths.
