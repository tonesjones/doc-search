---
title: "Managing Custom Component Versions"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/managing-custom-component-versions.html"
content_id: "qK3GgPII01TGlJe~9jg4bw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:14.352411+00:00"
---

# Managing Custom Component Versions

A custom component can contain one or more versions. Version-level pages provide detailed
information about a specific custom component version, including licensing information,
usage information, vulnerabilities, origin IDs, and other version-specific settings.

## Before you begin

- You must have the **Component Manager**
  role.
- A custom component must already exist.

## Overview tab

The **Overview** tab displays summary information about the selected custom
component version, including project usage, vulnerability information, licensing
information, and approval status. The page provides a high-level view of the
component version and its associated metadata:

- The **Where Used** section lists the projects that use the custom
  component version.

  You must have permission to view a project before it appears in the
  table.

  The table includes the following information:

  | Column | Description |
  | --- | --- |
  | **Project** | Name of the project that uses the custom component version. |
  | **Version** | The project version that uses the component version. |
  | **Released** | Indicates whether the project version has been released. |
  | **Phase** | Lifecycle phase assigned to the project version. |

  From this table, you can:

  - Select a project name to open the project.
  - Select a project version to view its BOM.
- The **Vulnerabilities** section displays the total number of
  vulnerabilities associated with the custom component version.

  When a valid CPE 2.3 value is associated with the component version, Black Duck SCA can associate known vulnerabilities with that
  component version. Associated vulnerabilities can be viewed on the
  Vulnerabilities tab.
- The **License** section displays the license assigned to the custom component
  version.
- The **Approval Status** section displays the current approval status assigned to the
  custom component version.
- Click **More Details** to view additional information about the customc
  omponent version, including:

  - Last modified date and user
  - Notes
  - Tags
  - SBOM fields
  - Custom fields

  The **SBOM Fields** section can include metadata associated with the
  custom component version, such as:

  - Download location
  - CPE value
  - Component hash
  - Component hash algorithm

## Vulnerabilities tab

The **Vulnerabilities** tab displays vulnerabilities associated with the custom component
version.

Vulnerabilities for a custom component version are determined by the CPE value
assigned to the component version. When a valid CPE 2.3 value is associated with the
version, Black Duck SCA can associate known vulnerabilities
with that component version. Associated vulnerabilities are included in BOM risk
calculations, policy evaluation, notifications, and reports.

Note: Black Duck SCA accepts both CPE 2.2 and CPE 2.3 values. Vulnerability
association is supported only for valid CPE 2.3 values. Vulnerability associations
are preserved when project versions are converted to LTS.

The assigned CPE value is displayed at the top of the page.

The table lists vulnerabilities associated with the custom component version.

| Column | Description |
| --- | --- |
| **Identifier** | The vulnerability identifier. Select a vulnerability to view additional details. |
| **Published** | The date the vulnerability was published. |
| **Overall Score** | The overall vulnerability severity score and severity level. |
| **CVSS Version** | The Common Vulnerability Scoring System (CVSS) version used to calculate the score. |

Some vulnerabilities may display additional indicators, such as inclusion in the CISA Known
Exploited Vulnerabilities (KEV) catalog.

## Origin IDs tab

The **Origin IDs** tab displays the origin identifiers associated with the custom component
version.

Origin IDs can be used to identify software packages and help match scan results to
the custom component version.

The table displays the origin identifiers that are associated with the component
version.

| Column | Description |
| --- | --- |
| **External ID** | The external identifier associated with the custom component version. An External ID consists of:  - **Namespace**–The package ecosystem or source associated with   the package. - **PackageID** – The package identifier within the selected   namespace. - **OriginVersion** – The version associated with the package   identifier. |
| **Package URL (PURL)** | The package URL (PURL) associated with the external identifier, if one exists. |

You can use the **Filter** menu to limit the results displayed in the table.

## Settings tab

The **Settings** tab provides access to version-level information and configuration
settings for the custom component version.

From the Settings tab, you can:

- Update component version details.
- Manage licenses associated with the component version.
- View or modify custom field values.
- View SBOM-related metadata.
- Manage origin identifiers associated with the component version.

The Settings tab contains the following pages:

| Page | Description |
| --- | --- |
| **Component Version Details** | View and update general information about the component version, including version information, approval status, CPE values, and deletion settings. |
| **License** | View and manage licenses associated with the component version. |
| **Custom Fields** | View and manage custom fields associated with the component version. |
| **SBOM Fields** | View SBOM-related metadata associated with the component version. |
| **Origin IDs** | View and manage origin identifiers associated with the component version. |

### Component Version Details

The **Component Version Details** page allows you to view and update information
associated with the custom component version:

- The **Settings** section contains general information about the
  component version.

  You can:

  - Modify the version identifier.
  - Specify a release date.
  - Add or update notes.
  - Assign an approval status.

  After making changes, click **Save**.
- The **CPE (Common Platform Enumeration)** section is used to associate
  a CPE value with the custom component version.

  Black Duck SCA accepts both CPE 2.2 and CPE 2.3
  formats. However, only valid **CPE 2.3** values are used to associate
  vulnerabilities with a custom component version. When a valid CPE 2.3
  value is configured, Black Duck SCA can associate
  known vulnerabilities with the component version. Vulnerabilities
  associated with the component version can be viewed on the
  **Vulnerabilities** tab.

  After updating the CPE value, click **Save**.
- The **Delete Version** section allows you to delete the custom
  component version.

  When you delete a version, the version information is permanently removed
  and cannot be restored.

  Important: A custom component must contain at least one version.
  You cannot delete a version that is currently used by a project.

### License

The **License** page allows you to view and manage the licenses associated with the custom
component version.

You can:

- Modify the existing license.
- Add additional licenses.
- Add a license group.
- Reset unsaved changes.

After making changes, click **Save**.

### Custom Fields

The **Custom Fields** page displays custom field values associated with the custom
component version.

Custom fields allow administrators to collect and track additional information
that is specific to their organization's workflows and requirements. Existing
custom field values are displayed on this page.

If no custom fields have been defined or assigned to the component version, the
page displays No Results Found.

### SBOM Fields

The **SBOM Fields** page allows you to view and manage additional metadata that can be
included in Software Bill of Materials (SBOM) reports.

From this page, you can specify:

- **Download Location**–The location from which the software package can be
  obtained.
- **Hash Value** – A hash used to verify the integrity of the software
  package.
- **Hash Algorithm** – The algorithm used to generate the hash value.

After making changes, click **Save**.

Note:

The **CPE (Common Platform Enumeration)** field is no longer configured
from the **SBOM Fields** page.

Custom component version CPE values are now managed from the **Component
Version Details** page. A valid CPE 2.3 value can be used to associate
vulnerabilities with a custom component version.

### Origin IDs

The **Origin IDs** page allows you to view and manage origin identifiers associated with
the custom component version.

Origin IDs map external package identifiers, such as External IDs and Package
URLs (PURLs), to a custom component version. During a scan, if a matching
identifier is discovered, Black Duck can automatically create a match to the
custom component version.

From this page, you can:

- View origin identifiers associated with the component version.
- Add new origin identifiers.
- Filter the displayed results.
- Edit or Delete an origin identifier by using the **Options** menu ( [image: Options button] ) for that entry.

The table displays the following information:

| Column | Description |
| --- | --- |
| **External ID** | The external identifier associated with the custom component version. An External ID consists of:  - **Namespace**–The package ecosystem or source   associated with the package. - **PackageID** – The package identifier within the   selected namespace. - **OriginVersion** – The version associated with   the package identifier. |
| **PURL (Package URL)** | The package URL associated with the origin identifier, if one exists. |

To associate an additional origin identifier with the custom component version, click
**Add** and provide the required origin information.
