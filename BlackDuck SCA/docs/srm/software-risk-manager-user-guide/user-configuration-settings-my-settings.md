---
title: "User Configuration Settings (My Settings)"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/user-configuration-settings-my-settings-.html"
content_id: "BOS6uc78Xlq1GapI64cQvg"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:02:50.829732+00:00"
content_hash: "f1f4fdea892db35fcdbfb747b3ae4a4b2613f8407d21541d0b89a33e7e27d62c"
---

# User Configuration Settings (My Settings)

User Configuration settings, or "My Settings," allows you to set notifications, manage
passwords, and configure personal access tokens, which can be used to access the
Software Risk Manager REST API.

Click your username in the upper right corner of the page and select My Settings to open
the My Settings page.

[image: image]

[image: image]

For more information on user configuration settings, see the following topics:

- Configuring email notifications
- Changing your password
- Managing personal access tokens

## Configuring Email Notifications

Email notifications allow you to receive emails when a policy status changes or when
there's an analysis failure. (For more information on polices and policy status, see
the Policies Overview
section.)

**To configure email notifications:**

1. Click your username in the upper right corner of the page and select My
   Settings from the dropdown menu.

   [image: image]
2. Select Notifications from the top menu to open the Notifications page.

   [image: image]
3. Enter your email address in the Email field.
4. Use the toggles to enable email notifications.

   There are four
   notification options:
   - **Project Policy status email notifications.** Sends an email
     when there's a policy status change for a project.
   - **Analysis failure email notifications.** Sends an email when
     there is an analysis failure for a project.
   - **Upcoming API Key expirations.** Sends an email when an API
     Key is due to expire.
   - **Upcoming Personal Access Token expirations.** Sends an
     email when a Personal Access Token is due to expire.

   Changes are saved automatically.

## Changing Your Password

Users can change their own password from the My Settings page. (Admins can also
change user passwords. See Changing a User
Password.)

**To change your password:**

1. Click your username in the upper right corner of the page and select My
   Settings from the dropdown menu.

   [image: image]
2. Select Password from the top menu.

   [image: image]
3. Enter your current password.
4. Enter and confirm your new password.

   Passwords must be at least 12
   characters.
5. Click Change Password.

## Managing Personal Access Tokens

The Personal Access Tokens page displays a list of users and usage data and allows
you to generate a new token or delete an existing one.

### Viewing Existing Tokens

**To view personal access tokens:**

1. Click your username in the upper right corner of the page and select My
   Settings from the dropdown menu.

   [image: image]
2. Select Personal Access Tokens from the top menu.

   [image: image]

   This page displays the existing tokens and usage data. Click the
   column headers to sort the list.

### Generating Personal Access Tokens

**To generate a personal access token:**

1. Click your username in the upper right corner of the page and select My
   Settings from the dropdown menu.

   [image: image]
2. Select Personal Access Tokens from the top menu.

   [image: image]

   This page displays the existing tokens and usage data.
3. Click Generate Token to create a new personal access
   token.

   [image: image]
4. Enter a name for the token.
5. Select an expiration. (The default is 90 days.)
6. Select permission options:
   - **Inherit all of my permissions.** The token will include all
     of your configured roles.
   - **Inherit specific permissions** (Read, Create, Update,
     Manage). The token will inherit the selected roles only. For
     example, selecting "Read" will allow the token to read any
     project where you have the "Read" permission set.

   Note: This setting will not override or grant permissions that a
   user doesn't already have.
7. Click Generate Token.

   [image: image]
8. Copy and save your new token.

   Once this window is closed, the token
   cannot be redisplayed.
9. Click Done to close the window.

### Deleting a Token

**To delete a personal access token:**

1. Click your username in the upper right corner of the page and select My
   Settings from the dropdown menu.

   [image: image]
2. Select Personal Access Tokens from the top menu.

   [image: image]
3. Locate the token you want to delete and click Delete Token.

   [image: image]
4. Click Delete to confirm.
