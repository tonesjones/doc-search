---
title: "Software Bill of Materials (SBOM) report"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/software-bill-of-materials-sbom-report.html"
content_id: "6vAmtZuo7ZkpMGY9vvYAUA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:52.020398+00:00"
---

# Software Bill of Materials (SBOM) report

A software Bill of Materials (SBOM) is a list of all the open source and third-party
components present in a codebase. An SBOM also lists the licenses that govern those
components, the versions of the components used in the codebase, and their patch status,
which allows security teams to quickly identify any associated security or license
risks. See the individual SPDX and CycloneDX mapping entries for additional
details on fields found in their SBOM reports.

You can export your SBOM report for a specific project version. SBOM reports can also be
used to import project information into Black Duck.

**To run a Software Bill of Materials report at the project version level:**

1. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
2. Select the version of the project for which you want to run the report.
3. Select the **Reports** tab.
4. Click **+ Create New Report** and select **Software Bill of Materials
   (SBOM)**.
5. Select a SBOM
   template from the **Template** dropdown menu. The default SBOM
   template will automatically be selected, but can be changed if
   desired.
6. Select the desired SBOM specification:

   - [SPDX v2.2](https://spdx.dev/wp-content/uploads/sites/41/2020/08/SPDX-specification-2-2.pdf)
   - [SPDX v2.3](https://spdx.github.io/spdx-spec/v2.3/)
   - [SPDX v3.0](https://spdx.github.io/spdx-spec/v3.0/)
   - [CycloneDX v1.3](https://cyclonedx.org/docs/1.3/json/)
   - [CycloneDX v1.4](https://cyclonedx.org/docs/1.4/json/)
   - [CycloneDX v1.5](https://cyclonedx.org/docs/1.5/json/)
   - [CycloneDX v1.6](https://cyclonedx.org/docs/1.6/json/)
7. Select the desired Report Format:

   - JSON (CycloneDX SBOM reports only support this format)
   - YAML
   - RDF
   - tag:value
8. Optionally, you can expand the **Template Details** to see the fields included
   in the selected SBOM template.
9. Click **Create** to run the report.
10. Click the link to download and view the report.

Note: If the **Don't generate SBOM reports for projects with policy violations** option
has been enabled for this project's group and the project has policy violations, the
option to generation a SBOM report will be disabled.

## What fields are imported from SBOMs

When importing Software Bill of Materials (SBOMs), not all fields are processed by
Black Duck SCA. Understanding which specific fields are
considered is essential for users to effectively utilize SBOM functionality and
ensure comprehensive vulnerability management. This section outlines the fields that
Black Duck SCA evaluates during the SBOM import process,
providing greater transparency into the detailed SPDX functionality and how it can
be leveraged in your projects.

Table 1. SBOM Fields Imported by Black Duck

| Field | CycloneDX | SPDX 2.x | SPDX 3.x | Notes |
| --- | --- | --- | --- | --- |
| **Component/Package Name** | `Component.name`  [Reference](https://cyclonedx.org/docs/1.6/json/#components_items_name) | `Package.name`  [Reference](https://spdx.github.io/spdx-spec/v2.3/package-information/#71-package-name-field) | `Software.Package.name`  [Reference 1](https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Classes/Package/)  [Reference 2](https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/) | **Mandatory**, the whole import fails if even a single Component does not have the name field  (an empty value in the name field causes no failure)  Always exported |
| **Component/Package BlackDuck IDs** | `Property` with names `BlackDuck-Component`, `BlackDuck-ComponentVersion`, `BlackDuck-ComponentOrigin`  [Reference](https://cyclonedx.org/docs/1.6/json/#components_items_properties) | `ExternalRef` with types `BlackDuck-Component`, `BlackDuck-ComponentVersion`, `BlackDuck-ComponentOrigin`  [Reference](https://spdx.github.io/spdx-spec/v2.3/package-information/#721-external-reference-field) | `ExternalRef` with types `BlackDuck-Component`, `BlackDuck-ComponentVersion`, `BlackDuck-ComponentOrigin`  [Reference](https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/ExternalIdentifier/) | **Optional**, used for matching  (*OriginID* > *VersionID* > *ComponentID*)  Always exported |
| **Component/Package URL** | `Component.purl`  [Reference](https://cyclonedx.org/docs/1.6/json/#components_items_purl) | `ExternalRef` with type `purl`  [Reference](https://spdx.github.io/spdx-spec/v2.3/package-information/#721-external-reference-field) | `ExternalIdentifier` with type `purl`  [Reference](https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/ExternalIdentifier/) | **Optional**, used for matching  Export controlled by template |
| **Component/Package Version** | `Component.version`  [Reference](https://cyclonedx.org/docs/1.6/json/#components_items_version) | `Package.versionInfo`  [Reference](https://spdx.github.io/spdx-spec/v2.3/package-information/#73-package-version-field) | `Software.Package.packageVersion`  [Reference 1](https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Classes/Package/)  [Reference 2](https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/packageVersion/) | **Optional**  Always exported |
| **Component/Package Supplier** | `Component.supplier`  [Reference](https://cyclonedx.org/docs/1.6/json/#components_items_supplier) | `Package.supplier`  [Reference](https://spdx.github.io/spdx-spec/v2.3/package-information/#75-package-supplier-field) | `Software.Package.suppliedBy`  [Reference 1](https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Classes/Package/)  [Reference 2](https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/suppliedBy/) | **Optional**  Only persisted for matched *Components*  Export controlled by template |
| **Component/Package Originators** | `Component.authors`  [Reference](https://cyclonedx.org/docs/1.6/json/#components_items_authors) | `Package.originator`  [Reference](https://spdx.github.io/spdx-spec/v2.3/package-information/#76-package-originator-field) | `Software.Package.originatedBy`  [Reference 1](https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Classes/Package/)  [Reference 2](https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/originatedBy/) | **Optional / Export only**, not persisted during import  Export controlled by template |
| **Component/Package CPE** | `Component.cpe`  [Reference](https://cyclonedx.org/docs/1.6/json/#components_items_cpe) | `ExternalRef` with type `cpe22Type` or `cpe23Type`  [Reference](https://spdx.github.io/spdx-spec/v2.3/package-information/#721-external-reference-field) | `ExternalIdentifier` with type `cpe`  [Reference](https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/ExternalIdentifier/) | **Optional**  Only persisted for matched *Components*  Export controlled by template |
| **Component/Package Hash** | `Component.hashes[0].content`  [Reference](https://cyclonedx.org/docs/1.6/json/#components_items_hashes_items_content) | `Package.checksums[0].value`  [Reference](https://spdx.github.io/spdx-spec/v2.3/package-information/#710-package-checksum-field) | `Software.Package.verifiedUsing`  [Reference 1](https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Classes/Package/)  [Reference 2](https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/)  [Reference 3](https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/IntegrityMethod/)  [Reference 4](https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/PackageVerificationCode/) | **Optional**  Only first hash persisted in import  Export controlled by template |
| **Component/Package Hash Algorithm** | `Component.hashes[0].alg`  [Reference](https://cyclonedx.org/docs/1.6/json/#components_items_hashes_items_alg) | `Package.checksums[0].algorithm`  [Reference](https://spdx.github.io/spdx-spec/v2.3/package-information/#710-package-checksum-field) | `Software.Package.verifiedUsing`  [Reference 1](https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Classes/Package/)  [Reference 2](https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/)  [Reference 3](https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/IntegrityMethod/)  [Reference 4](https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/PackageVerificationCode/) | **Optional**  Only the algorithm of the first hash persisted in import  Export controlled by template |
| **Component/Package Comment** | N/A | `Package.comment`  [Reference](https://spdx.github.io/spdx-spec/v2.3/package-information/#720-package-comment-field) | `Software.Package.comment`  [Reference 1](https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Classes/Package/)  [Reference 2](https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/) | **Optional**  Only persisted for matched *Components*  Export controlled by template |
| **Component/Package Valid Until Date** | N/A | `Package.validUntilDate`  [Reference](https://spdx.github.io/spdx-spec/v2.3/package-information/#727-valid-until-date) | `Software.Package.validUntilTime`  [Reference 1](https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Classes/Package/)  [Reference 2](https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/validUntilTime/) | **Optional**  Only persisted for matched *Components*  Export controlled by template |
| **Component/Package Download Location** | `ExternalReference` with type `distribution`  [Reference](https://cyclonedx.org/docs/1.6/json/#components_items_externalReferences_items_type) | `Package.downloadLocation`  [Reference](https://spdx.github.io/spdx-spec/v2.3/package-information/#77-package-download-location-field) | `Software.Package.downloadLocation`  [Reference 1](https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Classes/Package/)  [Reference 2](https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/downloadLocation/) | **Optional**  Only persisted for matched *Components*  Export controlled by template |
| **Component/Package Usage** | N/A  CycloneDX has no `RelationshipTypes`, so we always assign `HAS_PREREQUISITE` | `RelationshipType`  [Reference](https://spdx.github.io/spdx-spec/v2.3/relationships-between-SPDX-elements/#111-relationship-field) | `Core.relationshipType`  [Reference](https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/relationshipType/) | **Optional**  Only persisted for matched *Components*  Always exported |
| **Component/Package Declared License** | N/A | `Package.licenseDeclared`  [Reference](https://spdx.github.io/spdx-spec/v2.3/package-information/#715-declared-license-field) | `Relationship with hasDeclaredLicense`  [Reference 1](https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/Relationship/)  [Reference 2](https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Vocabularies/RelationshipType/) | **Optional**, during import used only during *Component* auto-creation functionality, not persisted  (used for finding out the *License* for the *Custom Component*) |
| **Component/Package Concluded License** | `Component.licenses`  [Reference](https://cyclonedx.org/docs/1.6/json/#components_items_licenses) | `Package.licenseConcluded`  [Reference](https://spdx.github.io/spdx-spec/v2.3/package-information/#713-concluded-license-field) | `Relationship` with `hasConcludedLicense`  [Reference 1](https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/Relationship/)  [Reference 2](https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Vocabularies/RelationshipType/) | **Optional**, during import used only during *Component* auto-creation functionality, not persisted  (used for finding out the *License* for the *Custom Component*) |
| **Component/Package Declared License Comment** | N/A | `Package.licenseComments`  [Reference](https://spdx.github.io/spdx-spec/v2.3/package-information/#716-comments-on-license-field) | `Relationship` with `comment` (e.g., `hasDeclaredLicense`)  [Reference 1](https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/Relationship/)  [Reference 2](https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/) | **Optional**  Only persisted for matched *Components*  Export controlled by template |
| **SBOM Type** | `Metadata.lifecycles.phase`  [Reference](https://cyclonedx.org/docs/1.6/json/#metadata_lifecycles_items_oneOf_i0_phase) | N/A | `Software.sbomType`  [Reference 1](https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/sbomType/)  [Reference 2](https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Vocabularies/SbomType/) | **Optional**  Export controlled by template |

## Ignored SBOM fields during import

**CycloneDX**

- Additional *Component/Package* checksums/hashes & algorithms after
  first one
- *Relationship*s and *Relationship* comments
- Originators beyond author parsing
- All properties except the
  *BlackDuck-Component,**BlackDuck-ComponentVersion* and
  *BlackDuck-ComponentOrigin*
- Non-*DISTRIBUTION* external references (they’re parsed but only
  *distribution* used for the *downloadLocation*)
- Additional supplier contacts after the the first email

**SPDX SBOM**

- Additional *Component/Package* checksums/hashes & algorithms after
  first one
- *Relationship*s and *Relationship* comments beyond
  *RelationshipType* (*SPDX 2.x* and *SPDX 3.x*), and
  *License*s (*SPDX 3.x*)
- Originators beyond author parsing
