---
title: "Prerequisites: Azure Black Duck Security Bulk Onboarding"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/prerequisites-azure-black-duck-security-bulk-onboarding.html"
content_id: "uocGvKIzKWDtfbyxHCAsCA"
version: "latest"
section: "Azure DevOps Integrations"
scraped_at: "2026-08-08T23:48:13.731272+00:00"
---

# Prerequisites: Azure Black Duck Security Bulk Onboarding

The prerequisites for using Black Duck Security Bulk Onboarding for Azure DevOps are found here. Please ensure all requirements in each section are completed.

## Supported Azure DevOps instances

- Azure DevOps services ([https://dev.azure.com](https://dev.azure.com/))

Note: Currently Azure DevOps Server (on-premises) is not supported for Azure DevOps bulk onboarding.

## Azure Tenant and Consent Requirements

- All apps must have proper multi-tenant configuration
- Admin consent

  - If you see **"Need admin approval"**, admin consent is required

## Minimum role requirement

To use Black Duck Security Bulk Onboarding for Azure DevOps, the authenticated user must have the following permissions across the organization, project, repository, pipeline and library levels.

**Organization level**

| Requirement | Details |
| --- | --- |
| **Organization membership** | The user must be a member of the Azure DevOps organization with access to the target projects. |
| **Access level** | Minimum **Basic** access level (Stakeholder access is not sufficient). |
| **Extension installation** | The Black Duck Security Scan extension is automatically installed at the organization level by the onboarding solution. The authenticated user must have **Project Collection Administrator** membership, or the **"Edit collection-level information"** permission set to **Allow**, so that the app can install the extension on their behalf. If the user does not have this permission, an Organization Administrator must pre-install the extension manually from the Azure DevOps Marketplace. |

**Project level**

The user must be a member of the project with at minimum the **Contributor** role. The table below outlines the built-in project-level groups and their relevance to bulk onboarding:

| Project Group | Repository access | Pipeline management | Variable groups (library) | Suitable for bulk onboarding? |
| --- | --- | --- | --- | --- |
| **Readers** | Read-only | View only | Reader | No |
| **Contributors** | Read + Write | Create & edit pipelines, queue builds | Creator (can create new variable groups) | Yes (minimum recommended) |
| **Build administrators** | Read + Write | Full build management | Administrator | Yes |
| **Project administrators** | Full control | Full control | Administrator | Yes (recommended for large-scale onboarding) |

Tip: For bulk onboarding across many repositories, **Contributor** is the minimum required role. If the user also needs to manage variable group permissions for other team members or configure service connections, **Build Administrator** or **Project Administrator** is recommended.

**Repository level permissions**

| Permission | Required | Purpose |
| --- | --- | --- |
| **Read** | Yes | Clone and read repository contents to list repos and inspect existing files. |
| **Contribute** | Yes | Push the generated pipeline YAML file to the repository. |
| **Create branch** | Yes | Create a new branch for the pipeline configuration (used for PR-based deployment). |
| **Contribute to Pull Requests** | Yes | Create pull requests when using the PR deployment method. |
| **Bypass policies when pushing** | Optional | Only needed if branch policies are enforced on the target branch and direct push is required. Not recommended for general use. |

Note: Contributors inherit Read, Contribute, Create Branch and Contribute to Pull Requests permissions by default. These permissions are inherited from the project-level "Git Repositories" security node down to individual repositories.

**Pipeline / build permissions**

The following pipeline permissions are required to create and manage Azure Pipelines during bulk onboarding:

| Permission | Required | Purpose |
| --- | --- | --- |
| **Edit build definition** | Yes | Create and modify pipeline YAML definitions. |
| **Create build definition** | Yes | Create new pipeline definitions for each onboarded repository. |
| **Queue builds** | Yes | Trigger initial pipeline runs after deployment. |
| **Edit queue build configuration** | Yes | Configure runtime parameters when queuing builds. |
| **View build definition** | Yes | Verify pipeline creation and status. |

Note: Contributors have these permissions by default.

**Library (variable groups) permissions**

Variable groups store the credentials (server URLs, API tokens, passwords) referenced by the generated pipeline. The Library uses a role-based security model:

| Library role | Capabilities | When needed |
| --- | --- | --- |
| **Reader** | View variable groups (secret values remain hidden). | Viewing existing variable groups. |
| **User** | Reference variable groups in pipelines. | If variable groups are pre-created by an administrator. |
| **Creator** | Create new variable groups at the project level. | If the user needs to set up variable groups for Black Duck credentials. |
| **Administrator** | Full control: create, edit, delete, and manage security for variable groups. | If the user needs to manage variable group access for other team members. |

Note: Contributors are assigned the **Creator** role at the project level by default. The creator of a variable group automatically becomes its **Administrator**.

**Entra ID scopes**

Black Duck Security Bulk Oonboarding authenticates via Entra ID using the `user_impersonation`, offline_access, openid, and profile scopes, which delegates the authenticated user's permissions. This means the bulk onboarding solution can only perform actions that the authenticated user is authorized to do. The user does not need to configure separate API scopes, the OBO flow handles this automatically.

**Summary: quick reference**

| Level | Minimum requirement |
| --- | --- |
| **Organization** | Member with Basic access level |
| **Project** | Contributor role (minimum) |
| **Repositories** | Read, Contribute, Create Branch, Contribute to Pull Requests |
| **Pipelines** | Create & Edit Build Definition, Queue Builds |
| **Library** | Creator role (for variable group setup) or User role (if pre-configured) |
| **Extension** | Auto-installed by the app (requires Project Collection Administrator or pre-installed by an admin) |

## Black Duck Security Scan Extension

The Black Duck Security Scan extension must be available in your Azure DevOps organization to use the Azure Pipeline task integration method (recommended).

**To install the extension:**

1. Navigate to your Azure DevOps organization settings.
2. Go to Extensions > Browse marketplace .
3. Search for **"Black Duck Security Scan"** published by **blackduck**.
4. Click **Get it free** and select your organization.
5. Click **Install**.

Note: Black Duck Security Bulk Onboarding will attempt to automatically install the extension when deploying a pipeline using the Azure Pipeline task method. However, this requires Organization Administrator permissions for the authenticated user.

Alternatively, the extension can be requested by a project contributor and approved by an organization administrator.

## Next steps

Once all prerequisites are satisfied, proceed to the user guide to ensure that preliminary steps have been considered and perform the configuration process.
