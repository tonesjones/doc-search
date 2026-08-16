---
title: "Null coalescing"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/null-coalescing.html"
content_id: "DBO02uVoaTzLUa7Hew0FHQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:23.765671+00:00"
---

# Null coalescing

The null-coalescing operator `??` is not strictly speaking an addition operation,
but it does have the same precedence as the other additive operators.

This operator evaluates its left-hand operand. If this is not `null`,
this is the value that `??` returns; otherwise, it returns its right-hand operand.
The point is to return a result that is usable in expression evaluations, and will not cause a run-time failure.

The following expression returns the same result as `??`, but does so in a lengthier fashion:

[image: CXM code follows]

```
    leftHandOperand matches NonNull as noLongerNull ? noLongerNull
                                                    : rightHandOperand
```

For more information, see Handling null values
