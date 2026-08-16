---
title: "The result of a for-loop"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-result-of-a-for-loop.html"
content_id: "OxUEUxtvhsv2dWaK_jfaHg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:33.964546+00:00"
---

# The result of a for-loop

The result of a `for` loop is a set that contains
each `result-expression` that was found by the loop and whose value was not `null`.

For example, the following sample code shows a simple `for-loop-expression`
(we presume that the function `odd()` has been coded previously,
perhaps in a library):

[image: CXM code follows]

```
    for x in [1, 2, 3, 4, 5, 6]
        where odd(x) :
            x * 2
```

The preceding code produces a set that contains twice the value of each odd number in the `set-producing-expression`.
The following snippet shows this result:

[image: CXM code follows]

```
    [2, 6, 10]
```
