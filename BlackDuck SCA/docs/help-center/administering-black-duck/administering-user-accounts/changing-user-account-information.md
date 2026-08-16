---
title: "Changing user account information"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/changing-user-account-information.html"
content_id: "m8ulJ1iDNu901hiTc2OaCA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:40.878859+00:00"
---

# Changing user account information

You can modify the information for internal or external user accounts.

Note: If you have enabled LDAP, you can manage user account information on the LDAP server or, in
Black Duck (for *external* Black Duck user accounts only). Note that any changes
you make to user account information in Black Duck for *external*
Black Duck user accounts will be overwritten the next time user information is
synchronized with the data on the LDAP server.You can only update the information for an
external user if an administrator has configured either SAML *or* LDAP in Black
Duck. If *both* SAML and LDAP are enabled, or both are disabled, you cannot modify
the information for an external user.

To change user account information:

1. Log in to Black Duck SCA.
2. Click [image: Administration icon] .
3. Select **Users** to display the **Users & Groups** page.
4. Find the user whose information you want to change:
   - Filter the users that appear on the page.
   - Sort the list of users by selecting any of the column names. An arrow
     next to the column name indicates the direction the list is
     sorted.
   - Use the pagination bar at the bottom of the list to go to the appropriate
     page if there are more users than are listed on this page.
5. Select the username to open the *Username*'s User Details page.
6. Select the **User Details** tab.
7. Enter the updated information in the **User Details** section.

   Note: If you are updating information for internal users in the **Internal User Details**
   section and password requirements have been defined, you will not be able to
   save the updated information if this user's password does not meet the password
   requirements; an error message appears notifying you of which password
   requirements are not met. Update the user's password to meet the password
   requirements and then update the information in this section.
8. Click **Update**.
