---
title: "Assign subscriptions to applications"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/assign-subscriptions-to-applications.html"
content_id: "aG92uiiOD7zZggzZovN8_w"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:50.850678+00:00"
content_hash: "cf48375d3c08f0af381ec9c8986bb903b46f279571161a2ed3763f5e55d3b615"
---

# Assign subscriptions to applications

Organization Administrators and Organization Application Managers can add subscriptions to preexisting applications, and replace application subscriptions with concurrent (team member) subscriptions.

## Update an application's subscriptions

To update an application's subscriptions, follow these steps:

1. Go to Portfolio and select the application you wish to modify.
2. Go to Settings > Subscriptions.

   Note: The Subscriptions tab is context-sensitive. The options on this tab vary depending on the subscriptions available in your organization.
3. Select [image: icon edit pencil] Edit.
4. Make changes, as required. You can:

   | Action | Description |
   | --- | --- |
   | Add a DAST, SAST, SCA, External Analysis, and/or Binary subscription to the application | If you haven't already assigned a subscription to the application, you can do so. Subscriptions:  - DAST. - Concurrent (team member) - the only subscription type that can include Binary. - Applications - individual SAST, SCA (Package Manager or Signature Analysis), and/or External Analysis. After a subscription is assigned to an application, you cannot change or remove it (but you may be able to replace application subscriptions with concurrent subscriptions, described below). |
   | Replace application subscriptions with concurrent (team member) subscriptions | If application and concurrent subscriptions are available in your organization, you can replace application subscriptions with concurrent subscriptions. Important: You cannot replace an application's concurrent subscriptions with application subscriptions. |
5. Select Save.

   A notification appears.
6. Select OK to confirm your changes.

## Update the subscriptions assigned to multiple applications

Organization Administrators can update the subscriptions assigned to multiple applications at the same time.

To assign a subscription to multiple applications at the same time, follow these steps:

1. Go to My Organization > Subscriptions.
2. Select a DAST or application subscription.

   Tip: A list of applications the subscription is assigned to appears under Applications. Any changes you make in later steps will affect all the applications listed in the table.
3. Under Applications, select Edit Subscriptions.

   The Edit Subscriptions button only appears when you can make changes. When selected, the Move Applications window opens.
4. Make changes, as required. You can:

   | Action | Description |
   | --- | --- |
   | Add a DAST, SAST, SCA, External Analysis, and/or Binary subscription to the application | If none of the applications are assigned subscriptions, you can do so. Subscriptions:  - DAST. - Concurrent (team member) - the only subscription type that can include Binary. - Applications - individual SAST, SCA (Package Manager or Signature Analysis), and/or External Analysis. After you assign one or more subscriptions to applications, you cannot change or remove them (but you may be able to replace application subscriptions with concurrent subscriptions, described below). |
   | Replace application subscriptions with concurrent (team member) subscriptions | If all the applications use the same application subscription (and application and concurrent subscriptions are available in your organization), you can replace application subscriptions with concurrent subscriptions. Important: You cannot replace concurrent subscriptions with application subscriptions. |
5. Select Save.

   A notification appears.
6. Select OK to confirm your changes.
