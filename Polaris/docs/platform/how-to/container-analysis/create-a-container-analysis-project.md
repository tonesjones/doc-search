---
title: "Create a Container Analysis project"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/create-a-container-analysis-project.html"
content_id: "w4T7X9~fWlzpfiswgEyCjQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:16.367107+00:00"
content_hash: "4203eb7a40b42eb353f450008688bede8503a52d234937cdf9bb1d1ee5a1ca3d"
---

# Create a Container Analysis project

Create a Container Analysis project in Polaris to run scans against container images.

## Prerequisites

Before you begin, make sure that:

- Your organization has a Container Analysis entitlement. Contact your Organization Admin or Organization App Manager if you are unsure.
- You have permission to create projects. See [Roles and permissions](../../reference/roles-and-permissions.md).
- An Organization Admin or Organization App Manager has either:
  - Created an application that uses your Container Analysis subscription. See Create an application.
  - Assigned your Container Analysis subscription to a preexisting application. See [Assign subscriptions to applications](../assign-subscriptions-to-applications.md).

## Create a Container Analysis project

1. Go to Portfolio and select an application with a Container Analysis subscription.
2. Select Create > New Project(s).
3. Select Container Analysis as the project type.
4. Enter a Project Name (maximum 255 characters). The name must be unique within your organization.
5. (Optional) Enter a Description.
6. Select Save.

Polaris creates the Container Analysis project. You can now add containers to the project and run scans against them. See [Add a container to a Container Analysis project](add-a-container-to-a-container-analysis-project.md) and How to run Container Analysis.
