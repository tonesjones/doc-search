---
title: "Overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/overview.html"
content_id: "doAwojdySrD5VTU0iC9Iug"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:04.859916+00:00"
---

# Overview

The PCI DSS report generator uses analysis results for a Coverity Connect project to
evaluate the analyzed codebase. Based on this evaluation, it creates a report, which
details the assessments that were done, provides a summary of findings, and specifies
the remediations needed. Information from this report is of special interest to
application security assurance teams and their clients.

The PCI Security Standards Council is a global forum for the ongoing development,
enhancement, storage, dissemination and implementation of security standards for account
data protection. The Payment Card Industry Data Security Standard (PCI DSS) was
developed to encourage and enhance cardholder data security and facilitate the broad
adoption of consistent data security measures globally. PCI DSS provides a baseline of
technical and operational requirements designed to protect account data.

Important: You are required to generate a CVSS report before you can use the PCI DSS
report generator because the latter depends upon the vulnerability scoring system
defined by CVSS. For information about generating a CVSS report, see
Generating a CVSS Report
in the Configuring and Generating Coverity Reports.

You can localize reports by setting the `locale` filed of your report
generation configuration file.

This chapter describes the workflow needed for generating a PCI DSS report and explains
how you interpret report findings.
