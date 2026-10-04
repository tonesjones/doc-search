---
title: "Make an access token"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/make-an-access-token.html"
content_id: "M8YO6g2it2U5ZvgyxfabHg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:21.405737+00:00"
content_hash: "55c54027bc36a51ed5993abca413d350091ea52a8dc02c2d7807353dbca4f6c0"
---

# Make an access token

Access tokens created in the Polaris UI can be used for authentication with Polaris APIs, and for automation using the Bridge CLI, and for connecting MCP-compatible clients to the Issue Management MCP server. Tokens can only be made by using the web UI.

Note: You select how long an access token remains valid when you create it. Access tokens will also expire if unused for 30 days.

Alternatively, Organization Administrators can create service account tokens. See [Service Accounts for Polaris](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/d9540d417e952b4580e8f0dd120ba6de.topic) for more information.

To create an access token, follow these steps:

1. In Polaris, click your profile name, then select Account.
2. Click Access Tokens.
3. Click Create New Token.

   [image: A screenshot showing the Access Tokens page and the Create New token button.]
4. Enter a name for the token in the Token Name field (limit is 255 characters).

   [image: Screenshot of the form for creating a new token.]
5. Select an expiration period for the token using the Expiration dropdown.

   You can select 7 days, 30 days, 60 days, 90 days, 365 days, Custom, or No expiration. The default is 365 days.

   If you select Custom, an Expiration Date date picker appears. Select the date on which you want the token to expire. Custom expiration dates cannot be more than two years from the current date.

   Important: Regardless of the expiration option you select, tokens automatically expire after 30 days of inactivity.
6. Click Save.
7. Copy the token and store it in a safe place.

   [image: A screenshot showing the result of making a new token. The token can be copied immediately to your clipboard by using the copy button.]   

   Note: You only get one chance to copy the token. If it is lost, you won't be able to copy it again, but you can make a new one.
