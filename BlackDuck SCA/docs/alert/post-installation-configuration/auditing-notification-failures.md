---
title: "Auditing Notification Failures"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/auditing-notification-failures.html"
content_id: "TPVU0CNYSgA1_IEiI~K81g"
version: "8.4.0"
section: "Post Installation Configuration"
scraped_at: "2026-08-08T23:46:37.876154+00:00"
---

# Auditing Notification Failures

The **Audit Failures** page lists event notifications that were not sent. You can use
this page to audit notification activity and to resend notifications if necessary.

## About auditing in Alert

- Click an item in the list for detailed information about an event. To resend
  an event, click the refresh icon in the far right column.
- When re-sending a notification, Alert verifies that the notifications match a
  configured job, and highlights the notifications that did not match a job
  and shows an error.

  - When resending, notifications are sent to all jobs in the
    Distribution Jobs tab. For each job, the notification is sent if it
    matches the distribution job filter criteria.
  - If the filter criteria for the job has changed since the audit
    message was viewed, then resending does not work because the
    notification no longer matches the filter criteria of the
    job.

For notifications matching multiple Jobs, Alert displays the jobs that the
notifications matched. Each job displays its own status and timestamps for last
sent.

All failed provider notifications display in the **Audit Failures** table.

## Viewing the audit table

To access the **Audit Failures** table, click **Audit Failures** in the left
navigation panel.

Figure 1. Alert Failure table
[image: Alert Failure Table]

The **Audit Failures** table displays the following information for each event.
You can sort the table using any of the column headings.

- **Provider** Black Duck
- **Notification Type** Double-clicking the notification type displays the
  notification details.
- **Time Retrieved** Time when the data was retrieved from Black Duck.
- **Last Sent** Time when the notification was last attempted to be sent.
- **Failed Jobs** Count of failed notification jobs.
- **View** Opens a pop-up with failure details.
- **Refresh** Refreshes the job status.

To resend an event, click the refresh icon that corresponds with the specific event
row in the far right column.

You can click the **View** icon for each entry in the **Audit Failure** table
to see additional details.

Tip: When an audit failure is appearing in the **Audit Failure**
table, users can click the 'View' icon beside the entry, to show the amount of
failing jobs within that row.

Clicking the **View** icon in the **Audit Failure** table provides the
following display options.

- **Distribution Jobs:** (Default view) This tab displays the list of jobs
  that distributed the notification.

  - You can resend a distribution job notification by selecting the
    **Refresh** icon next to the job.

Figure 2. Alert Failure details
[image: Alert Failure details]

- **Notification Content:** This tab displays the notification details
  configured by the distribution job and sent in the notification.

Figure 3. Alert Failure notification content
[image: Alert Failure notification content]
