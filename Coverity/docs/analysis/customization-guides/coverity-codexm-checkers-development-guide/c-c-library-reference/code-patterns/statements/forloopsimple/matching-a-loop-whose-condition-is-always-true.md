---
title: "Matching a loop whose condition is always true"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/matching-a-loop-whose-condition-is-always-true.html"
content_id: "gs0gwM7LSqqYgh6ejz9kOA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:59.816216+00:00"
---

# Matching a loop whose condition is always true

The `foreverLoop` CodeXM pattern below matches a loop with a
constant `true` condition, such as `for(;;)`
or `while(1)` or a similar construct.

[image: CXM code follows]   

```
    // Some idioms to say "true" in C and C++
                pattern alwaysTrueConstant {
                | booleanLiteral { .isTrue == true }
                | intLiteral     { .valueInt != 0 }
                | binaryOperator { .lhsExpression == intLiteral{ .valueInt != 0 };
                .operator == `!=`;
                .rhsExpression == intLiteral{ .valueInt == 0 }
                }
                | binaryOperator { .lhsExpression == intLiteral{ .valueInt == 0 };
                .operator == `!=`;
                .rhsExpression == intLiteral{ .valueInt != 0 }
                }
                };
                
                // Detecting forever-while and forever-for loops
                pattern foreverLoop {
                | whileLoop     { .conditionExpression == alwaysTrueConstant }
                | forLoopSimple { .conditionExpression == alwaysTrueConstant }
                };
```
