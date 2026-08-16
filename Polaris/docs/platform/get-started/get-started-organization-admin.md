---
title: "Get started: Organization Admin"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/get-started-organization-admin.html"
content_id: "gG09eV9e7z94KYdRux1JpA"
product_key: "polaris-platform-latest"
section: "Get Started"
scraped_at: "2026-08-12T19:55:52.357579+00:00"
content_hash: "5aed808eb43677f15adcc2470475046589fba0964ebe7b2265b3b00eeb8af437"
---

# Get started: Organization Admin

Before you begin, we recommend reading the following:

- Polaris product overview
- Subscriptions and Entitlements
- Roles and permissions on Polaris
- Polaris data model
- Create and manage Policies
- Manage your default policies

**Goals**

As your organization's Org Admin, start by doing the following:

- Invite users in your organization to sign into Polaris
- Make at least one user an Organization Application Manager, so they can create the applications and projects that other users will join
- Decide whether to allow Polaris to send notifications to users

## Review your personal settings

1. Navigate to your personal settings by clicking on your profile name in the top right corner of the browser tab.
2. Select Account.
3. Select Notifications.
4. Review your notification settings.

   [image: A screenshot of the notification settings checkboxes.]

   Use the checkboxes to select the types of email notifications you'd like to receive.

   Note: If you can't make changes, it means an Org Admin has turned off notifications for the organization. You won't be able to change settings and won't receive notifications.

   Note: If you disable Reports, you will not receive an email when a report you created is ready. See [Create a report](../how-to/create-a-report.md) for more information.

## Invite users to join Polaris

Note: After you set up single sign-on (using an identity provider (IDP) that supports SAML 2.0), you need to use your IDP to grant users access to Polaris. See [Set up single sign-on (with SAML 2.0)](../how-to/set-up-single-sign-on-with-saml-2-0.md) for more information.

1. Go to My Organization > Users.
2. Select Add User.

   [image: Screenshot of the Add User button.]
3. Complete the form on the Add User page.

   [image: Screenshot of the Add User form.]

   Table 1. 'Add User' fields

   | Field name | Description |
   | --- | --- |
   | First Name | This user's first (given) name. |
   | Last Name | The user's surname. |
   | Email | The user's email address in your company domain. |

   Important: To ensure links to Black Duck Community (found on the Help page) function as expected, English characters should be used for first and last names.
4. Assign the user a global role (Organization Administrator or Application Manager), or select No Global Role.

   Note: For more information on roles and permissions, see [Roles and permissions](../reference/roles-and-permissions.md).
5. Click Save.
6. (Optional) Assign the user to one or more groups. Select the user's groups with the Select groups pulldown menu and select Add.

   Note: For more information on groups, see [Manage access with groups](../how-to/manage-access-with-groups.md).
7. Repeat these steps for each user you wish to invite to Polaris.

   New users receive an email invitation, similar to the one you received, with a link to help them create a password and sign in.

   Note: The link to create a password expires after 24 hours.

## Create at least one Organization Application Manager

1. From My Organization > Users.
2. Select the user whom you want to modify.
3. On the Edit User page, use radio buttons to select Application Manager.
4. Click Save.

   The user will receive a notification of the role change.

## Disable notifications if desired

Notifications are enabled for the organization by default but disabled for individual users. Users can decide which notifications to receive or they can decide not to receive notifications at all. An Organization Admin can disable notifications for the entire organization.

1. If you wish to disable notifications for everyone, go to My Organization > General.
2. Uncheck Enable email notifications for all users.

   [image: Screenshot of the Org Notifications page.]
