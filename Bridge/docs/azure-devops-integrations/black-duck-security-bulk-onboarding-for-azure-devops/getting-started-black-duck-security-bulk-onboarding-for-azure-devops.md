---
title: "Getting started: Black Duck Security Bulk Onboarding for Azure DevOps"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/getting-started-black-duck-security-bulk-onboarding-for-azure-devops.html"
content_id: "f~4Cdg1hZugZkc1IBU6KTg"
version: "latest"
section: "Azure DevOps Integrations"
scraped_at: "2026-08-08T23:48:16.615933+00:00"
---

# Getting started: Black Duck Security Bulk Onboarding for Azure DevOps

**Welcome to the Black Duck Security Bulk Onboarding user guide**

This guide helps you get started with the Black Duck Security Onboarding Solution for Azure DevOps. It explains the basic setup process, configuration options, and common operations you can perform while using the application.

Black Duck Security Bulk Onboarding provides automated security scanning capabilities for your Azure DevOps repositories, helping you identify vulnerabilities, license compliance issues, and security risks in your codebase.

The onboarding solution will generate and deploy a pipeline configuration that is committed to selected repositories within an organization and project for conducting scans for supported Black Duck platforms: Black Duck® SCA, Coverity or Polaris.

Black Duck Security Bulk Onboarding for Azure DevOps is available at <https://integrations.blackduck.com/onboard>

It is recommended that the following preliminary steps are performed:

- Prerequisites: Please read before going into action.
- Variables setup: Set up variable groups referenced within the generated pipeline file at the project level. Variable groups store platform credentials (server URLs, tokens, passwords) that the pipeline references at runtime.

## Azure pipeline variable groups setup

The generated pipeline file references variables and secrets stored in Azure DevOps Variable Groups. This section explains how to create and configure variable groups at the project level.

Before proceeding, ensure all requirements in the prerequisites are met.

Note: Ensure all required variables and secrets are configured in a variable group before proceeding to generate the scan pipeline for review and deployment. If customized names are needed, then the generated pipeline file must be updated to reflect the new names. This can be done at the stage when reviewing the pipeline..

Please refer to the appropriate platform documentation for an overview of the required secrets and variables:

- Black Duck® SCA
- Coverity
- Polaris

**Creating a variable group**

Variable groups in Azure DevOps are managed at the project level and can be shared across multiple pipelines.

- Go to Azure DevOps > Select Project
- Navigate to Pipelines > Library from the left navigation.
- Click + Variable Group.
- Enter a variable group name (e.g. Polaris, Black Duck® SCA, Coverity).
- Add required variables:
  - Click + Add for each variable.
  - Enter the name and value.
  - For sensitive values (tokens, passwords), click the lock icon to mark the variable as secret.
- Click Save.

[image: Screenshot create new variable group]

Note: The variable group name specified here will be referenced in the generated pipeline YAML. During the configuration process, you will select the variable group from a dropdown list.

**Required variables by platform**

The required variables and secrets per platform are described in the tables below.

Table 1. Coverity variables and secrets

| Type | Name | Description | Example |
| --- | --- | --- | --- |
| Variable | `COVERITY_URL` | Coverity server URL | `https://coverity.blackduck.com` |
| Secret | `COVERITY_USER` | Coverity | `$COVERITY_USER` |
| Secret | `COVERITY_PASSPHRASE` | Coverity | `$COVERITY_PASSPHRASE` |

Table 2. Black Duck® SCA variables and secrets

| Type | Name | Description | Example |
| --- | --- | --- | --- |
| Variable | `BLACKDUCKSCA_URL` | Black Duck® SCA server URL | `https://sca.blackduck.com` |
| Secret | `BLACKDUCKSCA_TOKEN` | Black Duck® SCA access token | `$BLACKDUCKSCA_API_TOKEN` |

Table 3. Polaris variables and secrets

|  |  |  |  |
| --- | --- | --- | --- |
| Variable | `POLARIS_SERVER_URL` | Polaris server URL | `https://polaris.blackduck.com` |
| Secret | `POLARIS_ACCESS_TOKEN` | Polaris access token | `$POLARIS_ACCESS_TOKEN` |

Note: Ensure all required variables and secrets are configured before proceeding to generate the scan pipeline for review and deployment.

## Azure DevOps Entra ID authorization

When first accessing Black Duck Security Bulk Onboarding, a prompt will be displayed to authorize the following permissions:

- Have full access to Visual Studio Teams Services REST APIs
- Maintain access to data you have given it access to
- View users basic profile

Note: For authentication, Azure DevOps Entra ID is being used with the following permission scopes: user_impersonation, offline_access, openid and profile.

Click Login with Azure to proceed. You will be redirected to the Microsoft login page to authenticate with your Azure DevOps account.

[image: image]

After successful sign in with your Microsoft accounts, you will need to accept required permissions:

[image: EDO permissions request screen]

If you do not have admin privileges, you will need to request admin consent:

[image: edo admin consent screen]

Note: If you do not have administrator privileges, you may need to request approval from an Azure Entra ID administrator.

- **Approval required with a justification box:** This UI appears when you've turned on the **Admin consent request workflow** in your tenant. End users who aren't admins can fill in a justification and submit a request directly from the consent screen. Designated reviewers (global, cloud app, or application admins) then get notified and can approve or deny the request.
- **Need admin approval without any request button:** This is the default block page when your tenant hasn't enabled the admin consent workflow (or when user consent is fully disabled). In this case, non-admins see a message telling them to ask an administrator — there's no built-in "request" flow.

## Onboarding process

Upon successful authentication, you'll be redirected to the Black Duck bulk onboarding screen. The Azure DevOps onboarding follows a hierarchical selection process:

- **Select Organization** : Choose the Azure DevOps organization.

  [image: Screenshot for selecting an organization]
- **Select Project**: Choose a project within the organization.

  [image: Screenshot for selecting project]
- **Select Repositories** : Choose repositories within the project.

  [image: Screenshot for selecting repositories]

Take a moment to review the dashboard components:

- **Select repositories**: Configure the repositories where a pipeline YAML file will be generated and committed.
- **Configure options**: Configure scan options for specific Black Duck platforms such as Black Duck® SCA, Coverity and Polaris.
- **Review pipeline**: Review a preview of the generated Azure Pipeline that will be deployed to the selected repositories for performing a Black Duck security scan.
- **Summary**: Summarizes the count of repositories where the pipeline will be deployed to. At this stage the pipeline can be submitted for deployment.

## Configure scan workflow

The Dashboard UI can be used to configure which repositories within a project a pipeline will be deployed to. A pipeline can be configured for the following Black Duck platforms:

- Black Duck® SCA
- Coverity
- Polaris

[image: Select repositories screen]

**Step 1: Select repositories**

1. Use the Select repositories screen to configure which repositories within the organization and project should be scanned.
   1. **Select organization**: Use the organization dropdown to select the Azure DevOps organization.
   2. **Select project**: After selecting an organization, a second dropdown will appear to select the Azure DevOps project within that organization.

      Note: The project selection step is unique to Azure DevOps. Azure DevOps organizes repositories within projects, which are in turn organized within organizations.
   3. **Select repositories**: The app automatically discovers and displays repositories based on the selected organization and project.
2. Select the repositories that the generated pipeline should be configured and deployed to:
   - **All repositories**: Configure and deploy the pipeline to all repositories within the selected project.
   - **Selected repositories**: Select specific repositories from the list.

[image: ADO App scan options]

**Step 2: Configure scan options**:

The Dashboard can be used to automatically generate an Azure Pipeline file based on scan options specified in the **Configure options** screen. The generated Azure Pipeline will be deployed to the selected repositories.

The following options can be configured:

- **Branches**: Scans can be configured to trigger in response to push events and when a Pull Request is created or updated. Use the push events and pull request text box to specify which branches will initiate scans for each type of event.
- **Pool selection** (Required): Choose the agent pool for the Azure Pipeline. Azure DevOps supports two types of pools:
  - **Microsoft-hosted pools**: Select "Azure Pipelines" and optionally specify a VM image:
  - **Self-hosted pools**: Select from available self-hosted agent pools configured in your Azure DevOps project. Optionally specify **Demands** (Agent.Name) to filter specific agents within the pool.

  Note: Pool selection is required for Azure Pipelines. The selected pool determines the build environment where scans will execute.
- **Variable groups** (Required): Select the variable group containing the platform credentials (server URLs, tokens, etc.). The dropdown displays variable groups available in the selected project. At least one variable group must be selected.

  Note: Variable groups must be pre-configured in Pipelines > Library before they can be selected here. See Azure Pipeline Variable Groups Setup.
- **Platform**: Select the Black Duck platform for scanning. Supported platforms include Coverity, Black Duck® SCA and Polaris. Upon selection, the Dashboard UI will dynamically update to display platform scan-specific options and instructions.
- **Scan method**: Choose between:
  - **Azure Pipeline - Black Duck Security Scan (recommended)**: Generate a scan pipeline that uses the `BlackDuckSecurityScan@2` Azure DevOps task. This is the recommended approach for Azure DevOps.
  - **CLI - Black Duck Bridge CLI**: Generate a scan pipeline that downloads the latest Bridge CLI and uses it directly to perform a security scan.

Note: Ensure all required variable group secrets are configured before clicking Next to proceed with generating a scan pipeline for review and deployment.

Refer to the Black Duck platform documentation pages for further details of scan configuration options and prerequisites:

- Black Duck® SCA
- Coverity
- Polaris

## Review workflow

The **Review pipeline** screen allows a generated pipeline to be previewed and edited before submission for deployment.

Note: The generated pipeline can include multiple scan jobs for different Black Duck platforms, such as Black Duck, Coverity or Polaris. To add a new scan job, return to the **Configure Options** screen and select a different Black Duck platform. Subsequently, when navigating back to the **Review pipeline** screen, the generated pipeline will be displayed with the configured options for the selected platform.

The **Review pipeline** screen displays an Azure Pipeline containing scan steps, specifically configured for the selected Black Duck platform. The pipeline is automatically generated for deployment to the selected repositories and simplified to include only the minimum fields required (e.g., default values for the product scans are omitted unless specified).

[image: Review workflow screen example]

Inline editing of the pipeline is available by clicking the Edit button. The editor automatically validates the syntax, preventing saves if errors are detected. It also issues warnings for potential issues, such as hardcoded secrets or variables, which do not block saving.

Note: Azure Pipelines uses the pipeline YAML file in your repository's root directory (e.g., `azure-pipelines.yml` or `{platform}-pipeline.yml`).

1. Review and adjust the pipeline as needed:
   - Use the Edit button to make direct edits to the pipeline file, such as:
     - Modify trigger conditions, including which branches will trigger a scan.
     - Adjust scan configuration parameters
     - Update pool/agent configuration.
     - Required credentials and variable group references.
     - Add custom steps or integrations.
2. When required changes have been made, then perform one of the following options:
   - Click the Previous button to configure scan options for a different Black Duck platform.
   - Click the Next button to confirm that the pipeline has been reviewed and all necessary amendments hae been made.

Note: After editing the pipeline, if the Previous button is selected, the UI will warn that the edits you made will be lost permanently.

## Deploy pipeline

The **Summary** screen displays the count of repositories where the pipeline will be deployed.

To submit a pipeline for deployment across the selected repositories follow the steps below:

1. **Review the deployment summary:**
   - Check that the count of selected repositories and pipeline filename is as expected.
   - Use the Previous button to navigate back to adjust if necessary.
2. **Choose the deployment method:**

   | Deployment method | Summary |
   | --- | --- |
   | **Direct commit**: Commit pipeline directly to default branch. | 1. The pipeline YAML file is committed directly to the default branch (typically `main`). 2. If the branch is protected, the app will automatically fall back to creating a Pull Request instead. 3. When a variable group is specified, an Azure Pipeline definition is automatically created, linked to the variable group, and an initial build is queued. |
   | **Pull Request**: Create a Pull Request with pipeline file changes. | 1. A feature branch is created (e.g., `blackduck-workflow-{hash}`). 2. The pipeline file is committed to the feature branch. 3. A Pull Request is created targeting the default branch. 4. The pipeline definition is created only after the Pull Request is merged. |

   [image: image]
3. **Submit:**
   - Click the Submit button and confirm deployment in the modal dialog.
   - Monitor the deployment progress in the onboarding status screen, which will update every 10 seconds.
   - Review the Failed Repositories List for any deployment issues.

   [image: Deployment summary progress]

## Troubleshooting and support

The table below summarizes common issues and their resolutions.

| Issue type | Issue | Symptoms | Solution |
| --- | --- | --- | --- |
| Authentication | Entra ID authorization failed | Unable to login or authorization error | - Clear browser cache and cookies. - Ensure correct Azure DevOps account is logged in. - Retry the authorization process. |
| Permissions | Insufficient project access | Error: 403 Forbidden when accessing project | - Verify project membership and role (minimum Contributor). - Request elevated permissions from the project administrator. |
| Extension | Extension installation failed | Error when deploying pipeline with Azure Pipeline task | - Verify that you have the Organization Administrator role. - Manually install the Black Duck Security Scan extension from the Azure DevOps Marketplace. |
| Variable groups | Variable group not found | Empty dropdown in variable group selection | - Ensure variable groups are created in Pipelines > Library for the selected project. - Check that all required variables are added and saved correctly. |
| Pool/Agent | Agent pool access denied | Pipeline fails to run after deployment | - Verify agent pool permissions in Project Settings > Pipelines > Agent pools. - Ensure the selected agent pool is authorized for the project. |
| Pipeline deployment | Pipeline creation failed | Deployment stuck in In Progress status | - Check repository write permissions. - Verify that the variable group is configured correctly. - Review deployment logs for detailed error information. - Check the error message displayed on the Summary page. |
| Pipeline execution | Scan step failed | Azure pipeline failed during scan execution | - Check if the `BlackDuckSecurityScan@2` extension is installed. - Verify that variable group secrets are correct and accessible. - Check pool/agent availability. - Ensure the VM image is valid for the selected pool. |
| Pipeline execution | Bridge CLI download failed | Script execution failed in pipeline | - Check network connectivity from the agent. - Verify that the Bridge CLI download URL is accessible. - Confirm that the agent OS matches the script type (bash vs PowerShell). |
