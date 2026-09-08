---
title: "Cloud Infrastructure Tool Mapping"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/cloud-infrastructure-tool-mapping.html"
content_id: "SOTLrpgcltjE7hrv0s3abg"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:52.092023+00:00"
content_hash: "7661f07b994b1aafa43a2197f23ec3ec60f285e0908f94a086716e8d02fc9920"
---

# Cloud Infrastructure Tool Mapping

The tables below show the severity and triage status mappings for all of the Cloud
Infrastructure tools that are supported by Software Risk Manager.

Tools are listed alphabetically.
Tool results are
mapped to the Software Risk Manager status shown at the top of each column. (A blank
cell indicates that an equivalent status value is unavailable or undefined.)

## Severity Mapping

Table 1.

| Cloud Infrastructure Tool | Critical | High | Medium | Low | Info | Unspecified |
| --- | --- | --- | --- | --- | --- | --- |
| **Prisma Cloud (RedLock)** | critical | high | medium | low | informational |  |
| **AWS Security Hub*** | critical, 80+ | high, 60–...–79 | medium, 40–...–59 | low, 20–...–39 | informational, 0–...–19 |  |
| **Azure Security Center** | critical | high | medium | low | informational |  |
| **Check Point CloudGuard** | Critical | High | Medium | Low | Informational |  |
| **Google SCC** | critical | high | medium | low |  |  |
| **Microsoft Defender for Cloud** | Critical | High | Medium | Low |  |  |
| **Wiz** | CRITICAL | HIGH | MEDIUM | LOW | INFORMATIONAL |  |

*AWS reports risk through a ranking [1–100] and a severity level [low, medium, etc.].
Both are listed.

## Triage Status Mapping

Table 2.

| Cloud Infrastructure Tool | Ignored | False Positive | To Be Fixed | Mitigated | Fixed | Reopened |
| --- | --- | --- | --- | --- | --- | --- |
| **Prisma Cloud (RedLock)** | Snoozed |  |  |  |  |  |
| **AWS Security Hub*** | suppressed |  | notified |  | resolved |  |
| **Azure Security Center** |  |  |  |  |  |  |
| **Check Point CloudGuard** |  |  |  |  |  |  |
| **Google SCC** | MUTED |  |  |  |  |  |
| **Microsoft Defender for Cloud** |  |  |  |  |  |  |
| **Wiz** |  |  |  |  |  |  |

For SRM Triage Status definitions, click here.
