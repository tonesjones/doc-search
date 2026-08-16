---
title: "Creating a new version of a project"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/creating-a-new-version-of-a-project.html"
content_id: "JvX_H3hEglzATm4YyWlQIQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:12.272763+00:00"
---

# Creating a new version of a project

When you create a project, it has one version. You can create more project versions as
needed.

To add a new project version:

1. Log in to Black Duck SCA.
2. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.

   Tip: If you wish to clone an existing version, click [image: Options button] in the row of the version of the project you want to clone and select
   **Clone**. The Clone Version dialog box appears with the information in
   the **Version to Clone** field completed.
3. Click **+ Create Version**.

   The Create a New Version dialog box appears.

     
    [image: Create a New Version dialog box]
4. Type a name for this version of the project. This name can be a numerical release
   number, a text description of the version, or any combination of both.
5. From the drop-down list in the **License** field, select the license for this
   project version. This value is used, for example, for the license of this
   project version when it is a subproject.
6. In the **Notes** field, type any information about this version of the project
   that distinguishes it from other project versions, or that will be useful to
   other developers working on the version or searching for it.
7. If appropriate, in the **Nickname** field type a nickname for the project
   version. This might be a development code name or a shortened name by which this
   version of the project is commonly called.
8. If known, in the **Release Date** field, click [image: Calendar] to select the anticipated release date for the project version or the
   actual date on which the project version was released.
9. From the drop-down list in the **Phase** field, select the development phase
   that this version of the project is currently in. The available options are:
   - In Planning (Default)
   - In Development
   - Pre-release
   - Released
   - Deprecated
   - Archived

   Note: The value in this field is used to calculate risk for the project.
   Archived versions are not included in project risk calculations. Click here for more information
   about project version phases.
10. From the drop-down list in the **Distribution** field, select the method by
    which this version of the project is being released. The available options
    are:

    - External (Default): An application/product that is sold to customer's
      externally for use. The source of the application/product is not
      available to the users but the product is provided externally.
    - SaaS (Software as a Service): An application/product that is shipped as a
      SaaS service (hosted only).
    - Internal: An application/product not sold and stays within the company.
      Essentially never leaves the company and gets into customer's hands.
    - Open Source: An application/product shared, essentially full open source
      (shared on github, etc. with full source code).

    Note: The value in this field is used to calculate risk for the project. Project versions that are internally
    distributed are not included in the risk calculations for the project.
11. Enable or disable **Data Retention**. Enabling this checkbox will prevent this
    Project Version from ever being deleted by the automated data deletion
    policies setup by your administrator.

    Once the project has been created, the project version on the project's page will
    display a lock ( [image: image] ) icon at the end of its row to indicate that this project version is
    protected from automated data deletion.

      
     [image: image]
12. Click **Save**.

    Black Duck saves the project version.
