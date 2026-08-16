---
title: "Access Tokens"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/access-tokens.html"
content_id: "BocinaESsYRJBs3WU1EkSg"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:52.831424+00:00"
---

# Access Tokens

User Administrators of the Black Duck system need a mechanism to maintain and control
access to Black Duck via access tokens. User access is often controlled via Single
Sign-On integration, but access tokens are managed independently by Black Duck.
Administrators need to ensure security of the system and therefore need the tools to
revoke or reset access when required. This page allows the User Administrator to manage
all access tokens by either curating the list manually or by setting up an automated
purging schedule.

The list of access tokens is composed of the following:

- **Name**: The name of the access token
- **Description**: The description given to the access token.
- **Owner**: The name of the user who created the access token.
- **Usage Count**: The number of times the access token was used.
- **Last Generated**: The date or time the access token was created or
  regenerated.
- **Last Used**: The date or time the access token was last used.

  
 [image: image]

## Manual access token deletion

To delete access tokens from the list manually:

1. Log in to Black Duck with the User Administrator role.
2. Click [image: image] .
3. Click **Access Tokens**.
4. Check the box next to any number of access tokens.
5. Click the **Delete** button. A **Delete Token** dialog box will
   appear.
6. Confirm the access token deletion by clicking the **Delete** button in the
   dialog box.

## Setting up the automated access token purge job

To change the access token purge job setting:

1. Log in to Black Duck with the User Administrator role.
2. Click [image: image] .
3. Click **Access Tokens**.
4. Set the desired period of time for the **Maximum weeks of
   inactivity**.
5. Check the **Enable Auto Purge Job** checkbox to activate the feature or
   remove the check to disable it.
6. Click either the **Save** button.

## On-demand access token purge

You can also initiate an on-demand purge immediately by clicking the **Purge
Now...** button. Clicking this button will open the Purge Access Tokens Now
dialog box.

  
 [image: image]   

Select either of the following options:

- **Purge by weeks of inactivity**: Set the time frame for the number of
  weeks of inactivity.
- **Purge all tokens**: Will delete all created access tokens.

Click the **Next** button to continue the action.

The job responsible for conducting the access token purging is ApiTokenPurgeCheckJob.
