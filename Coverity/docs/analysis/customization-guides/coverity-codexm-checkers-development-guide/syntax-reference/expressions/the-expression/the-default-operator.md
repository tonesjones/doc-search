---
title: "The 'default' operator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-default-operator.html"
content_id: "ib5Q3fOtEKDjhIPXnVxqNQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:22.330507+00:00"
---

# The 'default' operator

Besides introducing the default clause of a switch-expression, you can use the keyword `default` as an operator that matches any value.

The most common way to use `default` as an operator
is in a matches-expression; for example:

[image: CXM code follows]

```
&& objectPropertyValue(obj, "expiry") matches default as x
```

... In other words, this expression sets the value of `x` to equal the value of the `expiry`
property, regardless of what that value might be.
