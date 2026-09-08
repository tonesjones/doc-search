---
title: "DAST Tools Mapping"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/dast-tools-mapping.html"
content_id: "uMyE5qX528sF0A2s~HPjGg"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:47.251635+00:00"
content_hash: "051f1cb66db865f735c59ae11d1737ee79106ab7d25d6cb7d5c22cd5e50cfdd4"
---

# DAST Tools Mapping

The tables below show the severity and triage status mappings for all of the DAST tools that
are supported by Software Risk Manager.

Tools are listed alphabetically. Tool results are mapped to the Software Risk Manager status
shown at the top of each column. (A blank cell indicates that an equivalent status value is
unavailable or undefined.)

## Severity Mapping

Table 1.

| **DAST Tool** | Critical | High | Medium | Low | Info | Unspecified |
| --- | --- | --- | --- | --- | --- | --- |
| **Acunetix Desktop** |  | high | medium | low | info |  |
| **Acunetix 360** | CRITICAL | IMPORTANT, HIGH | MEDUIM | LOW | INFORMATION (BEST PRACTICE) |  |
| **AppSpider Vulnerability Summary** |  | 4 | 5 | 6 | 1, 0 |  |
| **APIsec** | Blocker, Critical | Major, High | Medium | Minor, Low | Info |  |
| **API Security Platform(ApiSec)** | Critical | High | Medium | Low | Info |  |
| **Arachni** |  | high | medium | low | informational |  |
| **Burp Suite** |  | high | medium | low | informational |  |
| **Continuous Dynamic (formerly WhiteHat)** | urgent (critical) | high |  | low | note (informational) | unspecified |
| **Defensics** |  | fail | warning |  |  |  |
| **Dynatrace** |  |  |  |  |  |  |
| **HP WebInspect** | 4 | 3 | 2 | 1 | 0 |  |
| **HCL AppScan Standard (enterprise)** | Critical | High | Medium | Low | Information |  |
| **HCL AppScan on Cloud (ASoC)** | Critical | High | Medium | Low | Information |  |
| **Imperva*** | CRITICAL | MAJOR | MINOR |  |  |  |
| **Invicti Standard** (formerly Netsparker) |  | Critical, Important, High | Medium | Low | Information (Best Practice) |  |
| **Invicti Enterprise** (formerly Netsparker Enterprise) | Critical | Important, High | Medium | Low | Information (Best Practice) |  |
| **Invicti Application Security Platform** | critical | high | medium | low | info |  |
| **OWASP ZAP** |  | 3 | 2 | 1 | 0 |  |
| **Polaris** | critical | high | medium | low | informational |  |
| **Qualys WAS** | 5 | 4 | 3 | 2 | 1 |  |
| **Rapid7 InsightAppSec** |  |  |  |  |  |  |
| **Rapid7 InsightVM** | Critical | Severe | Moderate |  |  |  |
| **Rapid7 Nexpose** | 8-...-10 | 4-...-7 | 0-...-3 |  |  |  |
| **Black Duck Managed Services Platform** | Critical | High | Medium | Low | Minimal |  |
| **Tenable WAS** | blocker / critical | major / high | medium | minor / low | info |  |
| **Tinfoil Web** | critical | high | medium | low | informational | unknown |
| **Trustwave App Scanner** |  | High | Medium | Low | all other values |  |
| **Veracode** |  | 4 | 3 | 2 | 1 |  |
| **WPScan** |  | all |  |  |  |  |
| **Sqlmap output** |  | all |  |  |  |  |

## Triage Status Mapping

Table 2.

| DAST Tool | Ignored | False Positive | To Be Fixed | Mitigated | Fixed | Reopened | None |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Acunetix Desktop** |  |  |  |  |  |  |  |
| **Acunetix 360** | Accepted Risk | False Positive |  |  | Fixed |  |  |
| **AppSpider Vulnerability Summary** |  |  |  |  |  |  |  |
| **APIsec** |  |  |  |  |  |  |  |
| **Arachni** |  |  |  |  |  |  |  |
| **Burp Suite** |  |  |  |  |  |  |  |
| **Continuous Dynamic (formerly WhiteHat)** | accepted, out of scope | Invalid, false |  | open, mitigated |  |  |  |
| **Defensics** |  |  |  |  |  |  |  |
| **Dynatrace** |  |  |  |  |  |  |  |
| **HP WebInspect** |  |  |  |  |  |  |  |
| **HCL AppScan Standard (enterprise)** |  | noise |  | passed | fixed | reopened |  |
| **HCL AppScan on Cloud (ASoC)** |  | noise |  | passed | fixed | reopened |  |
| **Imperva*** |  |  |  |  |  |  |  |
| **Invicti Enterprise** (formerly Netsparker Enterprise) | Accepted Risk | False Positive |  |  | Fixed |  |  |
| **OWASP ZAP** |  |  |  |  |  |  |  |
| **Polaris** | dismissed (any other reason) | dismissed (false positive) | to-be-fixed |  |  |  |  |
| **Qualys WAS** |  |  |  |  |  |  |  |
| **Rapid7 InsightAppSec** | ignored | false positive | verified |  | remediated |  | unreviewed, duplicate |
| **Rapid7 InsightVM** |  |  |  |  |  |  |  |
| **Rapid7 Nexpose** |  |  |  |  |  |  |  |
| **Black Duck Managed Services Platform** |  | False Positive |  |  |  |  |  |
| **Tenable WAS** |  |  |  |  |  |  |  |
| **Tinfoil Web** |  |  |  |  |  |  |  |
| **Trustwave App Scanner** |  |  |  |  |  |  |  |
| **Veracode** | Accept the Risk | Potential False Positive | Reported to Library Maintainer | Mitigate by Design, Mitigate by Network Environment, Mitigate by OS Environment |  |  |  |
| **WPScan** |  |  |  |  |  |  |  |
| **Sqlmap output** |  |  |  |  |  |  |  |

For SRM Triage Status definitions, click here.

*Imperva only produces severities for API Attack Analytics results and not for API Risks or
WAF Security Events. API Risk and WAF Security Event findings will only have Unspecified
severity in SRM.
