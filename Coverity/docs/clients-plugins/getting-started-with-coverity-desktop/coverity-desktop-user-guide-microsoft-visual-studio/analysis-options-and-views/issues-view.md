---
title: "Issues view"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/issues-view.html"
content_id: "Sv6Yf6KtvzlhYzPFenZ7Uw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:49:25.446594+00:00"
---

# Issues view

The Issues view displays in one of two modes:

- Local Issues mode displays the results of a local analysis.
  Note that the following screenshot shows the Local Issues mode
  with the "Show missing issues" option
  enabled.

  Figure 1. Local Issues mode
  [image: image]
- Remote Issues mode displays issues retrieved from the Coverity Connect server.

  Figure 2. Remote Issues mode
  [image: image]

If the Issues view is not open, select Coverity > Windows > Issues.

After running a local analysis or retrieving remote issues, the
Issues view displays a list of the returned issues. It is
possible that the list may be too large for you to effectively manage, or you might want
to organize your issues in a manner that makes sense for your particular task. For
example, you might want to list only the critical and open issues that are assigned to
you. You can use filtering and sorting in the Issues view to focus the scope of
your issues.

Each of the Issues view controls is described in the following table.

Table 1. Issues view buttons

| Button | Name | Action |
| --- | --- | --- |
| [image: image] | Refresh | Retrieves the data for the current page of issues and configuration information from the Coverity Connect server. Refresh is not available in Local Issues mode. |
| [image: image] | Re-run Analysis | Runs a local analysis using the same scope and options as the most recently completed analysis. You can use this to verify that your changes have fixed existing issues, and have not introduced any new issues. |
| [image: image] | Show/Hide missing issues | When enabled ("showing" missing issues), issues that exist in the reference stream but are missing in the latest local analysis will be displayed with a strike-through font, and no triage information. Additionally, any issues that were newly discovered by local analysis will be displayed in bold. Issues that exist both locally and in the reference stream will remain in plain font. See Local Issues mode for an example. When disabled ("hiding"), any issues that are missing from local analysis will not be displayed, and all existing issues will be displayed in plain font.  This option is not available in Offline mode. |

After you select a manageable number of issues to view, double-click
on an issue to open it in the editor.

When you open an issue, the source code file that contains the issue opens in the source
editor to the location where the issue occurs, placing markers that correspond to
relevant lines. Additionally, opening an issue loads the current triage information for
the issue in the Details view.
