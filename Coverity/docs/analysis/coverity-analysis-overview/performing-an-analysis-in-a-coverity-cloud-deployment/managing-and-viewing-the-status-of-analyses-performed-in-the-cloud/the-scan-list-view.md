---
title: "The Scan List view"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-scan-list-view.html"
content_id: "Wh3S2mO4OmXbYccTkopw7w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:39.785980+00:00"
---

# The Scan List view

The following sample illustrates a Scan List view, filtered to show all scan jobs for the
user 'admin' and the project 'doc-examples-js':

[image: image]

With no filtering selected, the Scan List view lists all all current and past analysis
scan jobs performed by this Coverity instance. This list provides the following scan job
information:

- **User**: The name of the user who ran the analysis scan job.
- **Project**: The project name.
- **Stream**: The stream
  name.
- **CreatedTime**: The date and time that the scan job was created.
- **Progress %:** The completion status of the scan job, in percent.
- **Status**: The status of the scan job; one of the following:
  - **Queued**: The analysis scan job is queued and is not yet running.
    Further information is not yet available.
  - **Running**: The analysis scan job is running. Refer to the
    Progress.
  - **Completed**: The analysis scan job completed and commited successfully.
    Analysis reports and logs are available.
  - **Failed**: The analysis scan job failed. Check the logs for
    details.
  - **Cancelled**: The scan job was cancelled.
- **Version**: The Coverity version on which the analysis scan job
  is scheduled and run.

Note: If a user, project, or stream is deleted, that user, project, or
stream appears in the Scan List view as '****'.

You can filter the content of the Scan List view list using the Connect UI filter (click
the Gear icon) to show all scan jobs for a specific user, project or stream. For
information on filtering, refer to "Edit
Settings" in the Coverity Platform 2026.6.0 User and Administrator Guide.

Selecting a scan from the list displays further information about that scan in the
**Scan Details** pane in the lower portion of the dashboard. The Scan Details
pane contains the following scan job information, available at a glance:

- **JobId**: The unique ID of the scan job.
- **State**: The status of the analysis; one of the following:
  - **Running**: The analysis is running. Refer to Progress.
  - **Completed**: The analysis completed and commited successfully. Analysis
    reports and logs are available.
  - **Failed**: The analysis failed. If a job fails, download the execution
    log for further information.
  - **Cancelled**: The scan job was cancelled.
- **Progress:** The completion status of the analysis, in percent.
- **CreatedTime**: The date and time that the analysis scan job was created.

If the status of the selected analysis is either Completed or Failed, the Scan Details
pane presents the following downloadable artifacts as generated:

- Analysis output details
- Analyzed intermediate directory
- Comparison report
- Execution logs

To refresh the Scan List view, click the refresh [image: image] button.
