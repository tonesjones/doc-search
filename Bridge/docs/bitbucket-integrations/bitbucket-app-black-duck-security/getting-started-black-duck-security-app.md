---
title: "Getting started: Black Duck Security App"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/getting-started-black-duck-security-app.html"
content_id: "LKph49o8X8rIwX0qSrZFwQ"
version: "latest"
section: "Bitbucket Integrations"
scraped_at: "2026-08-08T23:48:53.160796+00:00"
---

# Getting started: Black Duck Security App

**Welcome to the Black Duck Security App user guide**

This guide helps you get started with the Black Duck Security App for Bitbucket. It explains the basic setup process, configuration options, and common operations you can perform while using the application.

The Black Duck Security App provides automated security scanning capabilities for your Bitbucket repositories, helping you identify vulnerabilities, license compliance issues, and security risks in your codebase.

The app will generate and deploy a workflow that is merged with selected repositories within a workspace for conducting scans for supported Black Duck platforms: Black Duck® SCA, Coverity or Polaris.

It is recommended that the following preliminary steps are performed:

- **Prerequisites**: Please read before installation.
- **Enable Bitbucket pipelines**: Ensure Bitbucket pipelines are enabled for a workspace or for a small selection of repositories where the workflow will be deployed.
- **Bitbucket secrets and variables setup**: Setup secrets and variables referenced within the generated workflow file at the workspace level or for a small selection of repositories where the workflow will be deployed. This section includes recommended guidance on configuring a Bitbucket token to allow the workflow to perform post scan operations, e.g., injecting Pull Request comments.

## Enable Bitbucket pipelines

The Black Duck Security App provides an interface to configure, generate and deploy a workflow file to selected repositories. Subsequently, it is necessary to ensure that Bitbucket pipelines are enabled.

**Enable Bitbucket pipelines in the UI**

To enable Bitbucket Pipelines for a specific repository in the Bitbucket web UI:

1. Log in to your [Bitbucket account](https://bitbucket.org/product).
2. Navigate to target repository.
3. In the left-hand sidebar, navigate to Repository settings > Pipelines > Settings.
4. Toggle the option to **Enable pipelines**.

## Bitbucket secrets and variables setup

The generated workflow file, by default references variables, secrets and a Bitbucket Token.

This section explains an overview for how to add variables, secrets and token at the workspace and repository level.

Before proceeding, ensure all requirements in the Black Duck Security Prerequisites are met.

Note: Ensure all required variables, secrets and Bitbucket Token are configured before proceeding to generate the scan workflow for review and deployment. If customized names are needed, then the generated workflow file must be updated to reflect the new names. This can be done at the stage when reviewing the workflow.

Please refer to the appropriate platform documentation for an overview of the required secrets and variables:

- Black Duck® SCA
- Coverity
- Polaris

**Workspace level configuration (recommended)**

Variables specified for a workspace can be accessed from all repositories that belong to the workspace. You must be an administrator to manage workspace variables.

1. From the profile avatar menu select a workspace.
2. Select the **Settings** cog on the top navigation bar.
3. Select **Workspace settings** from the **Settings** dropdown menu.
4. From the sidebar menu, select Pipelines > Workspace variables

Workspace variables can be overridden by repository variables.

Workspace variables can be accessed by all users with the *write* permission for any repository (private or public) that belongs to the team or account.

You must be an administrator of a workspace or a repository to manage variables respectively.

**Repository level configuration**

Pipeline variables added at the repository level can be used by any user who has write access in the repository. To access and configure the repository variables, the user must be an **admin** of that repository.

From the repository, repository variables can be managed in Repository settings > Pipelines > Repository variables.

**Configure Bitbucket token**

A Bitbucket token is required to enable the workflow to add Pull Request comments, raise Auto Fix Pull Requests and upload SARIF reports. For details on the supported types of Bitbucket tokens see Configure Bitbucket API token.

Note: The generated workflows require secret `BRIDGE_BITBUCKET_API_TOKEN` to be defined.

## Install and authorize

The Black Duck Security App for Bitbucket provides access to a central user interface where you can configure and deploy security scan workflows to selected repositories within your workspace.

1. The app is available in [Atlassian Marketplace](https://marketplace.atlassian.com/apps/3177098645/black-duck-security?hosting=cloud&tab=overview) and you can install the app from the following [Distribution](https://developer.atlassian.com/console/install/bdc49953-773e-4ecf-9f2d-2ebf48d9d66b?signature=AYABeJw0MbE5EAqpNPXawJgBtRwAAAADAAdhd3Mta21zAEthcm46YXdzOmttczp1cy13ZXN0LTI6NzA5NTg3ODM1MjQzOmtleS83MDVlZDY3MC1mNTdjLTQxYjUtOWY5Yi1lM2YyZGNjMTQ2ZTcAuAECAQB4IOp8r3eKNYw8z2v%2FEq3%2FfvrZguoGsXpNSaDveR%2FF%2Fo0BlDvCatZx4eCgnvL8Vt4ltAAAAH4wfAYJKoZIhvcNAQcGoG8wbQIBADBoBgkqhkiG9w0BBwEwHgYJYIZIAWUDBAEuMBEEDNb9wKypl%2BEDajdmAgIBEIA72Ey9Mlpq%2F6%2FLBXV3w9lLTtEm%2BzN6o5A%2BiOE1BoeNB6eMUOSa7aKLAZxWZUnH75IDuXV9WSQ34nXHlMAAB2F3cy1rbXMAS2Fybjphd3M6a21zOmV1LXdlc3QtMTo3MDk1ODc4MzUyNDM6a2V5LzQ2MzBjZTZiLTAwYzMtNGRlMi04NzdiLTYyN2UyMDYwZTVjYwC4AQICAHijmwVTMt6Oj3F%2B0%2B0cVrojrS8yZ9ktpdfDxqPMSIkvHAHPFnAYKZ7Bwp1bmdX0lgZIAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMqRA0UtVmZCSlm3lcAgEQgDs3dCGNw2WxKkyxETh1YKavVnjgZWAgDOWP6WTULCXy1dVvW%2B%2Bjqo28T%2BGAXVDWOKfqmXSuZnI4KjTaDAAHYXdzLWttcwBLYXJuOmF3czprbXM6dXMtZWFzdC0xOjcwOTU4NzgzNTI0MzprZXkvNmMxMjBiYTAtNGNkNS00OTg1LWI4MmUtNDBhMDQ5NTJjYzU3ALgBAgIAeLKa7Dfn9BgbXaQmJGrkKztjV4vrreTkqr7wGwhqIYs5AZeWZirPS6srVKKET212uo8AAAB%2BMHwGCSqGSIb3DQEHBqBvMG0CAQAwaAYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAyNUvZnG7R4c7%2FQ71wCARCAO6XNMUKs%2BU9WNi26jlsPWBqTIwOlxPIrZ7ORpq36uSZIh71uTUwgy8xfq0DBKAL9QiN9%2F6wHF%2FcjYSccAgAAAAAMAAAQAAAAAAAAAAAAAAAAAH6IpMD1cAOhJ7OGwftge3T%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAADKazWTol9M2SYlyCpz7K3aWE6ECSpjiGPAAY5rMh9bQfl3D%2B8GOR3ciPWwKAtTcML2F4%2Fop2E2vNCPlsP3P3z8zKcg%3D&product=bitbucket) link.
2. Click on the Get App button
3. Select the Bitbucket workspace for where to install the app
4. Click the Install button
5. Navigate to the Bitbucket workspace where the app was installed
6. Click the settings cog icon displayed in the top right corner of the menu navigation bar
7. Select Workspace settings > Forge Apps > Black Duck Security For Bitbucket Cloud
8. Follow the install instructions below

Use the installer to select and configure the repositories to be onboarded from a Bitbucket workspace. On first use, the installer must be granted permission to access repositories in the selected workspace. The required permissions and configuration steps are explained below.

**Install**

Click the `Blackduck Security Setup` button to redirect to the configuration interface. Alternatively, visit the [**Onboarding**](https://integrations.blackduck.com/onboard/) URL and click the Bitbucket button to to log in and start onboarding.

Use the documentation link to access supporting documentation for the Black Duck Security App.

[image: Bitbucket app install screen]

**Authorize**

When first accessing the Black Duck Security App, a prompt will be displayed to authorize the following permissions:

- Read your account information
- Read your workspace's project settings and read repositories contained within your workspace's projects
- Read and modify your repositories and their Pull Requests
- Read your team membership information

Click **Grant access** to proceed.

[image: Black Duck Security App Permissions]

## Onboarding process

Upon successful authentication, you'll be redirected to the Black Duck onboarding screen to select a workspace and the associated repositories where a workflow YAML file will be generated and committed as a Pull Request for running scans.

[image: Workspace and repository selection screen]

Take a moment to review the dashboard components:

1. **Select repositories:** Select the repositories within a workspace where configured scans will be deployed to.
2. **Configure options:** Configure scan options for specific Black Duck platforms such as Black Duck® SCA, Coverity and Polaris.
3. **Review workflow.yml**: Review a preview of the generated Bitbucket workflow that will be deployed to the selected repositories for performing a Black Duck security scan.

   Note: If a `bitbucket-pipelines.yml` exists, then the generated configuration will be merged into the existing yml file
4. **Summary**: Summarizes the count of repositories where the workflow will be deployed to. At this stage the workflow can be submitted for deployment.

## Configure scan workflow

The Dashboard UI can be used to configure which repositories within a workspace a workflow will be deployed to. A workflow can be configured for the following Black Duck platforms:

- Black Duck® SCA
- Coverity
- Polaris

**Step 1: Select repositories**

Use the `Select Repositories` screen to configure which repositories within the workspace should be scanned. [image: Select Repositories screen]

1. Use the **Workspace** drop down list to select the workspace.

   Note: The app automatically discovers and displays repositories based on the selected workspace.
2. Select the repositories that the generated workflow should be configured and deployed to:

   Note: When a `bitbucket-pipelines.yml` file already exists in a repository, the generated workflow content will be merged into the existing pipeline.

   1. **All repositories**: Configure and deploy the workflow to all repositories within the workspace.
   2. **Selected repositories**: Select the repositories from a list. Use the following filter operations for assistance with repository selection:

      - **Search**: Filter by name or last updated time.
      - **Sort**: Click the `Repository`, `Project` or `Last Updated` column to order the repository list by name, project or date.
      - **Pagination**: Navigate the available repositories using the pagination buttons.
      - **Show only selected**: Display selected repositories in the list only.

One or more search filters can added to filter the repository list. This is achieved using the `Add filters` drop down list. The following filters can be combined and applied to repositories:

1. **Language:** Select one or more programming languages from this dropdown to filter the repository list by language. [image: Language filter screen]
2. **Project:** Select one or more projects from the dropdown list to filter repositories by project. [image: Project filter screen]
3. **Visibility:** Select either public or private to filter the repository list accordingly. [image: Visibility filter screen]

Note: Bitbucket Cloud does not provide automatic language detection for repositories. The language property in the repository metadata is not inferred from source code and remains empty unless explicitly set.

**For the language filter to function correctly in the UI or for API integrations, repository administrators must manually assign a language in the repository’s settings:**

1. Navigate to Repository Settings > Repository Details > Advanced
2. Select the appropriate language from the **Language** dropdown
3. Save changes

Only repositories with a manually defined language will appear under the language filter options. Repositories without a set language will be excluded from any specific language filter.

**Step 2: Configure scan options**

The Dashboard can be used to automatically generate a Bitbucket workflow file based on scan options specified in the `Configure Options` screen. The generated Bitbucket workflow will be deployed to the selected repositories. [image: Bitbucket App Global Scan Options]

The screen illustrated above highlights that the following options can be configured:

- **Branches**: Scans can be configured to trigger in response to push events and when a Pull Request is created or updated. Use the `push events` and `pull request` text boxes to specify which branches will initiate scans for each type of event.
- **Runner**: Choose the environment for the runner by specifying the tag name of the runner. If the runner is windows, the **windows** tag is required along with any other runner tag. Runner tags are comma-separated, for example: `windows`, `my.runner`.
- **Platform**: Select the Black Duck platform for scanning in the repository. Supported platforms include Coverity, Black Duck® SCA and Polaris. Upon selection, the Dashboard UI will dynamically update to display platform scan-specific options and instructions, such as which Bitbucket variables and secrets are required for the generated workflow to run successfully.
- **Scan method:** Choose between:

  - `CLI (default)`: Generate a scan workflow that downloads the latest Bridge CLI and uses it directly to perform a security scan.
  - `Bitbucket Pipe`: Generate a scan workflow that uses Black Duck Security Scan Pipe.

    Important: Bitbucket Pipe workflows are supported by Atlassian for Linux platforms only (Bitbucket cloud and self-hosted runners).

Note: Ensure all required Bitbucket variables and secrets are configured before clicking **Next** to proceed with generating a scan workflow for review and deployment.

Refer to the Black Duck platform documentation pages for further details of scan configuration options and prerequisites:

- Black Duck® SCA
- Coverity
- Polaris

## Review workflow

The `Review bitbucket-pipelines.yml` screen allows a generated workflow to be previewed and edited before submission for deployment.

Note: The generated workflow can include multiple scan jobs for different Black Duck platforms, such as Black Duck® SCA, Coverity or Polaris. To add a new scan job, return to the `Configure options` screen and select a different Black Duck platform. Subsequently, when navigating back to the `Review bitbucket-pipelines.yml` screen, the generated `bitbucket-pipelines.yml` will be displayed with the configured options for the selected platform (Black Duck® SCA, Coverity or Polaris).

The `Review bitbucket-pipelines.yml` screen is illustrated below with an example generated workflow for Black Duck® SCA. Refer to the following documentation pages for sample workflow jobs generated for each Black Duck platform:

- Black Duck SCA
- Coverity
- Polaris

The remainder of this section explains the workflow review process.

[image: Review bitbucket-pipelines.yml screen]

The `Review bitbucket-pipelines.yml` screen displays a Bitbucket workflow containing a single scan job, specifically added for selected Black Duck platforms.

The workflow is automatically generated for deployment to the selected repositories and simplified to include only the minimum fields required (e.g., default values for the product scans are omitted unless specified). When a repository already contains a `bitbucket‑pipelines.yml` file, the new workflow content is merged into the existing file rather than replacing it.

Inline editing of the workflow is available by clicking the `Edit` button. The editor automatically validates the syntax, preventing saves if errors are detected. It also issues warnings for potential issues, such as hardcoded secrets or variables, which do not block saving.

Note: Bitbucket runs your pipeline based on the bitbucket-pipelines.yml file in your repository's root.

1. Review and adjust the generated workflow as needed:
   - Use the `Edit` button to make direct edits to the bitbucket-pipelines.yml file, such as:

     - Modify trigger conditions, including which branches will trigger a scan.
     - Adjust scan configuration parameters.
     - Required credentials and tokens.
     - Add custom steps or integrations.
2. When required changes have been made, then perform one of the following options:
   1. Click the **Previous** button to configure scan options for a different Black Duck platform. Subsequently, when the `Review bitbucket-pipelines.yml` screen is revisited a scan job will be created or merged with the workflow for that platform.If a `bitbucket‑pipelines.yml` file already exists in a repository selected for onboarding, the workflow content will be merged into the existing file rather than replaced.

      Note: After editing the workflow, if the `Previous` button is selected, the UI will warn that the edits you made will be lost permanently.
   2. Click the **Next** button to confirm that the workflow has been reviewed and all necessary amendments have been made.

## Deploy workflow

The `Summary` screen displays the count of repositories where the `bitbucket-pipelines.yml` will be deployed by raising a Pull Request.

[image: Bitbucket App Deploy Summary Screen]

To submit a workflow for deployment across the selected repositories follow the steps below:

1. Review the deployment summary:

   Note: Check that the count of selected repositories and workflow filename (e.g., `bitbucket-pipelines.yml`) is as expected. Use the `Previous` button to navigate back to adjust if necessary.
2. The yml file will be committed as a Pull Request.
3. Click the **"Submit"** button and confirm deployment in the modal dialog.
4. Monitor the deployment progress in the onboarding status screen illustrated below, which will update every 10 seconds.

   Note: For repositories with branch protection rules the app automatically creates Pull Requests (PRs) to inject workflows. Review and manually merge Pull Requests using provided links to enable scans.
5. Review the **Failed Repositories List** for any deployment issues.

[image: Review failed repositories list checks] [image: Review failed repositories list for deployment issues]

## Troubleshooting and support

The table below summarizes common issues and their resolutions.

| Issue type | Issue | Symptoms | Solution |
| --- | --- | --- | --- |
| **Authentication** | OAuth Authorization Failed | OAuth Authorization Failed | - Clear browser cache and cookies - Ensure correct Bitbucket account is logged in - Check workspace membership status - Retry the authorization process |
| **Permissions** | Insufficient Repository Access | Error: `403 Forbidden` when accessing repository | - Verify repository collaboration status - Request elevated permissions from repository owner - Check workspace membership |
|  | Bitbucket CI/CD pipelines unavailable | Pipelines tab not visible in the repository | - Enable pipelines in repository settings - Check workspace pipelines policies - Verify the repository is not archived |
| **Workflow deployment** | Workflow Creation Failed | Deployment stuck in `In Progress` status | - Check repository write permissions - Verify branch protection rules - Confirm pipelines are enabled - Review deployment logs in portal |
