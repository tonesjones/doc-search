---
title: "CWE Support"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/cwe-support.html"
content_id: "k4qujX61s7EfG8CnEYs8lg"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:05.271260+00:00"
content_hash: "00ed87538cd2e0ef9b5c1f636061521ecc8f9989567a6fe3e215b8cf2f3cd935"
---

# CWE Support

The [Common Weakness
Enumeration (CWE)](https://cwe.mitre.org/) is a community effort lead by MITRE to provide a common
language to express software weaknesses.

Software Risk Manager leverages the CWE to provide correlation across the diverse set of
testing tools it supports. Software Risk Manager also allows you to define your own
correlation logic via the Rule Set page.
This allows you to correlate based on a group of CWEs or tool specific rule codes.

Software Risk Manager uses the CWE identifier specified by the tool. In cases where the
tool does not provide a CWE, that mapping is done automatically.

CWE information is readily available in Software Risk Manager. On the Findings page, you
can search by CWE or filter by CWE. This includes grouping CWEs by various standards
such as OWASP Top 10 or CWE/SANS Top 25. The CWE identifier is also shown in the Findings Table, and you can hover on
that identifier to get the full CWE name.

CWE information is also provided on the Finding Details page. There you can see the
full CWE name for the aggregated finding. For each individual tool result, the CWE used
for each tool is also provided. In both cases, a link to [MITRE's CWE
website](https://cwe.mitre.org/) is provided.

Finally, all reports (CSV, XML, PDF, Nessus, and AlienVault/NBE) contain CWE
information.

Note: Software Risk Manager currently supports CWE Version
4.19.1.
