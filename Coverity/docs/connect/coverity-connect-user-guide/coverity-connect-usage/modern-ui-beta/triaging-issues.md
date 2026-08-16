---
title: "Triaging issues"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/triaging-issues.html"
content_id: "kDbcukLU6LytuRMDWJmfyQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:02.175837+00:00"
---

# Triaging issues

Issue triage is the process of reviewing, classifying, and assigning issues found by
Coverity analysis. The modern UI provides a streamlined workflow for
triaging issues. For details about the pages and controls used in this workflow, see
Navigation and features.

The triage workflow follows these steps:

1. **Select a project.** On the Projects page, click a project name to view its
   issues.
2. **Find the issues to triage.** On the Issues page, use views, filters, and sorting to
   locate relevant issues. You can apply a predefined view, add filters to narrow
   the list by any column value, or sort by any column.
3. **Review the issue.** Click a CID to open the issue detail view. Examine the
   source code and event path to understand the issue. Use the CWE link and issue
   description to determine the nature of the defect.
   - **Source browser scope:** The source browser in the modern UI displays events for the
     currently selected issue only. In the classic UI, the source browser
     displays events for all issues present in the file. This change improves
     performance.
4. **Set triage attributes.** In the Triage pane, set the appropriate values for
   each attribute:
   - **Classification** — Categorize the issue (for example, Bug, False
     Positive, Intentional).
   - **Severity** — Set the priority level (for example, Major, Minor,
     Unspecified).
   - **Action** — Specify the required response (for example, Fix Required,
     Ignore, Modeling Required, Undecided).
   - **Owner** — Assign the issue to the appropriate person.
   - **Comments** — Add context about the triage decision for future
     reference.
5. **Review context.** Before saving, review the Detection History, Triage
   History, and Occurrences sections to understand the full picture of the
   issue.
6. **Save and continue.** Click Apply to save your triage
   changes, or click Apply + Next to save and move to the
   next issue.

**Bulk triage**

To triage multiple issues at once, select the checkboxes next to each CID on the Issues
page, then click the Triage button that appears. Set the
desired triage attributes in the triage controls, then click
Apply to save your changes to all selected issues.

If the AI-Assisted Triage Plug-in is enabled for the project, the modern UI can suggest triage
attribute values to help you triage faster. For details, see AI-Assisted Triage Plug-in (beta).

Note: Bulk triage and
AI-assisted bulk triage are not available for project views created under **issues:
project scope**.

For comprehensive triage documentation, including features available in the classic
interface, see Triaging issues, Managing issues,
and Finding issues.
