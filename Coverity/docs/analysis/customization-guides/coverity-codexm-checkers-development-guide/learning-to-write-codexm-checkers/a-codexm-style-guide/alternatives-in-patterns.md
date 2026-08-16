---
title: "Alternatives in patterns"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/alternatives-in-patterns.html"
content_id: "Uq98K8LtB3BB8G~rhlBI_A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:54.201363+00:00"
---

# Alternatives in patterns

Alternatives in multiline patterns that use the `|` separator should include the first, optional `|`.

The `switch` expression uses the same convention.

The following code shows an example:

[image: CXM code follows]

```
pattern operationExpressions {
    | binaryOperator as o ->
        {
            lhs = o.lhsExpression;
            rhs = o.rhsExpression
        }
    | unaryOperator as o ->
        {
            lhs = o.operandExpression;
            rhs = null
        }
};
```
