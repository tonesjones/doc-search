---
title: "C/C++ '#pragma' directives and '_Pragma()'operators"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/c/c-pragma-directives-and-_pragma-operators.html"
content_id: "6TCVIEmGhdH26tfKOU4gGg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:21.974986+00:00"
---

# C/C++ '#pragma' directives and '_Pragma()'operators

For C and C++ source code, *pragmas* are in-line annotations to note deviations
from a compliance standard.

Users might not want to or be able to support all the rules of a given standard. A
*compliance deviation* is the suppression of defects associated with a rule
that is enforced by a particular checker.

With pragmas, you can generate a deviation report (CSV file) when analysis has completed,
to record all the deviations in the current version of your project. Having a record of
the deviations might allow you to claim compliance and gain approval despite partial
adherence to the standard.

In this section:

- Annotating compliance deviations
- The '#pragma coverity compliance' directive
- The '_Pragma()_' compliance operator
