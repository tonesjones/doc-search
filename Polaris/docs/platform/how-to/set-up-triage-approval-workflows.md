---
title: "Set up triage approval workflows"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/set-up-triage-approval-workflows.html"
content_id: "1ecmSVF8yLTpHZ8ZaaTVtA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:50.305457+00:00"
content_hash: "02bae11a2e4f856490afeb85bf8607e5e8c851dd5230da74c3a63e608f5f4de2"
---

# Set up triage approval workflows

Learn how to set up issue and component triage approval workflows for your organization, application, or project.

## Overview

Triage approval workflows provide governance for issue and component triage activities in your organization. When enabled, triage approval workflows require designated approvers to review and approve triage actions before they take effect. This helps ensure consistency, accountability, and compliance with your organization's security policies.

Your triage approval workflow can be configured so any of the following changes require approval:

- Changing an issue's triage status to Dismissed when the reason for dismissal is set to Intentional, False Positive, or Other.
- Changing an issue's triage status to To Be Fixed.
- Changing an issue's Severity.
- Changing an issue's Fix-By Date.
- Including or excluding a component from your SBOM (SBOM include/exclude).

Additionally, when you enable Require reason/comment to justify the approval request, changes that require approval cannot be submitted without a comment.

### Approval workflow inheritance

The approval workflow you configure at the organization level serves as the default for all the applications and projects in your portfolio. However, approval workflows configured in applications and projects take precedence; an application's approval workflow overrides the organization-level approval workflow, while a project's approval workflow overrides both application and organization-level approval workflows.

To check the active approval workflow for an application or project, open the Triage tab.

- For an application, open the application and go to Settings > Triage.
- For a project, open the project and go to Settings > Triage.

When Inherited appears at the top of the Approval Workflow panel, the approval workflow that applies to the application or project is inherited.

[image: Screenshot of the Approval Workflow panel for an application.]

### Default approvers

By default, Organization Administrators, Organization Application Managers, and Application Administrators can approve triage requests. Default approvers can approve their own triage requests.

Tip: You can create custom roles that grant users permissions to Approve component triage requests or Approve issue triage requests. See [Manage permissions with custom roles](manage-permissions-with-custom-roles.md) for more information.

Find instructions to approve or reject triage requests here:

- Approve or reject issue triage requests
- Approve or reject component triage requests

### Modifying approval workflows

If you disable properties in a triage approval workflow while there are pending approvals, pending approvals are automatically approved when the workflow changes.

For example, say your organization's default approval workflow includes fix-by dates. When you disable fix-by dates in your organization's default approval workflow, all of the fix-by changes that are pending approval (in applications and projects that inherit the default approval workflow) must be approved to save your changes.

Auto-approval events appear in issue triage history (example below) and component triage history.

  
 [image: Screenshot of an auto-approve event in an issue's triage history.]

### Find issues and components that require triage approval

The pending approval [image: triage icon pending] icon appears on the Issues and Components tabs next to changes that require approval.

Use the Pending Approvals filter (available on the Issues and Components tabs) to identify issues and components with changes that require approval.

  
 [image: Screenshot of the Pending Approvals filter.]   

You can also monitor triage approval requests using the Triage Approval Overview Dashboard. See [Work with dashboards](work-with-dashboards.md) for more information.

## Organization-level approval workflows

To manage your organization's default approval workflow, follow these steps:

Note: Only Organization Administrators can customize the organization-level approval workflow.

1. Go to My Organization > Triage.
2. Under Approval Workflow, select Edit.
3. Modify your organization's approval workflow, as required.
4. Select Save.

   Important: If you disabled properties in the approval workflow before you selected Save, the Auto-Approve Pending Items window appears. To proceed, select Confirm.

## Application-level approval workflow

To manage an application's approval workflow, follow these steps:

Note: Organization Administrators, Organization Application Managers, and other users with permissions to manage application settings can manage application-level approval workflows.

1. Go to Portfolio and open an application.
2. Go to Settings > Triage.
3. Under Approval Workflow, select Edit.
4. Modify the application's approval workflow, as required.
5. Select Save.

   Important: If you disabled properties in the approval workflow before you selected Save, the Auto-Approve Pending Items window appears. To proceed, select Confirm.

## Project-level approval workflow

To manage a project's approval workflow, follow these steps:

Note: Organization Administrators, Organization Application Managers, Application Administrators, Application Contributors, and other users with permissions to manage project settings can manage project-level approval workflows.

1. Go to Portfolio, open an application, and open a project.
2. Go to Settings > Triage.
3. Under Approval Workflow, select Edit.
4. Modify the project's approval workflow, as required.
5. Select Save.

   Important: If you disabled properties in the approval workflow before you selected Save, the Auto-Approve Pending Items window appears. To proceed, select Confirm.

## Reset application and project-level approval workflows

After you customize an application or project's approval workflow, you can select Reset (at the top of the Approval Workflow panel) to revert the workflow to default settings. When you reset an application's approval workflow, the application will inherit your organization's approval workflow. When you reset a project's approval workflow, the project will inherit the application (if set) or organization-level workflow.

1. Open the application or project's settings:
   - For an application, go to Portfolio > select an application > Settings > Triage.
   - For a project, go to Portfolio > select an application > select a project > Settings > Triage.
2. Select Reset (at the top of the Approval Workflow panel).
