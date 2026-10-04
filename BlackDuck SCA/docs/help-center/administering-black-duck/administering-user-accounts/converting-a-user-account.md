---
title: "Converting a user account"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/converting-a-user-account.html"
content_id: "U3MGqvXYRmtXQPb5TWGJDA"
version: "2026.7"
section: "Welcome to Black Duck SCA"
scraped_at: "2026-10-04T23:32:19.151416+00:00"
content_hash: "65b3eb604048c313218ca79d7e07f67d1614de7cb8f49d797e72b3a562beea93"
---

# Converting a user account

You can convert an internal account to an external account or an external account to an internal account.

Note: Converting an internal user account to an external user account requires that an administrator has configured *either* SAML or LDAP in Black Duck. If *both* SAML and LDAP are enabled, or both are disabled, you will be unable to convert the internal user account to an external user account.

To convert an account:

1. Log in to Black Duck SCA.
2. Click [image: Administration icon] .
3. Select **Users** to display the **Users & Groups** page.

     
    [image: image]
4. Select the username of the account you wish to convert. The *Username*'s User Details page appears.

   Depending on whether the account you selected is an internal or external account, do one of the following:

   - To convert an existing external account to an internal account, click **Convert to Internal Account (Black Duck)**.
   - To convert an existing internal account to an external account, click **Convert to External Account (LDAP, SAML)**.
5. Do one of the following:
   - To convert from an external account to an internal account, enter the following information:
     - Username. Enter a username.
     - First Name. The existing first name is shown. You can retain the existing name or enter a new first name.
     - Last Name. The existing last name is shown. You can retain the existing name or enter a new last name
     - Email. This field is optional.
     - Password
     - Confirm password: This must match the password you entered. Black Duck validates this when you create the user account.
   - To convert an internal account to an external account, enter the following information:
     - Username. Enter a username.
     - First Name. The existing first name is shown. You can retain the existing name or enter a new first name.
     - Last Name. The existing first name is shown. You can retain the existing name or enter a new first name.
     - Email. This field is optional.

     Note that the passwords for external accounts are managed by LDAP, not by Black Duck.
6. Select whether this user is active or inactive. Clearing this check box inactivates this user.
7. Click **Save**.
