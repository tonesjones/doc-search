---
title: "Viewing project and project version audit information"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/viewing-project-and-project-version-audit-information.html"
content_id: "1uaHLHfRxvan_YKmALgl8w"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:22.345060+00:00"
---

# Viewing project and project version audit information

Black Duck tracks and displays all updates and changes that affect a
project and/or project version. Use this information to understand who made changes or
the events that caused changes to a project or project version. With this audit trail,
you can determine, for example:

- who made changes to the BOM, such as who reviewed a component, added a comment,
  or ignored a component
- what changes occurred due to a scan, such as what components were added or
  deleted and what changes occurred due to those components (for example, the
  vulnerabilities that were added)
- who created or deleted a project version
- when was a policy violation triggered or when was a component no longer in
  violation,
- when was a policy violation overridden or when was the override reversed
- when did a component in your BOM introduce a new vulnerability
- when was remediation information updated for a vulnerability on a component in
  your project
- when did someone add or remove users from a project
- when was a snippet match confirmed or ignored

Black Duck provides the following information:

- The object that affected the project or project version, such as a component,
  vulnerability, or scan
- The type of event, such as vulnerability was found or a component was edited
- Who caused the event in the format User: *username*. If the Black Duck
  system caused the event (for example components or vulnerabilities found during
  a scan or an update to Black Duck KnowledgeBase that changed a vulnerability),
  the column shows User: blackduck_system.
- Date and time this event occurred.

The following is an example of a new project and project version created during a
scan:

  
 [image: Project Audit Trail]   

Note the following:

- Information is shown for the past 24 hours with the most recent changes appearing
  at the top of the table. Use the date filter to view information for different
  periods of time.
- While the deletion of a project version appears at the project level, deletion of
  a project will not appear here.

To view audit information:

Audit information appears on the **Settings** tab of the project or project
version.

1. Log in to Black Duck SCA.
2. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
3. Do one of the following:
   - To view *project* level audit information, select the
     **Settings** tab and then select **Activity**.

       
      [image: Project Audit Trail]
   - To view *project version* level audit information, select the
     version, select the **Settings** tab, and then select
     **Activity**.

       
      [image: Project Version Audit Trail]
4. From this page:
   - Click > located to the left of the object name to view details of this
     event.

       
      [image: Audit Trail Details]
   - Filter the table to view specific information, such as activity during a
     specific date range or a specific type of event.

## SBOM fields

If SBOM fields are enabled, adding or
modifying these fields on the project version or component level will be logged in
the Activity tab as well. Click here for more
information on how to edit SBOM fields.
