---
title: "Editing a local or LDAP user"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/editing-a-local-or-ldap-user.html"
content_id: "Q5BTU2klbe51YTsRZgDkLA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:30.992172+00:00"
---

# Editing a local or LDAP user

After creating a user, you can edit its properties.

**To edit a user:**

1. Navigate to Configuration > Users & Groups.
2. Select the user to edit. In User Details, click
   Edit.
3. Edit the user properties.

   - Username: Required identifier for the users.

     New user names cannot match any existing user in the system.

     Note: If an existing user name is changed, then any authentication keys that
     were generated for it will need to be regenerated using
     `cov-manage-im`.
   - First Name: Optional entry for the first name of
     the user.
   - Last Name: Optional entry for the last name of the
     user.
   - Email: Optional e-mail address of between 6 and
     256 characters. The e-mail address is required for
     Notification.
   - Password: Required entry of between 6 and 32
     characters.
   - Confirm Password: Required entry that must match
     the password entry.
   - Account Type: Required user account type
     (Local or LDAP).

     All information about local users is stored in the Coverity Connect
     database. Information about LDAP users is stored both in the Coverity
     Connect database and an LDAP server, with the exception of
     passwords.

     As an administrator, you can control which types of user accounts are
     allowed to access Coverity Connect by disabling various authentication
     mechanisms through the Configuration > System > Authentication and Sign In screen.

     You can change the Type at any time by editing the user.

     Note: If you change an LDAP user to a local user, all LDAP groups are removed. After you add
     an LDAP user and apply your changes, the user is automatically
     synchronized with the LDAP server. For information about manually
     synchronizing users with LDAP groups, see Refreshing LDAP group
     membership.You cannot change the user name, domain, first
     name, last name, email, or password of an LDAP user because this
     information is stored on the LDAP server. You can change the
     Account Type from LDAP to Local (or vice
     versa).

     To email the new user an account
     notification that contains a Coverity Connect URL, name, and sign-in
     information, select Email sign-in instructions once you
     apply.

     Important: You can only send email sign-in instructions if you
     have configured email in Coverity Connect. The check box will be
     disabled if email is not configured.
   - Locale: Required UI display language for the
     particular user. You can select from the following:

     - English (United States) - default
     - Japanese (Japan)
     - Korean (Korean)
     - Chinese (Simplified Chinese)

     The language setting will take effect the next time the user signs
     in.

     Click OK to close the Edit
     dialog.
4. If necessary, in the Group Memberships tab, assign the
   user to an additional user group. For guidance, see Assigning a user to a group.

   By default, all users belong to the Users group.
5. If necessary, in the Roles tab, change the role settings
   for the user at the global, project, stream, or component level.

   For guidance with this task, see Managing roles for a user. Note
   that it is typical to reserve role assignment at the user level for special
   cases in which role assignment at a group level is not feasible or where you
   need to override a group-level role (see Assigning a user to a group). For details about roles, see Understanding how Coverity Connect applies roles.
6. Click Done to save your changes and exit.
