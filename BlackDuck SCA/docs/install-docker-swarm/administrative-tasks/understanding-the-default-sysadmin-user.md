---
title: "Understanding the default sysadmin user"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/understanding-the-default-sysadmin-user.html"
content_id: "XDGBNjcWzU5CcGjilxrV5A"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:59.194471+00:00"
---

# Understanding the default sysadmin user

When you install Black Duck SCA, there is a default system
administrator (sysadmin) account already configured. The default sysadmin user has all
roles and permissions associated with it.

Tip: As a best practice, you should use the default sysadmin account for your initial
log in and then immediately change the default password—blackduck—so that the server is
secure. To change your password, select **My Profile** from your username/user
profile icon in the upper right corner of the Black Duck UI.

To edit the default email address that is associated with the sysadmin user, go to the
**User Management** page on the Black Duck UI, select the
**sysadmin** user name, change the email address and save. To see the change, you
must log out and log in again.

To access the **User Management** page, the user account that you use must have the **User
Administrator** role, which is assigned, by default, to the sysadmin account. The
main purpose of the email address is as a contact reference for the user account.
