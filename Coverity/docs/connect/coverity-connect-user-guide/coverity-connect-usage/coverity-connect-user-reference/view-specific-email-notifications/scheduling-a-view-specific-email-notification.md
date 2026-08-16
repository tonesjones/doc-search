---
title: "Scheduling a view-specific Email notification"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scheduling-a-view-specific-email-notification.html"
content_id: "P2tV1DnajyFOBl1Mjd72TA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:36.777479+00:00"
---

# Scheduling a view-specific Email notification

Once you have configured your view with the appropriate filters, you can schedule a
periodic email notification by completing the steps below. You can only configure email
notifications on views that you own. If you would like to set up notifications on a view
that has been shared with you, duplicate the
view and configure the notification on the duplicate.

Note: If an email notification is created for a Dashboard of an
Hierarchy, the email will contain a graphic showing all of
the reports on the dashboard. If the email notification is for a specific report within
Hierarchies, then the single graphic for that report will
show in the email.

Table 1. Notification dialogs

|  |  |  |
| --- | --- | --- |
| [image: image] | [image: image] | [image: image] |

1. Open the View menu and select
   Notification.
2. To send notifications for this view, select On.
3. On the Schedule tab, choose the days and the time
   notifications are sent. Notifications can be sent daily, and must be scheduled
   at least once a week. If the view does not include any issues at the scheduled
   time, no email is sent.

   Note: Time should be entered in 24-hour format (5:00pm = 17:00)
4. Select Send email when a new snapshot is created to send
   an email when a commit of analysis data is completed.
5. Click Send email now to send the email report
   immediately.
6. On the Recipients tab, enter additional
   Users and Groups to receive
   the notification. The view owner is automatically included. They must be
   currently registered in Coverity Connect.

   Note: Disabled users and those with no associated email address will not receive
   notifications. Any notifications owned by a disabled user will not be
   sent.
7. In the CC and Reply To boxes, enter
   email addresses for users or mailing lists as needed. These users do not need to
   be registered users in Coverity Connect.
8. On the Projects or Hierarchies tab
   (depending on which part of Coverity Connect the dialog is accessed from), enter
   the project or hierarchy whose issues are included in the email. If you uncheck
   Restrict issues emailed to the following projects:,
   the notification will be active for all of your projects.

Notification emails will contain up to a maximum of 100 issues by default. This level can
be customized by your Coverity Connect administrator.

Each recipient may receive a different set of issues in the notification, relative to
his/her permissions, and the use of the relative
user filter. To receive an unfiltered version of the email notification,
enter the user's email in the CC field.
