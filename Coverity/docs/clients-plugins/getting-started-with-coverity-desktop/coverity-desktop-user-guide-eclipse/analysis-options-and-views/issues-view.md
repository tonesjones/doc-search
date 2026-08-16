---
title: "Issues view"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/issues-view.html"
content_id: "zRPUXdFOt5Px~tgmyPn31g"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:54.013606+00:00"
---

# Issues view

The Issues view displays in one of two modes:

- Local Issues mode displays the results of a local analysis.

  Figure 1. Local Issues mode
  [image: image]
- Remote Issues mode displays issues retrieved from the Coverity Connect server.

  Figure 2. Remote Issues mode
  [image: image]

If the Issues view is not open, select Coverity > Show View > Issues.

After running a local analysis or retrieving remote issues, the
Issues view displays a list of the returned issues. It is
possible that the list may be too large for you to effectively manage, or you might want
to organize your issues in a manner that makes sense for your particular task. For
example, you might want to list only the critical and open issues that are assigned to
you.

Each of the Issues view controls is described in the following table.

Table 1. Issues view buttons

| Button | Name | Action |
| --- | --- | --- |
| [image: image] | Filter | Opens the Issue Filters screen. The edit filters link, located within the Filter drop-down menu, also opens the Issue Filters screen. See Issue filters. |
| [image: image] | View Menu | Allows you to sort and configure the display of the issue listing. See Configuring the Issues view display. |
| [image: image] | Re-run Analysis | Runs a local analysis using the same scope and options as the most recently completed analysis. You can use this to verify that your changes have fixed existing issues, and have not introduced any new issues. |

After you select a manageable number of issues to view, double-click
on an issue to open it in the editor.

When you open an issue, the source code file that contains the issue opens in the source
editor to the location where the issue occurs, placing markers that correspond to
relevant lines. Additionally, opening an issue loads the current triage information for
the issue in the Details view.

To close the issue and remove the markers, click
Close in the Details view.
