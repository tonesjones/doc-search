---
title: "Creating a user account"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/creating-a-user-account.html"
content_id: "bf69Z6YxcQHTx_k~PrbNdw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:35.105621+00:00"
---

# Creating a user account

You can create a Black Duck user account for a local user (an internal user account) for
an external user (such as a user managed by an external source, such as LDAP).

If you have enabled LDAP, you can create users on your LDAP server instead of in Black Duck SCA. Black Duck will
authenticate user IDs against the LDAP server, and if the username and password are
valid, will copy the user ID to Black Duck database.

Note that with external user accounts:

- You can create users and assign roles without the user logging in to Black
  Duck.
- User information, such as the first or last name, can be changed in Black Duck,
  however passwords are not managed by Black Duck.
- The first name, last name, and email address of the external user will be
  overridden with the information present on the external server, (such as an LDAP
  server), at the time of login.
- An external user is only created when an administrator configures either SAML or
  LDAP in Black Duck. If both SAML and LDAP are enabled, or *both* are
  disabled, the external user will not be created.

To create a user account:

1. Log in to Black Duck SCA.
2. Click [image: Administration icon] .
3. Select **Users** to display the **Users & Groups** page.

     
    [image: image]
4. Click **+ Create User**. The Create a New User dialog box appears.

     
    [image: Create a New User Dialog Box]
5. Select whether this user is an internal (managed within Black Duck) or external
   (managed by LDAP, SAML) account.
6. Do one of the following:
   - For an internal user, enter the following information
     - Username.
     - First Name.
     - Last Name.
     - Email. This field is optional.
     - Password.

       If there are password requirements, those requirements are listed
       in this dialog box. Black Duck notes when each requirement is
       met. You will not be able to create the user account unless the
       password meets *all* requirements.
     - Confirm password: This must match the password you
       entered.
   - For an external user, enter the following information:
     - Username.
     - First Name.
     - Last Name.
     - Email. This field is optional.

     Note that the passwords for external accounts are managed by the
     external source such as LDAP, not by Black Duck.
7. Select whether this user is active or inactive. Clearing this check box
   inactivates this user.
8. Click **Create**.

   Black Duck creates the user
   account with the password you specified.

After creating a user, you can:

- assign roles to this
  user
- assign groups to this
  user
- add this user to a project team

If you created default groups,
this user is automatically added to the default group and is granted all roles and
access to all projects configured for that group.
