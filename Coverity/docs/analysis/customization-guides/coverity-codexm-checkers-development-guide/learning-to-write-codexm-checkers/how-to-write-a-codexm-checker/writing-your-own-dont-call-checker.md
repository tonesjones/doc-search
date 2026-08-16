---
title: "Writing your own Don't Call checker"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/writing-your-own-don-t-call-checker.html"
content_id: "n3pk_qInk2VsERllukJ3rg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:52.882598+00:00"
---

# Writing your own Don't Call checker

You can use CodeXM to add custom checkers of the *Don't Call* type.

A family of Coverity Analysis checkers known as *Don't Call* checkers (their names begin with "DC.")
report calls to functions that for one reason or another are considered risks to the security and integrity of a program.

Because it can execute operating system commands, the `system()` call in C and C++
is one such function, as we have mentioned before. Those sections were written with teaching the use of CodeXM in mind,
and so the examples they use are fragments of code.
Here is the complete code for a checker that provides a Don't Call for `system()`:

[image: CXM code follows]

```
include `C/C++`;

checker {
    name = "DONT_CALL_SYSTEM";
    reports = for call in globalset allFunctionCode % functionCall {
        .calledFunction.mangledName == "system"
    } : {
        events = [
            {
                description = "Calling " + call.calledExpression;
                location = call.location;
            }
        ];
    };
};
```

Although this is not a lengthy example, it brings together several of the features and techniques that previous sections have described.
