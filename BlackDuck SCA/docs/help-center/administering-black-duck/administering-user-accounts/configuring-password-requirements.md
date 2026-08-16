---
title: "Configuring password requirements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-password-requirements.html"
content_id: "Hx2WcMhM4yPcYwVYDkuwfw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:43.611857+00:00"
---

# Configuring password requirements

Users with the System Administrator role can set password requirements for *local*
Black Duck accounts. If enabled, Black Duck ensures that the new password meets your
requirements and also rejects passwords that are considered weak, such as "password",
"blackduck", or a user's username or email address.

Note: These requirements do not apply to external (LDAP or SAML) accounts.

System Administrators can:

- define the minimum password length (from 8 to 25 characters). The maximum length
  is 128 characters.
- define the minimum number of character types for the password (from one to four
  character types). Possible character types are lowercase letters, uppercase
  letters, numbers, or special characters.
- select whether to enforce the password requirements on current users when they
  log in to Black Duck.

  If you select this option, current users who try to log in with a password that
  does not meet the requirements will be forced to create a new password before
  they can access the system.

  Note that when using the Black Duck APIs, users with a password that does not
  meet your requirements will receive a 412 response code which will include the
  reason why the current password does not meet requirements.

If password requirements are enabled, all new passwords must satisfy the requirements.
Password requirements are still enforced on current users when they attempt to change
their password. Administrators must also create passwords that meet these requirements
when resetting a current user's password or when they make any changes to a user's
detail information (such as their first name).

By default, password requirements are enabled and have these settings:

- The minimum password length is eight characters.
- Only one character type is required.
- Password requirements are not enforced on current users when logging in to Black
  Duck.

To manage password requirements:

1. Log in to Black Duck with the System Administrator role.
2. Click [image: Admin icon] .
3. Select **System Settings**.
4. Click**Local Authentication**.
5. Add or remove the check in the **Enable Password Settings** checkbox to enable or disable
   password settings.
6. If you enabled password settings:

   1. Select the following:

      - **Minimum length**. Minimum number of characters in the
        password.
      - **Character requirements**. Select the minimum number of
        character types.

        For example, if you select the value 2,
        passwords must include at least two of the following: lowercase
        letters, uppercase letters, numbers, or special
        characters.
      - **Enforce configuration**. Select this option to enforce the
        password requirements on your current users when logging in to
        Black Duck.
   2. Click **Save**.
