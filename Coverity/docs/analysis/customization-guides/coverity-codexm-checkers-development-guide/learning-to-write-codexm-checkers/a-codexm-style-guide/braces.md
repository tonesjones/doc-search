---
title: "Braces"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/braces.html"
content_id: "NG18hNglQKmtJzHex8YAaA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:55.592112+00:00"
---

# Braces

Use the style known as the *One True Brace Style* (1TBS or OTBS).

This style is a variation of the Kernighan and Ritchie (K&R) style, the style used in those authors' book, *The C Programming Language*.

The salient points of the 1TBS style are:

- An opening brace is on the same line as the keyword that begins the block.
- A closing brace has the same level of indentation as the opening keyword.
- If a semicolon is required after a closing brace, both brace and semicolon appear on the same line.

The following code is an example of using the One True Brace Style:

[image: CXM code follows]

```
checker {
    name = "NO_GOTO";
    reports = {
        events = [
            // ...
        ];
    };
};
```

CAUTION:

Unlike some languages, CodeXM *does not support* using brackets to enclose a single statement
(as opposed to a block) for an `if` statement,
its `else` clause or `elsif` clauses,
or for the contents of a `for` loop.
