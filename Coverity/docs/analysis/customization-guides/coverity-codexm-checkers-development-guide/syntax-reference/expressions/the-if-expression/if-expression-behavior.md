---
title: "if-expression behavior"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/if-expression-behavior.html"
content_id: "PhO5SBs9eN6KscbfXdD9AQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:39.544094+00:00"
---

# if-expression behavior

Once the `conditional-expression` evaluates an `if-true-expression`,
it does not evaluate any subsequent expressions in the `if`.

If a `condition` defines a variable
(for example, via the matches-expression `as` keyword),
that variable remains in scope in the corresponding `if-true-expression`— but it is
*not* in scope or available in the `if-false-expression`.

Tip:
To choose among multiple conditions, the switch-expression can be an alternative to coding
an `if` statement that specifies multiple `elsif` clauses.
