---
title: "AI-assisted triage (limited availability)"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/ai-assisted-triage-limited-availability-.html"
content_id: "aK~t1Od4NNuS0Wjff2sQWg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:16.610677+00:00"
content_hash: "ce1df02f6b50c026f97a55cda99e2a048fad3607e50dcbac0900ed4a1365c826"
---

# AI-assisted triage (limited availability)

Use AI to get triage suggestions on issues with your SAST projects. Manually accept or reject automated suggestions, and use filters to display triaged issues based on their status or the confidence level of the AI assessment.

## Introduction

Polaris enables you to use AI-assisted triaging with issues found on SAST projects. This can be done on up to 20 issues at a time. The Black Duck LLM is used to assess the selected issues and provide recommendations, each of which are given a confidence rating. You can examine the AI-generated suggestions and either accept or reject them as needed. Each accepted suggestion initiates the standard approval workflow for the project. Canceling an ongoing AI triage job will stop incomplete triages on that job, but any completed triages in the job will retain their AI suggestions.

Important: The AI-assisted triage feature is available on request. Please contact Black Duck Support to enable this feature for your organization. After it's enabled, an org admin needs to activate the feature for your organization. You can also control whether AI triage is available to specific applications and projects, as needed.

Please note, AI-assisted triage:

- Requires a minimum Coverity version of 2026.6.0. Attempting to use the feature with an earlier version of Coverity will cause an error.
- Is only available on SAST projects during its initial launch.
- Can be used by anyone who has permission to manually triage issues.
- Can only be used on tests that were run after the feature was enabled.
- Can't be used on local scans.
- Can only be performed on tests run in the past 30 days, due to how long source code is retained. You can still accept or reject a triage on scans older than 30 days, but you can't request a new AI-assisted triage if the source code is no longer available.
- Records all accepted or rejected AI suggestions in the relevant issue history.

## Data sent to the LLM

The Polaris AI-assisted triage sends the following data to the LLM endpoint for analysis:

- Issue details such as checker name, merge key, function name, language, type / subtype, and all events in the defect trace (event descriptions, event tags, line numbers, and file paths).
- Relevant source code and code context.
- No historical triage data or version control information is sent to the LLM.

Important: Source code context from file mappings is transmitted to the configured LLM endpoint. Verify that the LLM endpoint meets your organization's security and data handling requirements before you enable the service.

## Suggestion confidence levels

The maximum confidence that an AI-assisted triage suggestion can have depends on the following:

| Confidence | Issue description |
| --- | --- |
| High | - Hardcoded secret. - C or C++ issue found by one of the 10 checkers that were added in Coverity 2026.3.0 (see list below). |
| Medium | C or C++ issue found by a checker other than the 10 listed below. |
| Low | Any scenario not covered by high or medium confidence. |

The 10 checkers capable of returning an AI triage suggestion with high confidence are:

- `DEADCODE`
- `FORWARD_NULL`
- `MISSING_LOCK`
- `NULL_FIELD`
- `NULL_RETURNS`
- `OVERRUN`
- `RESOURCE_LEAK`
- `UNCAUGHT_EXCEPT`
- `UNINIT`
- `UNINIT_CTOR`

Note: As this feature continues to be developed, higher confidence levels will be achievable with a wider range of checkers and code languages.

## Enable or disable AI-assisted triage for your organization

If you've successfully requested access to the AI triage feature, you can enable or disable it across your organization. Doing this will change whether the feature is available to all applications and projects in your organization by default, but it can be independently enabled or disabled for applications and projects as needed.

Note: The act of enabling or disabling AI triage for your organization is recorded in the audit log.

To enable or disable AI-assisted triage for your organization, follow these steps:

1. Go to My Organization > Triage.
2. Under AI Triage, select Edit.
3. Select the Allow AI Triage suggestions checkbox.

   Note: Changing this setting will apply the same selection to all applications and projects in your organization, except for any that already have a manually applied AI Triage suggestions setting.
4. Select Save.

AI triage actions and reporting are now available on all affected applications and projects.

## Lock or unlock AI-assisted triage settings for your organization

As an organization admin, you can lock AI triage settings to prevent anyone who isn't an organization admin from making changes to them for applications and projects. This lasts until you decide to unlock the settings.

To lock or unlock AI-assisted triage settings for your organization, follow these steps:

1. Go to My Organization > Triage.
2. Under AI Triage, select Lock section ( [image: Lock icon] ).

   Locking the settings changes the button from an open lock to a closed one ( [image: Unlock icon] ). Select the button again if you want to unlock the settings.

While the settings are locked, only organization admins can change them at the application or project level. Unlocking the settings allows anyone who can access them to change them.

## Enable or disable AI-assisted triage for an application

If you've successfully requested access to the AI triage feature and you want to change the default availability of the feature for a specific application, you can enable or disable it for that application. Doing this will make the feature available to all projects in the application by default, but it can be independently enabled or disabled for projects as needed.

Note: This setting may be locked, in which case only organization admins can change it. Speak to an admin for further information or to have the lock removed.

Important: AI-assisted triage is currently only available for SAST applications.

To enable AI-assisted triage for an application, follow these steps:

1. Go to Portfolio.
2. Select the name of the application you want to configure.
3. Select Settings > Triage.
4. Under AI Triage, select Edit.
5. Select the Allow AI Triage suggestions checkbox.

   Note:

   Changing this setting will apply the same selection to all projects in your application, except for any that already have a manually applied AI Triage suggestions setting.

   Changing the setting will also prevent changes to AI triage at the organization level from affecting this application and its projects.
6. Select Save.

AI triage actions and reporting are now available on the application and affected projects.

The word Modified now appears in the AI Triage setting section for the application. You can remove the override by selecting Reset and confirming the action when prompted.

## Enable or disable AI-assisted triage for a project

If you've successfully requested access to the AI triage feature and you want to change the default availability of the feature for a specific project, you can enable or disable it for that project.

Note: This setting may be locked, in which case only organization admins can change it. Speak to an admin for further information or to have the lock removed.

Important: AI-assisted triage is currently only available for projects in SAST applications.

To enable AI-assisted triage for a project, follow these steps:

1. Go to Portfolio.
2. Select the name of the application containing the project you want to configure.
3. Select the name of the project you want to configure.
4. Select Settings > Triage.
5. Under AI Triage, select Edit.
6. Select the Allow AI Triage suggestions checkbox.

   Note:

   Changing this setting will prevent changes to AI triage at the organization or application level from affecting this project.
7. Select Save.

AI triage actions and reporting are now available on the project.

The word Modified now appears in the AI Triage setting section for the project. You can remove the override by selecting Reset and confirming the action when prompted.

## Run AI triage on project issues

If AI triage is enabled for a SAST project, you can use it to get AI suggestions for triaging issues. This can be done on up to 20 issues at a time, after which a new button appears in the row for each triaged issue. You can use this button to take action based on the AI-generated suggestions for each issue.

Important: AI triage only works on tests that were run after AI-assisted triage was enabled. Due to the 30-day limit on retaining source code, you can't generate new AI triage suggestions for tests that were run more than 30 days ago.

Note: You can't run AI triage on issues that already have an AI triage in progress, or issues that have a pending AI triage suggestion.

To run AI triage on project issues, follow these steps:

1. Go to Portfolio.
2. Select the name of the application containing the project you want to triage.
3. Select the name of the project you want to triage.
4. Select the checkboxes of up to 20 issues.
5. Select Run AI Triage.

   A spinning icon next to the name of an issue indicates that an AI triage is in progress for that issue. When it changes to a star icon, the triage is complete and a suggestion is ready for inspection.

When all selected issues have the star icon next to their names, the AI triage operation is complete. You can then inspect the suggestions individually, and either accept or reject the suggestions—individually, or in bulk.

## Cancel an in-progress AI triage job

If you want to stop an ongoing AI triage job before all issues have been triaged, you can cancel the job. Doing this has the following effects on issues in the job:

- Any in-progress triage is terminated. There might be a brief delay while the request is processed.
- Not-started triages are canceled.
- Completed triages are unaffected, and their AI suggestions are retained.

To cancel an in-progress AI triage job, follow these steps:

1. Select the name of the application containing the project you want to modify.
2. Select the name of the project.
3. Select the checkbox of an issue that is part of the job you want to cancel.
4. If the Triage Selected Issues pane isn't already visible, select Triage 1 Selected.

   The Triage Selected Issues pane appears.
5. Next to the AI Triage In Progress message, select Cancel.

   A confirmation dialog appears.
6. In the dialog, select the cancel button to confirm you want to end the triage.

A request is made to cancel the job and, when that request is fulfilled, all affected issues are updated accordingly. As needed, you can re-triage any issue whose previous AI triage was canceled.

## Filter a project's issues based on AI triage status

To make it easier to work with issues that have been triaged using AI, there are two specific filters available in the Issues tab for projects with AI triage enabled. The first lets you display issues that have pending AI suggestions, and the second lets you filter out issues based on the confidence score (High, Medium, or Low) of those suggestions.

Note: Because only AI-triaged issues have an associated confidence score, if you apply the AI Confidence Level filter, all issues without AI suggestions will become hidden until you remove the filter.

To filter a project's issues based on AI triage status, follow these steps:

1. Go to Portfolio.
2. Select the name of the application containing the project you want to view.
3. Select the name of the project.
4. Select the filter ( [image: A screenshot of the icon used to open the filter panel.] ) button.
5. If you want to filter based on whether issues have an AI triage suggestion, under AI Triage Suggestion select either Yes or No.
6. If you want to filter based on the confidence score of AI triaged suggestions, under AI Confidence Level select any of High, Medium, or Low.
7. To remove any of the applied filters, deselect the corresponding checkbox or click Clear Filters.

The Issues tab refreshes automatically to show results based on your selections.

## Inspect an AI triage suggestion

After running an AI triage on an issue, a star icon next to its name indicates that there is an AI-generated suggestion awaiting a decision. Inspecting the suggestion provides more information about the nature of the issue, the recommended actions, and the confidence of the AI's assessment. You can accept or reject the suggestion here, as needed.

Note:

Accepting an AI triage suggestion will remove it, initiate the standard triage approval workflow for the project, and change the issue's Triage Status according to the result of the AI triage. For example, if the triage determines the issue to be a bug, accepting the suggestion updates its status to *To Be Fixed*, whereas a false positive or intentional behavior is updated to *Dismissed*.

Rejecting a suggestion will remove it but otherwise have no effect on the status of the issue.

To inspect the AI suggestion for an issue, follow these steps:

1. Go to Portfolio.
2. Select the name of the application containing the project you want to view.
3. Select the name of the project.
4. Next to the name of an issue with an AI suggestion, select the star icon (✨).

   The AI Triage Suggestion panel contains various information about the suggestion, including a text summary.
5. If you want more context for the suggestion summary, select View Rationale. When you've finished reading the AI Triage Rationale panel, use the x icon to close it.
6. If you're ready to decide whether to accept the suggestion, select either Accept or Reject as appropriate. If not, click anywhere outside the panel to close it.

If you've accepted or rejected the suggestion, the star icon disappears. If not, the suggestion remains until a decision is made. An event is added to the log for the issue, noting your choice.

## Accept or reject AI suggestions in bulk

After running an AI triage, a star icon next to an issue's name indicates that there is an AI-generated suggestion awaiting a decision. If you're ready to accept or reject the suggestions on multiple issues, you can do this in bulk to save time.

Note:

Accepting an AI triage suggestion will remove it, initiate the standard triage approval workflow for the project, and change the issue's Triage Status according to the result of the AI triage. For example, if the triage determines the issue to be a bug, accepting the suggestion updates its status to *To Be Fixed*, whereas a false positive or intentional behavior is updated to *Dismissed*.

Rejecting a suggestion will remove it but otherwise have no effect on the status of the issue.

To accept or reject AI suggestions in bulk, follow these steps:

1. Go to Portfolio.
2. Select the name of the application containing the project you want to view.
3. Select the name of the project.
4. Select the checkboxes of the issues you want to modify.
5. Select Pending AI Triage Suggestions, then either Accept or Reject to update all selected issues.

The AI suggestion is removed from all selected issues and the chosen action is applied to them. An event is added to the log for each selected issue, noting your choice.
