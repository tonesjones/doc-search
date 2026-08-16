---
title: "Constants"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/constants.html"
content_id: "9bekEps6mjKHsMJh3HFkiA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:57.686976+00:00"
---

# Constants

Avoid using "raw" literals in code. To improve maintainability and readability, use the `let` operator to create a global value that has a name.

Here is an example of creating a named constant:

[image: CXM code follows]

```
let b =
    switch(a) {
        | binaryOperator as o -> o.lhsExpression
        | unaryOperator as o -> o.operandExpression
        | default -> null
    }
```
