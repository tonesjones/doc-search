---
title: "About SCM read-only BOMs"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-scm-read-only-boms.html"
content_id: "aI4GJX3PTgmSqIbJijd_jQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:25:41.929933+00:00"
---

# About SCM read-only BOMs

Once a GitHub repository has been scanned, the results create a read-only bill of
materials (BOM).

To view a read-only BOM:

1. Select the project name using the **SCM** dashboard. The *Project Name*
   page appears.
2. Select the version that you want to view.

   The **Components** tab displays the BOM. The example below is what appears for
   a user with the BOM Manager role using the List view:

   [image: Read-only BOM]

## What's contained in a read-only BOM?

The read-only BOM is composed of the following sections:

- The header bar contains the project's name and version. It also contains the
  GitHub repository location and the date when the project was last
  scanned.
- The data table displays the following information:

  - The **Components** column lists the components found in the
    project. Clicking the component link displays the origin IDs where
    this component was found. You can also filter the component by using
    the *Filter components...* field.
  - The **License** column displays the license
    associated to the component.
  - The **Vulnerability Count** column displays the vulnerabilities
    linked to the component. Clicking the vulnerability count opens a
    modal containing a list of all the vulnerabilities associated to the
    selected component.

Note: The information presented in this BOM cannot be edited.

## What can you do with the read-only BOM?

You can:

- Manually reinitiate a scan by clicking the **Scan Now** button. This will
  update the project version with any changes that were made in the project
  repository. Note that initiating a rescan will unset any ignored
  components.
- Print the BOM by clicking the **Print** button.
- Delete a project version BOM by clicking the **Settings** tab and then
  clicking the **Delete Version** button.
