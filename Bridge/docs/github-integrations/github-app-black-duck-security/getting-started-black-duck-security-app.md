---
title: "Getting started: Black Duck Security App"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/getting-started-black-duck-security-app.html"
content_id: "YsrE0ygoBLMbJ0aB6tfQDw"
version: "latest"
section: "GitHub Integrations"
scraped_at: "2026-08-08T23:47:38.305228+00:00"
---

# Getting started: Black Duck Security App

**Welcome to the Black Duck Security App user guide**

This guide helps you get started with the Black Duck Security App for GitHub. It explains the basic setup process, configuration options and common operations you can perform while using the application.

The Black Duck Security App provides automated security scanning capabilities for your GitHub repositories, helping you identify vulnerabilities, license compliance issues, and security risks in your codebase.

The app will generate and deploy a workflow file to selected repositories within a workspace for conducting scans for supported Black Duck platforms: Black Duck® SCA, Coverity or Polaris.

It is recommended that the following preliminary steps are performed:

- **Prerequisites**: Please read before installation.
- **Enable GitHub Actions**: Ensure GitHub Actions are enabled for an organization or for a small selection of repositories where the workflow will be deployed.
- **GitHub secrets and variables setup**: Setup secrets and variables referenced within the generated workflow file at the organization level or for a small selection of repositories where the workflow will be deployed. This includes recommended guidance on configuring a GitHub token to allow the workflow to perform post scan operations, e.g. injecting Pull Request comments.

## Enable GitHub actions

The Black Duck Security app provides an interface to configure, generate and deploy a workflow file to selected repositories. Subsequently, it is necessary to ensure that GitHub Actions are enabled.

**Enable actions at the organization level**

To configure GitHub Actions for the Black Duck Security App:

1. Navigate to **Organization Settings → Actions → General**.
2. Under **Actions permissions**, select one of the following:
   - **Allow all actions and reusable workflows** (recommended for ease of use).
   - **Allow select actions and reusable workflows** (for restricted access):

     - Enable **Allow actions created by GitHub**.
     - Enable **Allow actions by Marketplace verified creators**.

For custom actions related to Black Duck Security Scan, if you want to restrict to specific actions, add the following to your allowed actions list:

```
blackduck-inc/black-duck-security-scan@*
```

See [Managing GitHub Actions permissions for your organization](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization) for more information.

**Enable actions at the repository level**

If deploying to a small set of repositories, then for each repository where scans will be executed:

1. Navigate to **Repository Settings → Actions → General**.
2. Select **Allow all actions and reusable workflows**.

## GitHub secrets and variables setup

The generated workflow file, by default references variables, secrets and a GitHub Token.

This section explains an overview for how to add secrets and variables at the organization and repository level. This also includes configuring a GitHub token to enable the workflow to add Pull Request comments, raise Auto Fix Pull Requests and upload SARIF reports.

Before proceeding, ensure all requirements in the Black Duck Security Prerequisites are met.

Note: Ensure all required GitHub variables, secrets and GitHub Token are configured before proceeding to generate the scan workflow for review and deployment. If customized names are needed, then the generated workflow file must be updated to reflect the new names. This can be done at the stage when reviewing the workflow.

Please refer to the appropriate platform documentation for an overview of the required secrets and variables:

- Black Duck® SCA
- Coverity
- Polaris

**Organization level configuration (recommended)**

To manage secrets across multiple repositories:

1. Navigate to **Organization Settings → Secrets and variables → Actions**.
2. Use the **Variables** tab to add non-sensitive configuration values.
3. Use the **Secrets** tab for authentication tokens.

**Repository level configuration**

For private repositories (or specific repository needs):

1. Navigate to **Repository Settings → Secrets and variables → Actions**.
2. Use the **Variables** and **Secrets** tabs to configure variables and secrets as required for the specific repository.

**Configure GitHub token**

To enable advanced features such as SARIF upload, Auto Fix Pull Requests and Pull Request comments, the Black Duck Security Scan Action sets the `github_token` parameter in the generated workflow file.

By default, provide users with the option to use the built-in GitHub token (`secrets.GITHUB_TOKEN`) with additional permissions configured in the workflow YAML.

This should be used, if it is possible to modify the token's default privileges to include write access.

**Using GitHub built-in token** (`secrets.GITHUB_TOKEN`) **(recommended default)**:

- If you select this option (default: yes), the generated workflow will:

  - Use `secrets.GITHUB_TOKEN`.
  - Include a static permissions block for `repo` and `workflow` scopes to grant required write access for post-scan actions (e.g., Pull Requests, comments).
  - Add a comment explaining the addition of the token.
- To configure permissions navigate to (**GitHub** → **Project** → **Settings** → **Actions** → **General** → **Workflow Permissions**).
- The token will be automatically created by GitHub at the start of each workflow run.

Note: When using GitHub’s built-in `GITHUB_TOKEN`, please ensure the following settings are enabled under **Settings →****Actions → General → Workflow Permissions**:

- **Read and write permissions**
- **Allow GitHub Actions to create and approve pull requests**

These permissions are necessary for workflows that automatically generate and approve pull requests.

For **GitHub Enterprise Cloud** users, these configurations may be managed through **Enterprise Policies**.

It is recommended to verify that the required permissions are allowed at the **Enterprise level**, since these can override organization or repository settings.

**Personal Access Token (PAT) setup**

1. Navigate to **Profile settings → Developer settings → Personal access tokens**.
2. Click **Generate new token** → **Tokens (classic)**.
3. Select the following scopes:

   - `repo` - Full access to private and public repositories.
   - `workflow` - Access to GitHub Actions and artifact uploads.
4. If you are using any custom name for the secret, e.g. `CUSTOM_TOKEN`, make sure to edit the workflow file accordingly as `github_token`: `secrets.CUSTOM_TOKEN` for Actions or

   `BRIDGE_GITHUB_USER_TOKEN: secrets.CUSTOM_TOKEN` for bridge-cli mapping.
5. For more information, see [Granting Additional Permissions](https://docs.github.com/en/actions/security-guides/automatic-token-authentication#granting-additional-permissions).

## Installation via GitHub Marketplace

1. Navigate to the Black Duck Security App in the [GitHub Marketplace](https://github.com/marketplace/black-duck-security).

   Note: It is necessary to connect a GitHub account to enable selection of repositories from an organization or personal profile.

   [image: Black Duck Security App GitHub Marketplace]
2. Click **Install It For Free** under the **plans and pricing** section.
3. Select the installation scope:
   - **All repositories** (organization-wide).
   - **Selected repositories** (specific repositories).
4. Review and authorize permissions (OAuth scopes: read:org, repo, workflow, admin:org_hook).
5. Update permissions if needed (e.g., grant access to additional repositories).
6. Click **Install & Authorize** to complete the installation. You will be redirected to the Black Duck Central UI at <https://integrations.blackduck.com/onboard/>.

[image: Black Duck Security App select repositories during install]

Proceed to onboarding process for an overview of how to onboard repositories.

## Installation via Black Duck Security integrations

1. Navigate to <https://integrations.blackduck.com/onboard/>.
2. Sign in to GitHub if prompted to do so.
3. Click the **Authorize Black Duck Security** button when prompted, to grant permission to retrieve the names of organizations and repositories. The `Let's Get Started With Black Duck` screen will be displayed.
4. Click **Install On GitHub** button on the **Let's Get Started With Black Duck** screen.[image: Let’s get started with Black Duck screenshot]
5. The installer will redirect to <https://github.com/apps/black-duck-security>.
   1. Click on **Install** button.
   2. Select the profile or organization where the GitHub app should be installed.
6. Select the installation scope:
   - **All repositories** (organization-wide).
   - **Selected repositories** (specific repositories).
7. Review and authorize permissions (OAuth scopes: read:org, repo, workflow, admin:org_hook).
8. Update permissions if needed (e.g., grant access to additional repositories).
9. Click **Install & Authorize** to complete the installation. You will be redirected to the Black Duck Central UI at <https://integrations.blackduck.com/onboard/>.

[image: Black Duck Security App Select Repositories During Install]

Proceed to onboarding process for an overview of how to onboard repositories.

## Onboarding process

Upon successful authentication, you'll be redirected to the Black Duck onboarding screen to select an organization and the associated repositories where a workflow YAML file will be generated and committed for running scans.

[image: Black Duck Security App dashboard]

Take a moment to review the dashboard components:

1. **Select Repositories:** Select the repositories within an organization where configured scans will be deployed to
2. **Configure Options:** Configure scan options for specific Black Duck platforms such as: Black Duck® SCA, Coverity and Polaris
3. **Review workflow.yml**: Review a preview of the generated GitHub workflow that will be deployed to the selected repositories for performing a Black Duck security scan.
4. **Summary**: Summarises the count of repositories where the workflow will be deployed to. At this stage the workflow can be submitted for deployment.

## Configure scan workflow

The Dashboard UI can be used to configure which repositories within an organization a workflow will be deployed to. A workflow can be configured for the following Black Duck platforms:

- Black Duck® SCA
- Coverity
- Polaris

**Step 1: Select repositories**

Use the `Select Repositories Screen` screen to configure which repositories within the organization should be scanned. [image: Repository selection screen]

1. Use the **Organization** drop down list to select the organization or a personal GitHub account.

   Note: The portal automatically discovers and displays repositories based on the selected organization.
2. Select the repositories that the generated workflow should be configured and deployed to:

   1. **All repositories**: Configure and deploy the workflow to all repositories within the organization.
   2. **Selected repositories**: Select the repositories from a list. Use the following filter operations for assistance with repository selection:
      - **Search**: Filter by name, language, license, visibility or topic.
      - **Sort**: Click the `Repository` or `Last Updated` column to order the repository list by name or date.
      - **Pagination**: Navigate the available repositories using the pagination buttons.
      - **Show only selected**: Display selected repositories in the list only.

**Step 2: Configure scan options**

The Dashboard can be used to automatically generate a GitHub workflow file based on scan options specified in the `Configure Options` screen. The generated GitHub workflow will be deployed to the selected repositories.

[image: Global scan options]

The screen illustrated above highlights that the following options can be configured:

- **Branches**: Scans can be configured to trigger in response to push events and when a pull request is created or updated. Use the `push
  events` and `pull request` text boxes to specify which branches will initiate scans for each type of event.
- **Runner**: Choose the environment for the GitHub runner, such as `ubuntu-latest`.
- **Platform**: Select the Black Duck platform for scanning in the repository. Supported platforms include Coverity, Black Duck® SCAand Polaris. Upon selection, the Dashboard UI will dynamically update to display platform scan-specific options and instructions, such as which GitHub variables and secrets are required for the generated workflow to run successfully.
- **Scan method:** Choose between:

  - `GitHub Action (default)`: Generate a scan workflow that uses Black Duck Security Scan GitHub Action.
  - `CLI`: Generate a scan workflow that downloads the latest Bridge CLI and uses it directly to perform a security scan.

Note: Ensure all required GitHub variables and secrets are configured before clicking **Next** to proceed with generating a scan workflow for review and deployment.

Refer to the Black Duck platform documentation pages for further details of scan configuration options and prerequisites:

- Black Duck® SCA
- Coverity
- Polaris

## Review workflow

The `workflow review` screen allows a generated workflow to be previewed and edited before submission for deployment.

Note: The generated workflow can include multiple scan jobs for different Black Duck platforms, such as Black Duck® SCA, Coverity or Polaris. To add a new scan job, return to the `Configure options` screen and select a different Black Duck platform. Subsequently, when navigating back to the `workflow
review` screen, the new scan job will be displayed as appended to the generated workflow, with the configured options for the selected platform (Black Duck® SCA, Coverity or Polaris).

The `workflow review` screen is illustrated below with an example generated workflow for Black Duck® SCA. Refer to the following documentation pages for sample workflow jobs generated for each Black Duck platform:

- Black Duck® SCA
- Coverity
- Polaris

The remainder of this section explains the workflow review process.

[image: Workflow review UI]

The `workflow review` screen displays a GitHub workflow containing a single scan job, specifically added for selected Black Duck platforms.

The workflow is automatically generated for deployment to the selected repositories and simplified to include only the minimum fields required (e.g., default values for the product scans are omitted unless specified).

Inline editing of the workflow is available by clicking the `Edit` button. The editor automatically validates the syntax, preventing saves if errors are detected. It also issues warnings for potential issues, such as hardcoded secrets or variables, which do not block saving.

A default workflow filename is generated in the `Filename` text box, which can be updated before proceeding.

1. Review and amend the generated workflow as necessary:
   - Use the `Edit` button to make direct edits to the workflow file, such as:
     - Modify trigger conditions, including which branches will trigger a scan.
     - Adjust scan configuration parameters.
     - Required credentials and tokens.
     - Add custom steps or integrations.
   - Use the `Filename` text box to update the default workflow filename that will be committed to the selected repositories.

     Important: If the repository already contains an existing workflow file with the same name, then the new workflow generated by the Black Duck GitHub App will overwrite the existing file. GitHub supports multiple workflows; however, using unique workflow filenames reduces the risk of overwriting workflows created by the Black Duck App. Ensure that the names of your workflows do not conflict to prevent unintended loss of configuration.
2. When required changes have been made then perform one of the following options:
   1. Click the **Previous** button to configure scan options for a different Black Duck platform. Subsequently, when the `workflow review` screen is revisited a scan job will be appended to the workflow for that platform.

      Note: After editing the workflow, if the `Previous` button is selected, the UI will warn that the edits you made will be lost permanently.
   2. Click the **Next** button to confirm that the workflow has been reviewed and all necessary amendments have been made.

## Deploy workflow

The `Summary` screen displays a count of the repositories where the workflow will be deployed.

At this point, there is the option to choose if the workflow can be submitted for deployment by:

- Committing directly to the main branch of each repository
- Raising a Pull Request

[image: Workflow summary]

To submit a workflow for deployment across the selected repositories follow the steps below:

1. Review the deployment summary:

   Note: Check that the count of selected repositories and workflow filename (e.g., `blackducksca-workflow.yml`) are as expected. Use the `Previous` button to navigate back to adjust if necessary.
2. If desired, select the option to commit the workflow as a Pull Request or direct commit.
3. Click the **"Submit"** button and confirm deployment in the modal dialog.
4. Monitor the deployment progress in the onboarding status screen illustrated below, which will update every 10 seconds.

   Note: For repositories with branch protection rules the app automatically creates Pull Requests (PRs) to inject workflows. Review and manually merge Pull Requests using provided links to enable scans.
5. Review the **Failed Repositories List** for any deployment issues.[image: image]

## Troubleshooting and support

The table below summarizes common issues and their resolutions.

| Issue Type | Issue | Symptoms | Solution |
| --- | --- | --- | --- |
| **Authentication** | OAuth Authorization Failed | OAuth Authorization Failed | - Clear browser cache and cookies - Ensure correct GitHub account is logged in - Check organization membership status - Retry authorization process |
|  | Token Expired | Intermittent authentication failures | - Navigate to portal settings - Click "Refresh GitHub Token" - Complete OAuth flow again |
| **Permissions** | Insufficient Repository Access | Error: `403 Forbidden` when accessing repository | - Verify repository collaboration status - Request elevated permissions from repository owner - Check organization membership |
|  | GitHub Actions Unavailable | Actions tab not visible in repository | - Enable Actions in repository settings - Check organization Actions policies - Verify repository is not archived |
| **Workflow deployment** | Workflow Creation Failed | Deployment stuck in "In Progress" status | - Check repository write permissions - Verify branch protection rules - Confirm Actions are enabled - Review deployment logs in portal |
