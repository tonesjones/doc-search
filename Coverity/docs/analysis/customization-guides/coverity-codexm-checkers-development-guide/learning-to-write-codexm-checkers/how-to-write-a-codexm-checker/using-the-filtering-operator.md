---
title: "Using the filtering operator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-the-filtering-operator.html"
content_id: "XKZdwiCj8VIAnXhMyEiTUg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:40.423878+00:00"
---

# Using the filtering operator

You can use the `%` operator, a set-filter expression (also known as the *which are* operator), to filter or simplify the code even further.

For this example, we'll use the `%` operator to help detect function calls.

**Use case:**
:   Add the *which are* operator `%` to our checker that finds calls to `system()`.

    This operator makes the code more concise and easier to read.

Since the CodeXM `where` clause happens to limit itself to just expressing a more precise `functionCall` pattern,
we can use the `%` operator and rewrite our code as follows
(we are only interested in those portions of the code that are function calls to `system()`):

[image: CXM code follows]

```
    for code in globalset allFunctionCode % functionCall {
        .calledFunction.identifier == "system"
    }
```

We can now quite economically define the entire checker, using both pattern decomposition and filtering, as follows:

[image: CXM code follows]

```
include `C/C++`;.

checker {
    name = "CALL_TO_SYSTEM";
    reports =
        for code in globalset allFunctionCode %
            functionCall { .calledFunction.identifier` == "system" } :
        {
            events = [
                {
                    description = "This is a call to "
                                  + "system".formattedAsCode
                                  + ".";
                    location    = code.location;
                }
            ]
        };
};
```

To summarize in plain English what the code does, the checker finds each call to the `system()` function, and reports each find.
The report describes the issue and shows where the call is located in the source code.

Note:
The construct `.formattedAsCode`, which we have not shown before, is a CodeXM property of any string value,
either constant or variable. It simply formats the string for display in Coverity Analysis output.
