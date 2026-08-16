---
title: "Extended Backus-Naur form"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/extended-backus-naur-form.html"
content_id: "mAjgGFrAZMpeE8U34vMIww"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:06.694079+00:00"
---

# Extended Backus-Naur form

This reference also describes CodeXM syntax by using Extended Backus-Naur Form (EBNF).
EBNF is a notation that uses text rather than graphics to describe programming-language syntax.

This reference also describes CodeXM syntax by using Extended Backus-Naur Form (EBNF).
EBNF is a notation that uses text rather than graphics to describe programming-language syntax.

**Attention:** The syntax diagrams and EBNF notation both describe exactly the same syntax.
However, they do so in slightly different ways.
Do not be alarmed if there is not always a one-to-one correspondence between the symbols of the two notations.

Many variations of EBNF are in use. The variation we use, and describe in this section,
is based on that used by the [W3C](https://www.w3.org/TR/REC-xml/#sec-notation).
This version is comparatively simple, clean, and free of clutter.

## Basic components of EBNF

- The colon-colon-equals ( `::=` ) symbol means "is defined as".
  The name of the syntax element being defined appears to the left of this symbol, and the definition appears to its right.
- Literal character sequences (known as *terminals* in BNF) are shown enclosed by single-quote strings:
  for example, `'keyword'`
  or `'+'`.
  They are to be typed exactly as shown (without the enclosing quote marks, of course).
- Other syntax elements (known as *nonterminals)* are not enclosed by quotes.
  Like syntax-diagram elements enclosed by rectangular boxes, such elements of grammar are described elsewhere in this reference.
- Character sequences that can vary are enclosed by square brackets ( `[`
  and `]` ).
  These elements use [regular expression](https://en.wikipedia.org/wiki/Regular_expression) notation.
  Regular expressions typically specify a range of allowable characters. For example,
  `[a-z]` means "any single lowercase letter" and
  `[0-9]` means "any single digit".
- When the first character after the opening square bracket is a caret ( `^` )
  this means "none of the following characters". For example,
  `[^a-z]` means "any character except a lowercase letter' and
  `[^"]` means "any character except a double-quote".
- Both single characters and character ranges can be combined within the square brackets.
  For example, `[A-Za-z]` means "any single upper- or lowercase letter".
- When the definition shows any of the preceding elements—terminal strings, nonterminal syntax elements, or character sequences—in a partiicular order,
  the program code must include those elements in that same order.
- The vertical bar, `|`, represents an alternative:
  your code can include either what appears immediately to the left of the bar, or what appears immediately to the right, but it cannot include both.
  By extension, several items, each separated by a vertical bar, represent many individual alternatives:
  Your code can choose any one of these alternatives, but only one.
- When parentheses, `(` and `)`, enclose a group of elements, that group can behave as a single entity.

## Modifiers to basic EBNF

The grammatical elements described in the previous list can optionally be qualified by one of the following regular-expression conventions.

Remember:
When a qualifier follows a parenthesized group, the qualifier applies to the entire group as if the group were a single entity.

- When an asterisk, `*`, follows an entity, that entity can appear in the code zero or more times.

For example, the following EBNF specifies a lowercase letter followed by zero or more digits:

`[a-z][0-9]*`

CAUTION:

No parentheses group the range of letters `[a-z]` with the range of digits, so the asterisk applies only to the range of digits.
This character sequence begins with a lowercase letter, but there can be only one of these.

- When a plus sign, `+`, follows an entity, that entity must appear in the code one or more times.

For example, the following EBNF specifies a sequence of one or more digits—in other words, it can represent any positive integer:

`[0-9]+`

- When a question mark, `?`, follows an entity, that entity can appear zero times or one—in other words,
  the element is optional.

For example, the following EBNF specifies an optional semicolon:

`';'?`
