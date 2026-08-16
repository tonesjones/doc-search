---
title: "Addressing coding standards violations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/addressing-coding-standards-violations.html"
content_id: "JcRduWDf0eBGM3I_nCT4nA"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:25.148734+00:00"
---

# Addressing coding standards violations

Using Coverity, you can validate for specific standards: AUTOSAR, DISA ASD STIG, PCI DSS, ISO TS 27961, MISRA, SEI CERT, and OWASP Web and Mobile standards.

However, validation against these standards poses its own challenges:

- Validating the coding rules defined by these checkers often generates huge numbers
  of findings.
- Additionally, different components of the product under development, such as system
  libraries, non-critical code, or third-party code might generate issues in numbers
  that dwarf (and hide) issues found in the critical IP sections.

For these reasons, compliance checkers might take a significant amount of time and
generate very large databases on the Coverity Connect server. Coverity offers a number
of strategies to manage these problems:

- You can skip over tangential code by injecting analysis only in the required sections.
- You can further minimize the time and resources required for analysis by running
  compliance analysis separately from quality and security analysis.
- You can post compliance results to different Coverity Connect servers than those
  used for quality and security issues.
- You can adjust the cadence, and thus the expense, of analysis to match the rate at
  which issues are required to be addressed. While you might want to check quality or
  security results daily, you might only need to check compliance results once a week
  or once a sprint.
