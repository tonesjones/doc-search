---
title: "Coverity Compliance Filtering Overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-compliance-filtering-overview.html"
content_id: "cd6NSAwuo8GR2RUkOWHGQQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:37.936352+00:00"
---

# Coverity Compliance Filtering Overview

Developing software using a code compliance standard (such as MISRA, AUTOSAR, or CERT)
can be a struggle. These types of software projects can produce very large quantities of
code compliance issues⁠. Developers need easy ways to know which issues to work on.
Architects and quality managers need easy ways to send only the most relevant issues to
developers. Coverity Compliance Filtering is specifically designed to help
architects/quality managers manage such projects by letting them place the developmental
focus on the issues of most importance. Specifically, Coverity Compliance Filtering
enables you to do the following:

- Regulate the quantity of issues sent to developers by blocking the creation of low-importance issues.
- Prioritize issues that are created.
- Centrally store and administer your issue blocking and prioritization policies.

In addition, Coverity Compliance Filtering provides developers with new abilities to
prioritize their development work without altering their workflow.

Attention:
Black Duck Software, Inc. recommends that you use standard Coverity Analysis checkers for CWE coverage when
CERT, MISRA, and AUTOSAR are not part of your compliance requirements. Coverity checkers are optimized to produce meaningful
security results with a minimum of false positives. Adding the compliance checkers can result in a greater number of false positives,
leading to redundant results and a negative impact on performance.
