---
title: "Infrastructure as Code (IaC) Tool Mapping"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/infrastructure-as-code-iac-tool-mapping.html"
content_id: "Kz_mSK_F5O_y3fCPPuDGTg"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:52.708909+00:00"
content_hash: "860ca7e1891a759a3cc1ea2b625a3084fc76f96aa210cb7e6dfc13ae8a616b56"
---

# Infrastructure as Code (IaC) Tool Mapping

The tables below show the severity and triage status mappings for all of the IaC tools
that are supported by Software Risk Manager.

Tools are listed alphabetically. Tool results are mapped to the Software Risk Manager
status shown at the top of each column. (A blank cell indicates that an equivalent
status value is unavailable or undefined.)

## Severity Mapping

Table 1.

| IaC Tool | Critical | High | Medium | Low | Info | Unspecified |
| --- | --- | --- | --- | --- | --- | --- |
| **Checkmarx One (IaC)** | CRITICAL | HIGH | MEDIUM | LOW | INFO |  |
| **Checkov** | CRITICAL | HIGH | MEDIUM | LOW |  |  |
| **Orca Security** | CRITICAL | HIGH | MEDIUM | LOW | INFO |  |

## Triage Status Mapping

Table 2.

| IaC Tool | Ignored | False Positive | To Be Fixed | Mitigated | Fixed | Reopened |
| --- | --- | --- | --- | --- | --- | --- |
| **Checkmarx One (IaC)** | NOT_EXPLOITABLE; PROPOSED_NOT_EXPLOITABLE |  | URGENT; CONFIRMED |  |  |  |
| **Checkov** |  |  |  |  |  |  |
| **Orca Security** |  |  |  |  |  |  |

For SRM Triage Status definitions, click here.
