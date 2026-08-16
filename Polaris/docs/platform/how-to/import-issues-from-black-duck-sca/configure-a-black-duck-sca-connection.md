---
title: "Configure a Black Duck SCA connection"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/configure-a-black-duck-sca-connection.html"
content_id: "xn4mq8y8oHe8cJsdfX805Q"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:26.899253+00:00"
content_hash: "7f6d1f8ad539dc1cfa59e6a9ed18077a69f20c73f75186ba78445ca976c9fd0d"
---

# Configure a Black Duck SCA connection

How to create and configure a connection between Black Duck SCA and Polaris, and disable or delete a connection.

To configure a connection to your Black Duck SCA instance, follow these steps:

1. Navigate to My Organization in the left-hand navigation menu.
2. Select Integrations.

   The Add Black Duck SCA Integration page is displayed.
3. In the Black Duck SCA section, select +New Connection.
4. Provide the following information:

   - Name (required): Enter a connection name.
   - Black Duck SCA URL (required): Enter the URL of your Black Duck SCA domain, e.g. `https://{your-company}.blackduck.com/`
   - API Token (required): Enter your Black Duck SCA user access token generated on the Access Tokens page.
5. Select Test Connection.

   A success message appears if the connection test was successful.
6. (Optional) In Application prefix (for new applications), enter a prefix to use in the names of Polaris applications mapped and created by the connector. Spaces are allowed. This helps avoid the creation of duplicate application names.

   Note: For example, you have a Black Duck SCA project named MyProject. If you enter the prefix `sca`, the mapped application created in Polaris is named `sca - MyProject`.
7. Click Save to create the connection.

The connection appears in the Black Duck SCA section and is enabled by default.

## Disable a Black Duck SCA connection

Disabling a connection stops daily syncs from Black Duck SCA and prevents users from triggering manual data syncs. From the My Organization > Integrations page:

In the Black Duck SCA section, identify the connection to sync, then toggle it to Off.

## Delete a Black Duck SCA connection

Delete a Black Duck SCA connection and, optionally, all mapped applications, projects and branches that contain only Black Duck SCA data.

1. Navigate to My Organization > Integrations.
2. In the Black Duck SCA section, identify the connection you want to delete, then select Delete from the three-dot menu.

   The Confirm Delete Connection dialog appears.
3. (Optional) Select the checkbox to delete all applications, projects, and branches created by the connection.

   Projects and branches that contain any native Polaris data, or data imported from other third-party tools, won't be deleted.
