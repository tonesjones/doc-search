---
title: "Understanding deviations"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/understanding-deviations.html"
content_id: "aMcJh7FRJmTcRt4En2Clyw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:39.637997+00:00"
---

# Understanding deviations

Deviations are violations of rules or checkers that for some reason we don’t intend to fix.

Coverity Connect provides three ways to deviate issues:

1. Add a rule or a checker to a coding-standard configuration file that is specified at analysis time.

   This causes analysis to ignore that rule or checker.
2. In Coverity Connect, triage an issue by assigning it a category of "Intentional".
3. If the language you program in is C or C++, you can use a *pragma* to specify a deviation for a particular portion of source code.

   This automatically triages certain issues to give them a category of "Intentional" at build, analysis, or commit time.

   For more information, see
   C/C++ '`#pragma`' directives and '`_Pragma()'`operators.

   Notice:
   You can also auto-triage an issue to be a false positive, but false positives are not deviations.
