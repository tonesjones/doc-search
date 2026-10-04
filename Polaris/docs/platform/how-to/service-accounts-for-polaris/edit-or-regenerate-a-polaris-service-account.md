---
title: "Edit or regenerate a Polaris service account"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/edit-or-regenerate-a-polaris-service-account.html"
content_id: "iD7O8oQE2ApAjXFNu33OHg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:18.492870+00:00"
content_hash: "1a6b2fb7dbb744ec3248c2b5458146beb228ce76c1d0f167fd2edf73f4ce2e65"
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
5. Change the expiration period of the service account's access token using the Expiration dropdown.

   You can select 7 days, 30 days, 60 days, 90 days, 365 days, Custom, or No expiration. If you select Custom, an Expiration Date date picker appears. Custom expiration dates cannot be more than two years from the current date.

   Important: Regardless of the expiration option you select, service account tokens automatically expire after 30 days of inactivity.

   Important: Changing the expiration period regenerates the service account's access token. The existing access token is invalidated immediately, and any automated process that uses it fails until you update that process with the new token.
6. For application-based roles only:
   1. Select Manage Applications.
   2. Edit the applications to which the service account has access based on the assigned role.
7. Click Save.

   Note: You cannot edit the name of a service account.

   If you changed the expiration period, the regenerated access token is displayed in obfuscated text. Select Copy to copy the new access token to your clipboard, and then store it securely.

   Important: The regenerated access token is only displayed once, and cannot be retrieved later.

## Regenerate a Polaris service account

Regenerating a Polaris service account deletes its existing access token and generates a new one.

Note: You can only regenerate a service account token before its expiration date. Regenerating a service account does not change its expiration date. To extend the life of a service account, edit the service account and change its expiration period before the access token expires.

1. Go to My Organization > Service Accounts.
2. Select the options [image: icon polaris options] icon next to the service account, then select Regenerate.

   The Regenerate Access Token dialog appears.

   Tip: If a service account's access token expires in seven days or less, you can regenerate it using the Regenerate link displayed in the Access Token Expires column.
3. Click Confirm.
4. The regenerated service account and its access token are displayed on the Service Accounts page. 

   The new access token is displayed in obfuscated text.
5. Select Copy to copy the access token to your clipboard, and then store it securely.

   Important: The service account's access token is only displayed when the account is created or regenerated, and cannot be retrieved later. The regenerated token expires on the same date as the token it replaced, and will also expire if unused for 30 days.
