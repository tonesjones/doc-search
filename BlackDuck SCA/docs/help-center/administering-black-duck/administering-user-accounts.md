---
title: "Administering user accounts"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/administering-user-accounts.html"
content_id: "UD3SArQgOzB~CA5xK4Mlig"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:33.477101+00:00"
---

# Administering user accounts

There are two ways to administer user accounts in Black Duck:

1. Administering user accounts manually. A user with the User
   Administrator role can:

   - Navigating the Users &
     Groups page
   - Add a new
     user account
   - Inactivate a
     user account
   - Change user account information
   - Change a
     user's password
   - Manage user
     roles
2. Enabling and
   configuring LDAP to manage user accounts.

   After you configure LDAP to manage user accounts for Black Duck,
   new user accounts will be automatically created the first-time users attempt to
   log in. Your LDAP server will then manage passwords and account details for
   those user accounts in Black Duck.

   Tip: If you are using LDAP to manage most of your user accounts in Black Duck, you can still manually manage those user accounts
   that do not also exist in your LDAP directory, such as a default system
   administrator account.

   Note that you can also create external user accounts.

Users with the System Administrator role can also configure the password
requirements for user accounts.
