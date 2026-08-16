---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "orDypdxON5_M4Vav0ZQt5A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:48.657443+00:00"
---

# Description

The `cov-blame` command computes the automatic ownership assignments
based on SCM (source code management) history and owner assignment rules. The SCM
history consists of when, where, and by whom the code was changed and the ownership
rules derive the owner of an issue based on the SCM history.

This command requires that source files remain in their usual locations in the
checked-out source tree. If the files are copied to a new location after checkout, the
SCM query will not work.

There are two main use cases for this command:

1. **`cov-blame` is automatically called
   for owner assignment as part of the commit process.**

   In this case, `cov-commit-defects` automatically calls
   `cov-blame` based on owner assignment rules provided to
   the Coverity Connect UI. `cov-commit-defects` invokes
   `cov-blame` to compute the ownership assignments. If
   the rule assigned to the stream requires SCM data,
   `cov-blame` first attempts to retrieve SCM data for
   files related to defects from the intermediate directory. If SCM data has
   not been imported to the intermediate directory, the command can directly
   query the SCM for the relevant history data using the
   `--scm*` options defined in
   `cov-commit-defects`. The assigned owners (SCM users)
   are then written back into the intermediate directory.
   `cov-commit-defects` then picks up the ownership
   assignment files and Coverity Connect sets the owner accordingly in the
   triage pane.
2. **`cov-blame` is manually invoked to
   test and compare ownership rules.**

   You can invoke `cov-blame` to produce a report of owner
   assignments for defects to help you accomplish the following:
   - Verify, before you commit, that the automatic ownership is producing the proper/expected
     assignments. You can specify one or more owner assignment rules
     through the `--owner-assignment-rules` option for
     comparison.
   - To compare automatic owner assignment to the owners that are
     already defined in Coverity Connect. In this way, you can see
     how successful an owner assignment rule would have been for
     historical defects that have already been manually assigned in
     Coverity Connect.

   Before you run `cov-blame`, you must have a have an existing preview report
   or generate one using `cov-commit-defects --preview-report-v2`.
   You may also generate the report using `cov-commit-defects
   --preview-report-v3`.
