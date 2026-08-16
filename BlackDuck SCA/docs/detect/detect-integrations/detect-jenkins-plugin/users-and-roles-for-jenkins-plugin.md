---
title: "Users and roles for Jenkins Plugin"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/users-and-roles-for-jenkins-plugin.html"
content_id: "_Cwgicwj8WJEy2st4qm1oA"
version: "11.5.1"
section: "Detect Integrations"
scraped_at: "2026-08-08T23:45:59.340223+00:00"
---

# Users and roles for Jenkins Plugin

First you must configure a user/API token in Black Duck SCA so that the Detect findings are analyzed in Black Duck SCA.

## Generating an API token

1. Log in into your Black Duck SCA instance.
2. From the user menu located on the top navigation bar, select My Access Tokens. The **My Access Tokens** page appears.
3. Click **Create New Token**. The Create New Token dialog box appears
4. Type your name in the **Name** field.
5. Optional: in the **Description** field, you can type a description or definition.
6. Select **Read and Write Access**.
7. Click **Create**. The API token displays in a pop-up window. For security reasons, this is the only time your user API token displays. Please save this token. If the token is lost, you must regenerate it.
8. Optional: To modify an access token that you created, click the arrow in the same row as the access
   token name to open a drop-down menu and select **Edit**, **Delete**, or **Regenerate**.
9. Configure the plugin with your Black Duck SCA url and the API token you just generated.

The following user roles are required for the user that you create in Black Duck SCA:

| Role | Action |
| --- | --- |
| Project Creator | Creates Black Duck SCA projects |
| Project Code Scanner | Populates project BOMGlobal Code Scanner can also be used to populate Project BOM |
| Global Code Scanner | Populates the project BOM, generates reports, checks for policy violations. |
| Project Manager | Generates reports |

**Note:** A user with the Global Code Scanner overall role can generate a report, but cannot delete the report. The Project Manager project role is required to delete the report.
