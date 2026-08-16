---
title: "Creating Custom Components and Component Versions"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/creating-custom-components-and-component-versions.html"
content_id: "8vfDHBcFgA2~U2FGlGueuA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:13.091316+00:00"
---

# Creating Custom Components and Component Versions

Create custom components and component versions to represent software that is not
available in the Black Duck KnowledgeBase. Custom components can be used to track
commercial, proprietary, internally developed, or otherwise unmanaged software within a
BOM.

## Before you begin

You must have the **Component Manager** role.

## Creating a custom component

1. Click [image: Manage] > **Components**.
2. Click **Add** > **Create Component**.
3. In the **Create Component** dialog, enter values for the component.

   The following fields are required:

   - **Name**
   - **Version**
   - **License**
4. Optionally, enter additional component information. See component and version fields
   below for more information on each field.
5. Click **Create**.

The custom component is created and appears in the **Components** list.

When a custom component is created, the initial component version is created
automatically using the version information provided during creation and appears in
the **Component Versions** list.

## Creating a new version for an existing custom component

1. Click [image: Manage] > **Components**.
2. Select the custom component for which you want to create a version. Note that
   you can also select the component from the **Component Versions**
   tab.
3. Click **+ Create Version**.
4. Enter values for the component version.

   The **Version** and **Licence** fields are required.
5. Optionally, update additional component information. See component and version fields below
   for more information on each field.
6. Click **Create**.

## Component and version fields

| Field | Description |
| --- | --- |
| **Name** | Name of the custom component. |
| **Version** | Initial version created for the custom component. |
| **License** | License associated with the component version. |
| **CPE** | A Common Platform Enumeration (CPE) identifier used to identify a software product. For custom component versions, a valid CPE can be used to associate known vulnerabilities with the component version. Black Duck SCA accepts both CPE 2.2 and CPE 2.3 formats. Vulnerability association is supported only for valid CPE 2.3 values.  Note: CPE is now an independent field and has been decoupled from the Origin namespace and can be set only using CPE field. |
| **Namespace** | Namespace used as part of the external package identification. |
| **Package ID** | Package identifier used as part of the external package identification. |
| **Origin Version** | Origin version associated with the external package identification. |
| **PURL** | Package URL (PURL) used to identify a software package. |
| **Release Date** | Release date for the component version. |
| **Approval Status** | Approval status assigned to the component. |
| **Description** | Additional information about the component. |
| **URL** | URL associated with the component. |

Important: If you provide a value for an **External ID** field, you must provide
values for all External ID fields.
