---
title: "Operator precedence"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operator-precedence.html"
content_id: "I9Y1enDMBau8kjdM79opVQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:21.670912+00:00"
---

# Operator precedence

Within an expression, operators have a *precedence* that determines the order of their evaluation in the absence of parentheses.

Precedence is a convention originated by algebra, and used by nearly all programming languages.
CodeXM use0s such a convention as well, though some of its operations are not commonly used in other contexts.

Operators also have an *associativity,* also applied in the absence of parentheses.
This determines the order of evaluation when operators appear in a sequence;
for example, the order in which to execute `x + y + z` would be ambiguous
without associativity.
Addition/subtraction and multiplication/division associate to the left, so the order of executing the previous example is
`( x + y ) + z`.
(Parentheses have top priority, and override the default precedence of operations.)

The following table shows the order of precedence for the CodeXM operators.
The top row has the highest precedence, the bottom row the lowest.

| Operator | Associativity |
| --- | --- |
| `() {}` | not associative |
| `.` | left |
| `[]` | not associative |
| `as` | not associative |
| `%` | left |
| `new` | not associative |
| `default` | not associative |
| `matches` | left |
| `!`, unary `-` | right |
| `* /` | left |
| `+ - ++ ??` | left |
| `<=>` | left |
| `> < >= <=` | left |
| `== !=` | left |
| `&&` | left |
| `||` | left |
| `>=>` | left |
| `?:` | right |
| `in` | not associative |
| `where` | not associative |
