---
title: "Authenticating users for SCM providers"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/authenticating-users-for-scm-providers.html"
content_id: "FOU2yVVtLIJuvqXn4LRbvQ"
version: "2026.7"
section: "Welcome to Black Duck SCA"
scraped_at: "2026-10-04T23:32:19.734560+00:00"
content_hash: "7f4113cb128caa777d0ec3f9514c4344348b4e90157b494acce0266c37966032"
---

# Authenticating users for SCM providers

Black Duck users wishing to use SCM integration must authenticate with GitHub cloud, or if the system administrator has configured it, GitHub Enterprise. This can be done at the time the SCM integration is used, such as attempting to assign a repository, or directly in the my profile area of Black Duck. Based on the selection, users will be redirected to an appropriate Git landing page where they will log into their account. If authentication is successful, users will be redirected back to the Black Duck application along with an access token. This token will be stored in the database for use in future communications with Git.

To authenticate yourself with a SCM provider:

1. Click your username on the top right of any page.
2. Select **SCM Providers**.
3. Click **Authenticate** next to the SCM server name. This will redirect you to the SCM server where you will be prompted to confirm you want to authorize the OAuth app and what access it has.
4. Click **Yes/Ok** to return to Black Duck.

You can also authenticate yourself when creating a new project.
