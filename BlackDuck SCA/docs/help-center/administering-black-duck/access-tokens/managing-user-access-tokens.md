---
title: "Managing user access tokens"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/managing-user-access-tokens.html"
content_id: "DiLiY0LU8bDiMWULXjHd9g"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:53.637643+00:00"
---

# Managing user access tokens

Black Duck SCA provides the ability for you to generate one or
more “tokens” for accessing Black Duck SCA APIs. These tokens are intended
to replace the use of username/password credentials in integration configurations, such
as Jenkins or for the Scan Client CLI. With access tokens, if a security breach occurs,
the user’s credentials (which might be their SSO or LDAP credentials) are not directly
compromised.

Note the following:

- Access tokens can only be created by the current user.
- Access tokens are tied to a user's account; therefore, an access token has the
  same role as the user who created the token.
- A user can have multiple tokens. Each token must have a unique name.
- Access tokens do not expire, but can be purged after a set period of
  inactivity.
- If a user is inactivated, their tokens are invalidated.

## Generating an access token

1. Log into Black Duck SCA.
2. From the user menu located on the top navigation bar, select **My Access
   Tokens**.

   The My Access Tokens page appears.

     
    [image: My Access Tokens page]
3. Click **Create New Token**. The Create New Token dialog box appears.

     
    [image: Create New Token dialog box]
4. Enter a name, description (optional), and select the scope for this token (read
   or read and write access). You can only select one access for a token.
5. Click **Create**.

   The *Access Token Name* dialog box appears with the access token.
6. Copy the access token shown in the dialog box. This token can only be viewed here
   at this time. Once you close the dialog box, you cannot view the value of this
   token.
7. Click **Close**.

## Regenerating an access token

You can regenerate a new access token which provides a different key for the same name,
description, and access.

1. Log into Black Duck SCA.
2. From the user menu located on the top navigation bar, select **My Access
   Tokens**.

   The My Access Tokens page appears.

     
    [image: My Access Tokens page]
3. Click [image: image] in the row
   of the token you want to regenerate and select **Regenerate**.

   The Regenerate User Access Token dialog box appears.
4. Click **Regenerate** to confirm.

   The *Access Token Name* dialog box appears with the new access token.
5. Copy the access token shown in the dialog box. This token can only be viewed here
   at this time. Once you close the dialog box, you cannot view the value of this
   token.
6. Click **Close**.

## Deleting an access token

1. Log into Black Duck SCA.
2. From the user menu located on the top navigation bar, select **My Access
   Tokens**.

   The My Access Tokens page appears.

     
    [image: My Access Tokens page]
3. Click [image: image] in the row
   of the token you want to remove and select **Delete**.

   The Delete User Access Token dialog box appears.
4. Click **Delete** to confirm.
