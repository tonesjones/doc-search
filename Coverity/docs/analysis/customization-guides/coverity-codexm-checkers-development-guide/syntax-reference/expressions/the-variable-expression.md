---
title: "The variable-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-variable-expression.html"
content_id: "VJuuyEBLUiIhcPO0s185ig"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:57.410072+00:00"
---

# The variable-expression

In CodeXM, a *variable* is an entity that has been given an identifier to name it.

Examples include a global constant defined by const-definition,
a local constants defined by a parent let-binding-expression,
and a named value defined by a matches-expression that uses the keyword `as`.

**Remember:**
The CodeXM documentation often uses the term "variable" by analogy with other languages,
but because CodeXM is a functional language, even named values are constant.
They are available, with the same value, a long as they remain in scope.

(You can, on the other hand, create a record that is based on an existing record but with some of the property values changed:
See record-update-expression.)

## Syntax

Once it has been created, you simply refer to a variable by its identifier.

  
 [image: Syntax diagram, variable-expression]   

```
variable-expression ::=
    identifier
```
