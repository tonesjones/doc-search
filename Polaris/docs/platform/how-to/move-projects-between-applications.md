---
title: "Move projects between applications"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/move-projects-between-applications.html"
content_id: "CJl5Y5UXPRChDXDVl3EQwg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:08.180244+00:00"
content_hash: "e066f9345780fe841fe501c954ccc81cac7cf9fa9455083b485ff1bf1ac93016"
---

# Move projects between applications

Move projects between applications to reorganize your portfolio.

You can move SAST & SCA projects from one application to another. When a project moves, Polaris preserves:

- Test results
- Issue and component triage data
- Policies
- Branches
- SCM integration settings

Important: Access permissions always follow the destination application — users and groups not assigned to the destination application lose access to the project after the move.

When moving a project, you can choose to preserve settings the project inherits:

- Inherit new application settings: The project adopts settings from the destination application, including code exclusion rules, triage approval workflow, auto-branch deletion, and labels. Settings already customized at the project or branch level are not changed. Pending triage approvals are auto-approved when the new triage workflow takes effect.
- Keep previous application settings: The settings from the original application are preserved. Analysis behavior does not change. Pending triage approvals remain in their current state.

## Prerequisites and limitations

- The source and destination applications must both use concurrent (team member) subscriptions. Projects cannot move to or from applications that use application-model subscriptions.
- The project must be a SAST & SCA project. DAST projects cannot be moved.
- You must be an Organization Admin, Organization Application Manager, Application Admin, or a user with explicit permissions to move projects.
  - Application Admins must have Application Admin access to both the source and destination applications.
  - Users granted the Move projects permission (via custom roles) must have that permission on both the source and destination applications.
- The destination application must not already contain a project with the same name. If necessary, rename the project before moving it.
- If the project has project-level SCM integration settings, those settings are preserved after the move but may not function as expected. Review and update SCM settings after the move if necessary.
- Only one move operation can run in your organization at a time. If a move is already in progress, wait for it to complete before starting another.

## Before you move a project

Before you move a project, we recommend you check if the project is:

- Connected to a repository in your SCM (via an SCM integration)
- Tested from a CI pipeline

Polaris won't delete or modify a project's SCM integration settings after the move. This can prevent the integration from functioning as expected after the move is complete.

Before you move a project you test from a CI system, we recommend you temporarily pause the pipeline used to test the project to avoid errors. Once the move is complete, update your pipeline's configuration to reference the destination application's ID (`polaris.application.name`), and resume testing.

## Instructions

For step-by-step instructions, see:

- Move a project to a different application
- Move projects to a different application
- Move all projects in an application to a different application
