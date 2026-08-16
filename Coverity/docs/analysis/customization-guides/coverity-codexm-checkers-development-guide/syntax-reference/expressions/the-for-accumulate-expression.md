---
title: "The for-accumulate-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-for-accumulate-expression.html"
content_id: "DYSSyQoYm8L0_FXwgeYv6Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:31.117716+00:00"
---

# The for-accumulate-expression

The `for-accumulate-expression` traverses a set or a list.
For each member that it visits, it performs an operation.
It accumulates the results of these operations,
then returns the accumulated value as its result.

(If you are familiar with functional programming, you might recognize this as a
[fold operation](https://en.wikipedia.org/wiki/Fold_(higher-order_function)) over a set of elements.)

## Syntax

The syntax of the `for-accumulate-expression` is very similar to the syntax of
the for-loop-expression. The main difference is the additional `accumulate` clause.

The keyword `for` introduces the loop variable.
The loop variable will be assigned, in turn, each of the values in the set being examined.
The set itself is introduced by the keyword `in`, followed by the variable or expression that represents
the set.

The keyword `accumulate` follows the `set-expression`.
It introduces the `accumulator-identifier`, which names the accumulator variable. This is followed by an
equals sign ( `=` ) followed by
an `initial-expression`.

(You have the option of also specifying an explicit type for the accumulator.)

To filter the set to only those members that meet a specific criterion, you can use the `where` keyword followed by a
`condition-expression` that describes the criterion.
(If you omit the filter condition, the loop visits every member of the set: It is as if the `condition-expression` were simply the value
`true`.)

Finally, a colon ( `:` ) introduces the `yielding-expression`.

The variable named by `identifier` is within scope, and can be referred to, in both the
`condition-expression` and the `yielding-expression`.
The `accumulator-identifier`, and any variable that is defined in the `where` clause,
is within the scope of the `yielding-expression`.

  
 [image: Syntax diagram, for-accumulate-expression]   

```
for-accumulate-expression ::=
    'for' identifier 'in' set-expression
    'accumulate'
        accumulator-identifier ( ':' type )? '=' initial-expression
        ( 'where' condition-expression )? ':' yielding-expression
```

The `set-expression` must result in a set or a list.

The `initial-expression` sets the initial value of the accumulator variable.

The `condition-expression` describes a condition (criterion).
Members of the set that do not meet this condition are not evaluated.

For each member that is evaluated, the result of the `yielding-expression` is assigned to the accumulator variable.
When the loop has completed, it returns the final value of the accumulator.
