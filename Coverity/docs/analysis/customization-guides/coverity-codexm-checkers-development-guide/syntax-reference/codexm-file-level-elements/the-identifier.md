---
title: "The identifier"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-identifier.html"
content_id: "4dln1lPVYCIljMVlyjIxxw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:10.790583+00:00"
---

# The identifier

Identifiers name elements of CodeXM syntax: variables, record properties, and so on. All identifiers use the same syntax.

## Syntax

An `identifier` begins with either an underscore ( `_` ) or a letter.
This first character can then be followed by zero or more letters, underscores, or digits.
Letters can be either upper case or lower case, but the two are not interchangeable.
CodeXM is case sensitive, so the identifier `variable` is a different
entity than `Variable`,
and both are different from `VARIABLE`.

The characters in an identifier must be in the set of allowable CodeXM characters.

```
identifier ::=
    [_a-zA-Z][0-9_a-zA-Z]*		// White space is not allowed.
```
