---
title: "Getting Started: Black Duck Security Bulk Onboarding"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/getting-started-black-duck-security-bulk-onboarding.html"
content_id: "8R1aCX26R7LClWR~u9zyaA"
version: "latest"
section: "GitLab Integrations"
scraped_at: "2026-08-08T23:47:56.893062+00:00"
---

# Getting Started: Black Duck Security Bulk Onboarding

**Welcome to the Black Duck Security Bulk Onboarding user guide**

This guide helps you get started with Black Duck Security Bulk Onboarding for GitLab. It explains the basic setup process, configuration options, and common operations you can perform while using the application.

Black Duck Security Bulk Onboarding provides automated security scanning capabilities for your GitLab projects, helping you identify vulnerabilities, license compliance issues and security risks in your codebase.

The bulk onboarding solution will generate and deploy a workflow that is merged with selected repositories within a group for conducting scans for supported Black Duck platforms: Black Duck® SCA, Coverity or Polaris.

It is recommended that the following preliminary steps are performed:

- **Prerequisites**: Please read before using the bulk onboarding solution.
- **CI/CD Variables setup**: Setup variables referenced within the generated workflow file at the group level or subgroup level or for a small selection of projects where the workflow will be deployed. This section includes recommended guidance on configuring a GitLab Personal Access Token to allow the workflow to perform post scan operations, e.g., injecting Merge Request comments, creating Fix Merge Requests.

## GitLab CI/CD variables setup

The generated workflow file, by default references variables, secrets and a GitLab Personal Access Token.

This section explains an overview for how to add variables, secrets and token at the workspace and repository level.

Before proceeding, ensure all requirements in the Black Duck Security Prerequisites are met.

Note: Ensure all required variables, secrets and GitLab Personal Access Token are configured before proceeding to generate the scan workflow for review and deployment. If customized names are needed, then the generated workflow file must be updated to reflect the new names. This can be done at the stage when reviewing the workflow.

Please refer to the appropriate platform documentation for an overview of the required secrets and variables:

- Black Duck® SCA
- Coverity
- Polaris

**Group level configuration (recommended)**

Variables specified for a group can be accessed from all projects that belong to the group. You must be an owner to manage group variables.

1. Go to GitLab.com
2. Click on the GitLab Home cog from the top left of the GitLab page.
3. Select Groups from the left navigation bar.
4. Select a particular group for which you want to onboard GitLab workflow.
5. Select CI/CD from the Settings dropdown menu.
6. From the Variables dropdown click on Add variable
   1. For adding a secret, use Masked or Masked and hidden option
   2. Uncheck Protect variable from the flags option
   3. Specify the Key and Value
   4. Click on Add Variable to save

      Note: A protected variable in GitLab CI/CD is only available to pipelines running on protected branches or protected tags.
      - If Protect variable is unchecked, the variable can be used by pipelines on any branch.
      - If Protect variable is checked, the variable will not be available in Merge Request pipelines and will only work on protected branches or tags.

Group variables can be overridden by subgroup/project variables.

Group variables can be accessed in the CI/CD pipeline by all users with the *write* access for any project (private or public).

You must be an owner of a group to manage variables.

**Subgroup level configuration**

CI/CD variables added at the subgroup level can be used by any user who has write access in the projects inside the subgroup. To access and configure the subgroup variables, the user must be an **owner** of that subgroup.

From the subgroup's settings, subgroup variables can be managed in Subgroup Settings > CI/CD > Variables > Add variable

**Project level configuration**

Pipeline variables added at the project level can be used by any user who has write access in the project. To access and configure the project variables, the user must be an **owner/maintainer** of that project.

From the project's settings, project variables can be managed in Project Settings > CI/C > Variables > Add variable.

**Configure GitLab Personal Access Token**

A GitLab Personal Access Token is required to enable the workflow to add Merge Request comments and raise Auto Fix Merge Requests. For details on the supported types of GitLab tokens see Configure GitLab User Token.

## GitLab OAuth 2.0 authorization

When first accessing Black Duck Security Bulk Onboarding, a prompt will be displayed to authorize the following permissions:

- Read your personal information
- Access the API on your behalf

Click **Authorize Black Duck Security** to proceed.

s [image: OAuth Authorization Screen]

## Onboarding process

Upon successful authentication, you'll be redirected to the onboarding screen to select a group or personal account and the associated repositories where a workflow YAML file will be generated and committed as a Merge Request for running scans.

Note: For authentication, GitLab OAuth 2.0 is being used with 2 permission scopes: `api` and `read_user`

[image: Initial Display Of Repositories Screen]

Take a moment to review the dashboard components:

- **Select projects**: Select the projects within a group or personal account where configured scans will be deployed to.
- **Configure options**: Configure scan options for specific Black Duck platforms such as Black Duck® SCA, Coverity and Polaris.
- **Review product-ci.yml**: Review a preview of the generated GitLab workflow that will be deployed to the selected projects for performing a Black Duck security scan.

  Note: When a `product-ci.yml` already exists in a project, it will replace the existing content. However, if a `.gitlab-ci.yml` exists, then the generated configuration will be merged into the existing yml file using an include reference of the `product-ci.yml`. If a `.gitlab-ci.yml` does not exist, a new .`gitlab-ci.yml` will be created along with the `product-ci.yml` file and submitted as a Merge Request.
- **Summary**: Summarizes the count of projects where the workflow will be deployed to. At this stage the workflow can be submitted for deployment.

## Configure scan workflow

The Dashboard UI can be used to configure which projects within a group or personal account a workflow will be deployed to. A workflow can be configured for the following Black Duck platforms:

- Black Duck® SCA
- Coverity
- Polaris

**Step 1: Select projects**

Use the `Select Projects` screen to configure which projects within the group or personal account should be scanned.

[image: image]

1. Use the **Group or Personal account** drop down list to select the group or personal account.

   Note: The onboarding solution automatically discovers and displays projects based on the selected group or personal account.
2. Select the projects that the generated workflow should be configured and deployed to:

   Note: When a `product-ci.yml` already exists in a project, it will replace the existing content. However, if a `.gitlab-ci.yml` exists, then the generated configuration will be merged into the existing yml file using an include reference of the `product-ci.yml`. If a `.gitlab-ci.yml` does not exist, a new .`gitlab-ci.yml` will be created along with the `product-ci.yml` file and submitted as a Merge Request.

   1. **All Projects**: Configure and deploy the workflow to all projects within the group or personal account.
   2. **Selected projects**: Select the projects from a list. Use the following filter operations for assistance with project selection:
      - **Search**: Filter by repository name (at least 3 character should be specified).

**Step 2: Configure scan options**

[image: image] The Dashboard can be used to automatically generate a GitLab workflow file based on scan options specified in the `Configure Options` screen. The generated GitLab workflow will be deployed to the selected repositories.

The screen illustrated above highlights that the following options can be configured:

- **Branches**: Scans can be configured to trigger in response to push events and when a Merge Request is created or updated. Use the `push events` and `merge request` text boxes to specify which branches will initiate scans for each type of event.
- **Runner tag**: Choose the environment for the GitLab runner. To generate runner OS specific scripts, select **Mac/Linux** or **Windows** from the `Runner Configuration` option. By default, a Mac/Linux (Bash) script will be generated. Runner tags are comma-separated, for example: `docker,linux,group1-runner`.

  Note: Please select only one type of runner tags (either Mac/Linux or Windows) for the selected projects. If you mix runner types, the workflow may fail because the scripts use different shells (bash vs. PowerShell).
- **Platform**: Select the Black Duck platform for scanning in the project. Supported platforms include Coverity, Black Duck® SCA and Polaris. Upon selection, the Dashboard UI will dynamically update to display platform scan-specific options and instructions, such as which GitLab CI/CD variables are required for the generated workflow to run successfully.
- **Scan method:** Choose between:
  - `GitLab Template (recommended)`: Generate a scan workflow that uses Black Duck Security Scan Template.
  - `CLI - Black Duck Bridge CLI`: Generate a scan workflow that downloads the latest Bridge CLI and uses it directly to perform a security scan.

  Note: Ensure all required GitLab CI/CD variables are configured before clicking **Next** to proceed with generating a scan workflow for review and deployment.

Refer to the Black Duck platform documentation pages for further details of scan configuration options and prerequisites:

- Black Duck® SCA
- Coverity
- Polaris

## Review workflow

The `Review product-ci.yml` screen allows a generated workflow to be previewed and edited before submission for deployment.

Note: The generated workflow can include multiple scan jobs for different Black Duck platforms, such as Black Duck® SCA, Coverity or Polaris. To add a new scan job, return to the `Configure options` screen and select a different Black Duck platform. Subsequently, when navigating back to the `Review product-ci.yml` screen, the generated `product-ci.yml` will be displayed with the configured options for the selected platform (Black Duck® SCA, Coverity or Polaris).

The `Review blackducksca-ci.yml` screen is illustrated below with an example generated workflow for Black Duck® SCA. Refer to the following documentation pages for sample workflow jobs generated for each Black Duck platform:

- Black Duck® SCA
- Coverity
- Polaris

The remainder of this section explains the workflow review process.

[image: Review workflow screen example]

The  `Review blackducksca-ci.yml`  screen displays a GitLab workflow containing a single scan job, specifically added for selected Black Duck platforms.

The workflow is automatically generated for deployment to the selected projects and simplified to include only the minimum fields required (e.g., default values for the product scans are omitted unless specified). When a `blackducksca-ci.yml` already exists in a project, it will replace the existing content. However, if a `.gitlab-ci.yml` exists, then the generated configuration will be merged into the existing yml file using `include` reference of the `blackducksca-ci.yml` and if `.gitlab-ci.yml` does not exist, a new `.gitlab-ci.yml` will be created along with the `blackducksca-ci.yml` file and submitted as merge request.

Inline editing of the workflow is available by clicking the `Edit` button. The editor automatically validates the syntax, preventing saves if errors are detected. It also issues warnings for potential issues, such as hardcoded secrets or variables, which do not block saving.

Note: GitLab runs your pipeline based on the `.gitlab-ci.yml` file in your project's root.

1. Review and adjust the generated workflow as needed: Use the **Edit** button to make direct edits to the workflow.yml file, such as:
   - Modify trigger conditions, including which branches will trigger a scan.
   - Adjust scan configuration parameters.
   - Required credentials and tokens.
   - Add custom steps or integrations.
2. When required changes have been made, then perform one of the following options:
   1. Click the **Previous** button to configure scan options for a different Black Duck platform. Subsequently, when the `Review blackducksca-ci.yml` screen is revisited a scan job will be created or merged with the workflow for that platform. When a `blackducksca-ci.yml` already exists in a project, it will replace the existing content. However, if a `.gitlab-ci.yml` exists, then the generated configuration will be merged into the existing yml file using `include` reference of the `blackducksca-ci.yml` and if `.gitlab-ci.yml` does not exist, a new `.gitlab-ci.yml` will be created along with the `blackducksca-ci.yml` file and submitted as Merge Request.

      Note: After editing the workflow, if the `Previous` button is selected, the UI will warn that the edits you made will be lost permanently.
   2. Click the **Next** button to confirm that the workflow has been reviewed and all necessary amendments have been made.

## Deploy workflow

The `Summary` screen displays the count of projects where the `blackducksca-ci.yml` will be deployed by raising a Merge Request.

[image: Deploy Workflow Summary Screen]

To submit a workflow for deployment across the selected projects follow the steps below:

1. Review the deployment summary:

   Note: Check that the count of selected repositories and workflow filename (e.g., `blackducksca-ci.yml`) is as expected. Use the `Previous` button to navigate back to adjust if necessary.
2. The yml file will be committed as a Merge Request and with necessary changes in `.gitlab-ci.yml` file.
3. Click the Submit button and confirm deployment in the modal dialog.
4. Monitor the deployment progress in the onboarding summary screen illustrated below, which will update every 10 seconds.
5. Review the Failed Projects List for any deployment issues.

[image: image]

[image: Deploy Workflow Failed Repositories Summary]

## Automatic Merge Request creation

Currently GitLab onboarding process is available through creating Merge Requests only. While creating Merge Requests, below approach is followed:

1. `product-ci.yml`
   - Already exists: The existing `product-ci.yml` will be replaced with the newly generated content.
   - Does not exist: A new `product-ci.yml` will be created.
2. `.gitlab-ci.yml`
   - Already exists: The pipeline setup will be merged into the existing file by adding:
     - an `include` reference that points to the generated `product-ci.yml`
     - a stage name `blackduck_security` in `stages` section to queue up the job specified in `product-ci.yml`
   - Does not exist: A new `.gitlab-ci.yml` file will be created and both files will then be submitted together as a merge request.

     Note: If the `product-ci.yml` is already referenced inside `.gitlab-ci.yml`, then there will be no modification in `.gitlab-ci.yml` file content and only `product-ci.yml` will be submitted as a merge request.

## Troubleshooting and support

| Issue type | Issue | Symptoms | Solution |
| --- | --- | --- | --- |
| **Authentication** | OAuth authorization failed | OAuth authorization failed | - Clear browser cache and cookies - Ensure correct GitLab account is logged in - Retry the authorization process |
| **Permissions** | Insufficient project access | Error: `403 Forbidden` when accessing project | - Verify project collaboration status - Request elevated permissions from repository owner |
| **Workflow deployment** | Workflow creation failed | Deployment stuck in `In Progress` status | - Check project write permissions - Check if required GitLab CI/CD variables are configured correctly - Review deployment logs in portal - Check error message if available in Summary page. |
| **Workflow scan execution** | Bash/Powershell script injection failed | GitLab pipeline failed | - Check if `product-ci.yml` is correctly injected inside `.gitlab-ci.yml` - Check if `blackduck_security` is correctly queued under `stages` - Check if runner tags are correct or runner is accessible for the project. - Check if the generated scripts (bash vs powershell) is correct with specified runner tags - Check if mixer of runner tags (both Linux/MacOS and Windows) are specified |
