---
title: "Overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/overview.html"
content_id: "b1IeC_U8q1R~038B_qZCww"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:00.164467+00:00"
---

# Overview

The Mobile OWASP Top 10 report generator uses analysis results for a Coverity Connect project
to evaluate the analyzed codebase. Based on this evaluation, it creates a Mobile OWASP
Top Ten report, which details the assessments that were done, provides a summary of
findings, and specifies the remediations needed. Information from this report is of
special interest to application security assurance teams and their clients.

The Mobile OWASP Security Project provides developers and security teams the resources they
need to build and maintain secure mobile applications. The project's goal is to classify
mobile security risks and provide developmental controls to reduce their impact or
likelihood of exploitation. The Mobile OWASP Top 10 lists the ten top security risks to
mobile applications.

You can localize reports by setting the `locale` field of your report generation
configuration file.

This chapter describes the workflow needed for generating a Mobile OWASP Top 10 report and
explains how you interpret report findings.
