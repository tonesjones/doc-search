---
title: "Using the 'debug()' function"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-the-debug-function.html"
content_id: "BjRfOTsc22K1Hd_FmSccvQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:47.661257+00:00"
---

# Using the 'debug()' function

The `debug()` function is useful when you debug your CodeXM checker.

This function prints its parameter (for example, a message string, the value of a variable, or both) to the console while your CodeXM checker executes.

Attention:
The `debug()` function does not generate output unless you specify the
`--codexm-print-debug` option when you invoke `cov-analyze`.

Because all functions return values (and you might not care what `debug()` returns),
when you use the `debug()` function wrap it inside a `let ... in` expression.

The following code sample shows how you might call `debug()`. (Because we don't care about the value that
`debug()` returns, we use the underscore as a placeholder variable name. We won't reference it elsewhere.)

[image: CXM code follows]

```
    for e in globalset allFunctionCode % someFilterPattern :
        let
            _ = debug("Value of e is: " + e)    // The message from debug()
                                                // is printed to the console.
        in {
                // Whatever you would ordinarily specify here
                // as the body of the 'for' expression.
    }
```

The code in this example prints to the console every expression that matches the filter pattern provided.
