---
title: "Changing a user's password"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/changing-a-user-s-password.html"
content_id: "na4AlyMPj0kVMrseHr~Xag"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:44.978965+00:00"
---

# Changing a user's password

Note: If you have enabled LDAP authentication, user account passwords are managed by LDAP. You
will not be able to change passwords in Black Duck.

To change a user's password:

1. Log in to Black Duck SCA.
2. Click [image: Administration icon] .
3. Select **Users** to display the **Users & Groups** page.

     
    [image: image]
4. Find the name of the user whose password you want to reset:
   - Filter the users that appear on the page.
   - Sort the list of users by selecting any of the column names. An arrow
     next to the column name indicates the direction the list is
     sorted.
   - Use the pagination bar at the bottom of the list to go to the appropriate
     page if there are more users than are listed on this page.
5. Select the username to open the *Username* page and click **Reset Password for
   User**.
6. In the Reset Password for User dialog box, type the new password in the
   **Password** field.

   If there are password requirements, those requirements are listed in this dialog
   box. Black Duck notes when each requirement is met. You will not be able to save
   this password if it does not meet *all* requirements.
7. Type the same password in the **Confirm Password** field.
8. Click **Save**.
