---
title: "Interpreting the Hyundai report"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/interpreting-the-hyundai-report.html"
content_id: "m1CPEcrAa9Um2adAJZrdcA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:31.955151+00:00"
---

# Interpreting the Hyundai report

The Hyundai Coding Standard is the Coding Guide for Automotive Embedded System which provides
secure coding standards for commonly-used programming languages such as C, C++ and Java.
These coding standards provide a set of rules and recommendations to develop safe,
reliable, and secure systems.

Coverity Static Analysis finds violations based on the Hyundai Coding Standards for C,
C++ and Java.

Hyundai standards, described in Appendix "HYUNDAI rules" of the Coverity 2026.6.0 Checker Reference, divide their
compliance tests into a set of rules. Not all rules can be checked using static
analysis. Those that are checkable with static analysis are further divided into those
that the specific analysis tool actually can check and those that it
cannot.

Each rule has an
assigned severity, which is the product of three risk assessment values. These three
values are severity, likelihood, and remediation cost based on FMECA (IEC 60812, Failure
Mode Effects & Criticality Analysis) in the CERT C standard. Each rule also has
level as High, Middle and Low.

The software team should validate code by proceeding from the highest to the lowest
priority level.

Hyundai Coding Standard compliance includes the development of formal procedures,
processes and documentation, assets that are outside of the scope of static analysis
tools. As such, those tools cannot judge whether software is Hyundai Coding Standard
compliant, however they can judge whether it is not Hyundai Coding Standard
compliant.

Hyundai Coding Standard compliance requires that a software product have no defects or
exploitable vulnerabilities.

Note: The total number of issues in the report should be equal to the sum of
all values in the Count column in Coverity Connect while in
Issues mode. This is not necessarily the same as the number of matching issues shown in
Connect.

Following several summaries, the Hyundai Coding Standard Report provides detailed
information about Hyundai Coding Standard rules and your code's compliance. Each entry
provides information like the following:

- A *rule identifier* (Rule ID) that specifies the rule being validated; for
  example, MC-EXP-011.
- A *description* that explains the rule that is being validated; for example
  "Do not access a variable through a pointer of an incompatible type."
- The *severity* of the rule - either *Low*, *Middle* or
  *High*.
- The *level* of the rule - either *Low*, *Middle* or
  *High*.
- The *likelihood* of the rule - either *Low*, *Middle* or
  *High*.
- The rule's *cost of implementation* - either *Low*, *Middle* or
  *High*.
- Whether the rule has been dismissed or not in the Connect GUI.
- The number of times the rule has been violated. This number is a count of
  individual occurrences of violations. By contrast, the violation (or issue)
  count in Coverity Connect counts "merged," or fully distinct, groups of
  violations.

## Coverity Terminology

The table below compares Hyundai Coding Standard terminology to Coverity to help you
understand more about the Hyundai Coding Standard violations in terms of Coverity
issues.

| Hyundai Coding Standard | Coverity |
| --- | --- |
| Violation | Occurrence |
| False Positive | False Positive |
| Has Deviation | Intentional |
| True Positive | Bug |
| Unclassified | Unclassified or Pending |
