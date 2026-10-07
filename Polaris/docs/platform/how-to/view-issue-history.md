---
title: "View issue history"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/view-issue-history.html"
content_id: "snUr2rgonifA7R2LtEVdlQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:19.793926+00:00"
content_hash: "904d7890a9fcf597016d843b8195060fb136a146f6b986303cb9cc2801dc0171"
---

# View issue history

You can view triage and detection history for issues in your projects and tests.

There's more than one place where you can find issue history in Polaris. The Issues tab (Portfolio, select an application, select a project, and open the Issues tab) is used in this example, but you can view issue history wherever the issues table appears.

Note: Triage history is not branch-specific. All of the triage events for an issue (across branches in the same project) are shown.

1. Select an issue with the checkbox on the left side of the table.

   Note: Issue history does not appear when you select multiple issues.
2. Click Triage Selected or (if you only have observer access to the application) View Issue History.

   The Issue History panel appears with Triage information displayed.

   [image: triage history]

   The triage timeline displays up to four of an issue's most recent triage events. Each triage event can include any of the following:

   - An issue's triage status changes.
   - An issue's owner changes.
   - A comment is added to an issue.
   - An issue's fix-by date changes.
   - An issue's severity changes.
   - An issue's bug tracking ID changes.
   - An AI-assisted triage suggestion is accepted or rejected. Entries for accepted suggestions include the classification (such as Bug, False Positive, or Intentional) and confidence level of the suggestion.
   - Polaris closes (or attempts to close) the ticket linked to the issue in an external issue tracker. See [Issue tracking integrations](issue-tracking-integrations.md) for more information.
   - A triage status change in Polaris affects the status of a ticket in an external issue tracker, or vice versa.
   - A fix-by date in Polaris is synchronized with the due date on a linked Azure DevOps, Jira, or ServiceNow ticket, or vice versa. Fix-by date synchronization is not available for GitHub Issues or GitLab Issues.
   - Synchronizing statuses between an external issue tracker and Polaris fails. The reason for the failure is included in the event; for example, an expired token or a workflow restriction.

   Note: Triage status and fix-by date synchronization events only appear in triage history if those features are configured in the project's integration options. See Automatically close tickets and synchronize triage statuses for more information.

   Select Show More + (near the bottom of the panel) to load up to 100 more triage events.

   Note:

   **Triage events imported from third-parties.** Triage events imported from third-party tools (by running external analysis tests) appear in the timeline with the text `Imported from` followed by the tool name; for example, `Imported from Black Duck SCA` indicates the event was imported from the Black Duck® SCA tool.

   Imported triage events are attributed to external users if the third-party tool provides this information. An external username is followed by the text `(Imported)`. `Imported by System` indicates that the triage event could not be attributed to an external user. For more information about this feature, see [Import results from third-party tools (limited availability)](import-results-from-third-party-tools-limited-availability.md).
3. To view the issue's detection history, select Detection.

   [image: detection history]   

   Earlier detection events appear near the top of the list. There are three types of detection events:

   - First detected: The first test of the branch in which the issue was detected.
   - Absent: A test in which an issue is no longer detected.
   - Re-detected: A test in which an absent issue is detected again.

   Note: Detection history is branch-specific. Detection events for the same issue can vary between branches.

   Note: Detection events are only added to the list when an issue's detection status changes. For example, if an issue is absent in three consecutive tests, only one absent event appears in the issue's detection history—with completed date and time of the earliest test.
