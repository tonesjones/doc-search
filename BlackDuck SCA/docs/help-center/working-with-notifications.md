---
title: "Working with notifications"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/working-with-notifications.html"
content_id: "7PGdCQouS0ohfX1PoPhzXA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:23.909208+00:00"
---

# Working with notifications

HUB-2824, 5518, 6547, 6388, 8018, 6963 Notifications
appear in Black Duck on the components in projects in which you are a member or group
member – your watched projects.

Notifications alert you when:

- Security vulnerabilities are published or updated against components that are
  included in one or more of your projects.
- Estimated
  Security Risks that have been added or removed from components
  without a version.
- Actions you perform affect the vulnerabilities in BOM components, such as:

  - Editing, adding, or removing components which have
    vulnerabilities.
  - Unmapping a scan from a project.
  - Rescanning code or a Docker image.
  - Ignoring or no longer ignoring a component.
  - Modifying file(s) so that they are matched to a different
    component.
- Components have violated a policy.
- Policy violations have been overridden.
- Components no longer violate a policy.
- You are approaching or are exceeding your code size
  limit.

Tip: You can remove projects you are watching so that you do not receive notifications
for those projects or components in those projects.

## Viewing notifications

1. Open the notifications list by selecting [image: image] .
2. To manage the notifications, select **See All Notifications** located at
   the bottom of the list.

## Filtering notifications

By default, the Notifications page is filtered. To further refine your search, select from the
following options:

- **Created**: See all notifications created in a specified timeframe, such as Today, Past
  three days, Past week, and Past month.
- **Notification State**: Filter notifications based on their current state, such as New,
  Seen, Visited, or Hidden. Please note that the Seen and Visited filters
  currently share the same behavior.
- **Notification Type**: Display notifications based on their type, such as Component with
  Unknown Version, Rule Violation, Policy Override, Vulnerability, Project,
  Project Version, License Limit, or Rule Violation Cleared.

Note: If no options are selected for the Notification State or Notification Type filters, they
default to including all options.

## Viewing more information

To view more information on security vulnerabilities and BOM component
adjustments:

1. Open the Notifications page by selecting [image: image] and select **See
   All Notifications**.
   - Select a component version to open the **Security** tab of the Black Duck KB
     component version page.
   - Select a vulnerability record (such as CVE-2017-1234) to view the
     vulnerability details page for that security vulnerability.

To view more information on policy violations and overrides:

1. Open the Notifications page by selecting [image: image] and select
   **See All Notifications**.
2. Select a policy violation or a policy violation override to open the BOM
   page.

   Users with the appropriate role can override a policy violation or remove a policy violation that was overridden.

To view more information on code limits:

The notification automatically appears at the top of the page when you are close to
exceeding your code size
limits:

  
 [image: image]   

1. Open the notifications list by selecting [image: image] .
2. Select **See All Notifications** located at the bottom of the list.
3. To upgrade your code limit, contact Customer Support.

## Hiding notifications

You can hide notifications so that they no longer appear in the drop-down list and appeared
grayed out on the Notifications page.

1. Open the notifications list by selecting [image: image] .
2. Select **See All Notifications** located at the bottom of the list to display the
   Notification page.
3. Click [image: Hide icon] located at the end of the notification's row. Conversely, click
   [image: Unhide icon] to unhide a hidden notification.

## Internal SSL certificate expiration alert

The internal SSL certificate expiration alert notifies users when their SSL
certificates are approaching their expiration date. This proactive alert system
notifies users 30 days in advance, ensuring timely renewals and uninterrupted secure
connections.

The internal SSL certificate expiration alert is automatically enabled within the
application. Users will receive notifications through the application interface or
via configured alert channels as the expiration date approaches.
