---
title: "Desktop Analysis usage tracking"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/desktop-analysis-usage-tracking.html"
content_id: "Smb_7Z6a0UGsC9yPXXZmyQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:01.630813+00:00"
---

# Desktop Analysis usage tracking

Defects that are first discovered by Desktop Analysis have their "First Detected By"
attribute set to *Preview*. Defects found through other means will have different
values for this attribute (*Snapshot* or *API*, for example). This distinction
allows you to specifically track the number of defects discovered by Desktop Analysis.
To do so, complete the following steps:

1. Log in to Coverity Connect.
2. Make sure you have the correct project open, and navigate to an Issues: Project
   Scope view ("All In Project" for example).
3. Click the "gear" icon to edit the view settings, and open the Columns
   tab.
4. Enable the First Detected By and First
   Snapshot columns.
5. Open the Filters tab, and click to open the First Detected
   By filter.
6. Check the box for Preview. This will filter all of the defects in the
   project to display only those *first* found by Desktop Analysis.

Once the view has been filtered, note in particular the First
Snapshot column. This displays the snapshot when this CID was first
committed to Coverity Connect. If this column is blank, that means that the defect was
found by `cov-run-desktop` and not yet committed to Coverity Connect
(this could be because the defect was fixed immediately after being discovered by
Desktop Analysis, or simply because it was discovered very recently and has yet to be
committed).

Note: When `cov-run-desktop` finds a new defect, it assigns it a CID and sets its
owner to the current user. However, defect occurrence information is only communicated
to Coverity Connect when the CID is committed with
`cov-commit-defects`. This means that when you attempt to open a defect
in Coverity Connect that has not yet been committed, you will see an error explaining
that "No further information for this CID exists on Coverity Connect."
