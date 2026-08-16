---
title: "Edit or regenerate a Polaris service account"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/edit-or-regenerate-a-polaris-service-account.html"
content_id: "iD7O8oQE2ApAjXFNu33OHg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:06.920471+00:00"
content_hash: "e2f1ea96decd49d9a46f40ba1c655ade0db51482d2edae97594257a1558e90b3"
---

# Edit or regenerate a Polaris service account

Learn how to edit or regenerate a Polaris service account in the user interface.

Only Organization Administrators can perform these tasks.

## Edit a Polaris service account

To edit a Polaris service account in the user interface, follow these steps:

1. Go to My Organization > Service Accounts.
2. Select the options [image: icon polaris options] icon next to the account you want to edit, then select Edit. You can also select the service account name.

   The Edit Service Account page appears.
3. Edit the Role Type to either Global (all applications) or Application.
4. Edit the Role assigned to the service account.
5. For application-based roles only:
   1. Select Manage Applications.
   2. Edit the applications to which the service account has access based on the assigned role.
6. Click Save.

   Note: You cannot edit the name of a service account.

## Regenerate a Polaris service account

Regenerating a Polaris service account deletes its existing access token and generates a new one. You can regenerate a service account at any time, including after it has expired. We recommend that you regenerate a service account within seven days of its expiry time.

1. Go to My Organization > Service Accounts.
2. Select the options [image: icon polaris options] icon next to the service account, then select Regenerate.

   The Regenerate Access Token dialog appears.

   Tip: If a service account's access token expires in seven days or less, you can regenerate it using the Regenerate link displayed in the Access Token Expires column.
3. Click Confirm.
4. The regenerated service account and its access token are displayed on the Service Accounts page. 

   The new access token is displayed in obfuscated text.
5. Select Copy to copy the access token to your clipboard, and then store it securely.

   Important: The service account's access token is only returned when the account is created, and cannot be retrieved later. Service account tokens automatically expire one year after creation, and will also expire if unused for 30 days.
