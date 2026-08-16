---
title: "Overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/overview.html"
content_id: "DNCgn37WGGRRi6gEQ76jpQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:55.504917+00:00"
---

# Overview

The OWASP Web Top 10 report generator uses analysis results for a Coverity Connect
project to evaluate the analyzed codebase. Based on this evaluation, it creates an OWASP
Top Ten report, which details the assessments that were done, provides a summary of
findings, and specifies the remediations needed. Information from this report is of
special interest to application security assurance teams and their clients.

The OWASP (Open Web Application Security Project) Foundation is an international
organization whose mission is to advance the cause of secure software. As part of its
activities, OWASP publishes a report of the most critical web application security flaws
in rank order based on the input of a worldwide group of security experts.
The OWSAP Top 10 List is referenced by many standards including MITRE, PCI DSS, DISA,
and the FTC. For more information, see <https://owasp.org>.

**OWASP Top 10 2017**

By default, Coverity generates a report based on the 2017 Top 10.

The OWASP Top 10 for 2017 include the following categories:

- Injection (A1:2017)
- Broken Authentication and Session Management (A2:2017)
- Sensitive Data Exposure (A3:2017)
- XML External Entities (A4:2017)
- Broken Access Control (A5:2017)
- Security Misconfiguration (A6:2017)
- Cross-site Scripting (A7:2017)
- Insecure Deserialization (A8:2017)
- Using Components with Known Vulnerabilities (A9:2017)
- Insufficient Logging and Monitoring (A10:2017)

Source: <https://owasp.org/www-project-top-ten/2017/>

**OWASP Top 10 2021**

Coverity can also generate a report based on the 2021 Top 10.

The OWASP Top 10 for 2021 include the following categories:

- Broken Access Control (A01:2021)
- Cryptographic Failures (A02:2021)
- Injection (A03:2021)
- (New) Insecure Design (A04:2021)
- Security Misconfiguration (A05:2021)
- Vulnerable and Outdated Components (A06:2021)
- Identification and Authentication Failures (A07:2021)
- (New) Software and Data Integrity Failures (A08:2021)
- Security Logging and Monitoring Failures (A09:2021)
- (New) Server-Side Request Forgery (A10:2021)

Source: <https://owasp.org/www-project-top-ten/>

**OWASP Top 10 2025**

Coverity can also generate a report based on the 2025 Top 10.

The OWASP Top 10 for 2025 include the following categories:

- Broken Access Control (A01:2025)
- Security Misconfiguration (A02:2025)
- Software Supply Chain Failures (A03:2025)
- Cryptographic Failures (A04:2025)
- Injection (A05:2025)
- Insecure Design (A06:2025)
- Authentication Failures (A07:2025)
- Software or Data Integrity Failures (A08:2025)
- Security Logging and Alerting Failures(A09:2025)
- Mishandling of Exceptional Conditions (A10:2025)

See Configuring an OWASP Web Top 10 Report
for information about choosing between the OWASP Top 10 2017, 2021, or 2025 categories.

The report provides additional information about each of these categories.

You can localize reports by setting the `locale` field of your report
generation configuration file.

This chapter describes the workflow needed for generating an OWASP Web Top 10 report and
explains how you interpret report findings.
