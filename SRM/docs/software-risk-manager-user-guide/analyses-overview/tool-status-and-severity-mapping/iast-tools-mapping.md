---
title: "IAST Tools Mapping"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/iast-tools-mapping.html"
content_id: "gKHJadm_0ERP5ogbaw4V1A"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:47.943791+00:00"
content_hash: "38db961939dce633f73bd1d76c6257662d74d84c14ef002760a5334b92735980"
---

# IAST Tools Mapping

The tables below show the severity and triage status mappings for all of the IAST tools
that are supported by Software Risk Manager.

Tools are listed alphabetically. Tool results are mapped to the Software Risk Manager
status shown at the top of each column. (A blank cell indicates that an equivalent
status value is unavailable or undefined.)

## Severity Mapping

Table 1.

| **IAST Tool** | Critical | High | Medium | Low | Info | Unspecified |
| --- | --- | --- | --- | --- | --- | --- |
| **Checkmarx (IAST)** | Critical / 4 | High / 3 | Medium / 2 | Low / 1 | Informational / 0 | Unspecified, Unknown |
| **Contrast** | Critical | High | Medium | Low | Note |  |
| **HCL AppScan on Cloud** | Critical | High | Medium | Low | Information |  |
| **NowSecure Workstation** |  |  |  |  |  |  |
| **Q-MAST** | CRITICAL | HIGH | MEDIUM | LOW |  |  |
| **Black Duck Seeker** | critical | high | medium | low | informational |  |

## Triage Status Mapping

Table 2.

| IAST Tool | Ignored | False Positive | To Be Fixed | Mitigated | Fixed | Reopened |
| --- | --- | --- | --- | --- | --- | --- |
| **Checkmarx (IAST)** |  | NOT_A_PROBLEM | CONFIRMED | REMEDIATED |  |  |
| **Contrast** | URL access limited or internal security control | False Positive | Confirmed or Suspicious | Remediated |  |  |
| **HCL AppScan on Cloud** |  | noise |  | passed | fixed | reopened |
| **NowSecure Workstation** |  |  |  |  |  |  |
| **Q-MAST** |  |  |  |  |  |  |
| **Black Duck Seeker** | Ignored / Won't Fix / Intentional, Archived | False Positive |  |  | Fixed |  |

For SRM Triage Status definitions, click here.
