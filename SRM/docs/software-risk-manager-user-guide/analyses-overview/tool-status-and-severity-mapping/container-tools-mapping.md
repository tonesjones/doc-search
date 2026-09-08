---
title: "Container Tools Mapping"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/container-tools-mapping.html"
content_id: "gBwGxIet6xQEwzziE_NbwA"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:51.425644+00:00"
content_hash: "fe64b624aaa462e1287f0e02fbfa04dfc1250d4ba6606df2477945a60a77b14c"
---

# Container Tools Mapping

The tables below show the severity and triage status mappings for all of the Container
tools that are supported by Software Risk Manager.

Tools are listed alphabetically. Tool results are mapped to the Software Risk Manager
status shown at the top of each column. (A blank cell indicates that an equivalent
status value is unavailable or undefined.)

## Severity Mapping

Table 1.

| Container Tool | Critical | High | Medium | Low | Info | Unspecified |
| --- | --- | --- | --- | --- | --- | --- |
| **Anchore** | critical | high | medium | low | negligible |  |
| **Aqua CSP** | critical | malware, high | sensitive data, medium | low | negligible | unknown |
| **Check Point CloudGuard** | Critical | High | Medium | Low | Informational |  |
| **Dynatrace*** | CRITICAL | HIGH | MEDIUM | LOW |  |  |
| **Grype Reader** | Critical | High | Medium | Low |  | Unknown |
| **GitLab Security** | critical | high | medium | low | informational |  |
| **Harbor** | Critical | High | Medium | Low | Negligible | Unknown |
| **Google SCC** | critical | high | medium | low |  |  |
| **Microsoft Defender for Cloud** | Critical | High | Medium | Low |  |  |
| **NeuVector** | critical | high / error | medium / warn | low / note |  |  |
| **Orca Security** | CRITICAL | HIGH | MEDIUM | LOW | INFO |  |
| **Prisma Cloud Compute (Twistlock)** | critical / important | high | medium / moderate | low |  |  |
| **Snyk Container** | critical | high | medium | low |  |  |
| **Trivy** | CRITICAL | HIGH | MEDIUM | LOW |  | UNKNOWN |

*Dynatrace only produces severities for Vulnerability results and not for Attack results.
Dynatrace Attack findings will have no severity in SRM.

## Triage Status Mapping

Table 2.

| Container Tool | Gone | New | Ignored | False Positive | To Be Fixed | Mitigated | Fixed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Anchore** |  |  |  |  |  |  |  |
| **Aqua CSP** |  |  |  |  |  |  |  |
| **Check Point CloudGuard** |  |  |  |  |  |  |  |
| **Dynatrace*** |  |  |  |  |  |  | RESOLVED |
| **Grype Reader** | Fixed | not-fixed, unknown | wont-fix |  |  |  |  |
| **GitLab Security** |  |  |  |  |  |  |
| **Harbor** |  |  |  |  |  |  |  |
| **Google SCC** |  |  | MUTED |  |  |  |  |
| **Microsoft Defender for Cloud** |  |  |  |  |  |  |  |
| **NeuVector** |  |  |  |  |  |  |  |
| **Orca Security** |  |  |  |  |  |  |  |
| **Prisma Cloud Compute (Twistlock)** |  |  |  |  |  |  |  |
| **Snyk Container** |  |  | ignored |  |  |  | patched |
| **Trivy** |  |  |  |  |  |  |  |

For SRM Triage Status definitions, click here.
