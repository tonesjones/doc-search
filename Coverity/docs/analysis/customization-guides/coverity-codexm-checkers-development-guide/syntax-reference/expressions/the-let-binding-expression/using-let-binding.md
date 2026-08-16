---
title: "Using let-binding"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-let-binding.html"
content_id: "X1xZOe8f9VmjaWsZ7aBOkA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:41.850450+00:00"
---

# Using let-binding

The `let-binding-expression` defines a variable, computes its value,
then makes that variable available to a subsequent expression during which the variable is accessed.

Because CodeXM is a functional programming language (not a procedural one), the value of a "variable" does not change while the
variable is in scope.
You cannot assign a new and different value to an existing variable.

The following code scheme shows this construction:

[image: CXM code follows]

```
    let x = // Some computation
        in  // An expression that refers to x
```

**Not really exceptions:**
With a `for-loop-expression` or a `for-accumulate-expression`,
the loop variable *does* change over time.
In both these cases, even though the variable changes while the loop is running, the value the loop returns cannot change any further,
so loops are not an exception to the general rule.
