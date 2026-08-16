---
title: "Understanding projects in Black Duck"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/understanding-projects-in-black-duck.html"
content_id: "QpdKNdqCRMoVJH9Iwr44zQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:13:58.140808+00:00"
---

# Understanding projects in Black Duck

Black Duck helps project teams manage project information and
the OSS components that are being used in each of the versions of a project.

At the project level, team members can:

- Update the project and project version information.

  This information is searchable in Black Duck.
- Manage tags associated with
  the project.

  This information is searchable in Black Duck.
- Create a new version of the project.
- Manage project team membership.
- Delete a project
  or project version.

The **My Projects** dashboard lists all projects where you are a member
or where you have project-group privileges. Select the name of the project to go to the
*Project Name* page which displays the **Overview** tab by default.

  
 [image: Project Name page]   

This tab provides the following information for each version in this project:

| Column | Description |
| --- | --- |
| N/A | Icons shown to the left of the version name:   - [image: Policy violation icon] Policy   violation. Select the icon to view information on   the policy violation. - [image: Policy violation override icon] Policy violation has been overridden.   Select the icon to view information on the policy violation. |
| Version | Name of the project version. |
| Phase | The development phase of this version. The possible values are:   - In Planning - In Development - Pre-release - Released - Deprecated - Archived   The value in this field is used to calculate risk for the project. Archived versions are not included in project risk calculations. Click here for more information about project version phases. |
| Last Updated | When this project version was last updated. Hover over the value to see:   - When the scan mapped to this version of the project was last   scanned. If there are multiple scans mapped to this version   of the project, this is when any of those scans was most   recently scanned. - When the BOM was last updated. There are several ways that   the BOM could have been updated, including manual   adjustments, new scans of existing code or Docker images,   and newly-mapped scans. |
| Last Scanned | Date of the last scan for this project version. Hover over the value to see the date and time. |
| License | Name of the license for this project version. |
| Security Risk | Bars show the critical, high, medium, and low security risk levels for the OSS components in this version of the project.  Select the bar to view the number of affected components. |
| License Risk | Bars show the high (100% red), medium (50% red), and low (100% gray) license risk levels for the OSS components in this version of the project.  Select the bar to view the number of affected components. |
| Operational Risk | Bars show the high (100% red), medium (50% red), and low (100% gray) operational risk levels for the OSS components in this version of the project.  Select the bar to view the number of affected components. |

Above the table, the following information is shown:

- **Description**. Description of this project. Select the **Settings** tab
  to create or revise the description.
- **Created**. The user who created this project and the date it was
  created.
- **Updated**. The user who last updated this project (by modifying any project
  information or by adding a member) and the date it was last updated.

  Updates do not include adding or modifying a project version.
- **Tags**. Any tags
  for this project.
- **Additional Fields**. Project custom field information.
