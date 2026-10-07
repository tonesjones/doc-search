---
title: "ASTNodePattern Superclass"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/astnodepattern-superclass.html"
content_id: "OHPzwgYN7DwSoRVYGvJcig"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:56.970020+00:00"
---

# ASTNodePattern Superclass

The ASTNodePattern is primarily used as a superclass for
StatementPattern and ExpressionPattern. It is
also used to inspect the tree hierarchy formed by all ASTNodes (for
instance, an expression can be contained within a `for` loop). It also
has a function, recursive_match, that returns a list of all the
ASTNodes underneath (and including) the given one that matched
the pattern.
