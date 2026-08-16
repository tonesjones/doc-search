---
title: "Update your self-hosted SCM connections within an application"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/update-your-self-hosted-scm-connections-within-an-application.html"
content_id: "_fo2B9EqTQVTH54NNvnXyA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:11.520629+00:00"
content_hash: "4ba3a23220a793655ed6319fe6343a35394ee24bb26dc6e462b94d6a92b4ea18"
---

# Update your self-hosted SCM connections within an application

Update or replace the URL, secure tunnel, or access token for your on-premises SCM provider.

Use these steps if your access token has expired, if you need to update the SCM URL or secure tunnel, or if you need to update the token scope to enable synchronization or event-based testing.

1. On the Portfolio page, select an application by clicking on its name.
2. Click Settings > Integrations.
3. Click the Edit icon next to Connected SCM.
4. Update the connection details as needed:
   1. Enter a new private SCM URL.
   2. Select URL is in a private network, then select a different Secure Tunnel from the dropdown (see Prerequisites).
   3. Under Repository Access Token, enter the updated access token (see Prerequisites).
5. Click Connect.

   You should receive a Connection Successful message. If your connection test is unsuccessful, check the following:

   - Verify that your network connection is stable.
   - Verify that the Repository Access Token is accurate.
   - Check that the Repository Access Token is still valid and has not expired.
   - Check that you selected the correct provider for your source repository.
   - Check that your organization allows the use of a personal access token (classic).
   - Check that you have authorized the access token for use outside SSO (if applicable).
6. If the connection is successful, click Save.
