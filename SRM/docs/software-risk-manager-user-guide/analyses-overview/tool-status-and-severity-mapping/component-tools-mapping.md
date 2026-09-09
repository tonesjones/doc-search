---
title: "Component Tools Mapping"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/component-tools-mapping.html"
content_id: "2eBjLiY7w2P_hp5DZc7Kbw"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:50.724271+00:00"
content_hash: "9d85da088fea148efef74bdd3bf06a7d5b051e84f04fc530a38e63ab42446d3e"
---

# Component Tools Mapping

The tables below show the severity and triage status mappings for all of the Component
tools that are supported by Software Risk Manager.

Tools are listed alphabetically. Tool results are mapped to the Software Risk Manager
status shown at the top of each column. (A blank cell indicates that an equivalent status
value is unavailable or undefined.)

## Severity Mapping

Table 1.

| Component Tool | Critical | High | Medium | Low | Info | Unspecified | None |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Black Duck Binary Analysis**1 **CVSSv3 mapping*  ***CVSSv2 mapping* | >=9* | >=7* , >=7** | <=4* , <=4** | >0* , <=0** | =0* | <0* , <0** |  |
| **Black Duck Hub** | CRITICAL, BLOCKER | HIGH, MAJOR | MEDIUM, MINOR | LOW, TRIVIAL |  | UNKNOWN, UNSPECIFIED |  |
| **CAST Highlight** | critical | high | medium | low | advisory |  |  |
| **Checkmarx One (SCA)** | CRITICAL | HIGH | MEDIUM | LOW | INFO |  |  |
| **Continuous Dynamic (formerly WhiteHat) - (Legacy Rating System)** | urgent, critical | high | medium | low | informational, note |  |  |
| **Continuous Dynamic (formerly WhiteHat) - (Advanced Rating System)** | Critical | High | Medium | Low | Note |  |  |
| **Dependency-check** | critical | high | medium or moderate | low | informational | unknown | none |
| **Dependency-Track** | critical | high / fail | warn / medium | low |  |  | none |
| **Dynatrace**2 | CRITICAL | HIGH | MEDIUM | LOW |  |  | NONE |
| **GitHub Security** | CRITICAL | HIGH | MODERATE / medium |  |  |  |  |
| **GitLab Security** | critical | high | medium | low | informational |  |  |
| **JFrog Xray** | critical | high | medium | low |  |  |  |
| **NeuVector** | critical | high / error | medium / warn | low / note |  |  |  |
| **Orca Security (Vulnerabilities Scan)** | CRITICAL | HIGH | MEDIUM | LOW | INFO |  |  |
| **Polaris** | critical | high | medium | low | informational |  |  |
| **Retire.js** |  | high | medium | low |  |  |  |
| **Snyk Open Source** | critical | high | medium | low |  |  |  |
| **Snyk License Compliance Management** | critical | high | medium | low | informational |  |  |
| **Sonatype Nexus** | critical | severe | moderate | low | no threat, none |  |  |
| **Veracode** |  | 4 | 3 | 2 | 1 |  |  |
| **WhiteSource** |  | high, Rejected by policy | medium | low, Multiple licenses, Multiple library versions, New library version | License results |  |  |

1. To use CVSS version 3 mapping for CVSS version 2 scores, set
`cvss.use-cvss3-buckets = true` in the SRM props file.

2. Dynatrace only produces severities for Vulnerability results and not for Attack results.
Dynatrace Attack findings will have no severity in SRM.

## Triage Status Mapping

Table 2.

| Component Tool | Ignored | False Positive | To Be Fixed | Mitigated | Fixed | Reopened |
| --- | --- | --- | --- | --- | --- | --- |
| **Black Duck Binary Analysis** |  |  |  | FD (feature disabled) | VP (vendor patched) |  |
| **Black Duck Hub** | Duplicate, Ignored | Not Affected | Affected | Mitigated | Remediation Complete |  |
| **CAST Highlight** |  |  |  |  |  |  |
| **Checkmarx One (SCA)** | NOT_EXPLOITABLE; PROPOSED_NOT_EXPLOITABLE |  | URGENT; CONFIRMED |  |  |  |
| **Continuous Dynamic (formerly WhiteHat)** | accepted, out of scope | Invalid, false |  | open, mitigated |  |  |
| **Dependency-check** |  |  |  |  |  |  |
| **Dependency-Track** | not affected, suppressed | false positive |  |  |  |  |
| **Dynatrace** |  |  |  |  | RESOLVED |  |
| **GitHub Security** |  |  |  |  | CLOSED |  |
| **GitLab Security** |  |  |  |  |  |  |
| **JFrog Xray** |  |  |  |  |  |  |
| **NeuVector** |  |  |  |  |  |  |
| **Orca Security (Vulnerabilities Scan)** |  |  |  |  |  |  |
| **Polaris** | dismissed (any other reason) | dismissed (false positive) | to-be-fixed |  |  |  |
| **Retire.js** |  |  |  |  |  |  |
| **Snyk Open Source** | Ignored |  |  |  | Patched |  |
| **Snyk License Compliance Management** | Ignored |  |  |  |  |  |
| **Sonatype Nexus** | Not Applicable |  | Confirmed |  |  |  |
| **Vericode** | Accept the Risk | Potential False Positive | Reported to Library Maintainer | Mitigate by Design, Mitigate by Network Environment, Mitigate by OS Environment |  |  |
| **WhiteSource** |  |  |  |  |  |  |

For SRM Triage Status definitions, click here.
