---
title: "Setting up Black Duck Security Scan Extension"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/setting-up-black-duck-security-scan-extension.html"
content_id: "WYO_33ZWrl5SagC0bfg2cQ"
version: "latest"
section: "Azure DevOps Integrations"
scraped_at: "2026-08-08T23:48:21.935847+00:00"
---

# Setting up Black Duck Security Scan Extension

The following tasks explain how to setup Black Duck Security Scan Extension.

## Compatibility

Before adding Black Duck Security Scan Extension in your Azure DevOps pipeline, you must meet the following prerequisites:

- Black Duck Security Scan Extension supports Azure Devops Cloud
- Azure Devops Server (On-Prem) is supported for versions 2019, 2020, and 2022.
- Starting with Bridge version 3.5.1, the Black Duck Security Scan Extension now includes support for Linux ARM architectures.
- **Unsupported configuration:** Azure DevOps Server instances using the legacy URL pattern `http://machine-name:8080/tfs` are not supported. This includes:

  - Team Foundation Server 2019 or earlier versions that have been migrated to Azure DevOps Server 2019 or later while retaining the legacy TFS URL format.
  - Newly created Azure DevOps Server instances configured with the legacy TFS URL format.

  **Recommendation:** Use the modern Azure DevOps Server URL pattern for compatibility ([https://machine-name:8080/](http://machine-name:8080/tfs)).

## Install the Black Duck Extension

1. In an Azure organization, navigate to the **marketplace icon** > **browse marketplace**
2. Search "Black Duck Security Scan"
3. Install Black Duck Security Scan Extension for your organization

## Configure security permissions

Before using the Black Duck Security Scan Extension, ensure that the following permissions are granted:

- Contributor permissions for a repository are required to view a summary of all alerts for that repository.
- Project administrator permissions are required to dismiss alerts in Advanced Security.
- To manage permissions in Advanced Security, ensure membership of the [Project Collection Administrators](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-organization-collection-level-permissions?view=azure-devops) group. Alternatively request a Project Collection Administrator to set the **manage settings** permission to **Allow**.

## Set up Azure pipeline

For each repository an Azure pipeline should be setup:

1. Navigate to **Project** → **Pipelines** → **New Pipeline**.
2. **Connect to source code repository platform:** In the Connect tab, select the code repository platform, e.g. Azure DevOps, Bitbucket or GitHub.
3. **Select a repository**: In the Select tab, select a repository.
4. **Configure**: In the Configure tab, select a template, e.g. Starter pipeline. Azure will create an `azure-pipelines.yml` file in the root folder of the repository.
5. **Review**: In the Review tab, make any necessary edits.
6. **Save and run**: Choose **Save and run** to run the pipeline. Azure will display a commit message prompt. For this guide, choose **Commit directly to the main branch**. Choose **Save and run** again to close the prompt.
   1. A resource authorization error may be raised. Choose **Authorize resources**.
   2. The pipeline may require permission to run. Select **Job** to view the pipeline console output. From here the required permissions can be run. Select **Permit** to grant access

The pipeline will run using a Microsoft hosted agent.

If access to Azure DevOps Cloud is restricted due to corporate firewall rules or network policies, e.g. requiring VPN access to internal resources, an Azure self-hosted agent may be necessary. Azure agents can be [installed](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/agents) and used on GNU/Linux, macOS, Windows and Docker.

All Security Scan features available for Cloud are also supported in On-Prem environments. To set up an Azure Agent, please follow the Azure documentation below.

- [On-Prem Server 2022](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops-2022&tabs=yaml%2Cbrowser)
- [On-Prem Server 2020](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops-2020&tabs=yaml%2Cbrowser)
- [On-Prem Server 2019](https://learn.microsoft.com/en-us/previous-versions/azure/devops/pipelines/agents/agents?view=azure-devops-2019&tabs=yaml%2Cbrowser)

Note: If the agent download fails, a compatible version can be downloaded from the [Azure Pipelines Agent Releases](https://github.com/microsoft/azure-pipelines-agent/releases) page. Agent Compatibility for versions 3.x can be found [here](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/v3-agent).

## Set up pipeline for Pull Request events

To enable Pull Request scanning and automatated commenting for newly detected issues, the pipeline must be configured to trigger on Pull Request events. This feature is supported by Coverity, Polaris and Black Duck® SCA.

The configuration method depends on whether the pipeline is defined using Azure DevOps or the Azure Classic Editor.

**Azure DevOps**

A [Build Validation](https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies?view=azure-devops&tabs=browser#build-validation) policy must be setup on target branches (`main`, `develop`, etc.) to automatically trigger pipelines when code is pushed or Pull Requests are created.

For each target branch this can be achieved by selecting **Build validation policy** (Project > Project Settings > Repostories > Policies > Branch Policies > Add branch protection).

**Azure Classic Editor**

To trigger the pipeline for Pull Requests in Azure Classic Editor, perform the following steps.

1. Select the Triggers tab
2. Add branch filters, using values in one of the following tables.

   Table 1. Trigger on PR to main from any feature branch

   | Type | Branch specification |
   | --- | --- |
   | Exclude | Main |
   | Include | Feature/* |

   Table 2. Trigger on PR to main from a specific feature branch (e.g. feature/branch1)

   | Type | Branch specification |
   | --- | --- |
   | Exclude | Main |
   | Include | Feature/branch1 |

For further details, refer to the Microsoft documentation for [build completion triggers](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/pipeline-triggers-classic?view=azure-devops#add-a-build-completion-trigger)

## Configure Azure token

The `azure_token` parameter is required to provide the Black Duck Security Scan Extension with permission to add Pull Request comments, create fix Pull Requests and upload SARIF reports.

Table 3. Feature matrix for Black Duck security platforms using azure_token

| Platform | Pull Requests | | **SARIF upload** |
| --- | --- | --- | --- |
| **Comments** | **Fixes** |
| Black Duck® SCA | ✅ | ✅ | ✅ |
| Coverity | ✅ | ❌ | ❌ |
| Polaris | ✅ | ❌ | ✅ |
| Software Risk Manager | ❌ | ❌ | ❌ |

The Black Duck Security Scan Extension accepts an ephemeral build token or a Personal Access Token (PAT) as suitable values for the `azure_token` parameter.

Table 4. Minimum permissions required for tokens supported by the azure_token parameter

| Token | Description | Permissions | Example |
| --- | --- | --- | --- |
| [**System.AccessToken**](https://learn.microsoft.com/en-us/azure/devops/pipelines/build/variables?view=azure-devops&tabs=yaml#systemaccesstoken) | Built-in variable containing the ephemeral security token used by the running build. This is the **recommended** solution. | Ensure that **Contribute to pull requests** , **Create branch** and **Delete or disable repository** are set to **Allow** for the build service user in Project > Project Settings > Repository > Security | `azure_token: $(System.AccessToken)` |
| [**Personal Access Token (PAT)**](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows) | Generated by Azure DevOps upon [user setup](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows). Supports fine-grained permissions, with a configurable lifespan and must be stored in a secret variable for security. | Minimum permissions are: **Code-Full** and **Pull Request Threads-Read & Write**. | `azure_token: $(PAT_TOKEN)` |

## How to enable Advance Security?

A license is required to use Advanced Security. Details can be found here:  [Billing for GitHub Advanced Security for Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows)

**Which repository types are supported by Advanced Security?**

- The Advanced Security feature is supported in private and public repositories hosted on Azure DevOps.

To access the scanning tools and results, enable Advanced Security at the organization, project, or repository level.

**Organization-level onboarding**

1. Go to **Organization settings** for your Azure DevOps organization.
2. Select **Repositories**.
3. Select **Enable all**. An estimated number of active committers for your organization will appear.
4. Select **Begin billing** to activate Advanced Security for every existing repository in each project in an organization.
5. Optionally, select **Automatically enable Advanced Security for new repositories** so that newly created projects will have Advanced Security enabled.

**Project-level onboarding**

1. select **Project settings** for the Azure DevOps project.
2. Select **Repos**.
3. Select the **Settings** tab.
4. Select **Enable all**. An estimated number of active committers for the organization will appear.
5. Select **Begin billing** to activate Advanced Security for every existing repository in each project in the organization.
6. Optionally, select **Automatically enable Advanced Security for new repositories** so that newly created projects will have Advanced Security enabled.

**Repository-level onboarding**

1. Select **Project settings** for the Azure DevOps project.
2. Select **Repos** > **Repositories**.
3. Select the required repository.
4. Select **Enable all** and **Begin billing** to activate Advanced Security. A shield icon will appear in the repository view for repositories with Advanced Security enabled.

## Configure returned status in Classic Editor pipeline

1. Select: Classic Your Pipeline / Create a new Classic Editor Pipeline.
2. Select Black Duck Security Scan task → Go to Control Options → Check the field “Continue on error”.

   Note: When the “Continue on error” option is checked it becomes mandatory to use the returned status value in case of non-zero exit codes.
3. Add a new task in this Pipeline, e.g “Command Line Script”.
4. Select the Command Line Script task → Go to Control Options → Look for the “Run this task” field.
5. Select “Custom conditions” from the dropdown list.
6. Input an expected condition in the Custom condition input field. To use the returned status from Black Duck Security Scan task and run a new task conditionally, use a condition, similar to - `not(eq(variables['BlackDuckSecurityScan.status'], '0'))`.Subsequently, the new task will only execute when this condition (non-zero exit status) is met.It is also possible to print the returned status in the Command Line Script by adding the following to the Script section:

   ```
   echo Black Duck Security Scan exit status - $(BlackDuckSecurityScan.status)
   ```

   For conditional expressions further details are available at [Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/conditions?view=azure-devops).
7. Save and run the Classic Editor Pipeline to test the desired behavior.
