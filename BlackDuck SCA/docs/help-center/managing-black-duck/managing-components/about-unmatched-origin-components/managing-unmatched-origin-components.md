---
title: "Managing unmatched origin components"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/managing-unmatched-origin-components.html"
content_id: "zFW0b4WhTFU1NGyJzCblAg"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:30:23.371890+00:00"
---

# Managing unmatched origin components

The Unmatched Origins page allows users with the Component Manager role to manage
components with unmatched origins that are found throughout the projects on your server.

## Getting to the Unmatched Origins page

1. Log in to Black Duck as a user with the Component
   Manager role.
2. Click [image: image] .
3. Select **Unmatched Origins**.

## What's on the Unmatched Origins page?

On the Unmatched Origins page, you will find a table with the following
information:

- **Origin ID**: The namespace and package ID for the component package.
- **Type**: The type of origin identifier. Possible values are:

  - **External ID**: Comes from Package Management scan with format
    `namespace:external_id`.
  - **Package URL**: Comes from SBOM scan with proper Package URL
    format. (`pkg:...`)
- **Occurences**: Number of code locations or scans this package ID is found.
  Please note that this will only display occurrences for scans performed after
  upgrading to Black Duck 2023.7.0. Occurrences appearing in scans performed prior
  to this upgrade will not be tallied in this total.
- **Mapping**: The custom
  component to which this package is mapped to. Once a new scan is
  performed and this component is found, the entry will be removed from this table
  and added to the resulting BOM report. Clicking the component in the BOM will
  open the Source
  tab and display the mapped package.

Note: Matching to custom components requires the use of Detect 7 or higher and is currently
only supported for package manager scans.

## Filtering the unmatched origins table

The following filtering options are available:

- **Mapped**: Display origin IDs that are either mapped or unmapped to a project version.
- **Origin Type**: Display origin IDs of either external ID or package URL types.

You can also use the **Filter origins...** text field to search for specific
origin IDs.

## Mapping unmatched origin components

To map a component:

1. Click [image: Map origin ID button] at the end of the component's row. The Map Unmatched ID dialog box
   appears.
2. Select either Existing Component or Create New Component.

   - Existing Component: Click the **Component Name** dropdown box,
     select a custom
     component from the list, and then select a version from
     the **Version** dropdown menu.

     You can instead create a new version for the custom component by
     clicking **+ Create New Version** from the dropdown menu. Doing
     so will add new options to the dialog box. Enter the new version in
     the **New Version Name** field. Click the **License** dropdown
     to select a license from the list displayed. Optionally, you can add
     a release date and approval status.

     Click the **Map** button when you are satisfied with your
     selections to complete the mapping.

     [image: Map Unmatched ID dialog box]
   - Create New Component: Enter a name in the **Component Name** field
     for the custom component. Enter a version and select a license from
     their respective fields. Optionally, you can also add a description,
     URL, release date, and approval status. Click the **Map** button
     create the custom component and complete the mapping to the new
     component.

       
      [image: Map Unmatched ID create new component]

To unmap a component:

1. Click [image: Unmap component button] at the end of the component's row. The Remove Origin ID dialog box appears.

   [image: image]
2. Click the **Remove** button to confirm the unmapping.
