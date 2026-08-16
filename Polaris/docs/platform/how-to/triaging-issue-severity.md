---
title: "Triaging issue severity"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/triaging-issue-severity.html"
content_id: "4s98MVdpoKcT7mI5HDtb2w"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:52.531791+00:00"
content_hash: "aefb492dbf92b2b54f3d1aa21747bb8c8a60e9cfcbc4932857782ce52571fa8c"
---

# Triaging issue severity

When enabled, you can change the severity assigned to issues during triage.

When triaging issue severity is enabled, you can change the severity assigned to one or more issues during triage. Changes to issue severity are recorded in the issue history.

Note: You cannot change an issue's severity to Not Specified or None.

Changes to issue severity are applied across all branches in a SAST & SCA project. Set up a triage approval workflow if you require formal approval for changes to issue severity by users. See [Set up triage approval workflows](set-up-triage-approval-workflows.md) for more information.

## Lock triaging issue severity settings

Organization Administrators can lock the Allow triaging issue severity setting to control who can change it. Locking prevents lower-privileged roles from enabling or disabling triaging issue severity throughout your portfolio.

- When unlocked (default): Organization Administrators, Organization Application Managers, and Application Admins can enable or disable triaging issue severity in application or project settings.
- When locked: Only Organization Administrators can enable or disable triaging issue severity in application or project settings.

See [Lock or unlock triaging issue severity settings](triaging-issue-severity/lock-or-unlock-triaging-issue-severity-settings.md) for more information.

## Setting inheritance

The severity customization setting set at the organization level serves as the default for all applications and projects in your portfolio. However, severity customization settings assigned to applications and projects take precedence:

- An application's settings override organization-level severity customization settings.
- A project's settings override both application and organization-level severity customization settings.

To check the active severity customization settings for an application or project, open the Triage tab.

- For an application, go to Portfolio > select an application > Settings > Triage.
- For a project, go to Portfolio > select an application > select a project > Settings > Triage.

When Inherited appears at the top of the Triage panel, the severity customization settings that apply to the application (example below) or project are inherited.

[image: Screenshot of the Triage panel for an application.]
