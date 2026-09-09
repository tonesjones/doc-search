---
title: "Findings Overview"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/findings-overview.html"
content_id: "t8PTVJVXa2ScuziondCaWQ"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:00.318183+00:00"
content_hash: "8cf4efd9c240a2c34ad91a57ba5bfcf9c077e674e48c8ddfc742407e96fb4d94"
---

# Findings Overview

The findings page displays all the findings associated with a particular project or
projects, along with all the relevant supporting data.

Click the Findings icon in the navigation bar to open the Findings page.

[image: image]

You can generate a report of the findings by clicking the Generate Report button.

## Findings View Options

The Findings page provides a variety of information and project options, as detailed
below. You can customize what information is displayed by using the Configure
Columns and View buttons or clicking the column headings.

- Click Configure Columns to select which columns to display. Click to add or
  remove checkmarks.

  [image: image]
- Click View to select which findings to display. Use the toggles to display
  or hide information.

  [image: image]

  The viewing options are as follows:
  - Hide archived results.
  - Hide findings marked as "Gone."
  - Hide findings marked as "Fixed."
  - Hide findings marked as "Mitigated."
  - Hide findings marked as "Ignored."
  - Hide findings marked as "False Positive."

    The purpose of
    "hiding" or "un-hiding" findings is to exclude or include
    the associated findings from the Findings page. The
    "completed" triage statuses in these options are "Gone,"
    "Fixed," "Mitigated," "False Positive," and "Ignored." When
    turned ON, each setting will cause the findings marked with
    the particular triage status to be excluded from the page.
    This affects the table, filters, and counts throughout the
    Findings page. When turned OFF, the findings associated with
    that status will be included on the page. The default
    setting is ON.
- Click the column heading to re-sort the list.

### Findings List

The Findings page displays all the findings from the project analysis and
provides analysis data as well as links to additional information.

[image: image]

The analysis data is displayed in columns and includes the following information:

- **Severity** (icon). Displays the findings severity level.
- **Policy violation** (icon). Indicates a policy has been
  violated.
- **ID.** The ID of the finding.
- **Project** (displayed when viewing a list of findings for all
  projects). The name of the associated project. Click the link to open
  the Findings page for that specific project.
- **Type.** The finding type. Click the link to view details for that
  specific finding.
- **Tool.** The tool used to discover the finding.
- **CWE.** The finding's CWE data.
- **Location.** The location of the finding.
- **Finding Status.** The current status of the finding.
- **Triage Status.** The current triage status for the finding.
- **Triage Request Age.** The number of days since a triage approval was requested for the finding.
- **Assignee.** The person assigned to the finding.
- **Predicted Status.** Indicates the "predicted" status based on
  existing machine learning configuration settings.
- **Tags.** Any associated tags.
- **Fix By.** The fix-by date.
- **Attachments (icon).** Shows if there are any attachments (files)
  attached to the finding.

### Using Search/Display Filters

Filters allow you to determine which findings to display and provide information
about that subset of findings.

[image: image]

For more information on filters, see Searching Using Filters.

## Additional Findings Options

The process of generating and viewing finding data involves a variety of tasks. For
more information, see the following:

- Searching for Findings.
- Working with Filters.
- CWE Support.
- Performing Bulk
  Operations.
- Findings Table.
- Analysis Inputs List.
- Adding Manual Results.
- Using Machine Learning with Project
  Findings.
