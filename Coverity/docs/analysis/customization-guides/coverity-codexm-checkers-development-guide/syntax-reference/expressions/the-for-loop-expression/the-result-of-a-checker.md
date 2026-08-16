---
title: "The result of a checker"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-result-of-a-checker.html"
content_id: "Umcxci~ZOKvC1peyC2mhWw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:34.614672+00:00"
---

# The result of a checker

If your `for` loop is the main loop of a checker, then its
`result-expression` must have a specific form; namely, it must be an expression that contains
a record named `events`.

In its turn, `events` must
define two properties: one named `description` and the other named
`location`.

Both these properties contribute to the issue report:
the `description` specifies a string to display,
and the `location` specifies the code location where the issue was found.

For example, the following code shows the `result-expression` for a checker named `UNINIT_VAR`:

[image: CXM code follows]

```
    {
        events = [
            {
                description = "Variable "
                              + decl.variable
                              + " is declared but not initialized.";
                location = code.location; 
            }
        ]
    };
```

**A fine point:**
In this example, `code` is the loop variable.
When you traverse the `globalset`, the loop variable has a
`.location` property that contains the source-line number
where the loop criterion was met.
