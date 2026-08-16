---
title: "Adding a project mapping"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/adding-a-project-mapping.html"
content_id: "ROExukiZpkqLcoGaAm8xmQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:17.069738+00:00"
---

# Adding a project mapping

1. Click Add.
2. Click Select JIRA Project and select one of the projects
   available on the Jira server.
3. In Projects, start entering the name of a Coverity Connect
   project to add. Alternatively, click Edit to choose one
   or more projects from a list of all available projects.
4. For Mode, select Live or
   Test. Use Test while you are
   developing the integration. In Test, Coverity Connect
   issues are not actually sent to Jira.

   Note: When you are ready to start sending issues to Jira, change the
   Mode to Live.
5. On the next page, for Issue Type, choose the type of issue
   defined in the Jira project that will be assigned to all issues exported from
   Coverity Connect to that Jira project.
6. On the next page, assign a Coverity Connect field to each Jira field. Select each
   required Jira field and click Edit. To export information
   to other Jira fields, click Add.

   Figure 1. Add field mapping
     
    [image: image]
7. Select a Coverity Connect field to be the source of the value for the Jira field,
   or select Constant to set a constant value. Either or
   both options are shown, depending on settings in the Jira project.
8. After all Jira fields have been mapped to Coverity Connect fields, click
   Next to check the validity of the mappings. If they
   are valid, click Finish to save the map. If the Jira
   field values are not valid, helpful error messages will appear and you can click
   Back to edit them.
