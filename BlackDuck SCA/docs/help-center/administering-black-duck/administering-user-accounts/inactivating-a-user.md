---
title: "Inactivating a user"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/inactivating-a-user.html"
content_id: "_~O8bFt7lV~MvhT1yx8qfQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:42.324403+00:00"
---

# Inactivating a user

Note: If you have enabled LDAP, you should manage user records in the LDAP server. If you delete a
record in Black Duck and do not delete the user from the LDAP server,
the next time the user attempts to log in to Black Duck, their user
record will be recreated with data from the LDAP server.

To inactivate a user account:

1. Log in to Black Duck SCA.
2. Click [image: Administration icon] .
3. Select **Users** to display the **Users & Groups** page.

     
    [image: image]
4. Find the user you want to inactivate:

   - Filter the users that appear on the page.
   - Sort the list of users by selecting any of the column names. An arrow
     next to the column name indicates the direction the list is sorted.
   - Use the pagination bar at the bottom of the list to go to the appropriate
     page if there are more users than are listed on this page.
5. Select the user to display the *Username*'s User Details page.
6. Clear the **Active user** check box in the **Internal** or **External User
   Details** section and click **Save**.
