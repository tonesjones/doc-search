---
title: "API token"
source_url: "https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/api-token.html"
content_id: "s0SBRCBnmNmySHLNhnVb1g"
version: "latest"
section: "Black Duck C/CPP Tool"
scraped_at: "2026-08-13T16:16:56.243875+00:00"
---

# API token

Black Duck SCA API tokens are generated on a per-user basis. To scan to a new project and
view the results, the user who generates the API token for Black Duck C/CPP must at
minimum have the **Global Code Scanner**, **Global Project Viewer**, and
**Project Creator** roles assigned.

To scan to an existing project and view the results, the user must at minimum have the
project assigned to their user, and have the **Project Code Scanner** role assigned.
See [Understanding roles](https://documentation.blackduck.com/bundle/bd-hub/page/UsersAndGroups/Understanding_roles.html) in the Black Duck Help
documentation for more details on user roles.

Tip: Any user can create an API token without the need for special permissions.
This allows for flexible access management while ensuring that users can easily generate
tokens for their specific needs.

## Generating an API token

1. Go to the Black Duck SCA UI and log in.
2. From the user menu located on the top right of the navigation bar, select
   **Access Tokens**.
3. Click **+ Create Token**. The *Create Token* dialog box appears.
4. Enter the following information:

   - **Name**: The Name field is required and should contain a unique
     identifier for the API token. This name helps distinguish the token's
     purpose and usage, facilitating easier management and tracking of your
     API tokens.
   - **Description**: The Description field is optional and allows you to
     provide a brief summary of the API token's purpose. This helps identify
     its intended function for future reference, making it easier to manage
     and audit your API tokens.
   - **Scope**: The Scope options define the level of access granted by the
     API token. You can select from various scopes to specify which resources
     and actions the token can access. Choosing the appropriate scope is
     essential for maintaining security and ensuring that the token has the
     necessary permissions for its intended use.

     Note: To use with Black Duck C/CPP, the Scope must be **Read and Write
     Access**.
5. Click **Create**. The *Create Token* dialog box appears with the newly
   created access token.
6. Copy the access token shown in the dialog box. This token can only be viewed here
   at this time. Once you close the dialog box, you cannot view the value of this
   token.
