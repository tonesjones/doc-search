---
title: "Threat Modeling Tools Mapping"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/threat-modeling-tools-mapping.html"
content_id: "xI8C7pnc26HHXWc3H78S_w"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:49.955396+00:00"
content_hash: "c0e05039af065ca64382b6b2d0644b81c8a82ebcb1bb30f95c7c887c9a40cffe"
---

# Threat Modeling Tools Mapping

The tables below show the severity and triage status mappings for all of the Threat
Modeling tools that are supported by Software Risk Manager.

Tools are listed alphabetically. Tool results are mapped to the Software Risk Manager
status shown at the top of each column. (A blank cell indicates that an equivalent
status value is unavailable or undefined.)

## Severity Mapping

Table 1.

| Threat Modeling Tool | Critical | High | Medium | Low | Info | Unspecified |
| --- | --- | --- | --- | --- | --- | --- |
| **IriusRisk**1 | Critical (76-100) | High (51–75) | Medium (26–50) | Low (1–25) | Very Low (0) |  |
| **Microsoft Threat Modeling Tool 2016** |  | high | medium | low |  |  |
| **SD Elements** | 9+ | 7–8 | 5–6 | 1–4 |  |  |

1. IriusRisk threats are assigned a severity in SRM based on their Current Risk value.
The risk ratings are mapped to SRM severities based on [this mapping](https://support.iriusrisk.com/hc/en-us/articles/360042393071-Mapping-numeric-risk-ratings).

## Triage Status Mapping

Table 2.

| Threat Modeling Tool | Ignored | False Positive | To Be Fixed | Mitigated | Fixed | Reopened |
| --- | --- | --- | --- | --- | --- | --- |
| **IriusRisk** |  |  |  |  |  |  |
| **Microsoft Threat Modeling Tool 2016** | Not Applicable |  |  | Mitigation Implemented |  |  |
| **SD Elements** |  |  |  |  |  |  |

For SRM Triage Status definitions, click here.
