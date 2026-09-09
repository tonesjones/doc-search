---
title: "Rule Sets"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/rule-sets.html"
content_id: "O1zOeYJTq4nFgglG_7EX2g"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:37.082467+00:00"
content_hash: "3ee773da29e647014eb8e8b0ecbf50398f3514af7c8e3f84c0c2541289d4fd9f"
---

# Rule Sets

The Rule Set Page is accessed via the *Rule Set Associations* section of a
project's *Analysis Configuration* dialog. When you
access the Rule Set page, you will be able to view and sometimes edit a set of rules
that can be used to determine how different types of findings will correlate with each
other.

Each Rule Set has Rules, and each Rule has Criteria and identifying information.

Rule Sets are, as the name implies, a set of rules. Each rule acts as a strategy for
combining results from different tools and providing standard information for the
finding. Within a rule, a set of criteria can be defined, forming the underlying logic
for the rule. The identifying information for a rule can optionally include a Severity,
CWE, and Description, which will be shared by Findings created from that rule. For
example, a general "SQL Injection" rule may be created to capture specific results from
multiple tools and provide a shared description, making it easier to locate and
recognize standard vulnerabilities.

When result data is uploaded to a Software Risk Manager project, as long as that
project's *Prevent Correlation* setting is not
enabled, its associated rule set will be responsible for determining which types of
results represent the same types of problems. In this case, rules will be applied during
ingestion, when findings are created from tool results. If there are multiple tool
results belonging to the same rule and they occur at the same location, they will all be
associated with the same finding. Whether a tool result "belongs" to a rule is
determined by that rule's criteria.

## After Changing Rule Sets

Since a project's configured rule set determines the manner in which results are
correlated, changing that configuration necessitates an update of the correlation.
This happens when the configured rule set for a project is modified in any way, or
the *Analysis Configuration* is changed to use a different rule set. When this
happens, the Findings page will display a notification prompting users to do so.

## Additional Information

For more information on identifying information and rule criteria, see the following
topics:

- Rule Identifying
  Information.
- Rule Criteria.
