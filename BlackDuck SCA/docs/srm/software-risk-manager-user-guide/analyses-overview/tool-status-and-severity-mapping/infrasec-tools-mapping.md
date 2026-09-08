---
title: "InfraSec Tools Mapping"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/infrasec-tools-mapping.html"
content_id: "o0L8VwjM8Cz~jaMDJT~TEA"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:49.336029+00:00"
content_hash: "aefd1634c4bb200989d25ce79b48178b54bdb673173b7b3d0a01ed4bec110ee6"
---

# InfraSec Tools Mapping

The tables below show the severity and triage status mappings for all of the InfraSec
tools that are supported by Software Risk Manager.

Tools are listed alphabetically. Tool results are mapped to the Software Risk Manager
status shown at the top of each column. (A blank cell indicates that an equivalent
status value is unavailable or undefined.)

## Severity Mapping

Table 1.

| InfraSec Tool | Critical | High | Medium | Low | Info | Unspecified |
| --- | --- | --- | --- | --- | --- | --- |
| **AppDetective Pro** |  | high | medium | low | informational |  |
| **Tenable Nessus**1 | 4 | 3 or Cat I | 2 or Cat II | 1 | 0 or Cat III |  |
| **Rapid7 Nexpose** |  |  |  |  |  |  |
| **NMap**2 | 9+ | 7-...< 9 | 4-...< 7 | < 4 |  |  |
| **Qualys VM** | 5 | 4 | 3 | 2 | 1 |  |
| **Qualys CS** | 5 | 4 | 3 | 2 | 1 |  |
| **SCAP** |  | High | Medium | Low | Info |  |
| **Qualys VMDR** | 5 | 4 | 3 | 2 | 1 |  |

1. Tenable Nessus reports risk through
a "category" ranking (1-3) and a severity level (0-4).

2. NMap reports risk using a CVSS score.

## Triage Status Mapping

Table 2.

| InfraSec Tool | Ignored | False Positive | Fixed | Mitigated | Fixed | Reopened |
| --- | --- | --- | --- | --- | --- | --- |
| **AppDetective Pro** |  |  |  |  |  |  |
| **Tenable Nessus** |  |  |  |  |  |  |
| **Rapid7 Nexpose** |  |  |  |  |  |  |
| **NMap** |  |  |  |  |  |  |
| **Qualys VM** |  |  |  |  |  |  |
| **Qualys CS** |  |  |  |  |  |  |
| **SCAP** |  |  |  |  |  |  |
| **Qualys VMDR** |  |  |  |  |  |  |

For SRM Triage Status definitions, click here.
