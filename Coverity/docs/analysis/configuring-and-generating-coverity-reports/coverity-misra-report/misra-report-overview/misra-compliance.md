---
title: "MISRA compliance"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/misra-compliance.html"
content_id: "enQ40wfEla1pvzwWwYlF_Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:40.548684+00:00"
---

# MISRA compliance

The MISRA Compliance section of the report states whether the project was found to be
MISRA compliant or not, and shows the number of violations in each of the following
categories. For detailed information on how each scorecard element is calculated, see
the Methodology section of a generated report.

Mandatory violation count
:   This is the number of violations found that fall in the MISRA Mandatory
    category.

Required violation count
:   This is the number of violations found that fall in the MISRA Required category.

Deviations details
:   Lists deviations from the designated MISRA standard.

Document violation count
:   This is the number of violations found that fall in the MISRA Document category.

Advisory violation count
:   This is the number of violations found that fall in the MISRA Advisory category.

Disapplied violation count (MISRA C 2025)
:   This is the number of violations found that fall in the MISRA Disapplied category.

Additional Quality Measures
:   Additional measures are not considered in evaluating MISRA compliance, but are
    provided for informational purposes. They include:

    - Issue Occurrences Marked "False Positive" or "Intentional"
    - Non-MISRA Issues Occurrences
    - Snapshots older than 30 days
    - Deviations count

    Note:
    The number of violations reported is not condensed by rule (as it was in the original implementation).
    In other words, if Coverity Analysis detects 1,000 violations of rule X,
    this is reported as 1,000 violations in order to paint a realistic picture and to comply with
    MISRA standards.
