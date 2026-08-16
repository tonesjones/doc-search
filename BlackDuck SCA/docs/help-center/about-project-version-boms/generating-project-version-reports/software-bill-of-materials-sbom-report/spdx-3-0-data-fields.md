---
title: "SPDX 3.0 Data Fields"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/spdx-3.0-data-fields.html"
content_id: "zHnB007CJtk4UJKejfGHUw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:53.427334+00:00"
---

# SPDX 3.0 Data Fields

SPDX 3.0 is the latest version of the System Package Data Exchange specification, which
standardizes the way software bill of materials (SBOM) information is communicated. Black Duck SCA supports SBOMs in SPDX 3.0 format, providing detailed
metadata for software packages, components, and associated security data.

More information on the data fields can be found on the [SPDX
specification page](https://spdx.github.io/spdx-spec/v3.0.1/).

## Enhanced vulnerability information

The SPDX 3.0 SBOM format has been enhanced with improved vulnerability information.
Your reports now include clear vulnerability identifiers (using CVE, EUVD, and/or
BDSA IDs as configured in your SBOM export template), detailed scoring information
through various CVSS assessment relationships, and explicit status indicators for
each vulnerability's current remediation state. These enhancements enable you to
provide stakeholders with comprehensive security insights while ensuring the reports
remain structured and easy to interpret.

## What's included in your SBOM reports

Your SBOM reports now automatically filter vulnerabilities to show the most relevant
information:

- Vulnerabilities marked as "Duplicate," "Ignored," or "New" are not included in
  the reports
- Only after changing a vulnerability's status from "New" to another status will
  it appear in your SBOM reports

Your SPDX 3 reports include:

- Vulnerability identifiers (CVE, EUVD, and/or BDSA, depending on your SBOM export
  template settings)
- Detailed scoring information
- Clear status indicators showing if vulnerabilities are affected, fixed, not
  affected, or under investigation

## Vulnerability Class

Black Duck SCA includes the Vulnerability class in SPDX 3
reports. The vulnerability identifier types included in your reports are controlled
by your SBOM export template settings, where you can enable or disable CVE, EUVD,
and BDSA identifiers. All three are enabled by default.

**Primary identifier selection**

When multiple identifier types are enabled, a single primary identifier is selected
using the priority order CVE > EUVD > BDSA. The highest-priority enabled identifier
that exists for the vulnerability is used as the primary `spdxId` and
drives the scoring data in the associated CVSS assessment relationships.

- CVE ID: Used as the primary identifier when available. Appears with
  `externalIdentifierType` of `cve`.
- EUVD ID: Used as the primary identifier when no CVE exists. Appears with
  `externalIdentifierType` of
  `securityOther`.
- BDSA ID: Used as the primary identifier when no CVE or EUVD exists. Appears
  with `externalIdentifierType` of
  `securityOther`.

**Additional identifiers**

When a vulnerability has identifiers beyond the primary, all enabled identifiers
appear together in the `externalIdentifier` array of the
Vulnerability object. For example, a vulnerability with both a CVE and an EUVD
identifier would include both in the array:

- CVE identifier with `externalIdentifierType` =
  `cve`
- EUVD identifier with `externalIdentifierType` =
  `securityOther`

Note: SPDX 3.0 does not define dedicated `externalIdentifierType`
values for EUVD or BDSA. Both use the generic `securityOther` type.
You can distinguish them by the identifier string itself — EUVD identifiers begin
with "EUVD-" and BDSA identifiers begin with "BDSA-".

## CVSS Assessment Relationships

To provide detailed scoring information, the following relationships have been
added:

- **CvssV2VulnAssessmentRelationship**: Contains CVSS v2 scoring
  information
- **CvssV3VulnAssessmentRelationship**: Contains CVSS v3 scoring
  information
- **CvssV4VulnAssessmentRelationship**: Contains CVSS v4 scoring
  information

These relationships include the complete CVSS vector strings and scores, similar to
the ratings section in CycloneDX.

When multiple vulnerability identifier types are enabled, scoring data in the CVSS
assessment relationships is provided by the primary identifier source only. For
example, if a vulnerability has both a CVE and an EUVD identifier, the CVSS scores
and vectors come from NVD (the CVE source). Secondary identifiers do not contribute
additional assessment relationships.

## Vulnerability Remediation Representation

SPDX 3 reports now include specific relationships to represent the remediation status
of vulnerabilities:

- **VexAffectedVulnAssessmentRelationship**: Used for vulnerabilities with a
  "known affected" status, indicating the vulnerability is present and affects the
  component
- **VexFixedVulnAssessmentRelationship**: Used for vulnerabilities with a
  "fixed" status, indicating the vulnerability has been remediated
- **VexNotAffectedVulnAssessmentRelationship**: Used for vulnerabilities with a
  "known not affected" status, indicating the vulnerability does not affect the
  component
- **VexUnderInvestigationVulnAssessmentRelationship**: Used for vulnerabilities
  with an "under investigation" status, indicating the impact is still being
  assessed

Note: Unlike CycloneDX, SPDX 3 reports do not include CWE (Common Weakness Enumeration)
information due to limitations in the current SPDX 3 specification.

These enhancements align with the SPDX 3.0.1 specification and provide you with more
detailed information about vulnerabilities, their severity, and remediation
status.

## SPDX 3 status mapping

|  |  |
| --- | --- |
| **Black Duck SCA Vulnerability Status** | **SPDX VulnAssessmentRelationship relationshipType** |
| `AFFECTED` | `affects` |
| Duplicate | N/A - Not included in report |
| Ignored | N/A - Not included in report |
| `MITIGATED` | `doesNotAffect` with the justification `"security_justificationType": "inlineMitigationsAlreadyExist"` |
| `NEEDS_REVIEW` | `underInvestigationFor` |
| `NEW` | `underInvestigationFor` |
| `NOT_AFFECTED` | `doesNotAffect` |
| `PATCHED` | `fixedIn` |
| `REMEDIATION_COMPLETE` | `fixedIn` |
| `REMEDIATION_REQUIRED` | `affects` |
| `UNDER_INVESTIGATION` | `underInvestigationFor` |
