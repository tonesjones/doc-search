---
title: "Viewing a project version's BOM"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/viewing-a-project-version-s-bom.html"
content_id: "IiZO4s1LwxjjTl8pzMlj8A"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:23.022380+00:00"
---

# Viewing a project version's BOM

Once you have mapped a component scan or a Protex BOM to a project
version, the results automatically create the project version's BOM.

To view a project version's BOM:

1. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
2. Select the version that you want to view.

   The **Components** tab displays the
   BOM. The example below is what appears for a user with the BOM Manager role using the List view:

     
    [image: BOM page]   

   Tip: Refer to Black Duck online help system for
   information on how users with the BOM Manager and Project Manager role can
   modify the project version's BOM to reflect how you are actually using the OSS
   components in the project.

   Tip: Users with the appropriate role can modify the
   project version's BOM to reflect how you are actually using the components in
   the project:

   - Add a subproject to the
     BOM
   - Adjust the component and version in the project version's
     BOM.
   - Manually add a component to the BOM
   - Delete a manually-added component from the BOM
   - Ignore an automatically discovered component
   - Removing OSS components from a project version BOM
   - Choose whether to view
     the ignored components
   - Change a component's usage to not include it in a project version's
     BOM
   - Change the
     origin and/or origin ID
   - Select a different license
   - Exclude or include the component in the Notices File
     report

   Edits made to a BOM can apply to that project
   version BOM only or can apply to
   all project versions of a BOM.

   Feedback is sent to Black Duck KB when you adjust a
   BOM.

   All users who are members of projects or
   have project-group privilege can:

   - Output the BOM to a PDF
     file.
   - Add comments
     to a component version in a BOM.
   - Indicate that a component version is reviewed.
   - Compare BOM
     versions.
   - Use the table filter field to view only those components that match a
     specific text string, such as the project name. All users can also
     filter the BOM to view specific data in the table or use the risk
     graphs at the top of the page to filter the BOM to show only
     components that have the selected severity and type of risk.
