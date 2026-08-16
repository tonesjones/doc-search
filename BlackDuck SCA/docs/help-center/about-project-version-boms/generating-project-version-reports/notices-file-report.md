---
title: "Notices File report"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/notices-file-report.html"
content_id: "WAo~W0d0jbgGbBLMlbgmag"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:50.390252+00:00"
---

# Notices File report

The Notices File report provides a list of open source components, versions, the
associated license text, and optionally, copyright statements. You can use this report
to create an attribution report for your project release or to share BOM and license
information.

This report is available as a text file or in HTML format. Each format provides the
following information:

- Header information. Lists the project name, version, phase, and distribution.
- Components. Lists all components, component versions, subprojects, subproject
  versions, and associated licenses, including deep license
  data.

  You can exclude a component or subproject or add an attribution statement,
- Licenses. Provides the license text for all licenses listed in the
  **Components** section.

  You can edit the license text shown here.
- Other options:

  - Deep License Data: Adds deep licenses
    discovered via component origin to the list of components. Only
    available if deep licenses are enabled for the project.
  - File Copyright Text: Provides a Copyright Text section that contains copyright statements
    discovered in file matches. Only available if file matches are present.
  - File License Data: Licenses discovered in file matches. Only available if file matches are
    present.
  - License Data. Choose to include the licenses of components in the project.
  - License Text. Choose to include the text of licenses in the project.
  - Origin Copyright Text. Provides a report section that contains the copyright statements
    obtained from the Black Duck KnowledgeBase, edited KnowledgeBase
    copyright statements, and/or custom copyright statements for the open
    source components you use.

    User with the Copyright Editor role can create or
    edit copyright statements for an open source component version
    origin.
  - Unmatched File Discoveries: Provides an Unmatched File Data section that includes file
    discoveries unassociated with components in the project. Only available
    if unmatched files are present in the project.

The following is an example of a portion of the HTML version of the report:

  
 [image: Notices File report - HTML version]   

Note that licenses from the Unknown license family are not included in the Notices File report, however
the component with the unknown license is included in the report unless you select to
remove it.

Note: If you notice omissions or errors in the license text, contact Black Duck Support and provide
the correct information so that the Black Duck KnowledgeBase can be updated.

To run a Notices File report:

1. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
2. Select the version of the project for which you want to run the report.
3. Select the **Reports** tab.
4. Click **+ Create New Report**.
5. Select **Notices File** and then select the format for the report:
   - Text
   - HTML
6. Check or uncheck the **Include Subprojects** checkbox.
7. Optionally, select one or more of the following options:

   - Deep License Data
   - File License Data
   - File Copyright Text
   - License Data
   - License Text
   - Origin Copyright Text
   - Unmatched File Discoveries

   The Notices File report may take more time to run if any of these options are selected.
8. Click **Create** to run the report.
9. A link that includes the project, version name, and date appears when the report completes.
   Any user who is a member of the project can access the link.
   - If you selected the text format, download the report and extract the zip
     file locally.
   - If you selected the HTML format, select the link to open the report in a
     new tab.
