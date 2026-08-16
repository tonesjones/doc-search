---
title: "Viewing issues in a project"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/viewing-issues-in-a-project.html"
content_id: "YZht9grkbZzgvbYXFgsZuA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:15:01.430346+00:00"
---

# Viewing issues in a project

Black Duck provides information on the issues associated with a project
version as monitored by an issue tracking system. Currently, this feature is supported
using Black Duck Alert 6.2.0 and later.

Black Duck displays an **Issues** link in the project version header
for a project version if an issue tracking system was configured to the Black Duck project version using Black Duck Alert. Once Black Duck Alert
creates issues for this project version, the link appears. No additional configuration
is needed.

  
 [image: Issues in Header]   

Note that the **Issues** link does not appear if there are no issues or all issues
have been deleted.

Users with the Global Project Administrator, Global Project Manager roles and all project members (users assigned to the
project) can select the issues value to display the Issue Management table.

  
 [image: Issues Management dialog box]   

This table lists the issues created in the external issue tracking systems. You can then
use this table to see the status of the issue in your workflow.

The table provides the following information for each issue:

| Column | Description |
| --- | --- |
| Component | Component name and version affected by this ticket. |
| ID | Issue identifier. |
| Summary | Summary of the external issue. |
| Assignee | User assigned to this ticket. |
| Status | Status of the ticket. |
| Updated | Time when this ticket was last updated. |

Note that this table does not display all changes from the external issue tracker system.
Changes to the issue, such as manual changes to the description, will not be reflected
in the Black Duck issue table other than those changes made automatically to the issue
by Black Duck Alert.
