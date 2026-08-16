---
title: "SPDX 2.2 and 2.3 data fields"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/spdx-2.2-and-2.3-data-fields.html"
content_id: "8OsFX3OHloRWg6H5kQdSDQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:52.713525+00:00"
---

# SPDX 2.2 and 2.3 data fields

|  |  |
| --- | --- |
| Field | Description |
| `SPDXID` | This field contains the identify of the current SPDX document which may be referenced in relationships by other files, packages internally and documents externally. |
| `spdxVersion` | The version of SPDX used to generate this report. |
| `creationInfo` | `comment`: An optional field for creators of the SPDX document to provide general comments about the creation of the SPDX document or any other relevant comment not included in the other fields.  (SPDX 2.2 and 2.3): If SBOM Type was enabled in the SBOM template when the report was generated, it will be included here as `SBOM Type = <value>`.  `created`: The date and time (timestamp) when the document was created.  `creators`: The company or organization that created the SPDX document. If the SPDX document was created by an individual, the person's name will be indicated. If the SPDX document was created using a software tool, the name and version for that tool will be indicated.  `licenseListVersion`: The version of the SPDX License List used when the SPDX file was created. |
| `name` | The BOM project name. |
| `dataLicense` | The licensing under which the creator of this SPDX document allows related data to be reproduced. The only valid value for this property is http://spdx.org/licenses/CC0-1.0. |
| `documentNamespace` | URL to Black Duck's license and readme page on Github. |
| `documentDescribes` | This field contains the parent ID for the package. Displayed as `SPDXRef-package-[BOM project version UUID]`. |
| `packages` | This section contains both the exported project version (which is described by the `documentDescribes`) and also the project version BOM component(s). Each component will have the items listed below: `SPDXID`: The unique ID for the specified entry; project version or project version BOM components.  `comment`: General comments about the package being described.  `copyrightText`: The copyright text for the exported project version or its BOM component(s).  `description`: This field is a short description of the package.  `downloadLocation`: The URL to download the project version or its BOM component(s).  `externalRefs`: This section lists outside sources of information, metadata enumerations, asset identifiers, package manager URLs, or content relevant to the Package, such as a structured naming scheme identifying Packages with known security vulnerabilities.  `homepage`: The URL of the exported BOM project version or its project version BOM component(s).  `licenseConcluded`: The modified license(s) for the exported BOM project version or its project version BOM component(s).  `licenseDeclared`: The license(s) from the KnowledgeBase.  `name`: The name of the exported BOM project version or its project version BOM component(s).  `originator`: If the package identified in the SPDX file originated from a different person or organization than identified as Package Supplier, this field identifies from where or whom the package originally came.  `supplier`: The origin namespace ID.  `validUntilDate`: The end of the support period for a package from the supplier.  `versionInfo`: The version information of the exported BOM project version or its project version BOM component(s).  Note: Some of the values above may not have any information and will display a value of `NOASSERTION`. |
| components section | This section contains the same fields above, detailing the information for each of the components found in the project with the following exceptions:  - The `externalRefs` section will list   the URLs for the component and component version   pages in Black Duck. |
| `files` | Does not contain any data, displaying `[]` only. |
| `relationships` | `relationshipType`: Represents a relationship between two `SpdxElements`. Can be either `DEPENDS_ON` or `CONTAINS`. `spdxElementId`: Contains the parent package ID, as displayed in the `documentDescribes` section above.  `relatedSpdxElement`: Contains the child or related package ID for the component that is part of the relationship. |
| `hasExtractedLicensingInfos` | Contains all the licenses that do not have SPDX ID in the KnowledgeBase. They are added with a document-unique license ID. `name`: Name of the license.  `licenseID`: Contains the license's ID.  `extractedText`: Provide a copy of the actual text of the license reference extracted from the package or file that is associated with the License Identifier Assigned to aid in future analysis. |
