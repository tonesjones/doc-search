---
title: "Scorecard elements"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scorecard-elements.html"
content_id: "SXTjkGn61ooHe7nMZm5WBQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:14.337559+00:00"
---

# Scorecard elements

The scorecard shows the Target for each category and the actual
result, and indicates if the element passes or fails. For detailed information on how
each scorecard element is calculated, see the Methodology section
of a generated report.

CVSS Critical Count
:   This is a list of security vulnerabilities that have scored as
    Critical (between 9.0-10.0 on the CVSS score
    calculator). The policy prohibits these weaknesses, so the target is
    zero.

CVSS High Count
:   This is a list of security vulnerabilities that have scored as
    High (between 7.0-8.9 on the CVSS score
    calculator). The policy prohibits these weaknesses, so the target is
    zero.

CWE/SANS Top 25
:   This is a list of software weaknesses that are thought to be widespread and critical. The
    policy prohibits these weaknesses, so the target is zero.

    The Top 25 from
    the year 2019 will be used. You can configure Coverity Analysis to use the Top 25 of 2021, 2022, or 2023
    instead. See CVSS report configuration file.

OWASP Web Top 10
:   This is a list of prioritized security weaknesses relating to web application
    security. The policy prohibits
    these weaknesses, so the target is zero.

    The Top 10 from the year 2017 will be used.
    You can configure Coverity Analysis to use the Top 10 of 2021, instead.
    See OWASP Web Top 10 report configuration file.
