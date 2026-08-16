---
title: "Ways to triage components in Polaris"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/ways-to-triage-components-in-polaris.html"
content_id: "uGrqUlYF8uzZJ4ihWl26lQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:49.388966+00:00"
content_hash: "7dcbf6d1aad22b00f91c6b1252ce39c6b3792abf3bde3b4a666a67d26aa7dff7"
---

# Ways to triage components in Polaris

All components detected in tests or added to projects manually are automatically listed in your software bill of materials (SBOM), and the issues derived from components are included in your issues. Triaging a component allows you to exclude the component from your SBOM and automatically dismiss the component's issues. If needed, you can change an excluded component back to included.

Note the following when triaging components:

- This feature is project specific, meaning that when you triage a component, it will be triaged for the whole project but not for other projects.
- You can triage components captured in a tests, and components that are added manually.

  Note: Components you add manually can be deleted. See [Delete a manually added component](add-or-modify-components/delete-a-manually-added-component.md) for more information.
- Once you exclude a component, if it is detected in a later test, it will still appear as excluded.
- If the same component is detected in multiple branches of a project, you only need to triage it once. Triage actions are automatically applied across branches in a project.
- You can view the triage history of an individual component during triage.

  Note: Issue triage (see [Ways to triage issues in Polaris](ways-to-triage-issues-in-polaris.md)) is affected by component triage.
  - When you exclude a component, any non-dismissed issues derived from the component are automatically dismissed.
  - When you include a component, any issues related to the component that has been previously dismissed automatically, are now set to the default state (not triaged).
- If your organization uses a triage approval workflow, including or excluding a component may require approval to take effect. After you triage a component, the pending approval [image: triage icon pending] icon appears when approval is required. You can monitor triage approval requests on the Triage Approval Overview Dashboard. See [Set up triage approval workflows](set-up-triage-approval-workflows.md) and Work with dashboards for more information.
- Dismissed issues and excluded components (via issue and component triage) are not included in reports. Dismissed issues and excluded components are typically hidden on dashboards that show issues and components; adjusting filters may allow you to see them. After you include or exclude a component (and approve the change, if required), it can take up to 60 minutes for the change to affect reports and dashboards.

## How to exclude a component

1. Select components by: 

   - Manually selecting via checkboxes for individual, multiple, or all.
   - Using filters.
   - Clicking Triage All.
2. Click Triage (Selected or All).

   The Triage Selected Component panel opens.

   [image: Screenshot of Individual Issue Triage]

   1. Under SBOM, select Excluded.
   2. Enter a comment that describes the change you made in the Comment field.

      Note: Depending on your approval workflow, this step may be optional.
3. Click Save.

   Important: If your organization uses a triage approval workflow, certain changes may require approval to take effect. After you triage a component, the pending approval [image: triage icon pending] icon appears next to changes that require approval. See [Set up triage approval workflows](set-up-triage-approval-workflows.md) for more information.

## How to include a component (that has been excluded)

Components are included by default. If component(s) have been excluded, you can change it back to included.

1. Select components by: 

   - Manually selecting via checkboxes for individual, multiple, or all.
   - Using filters (**SBOM** > **Excluded**).
   - Clicking Triage All (after using filter if you want to triage all excluded components).
2. Click Triage (Selected or All).

   The Triage Selected Component panel opens.

   [image: Screenshot of Individual Issue Triage]

   1. Under SBOM, select Included.
   2. Enter a comment that describes the change you made in the Comment field.

      Note: Depending on your approval workflow, this step may be optional.
3. Click Save.

   Important: If your organization uses a triage approval workflow, certain changes may require approval to take effect. After you triage a component, the pending approval [image: triage icon pending] icon appears next to changes that require approval. See [Set up triage approval workflows](set-up-triage-approval-workflows.md) for more information.
