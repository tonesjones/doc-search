---
title: "Expressions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/expressions.html"
content_id: "JrD~Fx7cdb_ZLPjLBtXkrw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:20.031622+00:00"
---

# Expressions

One of the implications of CodeXM being a functional programming language is that, loosely speaking,
"everything is an expression".

More precisely, CodeXM has no statements that are executed sequentially, one after another;
rather, the logic in CodeXM takes the form of expressions that are evaluated.
Each expression produces a result that might in turn be used to further evaluate some other expression.
