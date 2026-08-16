---
title: "White space and comments"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/white-space-and-comments.html"
content_id: "uNUq2KtUgauguOtmA1ig_A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:08.016357+00:00"
---

# White space and comments

As with most software languages, white space in CodeXM is largely discretionary.

"A CodeXM style guide" does contain our
recommendations for laying out CodeXM code.

The exception is that you need white space to separate adjacent keywords and identifiers.

For example, `function myFunction` parses correctly,
but `functionmyFunction` does not: You need a space to separate the keyword
`function` from the identifier `myFunction`.

You can't put a space *within* an identifier.

Spaces within a literal character sequence, such as a string value or a member of an `enum`, are allowed and are significant.

In CodeXM, you can place a comment anywhere that white space is allowed and is not significant.
The format of comments in CodeXM will be familiar if you have used C, C++, or related programming languages.
Specifically, there are two kinds of comments:

- A comment enclosed between the character sequences `/*` and
  `*/`.
  These comments can span multiple lines:
- A comment that begins with the character sequence `//`.
  These comments run only from their beginning to the end of the line:

Here are examples:

[image: CXM code follows]

```
/*
    A multi-line comment:
    This one spans four lines.
*/
    
// This comment ends at the end of this line.
```
