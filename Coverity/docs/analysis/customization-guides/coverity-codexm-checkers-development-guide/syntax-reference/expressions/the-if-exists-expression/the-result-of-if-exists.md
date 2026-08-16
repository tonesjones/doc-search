---
title: "The result of if-exists"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-result-of-if-exists.html"
content_id: "w1cZ_zDNgO_VgG21kwsRNw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:38.066775+00:00"
---

# The result of if-exists

The result of an `if-exists-expression` is `null` if
the `set-producing-expression` is empty, or if the `set-producing-expression` does not contain
any member that meets the criterion expressed by the `condition-expression`.

While CodeXM is not procedural, this expression comes close.
You can visualize its operation as executing the following pseudocode:

```
if ( x in set-producing-expression satisfies condition-expression ) {
    return yield-expression				// The yield-expression is expressed in terms of x.
}
```
