---
title: "Viewing project version vulnerabilities"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/viewing-project-version-vulnerabilities.html"
content_id: "9S7meWmCTpiWCdeMg6Cnog"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:25:20.506947+00:00"
---

# Viewing project version vulnerabilities

Use the project version page's **Vulnerabilities** tab to view the security vulnerabilities
associated with the components used in a project version.

The information shown uses CVSS v3.x or CVSS v4.x scores, depending on which security risk
calculation you selected; by default CVSS v3.x scores are shown.

  
 [image: Vulnerabilities tab]   

This page has these sections:

- Vulnerabilities graph
- Filters
- Vulnerabilities table

## Vulnerabilities graph

  
 [image: Vulnerability graph]   

The Vulnerabilities graph shows how many vulnerabilities of each severity for each
component version and subproject used in this version of the project.

This graph lists the number of components which have this level of security risk as
their *highest* risk level – it is not the total number of components which
have this risk level. For example, if you select to view components with a medium
risk level, only those components that have medium as the highest risk level appear
in the table; components that have both high *and* medium vulnerabilities are
not shown.

Note: The number of components with vulnerabilities shown here may not be the same value
as shown in your project version BOM (**Components** tab). In the BOM, the
security graph aggregates similar components with different origins. On this page,
the graph displays security risk by unique component origins, as a vulnerability may
be origin-specific.

Select a severity level in the Vulnerabilities graph to view all vulnerabilities that
share the same level of risk.

## Filters

Use the **Filter components** field to view specific components. Click [image: image] to view other available filters.

- Some filter options apply to the values shown in the vulnerabilities table.
  If you select those filter options, components that have at least one
  vulnerability with the specified filter value will appear on the page.

- Filters filter the list of components shown on the left side of the page.
  However, the data shown in the vulnerability table for those components is
  not filtered.

  For example, if you select to view those components that have vulnerabilities
  with an overall score greater than 9.0, the page displays the list of
  components that have at least one vulnerability with an overall score
  greater than 9.0. The information shown in the vulnerability table for those
  components is not filtered: it still shows all vulnerabilities for the
  filtered components, including those vulnerabilities with an overall score
  less than 9.0.

## Vulnerabilities table

This section displays all vulnerabilities identified in the selected project version.
For each entry, you'll see the vulnerability ID, the number of affected components,
the overall risk score, current status, and indicators for exploitability, available
workarounds, and available solutions.

Click [image: image] next to a vulnerability to reveal additional
details.

The vulnerabilities table lists the following information for each vulnerability:

| Column | Description |
| --- | --- |
| Vulnerability ID | The identifier, value associated with this vulnerability, and any vulnerability tags (if applicable).  Select [image: image] in the table next to the vulnerability to view a brief description. Depending on the identifier, select to view the BDSA record and/or the CVE record.  Users with the appropriate role can also use this section to remediate the vulnerability by clicking the [image: image] icon next to the affected component. |
| Affected Components | Displays the number of components in the project version affected by this specific vulnerability. |
| Overall Score | Shows the Temporal score (for BDSA), or Base score (for NVD) and associated risk level. Hover over the Overall Score value to see the individual values.   - For BDSA, the Temporal, Base, Exploitability, and Impact   scores are shown. - For NVD, the Base, Exploitability, and Impact scores are   shown.   The Temporal score represents time-dependent qualities of a vulnerability taking into account the confirmation of the technical details of a vulnerability, the existence of any patches or workarounds, and the availability of exploit code or techniques.  The Base score reflects the overall basic characteristics of a vulnerability that are constant over time and user environments:   - Attack Vector (AV) - Attack Complexity (AC) - Priviledges Required (PR) - User Interaction (UI) - Scope (S) - Confidentiality (C) - Integrity (I) - Availability (A) - Exploit Code Maturity (E) - Remediation Level (RL) - Report Confidence (RC)   For more information, see the CVSS specification document section on [Exploitablility Metrics](https://www.first.org/cvss/v4.0/specification-document#Exploitability-Metrics).  The Exploitability score measures how the vulnerability is accessed and if extra conditions are required to exploit it, taking into account access vector, complexity, and authentication.  The Impact score reflects the possible impact of successfully exploiting the vulnerability, considering the integrity, availability, and confidentiality impacts. |
| Status | Remediation status of this vulnerability. Possible values are: Duplicate, Ignored, Needs Review, New, Mitigated, Patched, Remediation Complete, or Remediation Required. |
| Exploitable | Indicates whether an exploit for this vulnerability is available:   - – No exploit available - [image: image]   Exploit available |
| Workaround Available | Indicates whether a workaround for this vulnerability is available:   - – No workaround available - [image: image]   Workaround available |
| Solution Available | Indicates whether a solution for this vulnerability is available:   - – No solution available - [image: image]   Solution available |
