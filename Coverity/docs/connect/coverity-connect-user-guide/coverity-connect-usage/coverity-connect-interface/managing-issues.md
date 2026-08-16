---
title: "Managing issues"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/managing-issues.html"
content_id: "DSMO0duOOoRg7uFbTVofrw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:46:56.802906+00:00"
---

# Managing issues

Once you find and select a CID that is important to you (see Finding issues),
the Coverity Connect Source pane shows you where the issue occurs
in the source code and adds inline details to help you understand and address it. The
example in Figure 1 shows CID 10324 in both
Coverity Connect panes.

Figure 1. List of CIDs (upper pane) and Source pane (lower pane)
  
 [image: image]

In addition to inline commentary, the source code can include the icons described in
Table 1.

Table 1. Issue markers

| Marker | Description |
| --- | --- |
| [image: image] | Issue main event. |
| [image: image] | Multiple main events that occur on the same line. |
| [image: image] | Path event. |

For some issues, the Source pane provides a More info link to detailed
remediation advice and reference material. For example, all issues pertaining to web
application security provide this documentation (which is also available from the "Security reference" section in the Coverity 2026.6.0 Checker Reference). To supplement the inline comments and remediation
advice, Coverity Connect also provides closely related reference material, including
CWE and
checker documentation, to help
you understand and address the issue. Links to this information are provided in the top
of the triage pane (right pane).

Note: You can use the red or green bars located to the right of the vertical scroll bar to
quickly jump to the issue-related events in the source code. Coverity Connect allows you
to adjust the size of the panes in your browser. You can also show and hide the Triage
pane and the pane that contains the View types and dashboards.

You can use the icons
located between the View pane and the Source pane to control the display of
information and line numbers in the source code and to view the directory structure
in which the selected source file resides. To obtain descriptions of the icons, you
can mouse over them in Coverity Connect.

Data in the View pane can link to the
issues to which the data pertains. For example, see the links in Figure 1.
