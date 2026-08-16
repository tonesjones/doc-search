---
title: "Comparing BOMs"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/comparing-boms.html"
content_id: "R9NcD38JB79a_2UFFviYdA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:59.782974+00:00"
---

# Comparing BOMs

Use the Project Comparison window to view the differences between two project version
BOMs. You can view the differences between two versions of the same project or between
two versions of different projects.

Note: You can only compare projects which you have permission to view.

To view a comparison of two project version BOMs:

Note: While you can compare any two versions of a BOM for the same or different projects,
this page uses the terms "current" and "compared to" to differentiate the
versions.

1. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
2. Select the version name to open the **Components** tab and view the BOM.

   This
   is the "current" version of the BOM.
3. Select **Compare to** and then select a different version of this BOM or
   select **Other project** to select a different project and version.

   The Project BOM Comparison window appears.

     
    [image: Project BOM Comparison window]   

   At the top of the page are the projects and versions being compared. The
   "current" project and version of the BOM appears in the **Changes In**
   column.

   - If you selected to compare a different version of the same project, that
     project name and version appears in the **Compared To** column and
     the table shows the comparison of the two BOMs.
   - If you selected **Other project**, the table is empty; use the
     **Project** and **Version** fields to select the BOM to be
     compared and click **Compare**.

   This is the "compared to" version of the BOM.

This window shows the adjustments to components or subprojects that occurred in the BOM
and the associated change to the security risk. Adjustments to components consist
of:

- New components/subprojects. Components or subprojects in the "current" version of
  the BOM that were not in the "compared to" version of the BOM.
- Updated components/subprojects. While the components or subprojects were in the
  "'compared to" version of the BOM, one or more of the following changed:
  - Component/Subproject version
  - Usage
  - License
- Removed components/subprojects. The components or subprojects that were in the
  "compared to" version of the BOM that are not in the "current" version of the
  BOM.

Note the following:

- There is only a top-level comparison of subprojects: the components in
  subprojects are not compared.
- If you selected to maintain
  component adjustments to all versions of a project, the Project
  Comparison window may show little to no changes between versions of the same
  project.
- Only confirmed snippets are compared.

To view and work with the information that is important to you:

- Filter the information shown by the type of adjustment.

  Select the ***#* New Components**, ***#* Removed Components**, or
  ***#* Updated Components** filters located at the top right
  section of the window to filter the information shown in the table.

  Select ***#* Total Changed** to view all information. This is the default
  view.
- Print the information shown in the window.

  1. Click [image: Print icon] . A print dialog box appears.
  2. Configure the print settings and print the comparison.

| Column | Description |
| --- | --- |
| **Component** | Component or subproject name. |
| **Version** | Component or subproject version. |
| **Changes** | Possible values are:   - **Added**. The component or subproject is in the "current"   and "compared to" version of the BOM, however, it had a   different version in the "compared to" version of the BOM.   The version shown here is the version in the "current"   version of the BOM. - **Modified**. The usage or license for this   component/subproject version has changed. - **New**. The component or subproject is new – it was not   in the "compared to" version of the BOM. - **Removed**. The component/subproject was in the "compared   to" version of the BOM, however, it is not in the "current"   version of the BOM. - **Replaced**. The component/subproject is in the "current"   and "compared to" version of the BOM, however, there is a   different version in the "current" version of the BOM. The   version shown here is the version in the "compared to"   version of the BOM.   For modifications to ignored components:   - Components ignored in both versions are not compared. - Components ignored in the "compared to" version but not ignored in the "current" version   have a value of **New**. - Components ignored in the "current" version but not ignored   in the "compared to" version have a value of   **Removed**.   Note that for a modification to the version:   - The component/subproject and original version are shown with   **Replaced** as the value in the **Changes**   column. - The component/subproject and new version are shown with   **Added** as the value in the **Changes**   column.   In the following example, the component Lucene had version 1.4.3 in the "compared to" version of the BOM and version 4.5 in the "current" version of the BOM:   [image: BOM Comparison example] |
| **Usage** | Usage of the component or subproject version in the "current" version of the BOM.  Strikeout usage text shows the usage for this component version from the "compared to" version of the BOM. |
| **License** | Declared license of the component or subproject in use in the "current" version of the project.  Strikeout license text shows the license for this component version from the "compared to" version of the BOM. |
| **Security Risk** | Number of high risk (100% red), medium risk (50% red), and low risk (100% gray) vulnerabilities associated with this version of the component or with the subproject.  The value in the **Security Risk** column indicates an increase or decrease in security risk depending on the value in the **Changes** column. If the value in the **Changes** column is:   - **Removed** or **Replaced**. The value indicates a   decrease in security risk from the "compared to" version of   the BOM. - **New**, **Modified**, or **Added**. The value   indicates an increase in security risk from the "compared   to" version of the BOM. |
