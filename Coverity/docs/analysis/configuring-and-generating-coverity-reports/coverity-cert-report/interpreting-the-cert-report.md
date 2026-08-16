---
title: "Interpreting the CERT report"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/interpreting-the-cert-report.html"
content_id: "GUO0PuQ06yBTUUjb57ol1Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:12.383369+00:00"
---

# Interpreting the CERT report

The CERT division of the SEI (Software Engineering Institute) defines coding standards
for commonly-used programming languages such as C, C++, Java, and Perl, and the Android
platform. These standards provide a set of rules and recommendations to help you develop
safe, reliable, and secure systems. It is important to understand how CERT rules are
evaluated in order to understand reported violations and summaries.

CERT standards, described in Appendix "SEI CERT
rules" of the Coverity 2026.6.0 Checker Reference, divide their compliance
tests into a set of rules. Not all rules can be checked using static analysis. Each rule
has an assigned *priority*, which is the product of three risk assessment values
multiplied together. These values are assigned on a scale of 1 to 3 for likelihood,
severity, and remediation cost. This product is used to prioritize rules.

Priorities, in turn, may have ten possible values: from lowest to highest (1, 2, 3, 4, 6,
8, 9, 12, 18, 27). Each rule also has a *level*, which divides priorities into one
of three buckets:

- L3 for the lowest priorities of 1, 2 ,3 ,4
- L2 for priorities 6, 8, 9
- L1 for the highest priorities of 12, 18, 27

Software can be assessed as L1, L2, or L3 fully conforming, depending on the set of rules
used to validate the software. Compliance is evaluated as follows, from lowest to
highest:

- **Not conformant**: has one or more L1 rule
  violations.
- **L1 conforming**: complies with all L1 rules, but has L2
  violations.
- **L2 conforming**: complies with all L1 and L2 rules, but
  has L3 violations.
- **Fully conformant**: has no violations.

The software team should validate code by proceeding from the highest to the lowest
priority level. CERT compliance requires that a software product have no defects or
exploitable vulnerabilities.

Following several summaries, the CERT Report provides detailed information about CERT
rules and your code's compliance. Each entry provides information like the
following:

- A *rule identifier* that specifies the rule being validated; for example,
  PRE30-C.
- A *description* that explains the rule that is being validated; for example
  "Do not create a universal character name through concatenation."

  A reason might be provided if the rule is currently disabled in the analysis
  configuration.
- The *priority* of the rule.
- The *level* of the rule.
- Whether the rule is *supported* by the analysis.
- Whether the rule is *enabled* in the analysis configuration.
- The number of times the rule has been violated. This number is a count of
  individual occurrences of violations. By contrast, the violation (or issue)
  count in Coverity Connect counts "merged," or fully distinct, groups of
  violations.

Note: The total number of issues in the report should be equal to the sum of
all values in the Count column in Coverity Connect while in
Issues mode. This is not necessarily the same as the number of matching issues shown in
Connect.
