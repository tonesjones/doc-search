---
title: "Creating a SBOM or VEX Template"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/creating-a-sbom-or-vex-template.html"
content_id: "aBLLqJ4Lk6dlZGmxKKrD9Q"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:20.691669+00:00"
---

# Creating a SBOM or VEX Template

This page describes how to create templates for controlling the content of your exported
SBOM and VEX reports. Select the template type you want to create:

- Creating a SBOM template
- Creating a VEX template

Note:

**Required permissions:** To create SBOM or VEX templates, you must have Custom
Fields Administrator role permissions. All users with the appropriate module enabled
can view existing templates.

## Creating a SBOM template

To create a SBOM template:

1. Click [image: Manage] and then select **SBOM and VEX Templates**.
2. Click the **SBOM** tab.
3. Click **+ Create SBOM Template**.
4. Enter a name for the SBOM template in the **Name** field. This is a
   mandatory field.
5. Optionally, you may enter a description for the SBOM template in the
   **Description** field.
6. Enable the **Active** checkbox if you want this SBOM template to appear in
   the list of available options when creating a
   SBOM report.
7. Select a default SBOM specification from the **Default SBOM
   Specification** dropdown menu.
8. Select the desired report output type from the **Default Report Format**
   dropdown menu.
9. Select the desired fields to appear in the output for your SBOM template.

   Project Data:

   - **Creator**: Replaces default creator information with the
     person(s) or organization(s) that created the SBOM file.
   - **Project Alias**: Project Alias masks the name of your project
     version name in SBOM reports.
   - **Subproject Components**: Include subproject components in SBOM
     reports.
   - **Creator Comments**: An optional field for creators of the SBOM
     file to provide general comments about the creation of the SPDX file
     or any other relevant comment not included in the other fields.
   - **SBOM Type**: A field to indicate the stage of the
     software lifecycle where the SBOM was generated. This classification
     is based on guidance from [CISA's SBOM Types](https://www.cisa.gov/sites/default/files/2023-04/sbom-types-document-508c.pdf)
     initiative and provides better insight into the origin and intended
     use of the SBOM.

     Possible values:

     - **Design**: Represents a conceptual SBOM created during
       the planning phase, before code exists. Useful for
       architectural or procurement contexts.
     - **Source**: Derived from the source code and associated
       dependencies prior to compilation.
     - **Build**: Created as part of the build process, typically
       through automation in CI/CD pipelines.
     - **Analyzed**: Generated from scanning tools that inspect
       compiled or deployed software (e.g., binary analysis).
     - **Deployed**: Captures what is actually running in a given
       environment—may include runtime-specific packages or
       configurations.
     - **Runtime**: Indicates what the SBOM reflects components
       that were actively loaded, executed, or observed during the
       runtime operation of the software. These components may not
       be evident from source code or build artifacts alone but
       were detected through dynamic analysis or runtime monitoring
       tool.

     Notes:

     - If a user manually sets or overrides the SBOM Type, that
       value is retained in future SBOMs and will not be
       overwritten by subsequent scans.
     - If the SBOM Type cannot be automatically inferred based on
       the scan type and no value has been set by the user, the
       field will be exluded from the SBOM report—even if the SBOM
       Type field is enabled in the SBOM template.

   Component Data:

   - **Originator**: If the package identified in the SBOM file
     originated from a different person or organization than identified
     as Package Supplier, this field identifies from where or whom the
     package originally came.
   - **Description**: The description of the package.
   - **License Comment**: Include additional comments about the
     concluded license in SBOM reports.
   - **Supplier**: The organization that supplied the component that
     the BOM describes.
   - **PURL**: The package URL (PURL), or a specific location within a
     version control system (VCS) for the package.
   - **CPE**: CPE is a standardized method of describing and
     identifying classes of applications, operating systems, and hardware
     devices present among an enterprise's computing assets.
   - **Package Comment**: General comments about the package being
     described.
   - **Package Valid Until Date**: The end of the support period for a
     package from the supplier.
   - **Copyrights**: The copyright text for the exported project
     version or its BOM component(s).
   - **Homepage URL**: The URL of the exported BOM project version or
     its project version BOM component(s).
   - **Download Location**: The URL or a specific location within a
     version control system (VCS) that the component was downloaded
     from.
   - **Component Hash**: The intrinsic identifier for a component.
   - **Vulnerabilities**: Include component vulnerabilities in SBOM
     reports.

   Component Exclusions:

   - **Exclude components with usage of "Dev. Tool / Excluded"**
   - **Exclude Transitive Dependencies**: Exclude transitive
     dependencies from SBOM reports.
   - **Exclude Unconfirmed Snippet Matches**: Exclude unconfirmed
     Snippet matches from SBOM reports.
10. Click **Save** to finish creating the SBOM template.

## Creating a VEX template

Note: The VEX Templates tab is only visible when the VEX module is enabled in your license.

To create a VEX template:

1. Click [image: Manage] and then select **SBOM and VEX Templates**.
2. Click the **VEX** tab.
3. Click **+ Create Template**.
4. Optionally, clear the **Active** checkbox if you do not want this template
   available in all projects immediately. By default, the Active checkbox is
   enabled.
5. Enter a unique name for the VEX template in the **Name** field. This is a
   mandatory field. Duplicate names are not allowed.
6. Optionally, enter a description for the VEX template in the **Description**
   field.
7. Configure the following template fields:

   **Project Data:**

   - **Legal Disclaimer**: When enabled, includes the legal disclaimer
     configured in your project group's SBOM and VEX settings. The
     template controls only whether the disclaimer appears — the actual
     text is managed in your project group settings.
   - **TLP Designation**: When enabled, includes the Traffic Light
     Protocol (TLP) marking in the VEX document. The TLP value itself is
     configured in your existing TLP settings.

   **Subproject Data:**

   - **Subprojects Vulnerabilities**: When enabled, includes
     vulnerabilities from subprojects in the VEX output. When disabled,
     only the parent project version's vulnerabilities are included.

   **Vulnerability Data:**

   - **Comments**: When enabled, includes remediation comments
     associated with vulnerabilities in the VEX output.
   - **Type** (required — at least one must be selected):

     - **CVE**: Include CVE identifiers.
     - **BDSA**: Include BDSA identifiers. Only BDSA
       vulnerabilities emit scores in the report.
     - **EUVD**: Include EUVD identifiers.

   Note: Vulnerabilities that do not have any of the enabled identifier types are
   excluded from the report entirely. For details on how vulnerability ID selection
   affects report output, see How vulnerability ID selection works.
8. Click **Save** to finish creating the VEX template.

   Tip: Click Reset at any time before saving to restore all fields to their default values.

## Creating from an existing template

You can use any existing SBOM or VEX template as a basis for a new template:

1. Navigate to the appropriate tab (**SBOM** or **VEX**).
2. Locate the template you want to copy.

   - For SBOM templates: Click on the desired template and select
     **Create From...**.
   - For VEX templates: Select the desired template and choose
     **Copy**.
3. Enter a new unique name for the template.
4. Adjust the configuration as needed.
5. Click **Save**.
