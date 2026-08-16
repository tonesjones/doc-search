---
title: "Conditional Expressions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/conditional-expressions.html"
content_id: "uJgi6SsYM7EprFvoLzRung"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:57.007343+00:00"
---

# Conditional Expressions

Use the `?:` operator only for simple conditional expressions that fit onto a single line.
If the conditional expression requires more than one line, or if you think that readability is important, use `if then else endif` instead.

Here is an example of using the `?:` operator:

[image: CXM code follows]

```
let maxStr = (x > y) ? "x is greater" : "y is greater"
```

Here is an example of using `if then else endif`, spanning several lines:

[image: CXM code follows]

```
let maxStr =
    if (x > y) then
        "x is greater"
    else
        "y is greater"
    endif
```

Place the keywords `if`, `else`, and `endif` at the same indentation level.
This applies to `elsif` clauses as well, as in the following example:

[image: CXM code follows]

```
if a matches binaryOperator as b then {
    lhs = b.lhsExpression;
    rhs = b.rhsExpression
} elsif a matches unaryOperator as b then {
    lhs = b.operandExpression;
    rhs = null
} else {
    lhs = a;
    rhs = null
} endif
```

If the logic of the conditions is hard to follow, it might be better to nest `if`-expressions, as the next example shows:

[image: CXM code follows]

```
if e.type matches intType { .isSigned == true } then
    let interval = getIntegerInterval(e) in
        if interval.lower matches NonNull as lower && lower gt;= 0 then
            `NEVER`
        else
            if interval.upper matches NonNull as upper && upper < 0 then
                `SURE`
            else
                `UNKNOWN`
            endif
        endif
else
    `NEVER`
endif
```
