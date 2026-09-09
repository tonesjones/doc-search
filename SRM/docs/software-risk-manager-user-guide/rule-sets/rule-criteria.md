---
title: "Rule Criteria"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/rule-criteria.html"
content_id: "dFCWRWjJoccln5fIGz9Z4Q"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:38.713082+00:00"
content_hash: "64d0a97d1bb4ddc3e2cb52fc1d97bfb2bc0b39b6342ef276b58cfd1b04909ee4"
---

# Rule Criteria

A rule's criteria control which tool results will be matched with a rule. Note that each
criterion can only appear once in a rule set. If you attempt to add a criterion that
already exists in a different rule, you will be given the option to move the criterion
out of that rule, or cancel. Users with the `admin` role can edit the
criteria for each rule.

Criteria can be created for rules using the add criterion buttons for that rule. These
buttons are located at the bottom of the criteria list.

[image: image]

Criteria can be deleted from rules using the delete button for that criterion. The button
is hidden until you hover over the criterion in a rule's criteria list.

[image: image]

## Tool Criteria

The *Add Tool Criterion* form allows you to create criteria that operate on a tool result's
type. An individual tool criterion specifies a tool, category, and code. It will
match tool results whose raw values match the values specified by the criterion.

[image: image]

The exact values for the tool criterion fields vary depending on what is reported by
the tool. One way to discover these values is to look at the *Finding Details*
page for existing findings in Software Risk Manager. The *Tool*, *Tool
Category*, and *Tool Code* are displayed in the *Tool Details* for
each associated tool result.

[image: image]

The category and code fields are both optional. Omitting both will create a criterion
that matches all results from the specified tool. Omitting just the code will create
a criterion that matches all results from the specified tool marked as part of the
specified category. Some tools do not specify a tool category, in these cases the
tool category field will need to be left blank.

Note: Leaving the tool
category field blank does not act as a wildcard, so if the tool specifies
categories, they must be included in all rule criteria.

## CWE Criteria

The *Add CWE Criterion* form allows you to create criteria that operate on a tool result's
CWE. By specifying a CWE ID value, a CWE criterion will match tool results with that
CWE value.
