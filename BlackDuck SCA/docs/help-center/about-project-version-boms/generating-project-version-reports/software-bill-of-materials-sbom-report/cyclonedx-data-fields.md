---
title: "CycloneDX Data Fields"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/cyclonedx-data-fields.html"
content_id: "jKcWbEPbH_R8rgL8dBDBvQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:54.158869+00:00"
---

# CycloneDX Data Fields

## Enhanced vulnerability information

The CycloneDX SBOM provides enhanced vulnerability information in CycloneDX SBOM
reports. This improvement includes detailed vulnerability scores with their
corresponding scoring systems, comprehensive information about weakness types
through CWE references, and analysis details that show current status and planned
remediation actions. By adding this security context to your CycloneDX reports, you
can share more meaningful insights with stakeholders while maintaining a clear and
actionable format.

## What's included in your SBOM reports

Your SBOM reports now automatically filter vulnerabilities to show the most relevant
information:

- Vulnerabilities marked as "Duplicate," "Ignored," or "New" are not included in
  the reports
- Only after changing a vulnerability's status from "New" to another status will
  it appear in your SBOM reports

Your CycloneDX reports now include:

- Vulnerability scores with their scoring system (like CVSS)
- Information about the type of weakness (CWE)
- Analysis details including current status and planned actions

## Vulnerability Ratings

Each vulnerability now includes detailed scoring information:

- **Method**: Identifies the scoring system used (such as CVSSv31 or
  CVSSv4)
- **Vector**: Contains the complete CVSS vector string that details the
  characteristics of the vulnerability

For example:

```
"ratings": [
                {
                "method": "CVSSv31",
                "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"
                }
                ]
```

## Common Weakness Enumeration (CWE)

Vulnerabilities now include associated CWE identifiers, providing insight into the
type of weakness:

```
"cwes": [
                "CWE-79",
                "CWE-80"
                ]
```

## Analysis Information

The analysis section provides details about the vulnerability's remediation
status:

- **State**: Current status of the vulnerability (e.g., "resolved",
  "in_triage")
- **Justification**: Reasoning behind the assigned status (e.g.,
  "component_not_present")
- **Response**: Actions taken or planned in response to the vulnerability
  (e.g., "will_not_fix", "update")

```
"analysis": {
                "state": "resolved",
                "justification": "component_not_present",
                "response": "update"
                }
```

These enhancements align with the CycloneDX 1.6 specification and provide you with
more detailed information about vulnerabilities, their severity, and remediation
status.

## Data fields

|  |  |
| --- | --- |
| Field | Description |
| `bomFormat` | Specifies the format of the BOM. This helps to identify the file as CycloneDX since BOMs do not have a filename convention nor does JSON schema support namespaces. |
| `specVersion` | The version of the CycloneDX specification a BOM used for the report. |
| `serialNumber` | A string formatted by "urn:uuid:"+ a randomly generated UUID number. |
| `version` | The version allows component publishers/authors to make changes to existing BOMs to update various aspects of the document such as description or licenses. When a system is presented with multiple BOMs for the same component, the system should use the most recent version of the BOM. The default version is '1' and should be incremented for each version of the BOM that is published. Each version of a component should have a unique BOM and if no changes are made to the BOMs, then each BOM will have a version of '1'. |
| `metadata` | `timestamp`: The date and time (timestamp) when the document was created.  `tools`: Describes the tool(s) used in the creation of the BOM, which includes the name of the vendor who created the tool, the name of the tool itself, and the version of the tool.  `authors`: The name of the person(s) who created the BOM. May also contain the email address of the contact if present.  `component`: The component that the BOM describes; the name of the component, the component version, the type of component, and a `bom-ref` which can be used to reference the component elsewhere in the BOM.  `properties`: The SBOM Type of the generated SBOM. |
| `components` | `author`: The person(s) or organization(s) that authored the component.  `supplier`: The organization that supplied the component. `name`: The name of the component. This will often be a shortened, single name of the component. If this field is missing in the SBOM import, the filename of the SBOM will be used as the scan name in place of the missing metadata. `version`: The component's version. If there is no version information, this field is set as "Unknown".  `description`: Specifies a description for the component.  `licenses`: A list of all licenses associated to the component. If the license is a valid SPDX license, it will be displayed in the `id` field. If the license's SPDX id is not available it will be displayed in the `name` field.  `cpe`: Specifies a well-formed CPE name that conforms to the CPE 2.2 or 2.3 specification.  `purl`: The component package URL.  `pedigree`: The `notes` field lists the license display text. it is especially useful for complex license cases. The licenses section list all licenses objects in a flat list. By using this field, it can pass the complex license info.  `externalReferences`: This section contains the component url, e.g. host/components/[component UUID]/versions/[component version id].  `type`: Specifies the type of component.  `bom-ref`: An optional identifier which can be used to reference the component elsewhere in the BOM. Every `bom-ref` should be unique. |
| `dependencies` | Defines the direct dependencies of a component. `ref`: References a component by the components `bom-ref` attribute  `dependsOn`: The parent's identifier, either entity version UUID or enitity UUID if the version UUID is unavailable. |
| `vulnerabilities` (v1.4 only) | `id`: The primary identifier for the vulnerability, determined by which identifier types are enabled in your SBOM export template and the priority order CVE > EUVD > BDSA. The highest-priority enabled identifier that exists for the vulnerability is used. For example, if all three are enabled and a CVE exists, the CVE is the `id`; if no CVE exists but an EUVD does, the EUVD identifier is the `id`.  `source`: The source of the primary identifier. The `name` will be NVD for CVE, EUVD for EUVD, or BDSA for BDSA, corresponding to whichever identifier is used as the primary `id`.  `references`: Additional identifiers for the same vulnerability. When multiple identifier types are enabled in your SBOM export template and additional IDs exist beyond the primary, they appear here. For example, if CVE is the primary `id`, any corresponding EUVD and BDSA identifiers appear as references with their respective `source` `name`. References do not include duplicate score or vector metadata.  `ratings`: Vulnerability scoring data from the primary identifier source. The `source` `name`, `score`, `severity`, `method`, and `vector` values come from whichever source provides the primary `id` (NVD for CVE, EUVD for EUVD, or BDSA for BDSA). Only one set of ratings is included — secondary identifiers listed in `references` do not contribute additional ratings.  `description`: The description of the vulnerability from the primary source (NVD, EUVD, or BDSA). |

## CycloneDX status mapping

|  |  |
| --- | --- |
| **Black Duck SCA Vulnerability Status** | **CycloneDX Vulnerability Analysis State** |
| `AFFECTED` | `exploitable` |
| Duplicate | N/A - Not included in report |
| Ignored | N/A - Not included in report |
| `MITIGATED` | `not_affected` with the justification `protected_by_mitigating_control` |
| `NEEDS_REVIEW` | `in_triage` |
| `NEW` | `in_triage` |
| `NOT_AFFECTED` | `not_affected` |
| `PATCHED` | `resolved` |
| `REMEDIATION_COMPLETE` | `resolved` |
| `REMEDIATION_REQUIRED` | `exploitable` |
| `UNDER_INVESTIGATION` | `in_triage` |
