---
title: "Managing Custom Components"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/managing-custom-components.html"
content_id: "j2lfDkdU9mIR8Jk5bj3SYg"
version: "2026.7"
section: "Welcome to Black Duck SCA"
scraped_at: "2026-10-04T23:32:15.227141+00:00"
content_hash: "f174087f68dea20b6150b2c682f41e220baa5bb0ebe3e2cb3288605f12eb9619"
---

# Managing Custom Components

View and manage information about a custom component, including component details, versions, tags, approval status, custom fields, and SBOM metadata.

## Before you begin

You must have the **Component Manager** role.

## Open a custom component

1. Click [image: Manage] > **Components**.
2. Select the name of the custom component that you want to view.

## Overview tab

The **Overview** tab displays summary information about the custom component and its versions.

The information panel displays:

| Item | Description |
| --- | --- |
| **Approval Status** | The approval status assigned to the custom component. |
| **Description** | A description of the custom component. |
| **Tags** | Tags associated with the custom component. |
| **Custom Fields** | Custom field values assigned to the custom component. |

The versions table lists the versions that belong to the custom component.

| Column | Description |
| --- | --- |
| **Version** | Version of the custom component. Select a version to view information for that custom component version. |
| **Used Count** | Number of projects that use the custom component version. |
| **License** | License assigned to the custom component version. |
| **Released** | Release date for the custom component version. |

To create an additional version for the component, click **Create Version**.

## Settings tab

The custom component **Settings** tab provides access to component-level information and configuration settings.

- The **Component Details** page allows you to view and update component information, including:

  - Component Name
  - Description
  - URL
  - Notes
  - Approval Status

  After making changes, click **Save** to update the component.

  The **Delete Component** section is also available from the Component Details page. You can use this section to delete the custom component when it is no longer needed.

  Warning: You cannot delete a custom component that is currently in use.
- The **Custom Fields** tab displays any custom fields that have been defined for the custom component.
- The **SBOM Fields** tab displays SBOM-related metadata associated with the custom component.
