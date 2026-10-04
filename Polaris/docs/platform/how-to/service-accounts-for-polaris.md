---
title: "Service accounts for Polaris"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/service-accounts-for-polaris.html"
content_id: "qbkoKTy~Lp0M8O5AZeqgtw"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:18.430756+00:00"
content_hash: "aeaa3ed2936d37fefe8fc48832d70c2451754fe2838680f0051ea84f411c9775"
---

# Service accounts for Polaris

Learn how to create and manage service accounts for Polaris from the Polaris user interface.

Service accounts are a type of account used to perform automated tasks on behalf of a user or application. They are typically used in scenarios where a user is not present to provide authentication, such as in CI/CD pipelines or automated scripts.

Service accounts have their own set of credentials (access tokens) that can be used for authentication.

In Polaris, service accounts are managed by Organization Administrators, who can create, update, regenerate, and delete service accounts as needed.

Tip: Instead of using the Polaris user interface, you can manage service accounts with APIs. See [Service Accounts for Polaris](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/d9540d417e952b4580e8f0dd120ba6de.topic) for more information.

## Service account token expiration

When you create a service account, you select how long its access token remains valid. You can select a preset period of 7, 30, 60, 90, or 365 days, select a custom expiration date up to two years in the future, or select No expiration. The default is 365 days.

Important: Regardless of the expiration option you select, service account tokens automatically expire after 30 days of inactivity.

You can change a service account's expiration period at any time by editing the service account. Changing the expiration period regenerates the access token, which invalidates the existing token immediately, so plan to update any automated process that uses it.

To ensure your automated processes continue to function without interruption, change a service account's expiration period before its access token expires. If a service account token expires in seven days or less, the Service Accounts page displays a countdown of the number of days remaining until token expiry and a link to regenerate.

[image: The Service Accounts page showing one expired token and one token with 4 days remaining.]

## Monitor service account usage

Organization Administrators can monitor service account activity on the Audit Logs page (My Organization > Audit Logs). When an action is performed using a service account token, the service account's friendly name appears in the Token Name column. Additionally, audit logs record when a service account's access token is regenerated, when its expiration period is changed, and when an organization- or application-level role is assigned or unassigned.

Select Service Account Tokens using the Event Type dropdown to view events related to service accounts.

## Using service account tokens

Service account access tokens function identically to user access tokens for authentication purposes. After you create a service account, you can use the service account's access token for:

- Authentication in requests made to Polaris APIs.
- Authentication in CI pipelines that use the Bridge CLI (and Black Duck Security Scan plugins).

Note: Service account tokens can be used wherever access tokens are used.
