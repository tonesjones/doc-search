---
title: "Understanding scorecards"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/understanding-scorecards.html"
content_id: "hBlKrM7k79USRKxqBCIIzQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:17.504892+00:00"
---

# Understanding scorecards

The report opens with an Executive Summary that features a Scorecard showing the target
for each policy category, the actual result, and whether the codebase has passed for
that category. Policy categories are described next; for detailed information on how
each value is calculated, see the Methodology section of a generated report.

**Security Score**
:   This is a numerical value (0 to 100) calculated from the severity mapping
    specified when the report is configured. The score is compared to the
    configured Assurance Level to determine pass or fail.

    Severity levels are used to determine the security score: possible severity
    levels are `Very High`, `High`,
    `Medium`, `Low`, and `Very
    Low`. The highest severity level that has at least one issue
    associated with it will greatly influence the security score. Additional
    issues with a relatively higher severity level will have a greater impact on
    reducing the security score than will additional issues with a relatively
    lower severity level. As such, it's important to address issues with the
    highest severity level.

    While the full range of a possible security score is from 0 to 100, a project
    would need to contain more than 30 000 `Very High` severity
    level issues to receive a score lower than 30. Meanwhile, a project with a
    highest severity level of `Very Low` would need to contain
    more than 30 000 `Very Low` severity level issues to receive
    a score lower than 70.

    To give some further context, consider the standard Target Assurance Levels
    plus their corresponding Target Security Score values of AL1 (90), AL2 (80),
    AL3 (70), and AL4 (60) relative to the highest severity level that has at
    least one issue associated with it.

    - If `Very High` severity level issues exist, it will be
      nearly impossible to achieve AL3 (70), and it will be quite a
      challenge to achieve AL4 (60).
    - If all of the `Very High` severity level issues have
      been addressed, but at least one `High` severity
      level issue exists, it will be nearly impossible to achieve AL2
      (80), and it will be a reasonable challenge to achieve AL3 (70),
      with AL4 (60) being within easier reach.

      If all of the `Very High` and `High`
      severity level issues have been addressed, but at least one
      `Medium` severity level issue exists, it will be
      nearly impossible to achieve AL1 (90) and quite challenging to
      achieve AL2 (80), while AL3 (70) is more likely to be within reach,
      and AL4 (60) should be a relatively easy target to reach.

**OWASP Top 10**
:   This is a list of prioritized security weaknesses relating to web application
    security. If the policy prohibits these weaknesses, the target would be
    zero.

**CWE/SANS Top 25**
:   This is a list of software weaknesses that are thought to be widespread and
    critical. If the policy prohibits these weaknesses, the target would be
    zero.

**Analysis Date**
:   The codebase must have been analyzed within the last 30 days for this item to
    pass.
