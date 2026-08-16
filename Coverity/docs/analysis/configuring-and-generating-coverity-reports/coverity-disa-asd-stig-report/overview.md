---
title: "Overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/overview.html"
content_id: "1rrY_5kivKQoqXy78FN8og"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:22.619892+00:00"
---

# Overview

The DISA ASD STIG report generator uses analysis results for a Coverity Connect project to
evaluate the target codebase. Based on this evaluation, it creates a DISA ASD STIG report,
which details the assessments that were done and lists the location of the findings.
Information from this report is of special interest to application security assurance
teams that need to document their compliance with the DISA ASD STIGs that are relevant to
their code.

DISA (Defense Information Systems Agency) is a part of the Department of Defense; it oversees
the organization and communication of defense-related IT information, including STIG
(Security Technical Information Guides) guidelines, which provide guidance for hardening
information systems and software that might be vulnerable to attack. Coverity supports a
number of rules from the Application Security and Development (ASD) STIG by mapping
existing Coverity checkers to specific STIGs.

DISA ASD STIG violations are grouped in three categories and reported as such in the DISA
STIG report:

- **Category I** refers to any vulnerability that can
  directly and immediately result in loss of confidentiality, availability, or
  integrity. These vulnerabilities might allow unauthorized access to classified
  data or facilities, and can lead to a denial of service or access.

  Such risks might result in loss of life, damage to facilities, or mission
  failure. If an organization doesn't address them, it will not be granted an
  Authorization to Operate.
- **Category II** refers to any vulnerability that might
  result in loss of confidentiality, availability, or integrity. These
  vulnerabilities can lead to a Category I vulnerability, result in personal
  injury, damage to equipment or facilities, and degrade a mission.
- **Category III**  refers to any vulnerability that degrades
  measures to protect against loss of confidentiality, availability, or integrity.
  These vulnerabilities can lead to a Category II vulnerability, delay in
  recovering from an outage, or affect the accuracy of data and
  information.

You cannot localize DISA ASD STIG reports currently.

This chapter describes the workflow needed for generating a DISA ASD STIG report and explains
how you interpret report findings.

Note: The total number of issues in the report should be equal to the number of matching issues shown in
Connect.
