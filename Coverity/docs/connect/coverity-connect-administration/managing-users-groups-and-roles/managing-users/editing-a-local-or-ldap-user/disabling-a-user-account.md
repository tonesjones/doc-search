---
title: "Disabling a user account"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/disabling-a-user-account.html"
content_id: "HjqPKmFp2QeCKxVbokFD3A"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:34.103896+00:00"
---

# Disabling a user account

You can disable a user account to prevent that user from gaining access to Coverity
Connect.

Note: Compare to Locking and unlocking a user account.

**To disable a user account:**

1. Select a user from the user list.
2. In User Details, click
   Edit.
3. Under Additional Actions, select Disable account.

   Users that are disabled cannot log in to the system, cannot use password
   recovery, and cannot become owners of new issues. An administrator must unset
   this option to reestablish access (or create a new user account).

**To disable users who have been disabled or deleted in LDAP:**

If a user has been deleted from your LDAP server, you need to change the user account
type to Local before you can disable the user account. To change the account type, see
Editing a local or LDAP user.

You can also disable users who have been disabled in LDAP. The following steps will
result in disabling all users matching the specified filter, at midnight.

1. Go to Configuration > System > LDAP Configuration > User Search Settings.
2. In the **Disabled user filter** field specify an LDAP filter.

   The filter depends on the LDAP sever implementation. For example, it might be
   UserAccountControl:1.2.840.113556.1.4.803:=2 for Active
   Directory server.

To change the default schedule from 12am every night, you can add the
`ldap.users.disabled.sync.cron.schedule` property to the
`cim.properties` file. This property accepts a cron string in the
same format as cron schedules in the policy manager. For example, the following string
disables users every night at 3 a.m.: `ldap.users.disabled.sync.cron.schedule= 0
0 3 * * *`
