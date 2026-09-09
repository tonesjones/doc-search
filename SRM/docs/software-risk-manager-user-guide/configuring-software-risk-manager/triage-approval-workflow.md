---
title: "Triage Approval Workflow"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/triage-approval-workflow.html"
content_id: "sggZsG2CAQrYlrUid1lv6w"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:02:56.364001+00:00"
content_hash: "5ae7601ccea497e2ebcbde42f79d066fcf7690b1cd40e87b0249c5af281fb5ea"
---

# Triage Approval Workflow

Triage settings associated with findings can be changed by users with an
`admin` or `manage` role. Users who are unable to
change the triage status directly can submit a change for approval. Admins can configure
the triage workflow from the Settings menu.

SRM supports two approval workflow modes:

- **Single Level** — any user with the Manager or Admin role can approve or reject
  triage status change requests. This is the legacy mode.
- **Multi Level** — each status change request passes through an ordered chain of
  approval levels. Each level can require a designated user group to approve before the
  request advances to the next level.

Click the Settings icon in the navigation bar and select **Triage Approval Workflow**
from the left menu to open the configuration page.

Figure 1. Triage Approval Workflow — mode selector
  
 [image: image]

Managing the Triage Approval Workflow consists of the following tasks:

- Selecting the approval mode (Single Level or Multi Level)
- Configuring the workflow for all projects (Single Level mode)
- Configuring the workflow for specified projects (Single Level mode)
- Creating and managing approval chains (Multi Level mode)
- Submitting requests for status changes
- Monitoring approval progress (Approval Status column)
- Approving or rejecting status change requests

## Selecting an Approval Mode

The Triage Approval Workflow page displays a **Single Level** and a **Multi
Level** tab at the top. Click a tab to switch between modes. The current mode
is saved automatically.

- **Single Level** — uses the legacy radio-button configuration below the tab
  to enable or disable the workflow globally or per project.
- **Multi Level** — shows the **Multi-Level Approval Chain Setup** table
  where you create and manage named approval chains.

Switching from Multi Level back to Single Level clears the active default chain and
restores the legacy workflow setting. Any approval requests already in progress
continue through the chain configuration that was active when they were
submitted.

## Configuring Triage Workflow (Single Level)

When the **Single Level** tab is selected, this section provides three options for
triage approval configuration:

- No triage approval workflow. Select this option to restrict the ability to
  change status to admins and users with "update" or "manage" roles.
- Enabled triage approval workflow for all projects. Select this option to
  enable the approval workflow for all current and future projects.
- Enable triage approval workflow, but allow it to be configured at the
  Project level. Select this option to enable the workflow option on a project
  level.

Use the radio buttons to select an option. The selection will be saved
automatically.

Figure 2. Triage Approval Workflow — Single Level configuration
  
 [image: image]

For more information on changing the status of a finding, see the Change Status section.

## Configuring Triage Workflow for All Projects (Single Level)

Admins can enable the triage approval workflow across all projects.

**To enable the triage workflow for all projects:**

1. Click the Settings icon in the navigation bar and select **Triage Approval
   Workflow** from the left menu.
2. Select the **Single Level** tab.
3. Select **Enable triage approval workflow for all projects**.

## Configuring Triage Workflow for Specified Projects (Single Level)

Admins can configure the triage approval workflow on a per-project basis.

**To configure the triage workflow for a project:**

1. Click the Settings icon in the navigation bar and select **Triage Approval
   Workflow** from the left menu.
2. Select the **Single Level** tab.
3. Select **Enable triage approval workflow, but allow it to be configured at
   the Project level**.
4. Open the Projects page, click the project's dropdown configuration icon, and
   select **Triage Approval Config**.

   [image: image]
5. Select one of the following options:
   - Default (See Configuring Triage Workflow for All Projects.)
   - No triage approval workflow
   - Enable triage approval workflow

   [image: image]
6. Click **Save**.

## Managing the Approval Chain (Multi Level)

An **approval chain** is a named, ordered sequence of approval levels. Each level
has a label and an optional user group. When a status change request enters the
chain, it must be approved at every level in order before the new status takes
effect. Rejecting at any level cancels the request and requires a reason.

Only one approval chain is supported. Once created, it is marked as the default and
applied to all projects automatically.

Figure 3. Triage Approval Workflow — Multi Level chain setup
  
 [image: image]

**To switch to multi-level approval mode:**

1. Click the Settings icon in the navigation bar and select **Triage Approval
   Workflow** from the left menu.
2. Click the **Multi Level** tab.
3. If no chain has been created yet, click **Create Chain** and configure
   it. Once saved, multi-level mode becomes active.

### Creating the Approval Chain

**To create the approval chain:**

1. On the **Triage Approval Workflow** page, click the **Multi
   Level** tab.
2. Click **Create Chain**.
3. In the **Chain Name** field, enter a descriptive name for the chain
   (for example, *Standard 3-Level Chain*).
4. For each approval level:
   - Enter a **Level Name** (for example, *Security Reviewer
     Approval*).
   - Optionally, select a **User Group** from the dropdown. Only
     members of the selected group (and admins) will be able to
     approve that level. Leave blank to allow any user with the
     Manager or Admin role to approve.
5. To add more levels, click **Add Level**. Levels are processed in the
   order they appear in the table.
6. To remove a level, click the minus icon next to that row. A chain
   must have at least one level.
7. Click **Save**.

The chain is applied to all projects automatically.

### Editing the Approval Chain

**To edit the approval chain:**

1. On the **Triage Approval Workflow** page, click the **Multi
   Level** tab.
2. In the chain table, click the context menu icon and select
   **Edit**.
3. Modify the chain name or levels as needed.
4. Click **Save**.

Changes apply to new approval requests only. Requests already in progress
continue through the chain configuration that was active when they were
submitted.

## Creating a Status Change Request

**To create a triage status change request:**

1. Open the Findings page.
2. Locate the finding whose status you want to change and click the Status
   dropdown menu to open a list of Status options.
3. Select a new triage status.
4. If a multi-level approval chain is active, an information panel appears in
   the request dialog showing the chain name, the current approval level, and
   the approver group for that level.
5. Enter a comment and click **Submit**.

After submission, the finding's status changes to *Pending* until all approval
levels are satisfied.

## Monitoring Approval Progress

The Findings table includes an **Approval Status** column that shows the current
state of any pending status change request for each finding. If the column is not
visible, use the column settings icon in the Findings table header to add it.

- For multi-level requests, the column displays a level indicator such as *Level
  2 of 3*, showing how far the request has progressed through the
  chain.
- For single-level (legacy) requests, the column displays *Pending
  Approval*.
- Findings with no pending request show a dash.

## Approving or Rejecting a Status Change Request

Users with the Manager or Admin role, or members of the approver group configured for
the current approval level, can approve or reject a pending request.

**To approve a triage status change request:**

1. Open the Findings page.
2. Use the **Pending Triage Status** filter to list pending requests.
3. Click the approval button for the finding. In multi-level mode, the button
   label identifies the current level, for example *Approve Level 2 of 3
   (Security Team)*. If the button is disabled, you are not the
   designated approver for the current level.

After approval, the request advances to the next level. When all levels are approved,
the finding's status changes to the requested value.

**To reject a triage status change request:**

1. Open the Findings page and locate the pending request.
2. Click the approval button for the finding, then click **Reject**.
3. Enter a required reason for the rejection and click **Reject
   Request**.

Rejecting a request at any level cancels the entire request. The finding remains at
its current status. The rejection reason is recorded for audit purposes.
