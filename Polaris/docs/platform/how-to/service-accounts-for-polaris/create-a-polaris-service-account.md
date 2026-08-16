---
title: "Create a Polaris service account"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/create-a-polaris-service-account.html"
content_id: "itrgRorwXsSBMpijokPXmw"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:06.286929+00:00"
content_hash: "c1a73807963dc14f5f6e9b277f6d0617c72bc47e86cfe5832180a58f9a705e4b"
---

# Create a Polaris service account

Learn how to create a service account in the Polaris user interface.

To create a service account in the Polaris user interface, follow these steps:

Note: Only Organization Administrators can complete these steps.

1. Go to My Organization > Service Accounts.
2. Select Create Service Account.

   The Create Service Account page appears.
3. Enter a name in the Name field.

   Note: Service account names must be between 3 and 255 characters long.
4. Assign the service account a global or application-level role.

   To assign the service account a global role, follow these steps:

   1. Under Role type, select Global (all applications).
   2. Select Organization Administrator or Application Manager using the Role dropdown.

   To assign the service account an application-level role, follow these steps:

   1. Under Role type, select Application.
   2. Select Administrator, Contributor, Member, Observer or a custom role using the Role dropdown.
   3. Under Applications, select Manage Applications.

      The Manage Applications window opens.
   4. Use the checkboxes to select the applications you want to grant the service account access to.

      Tip: Use the Application Name or Labels filters to quickly find applications in your portfolio.

      [image: Screenshot of the Manage Applications window, with an active label filter.]
   5. Select Save.
5. Select Save.

   The service account's access token is displayed in the Access Token field.

   [image: Screenshot of the Service Accounts page when a service account is created, where the new service account's token can be copied.]

   Note: The token is obfuscated, by default. Select the show [image: icon show obfuscated] icon to view the token in plain text.
6. Select Copy to copy the service account's access token to your clipboard, and then store the token securely.

   Important: The service account's access token is only displayed when the service account is created, and cannot be retrieved later. Service account tokens automatically expire one year after creation, and will also expire if unused for 30 days.
