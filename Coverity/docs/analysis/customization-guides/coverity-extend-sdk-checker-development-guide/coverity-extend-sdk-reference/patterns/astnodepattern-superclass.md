---
title: "ASTNodePattern Superclass"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/astnodepattern-superclass.html"
content_id: "OHPzwgYN7DwSoRVYGvJcig"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:19.388053+00:00"
---

# ASTNodePattern Superclass

The ASTNodePattern is primarily used as a superclass for
StatementPattern and ExpressionPattern. It is
also used to inspect the tree hierarchy formed by all ASTNodes (for
instance, an expression can be contained within a `for` loop). It also
has a function, recursive_match, that returns a list of all the
ASTNodes underneath (and including) the given one that matched
the pattern.
