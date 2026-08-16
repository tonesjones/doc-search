---
title: "Setting Up SCM Providers"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/setting-up-scm-providers.html"
content_id: "oLoLvm6VbeV07jFPTCAIyQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:54.840692+00:00"
---

# Setting Up SCM Providers

SCM integrations allow for direct communication with SCM providers, enabling automatic
retrieval of repository and branch information during Detect scans on cloned Git
repositories. This integration enhances usability and data accuracy by populating
dropdowns and search boxes.

## Supported SCM Integrations

Currently, the following SCM integrations are supported:

- **GitHub**
- **GitHub Enterprise**
- **GitLab Self-Managed**
- **GitLab SaaS**
- **Bitbucket**
- **Bitbucket Data Center**

## Enabling SCM integration

SCM integration operates within a Kubernetes environment (either native or Kubernetes
in Docker - KinD). Follow these steps to enable SCM integration:

- **Install Required Helm Charts:** Use the helm charts to install the
  necessary components.
- **Activate the Feature:**

  - This feature is not enabled by default. To activate it, add the feature
    to your Product Registration key.
  - Update your `values.yaml` file with:

    ```
    enableIntegration: true
    ```

Note: Currently, self-signed certificates are not accepted for SCM integrations.

## Creating an OAuth App

Before setting up a SCM provider in Black Duck SCA, you must first
authenticate the project.

For GitHub and GitHub Enterprise, you must create an OAuth App:

1. Go to <https://github.com/settings/developers> and OAuth
   Apps and create a new app (or the corresponding URL for GitHub Enterprise).
2. Fill the following fields:

   - **Application Name**
   - **Homepage URL**: The URL of your Black Duck SCA
     Server
   - **Application Description**
   - **Authorization Callback URL**: `<Homepage
     URL>/api/scm/github/callback`
3. Click **Save**. This will generate the Client ID to be used in Black Duck SCA.
4. Click **Generate secret**. This will generate a secret string to be used
   in Black Duck SCA.

For GitLab Self-Managed:

1. Go to <gitlab_server_name>/-/profile/applications. You should see add new
   application.
2. Fill the following fields:

   - **Name**: provide any name.
   - **Redirect URI**: <bd_server_name>/api/scm/gitlab/callback
3. Uncheck the **Confidential** checkbox.
4. Enable API in the **Scopes** section.

For BitBucket:

1. Go to
   <bitbucket_server_name>/plugins/servlet/applinks/listApplicationLinks
2. Click **Create Link**.
3. Select **External application**.
4. Select **Incoming** in the **Direction** dialog box and then click
   OK.
5. Fill the following fields:

   - **Name**: Provide a name.
   - **Redirect URI**:
     <bd_server_name>/api/scm/bitbucket/callback
6. Check the **Write** checkbox under **Repositories** in the
   **Application permissions** section.

## Setting up a GitHub.com SCM integration

To set up a GitHub.com SCM integration:

1. Log into Black Duck SCA as a System Administrator.
2. Click [image: Admin button] and select **Integrations**.
3. Click **GitHub.com**.
4. Fill the following fields:

   - Check the **Enable Server** checkbox.
   - Enter the **Client ID** generated from the GitHub website.
   - Enter the **Secret** generated from the GitHub website.
5. Click **Save**.

## Setting up a GitHub Enterprise SCM integration

To set up a GitHub Enterprise SCM integration:

1. Log into Black Duck SCA as a System Administrator.
2. Click [image: Admin button] and select **Integrations**.
3. Click **GitHub Enterprise**.
4. Click **+ Add Server**.
5. Fill the following fields:

   - **Server Name**: Enter a name for your server.
   - **Server URL**: Enter your GitHub Enterprise server URL.
   - **Client ID**: Enter the **Client ID** generated from the
     GitHub website.
   - **Secret**: Enter the **Secret** generated from the GitHub
     website.
   - Check the **Enable Server** checkbox.
6. Click **Create**.

## Setting up a GitLab Self-Managed SCM integration

To set up a GitLab Self-Managed SCM integration:

1. Log into Black Duck SCA as a System Administrator.
2. Click [image: Admin button] and select **Integrations**.
3. Click **GitLab Self-Managed**.
4. Click **+ Add Server**.
5. Fill the following fields:

   - **Server Name**: Enter a name for your server.
   - **Server URL**: Enter your GitLab Self-Managed server URL.
   - **Client ID**: Enter the **Client ID** generated from the
     GitLab website.
   - **Secret**: Enter the **Secret** generated from the GitLab
     website.
   - Check the **Enable Server** checkbox.
6. Click **Create**.

## Setting up a GitLab SaaS SCM integration

To set up a GitLab SaaS SCM integration:

1. Log into Black Duck SCA as a System Administrator.
2. Click [image: Admin button] and select **Integrations**.
3. Click **GitLab SaaS**.
4. Click **+ Add Server**.
5. Fill the following fields:

   - **Server Name**: Enter a name for your server.
   - **Client ID**: Enter the **Client ID** generated from the
     GitLab website.
   - **Secret**: Enter the **Secret** generated from the GitLab
     website.
   - Check the **Enable Server** checkbox.
6. Click **Create**.

## Setting up a Bitbucket SCM integration

To set up a Bitbucket SCM integration:

1. Log into Black Duck SCA as a System Administrator.
2. Click [image: Admin button] and select **Integrations**.
3. Click **Bitbucket**.
4. Click **+ Add Server**.
5. Fill the following fields:

   - **Server Name**: Enter a name for your server.
   - **Client ID**: Enter the **Client ID** generated from the
     Bitbucket website.
   - **Secret**: Enter the **Secret** generated from the Bitbucket
     website.
   - Check the **Enable Server** checkbox.
6. Click **Create**.

## Setting up a Bitbucket Data Center SCM integration

Note: Black Duck SCA supports Bitbucket Data Center version 8.19. Users
should ensure they are using this version for optimal compatibility and
functionality. For personal repositories not linked to a project, the Bitbucket Data
Center integration only supports the default branch.

To set up a Bitbucket Data Center SCM integration:

1. Log into Black Duck SCA as a System Administrator.
2. Click [image: Admin button] and select **Integrations**.
3. Click **Bitbucket Data Center**.
4. Click **+ Add Server**.
5. Fill the following fields:

   - **Server Name**: Enter a name for your server.
   - **Server URL**: Enter your Bitbucket Data Center server URL.
   - **Client ID**: Enter the **Client ID** generated from the
     Bitbucket Data Center website.
   - **Secret**: Enter the **Secret** generated from the Bitbucket
     Data Center website.
   - Check the **Enable Server** checkbox.
6. Click **Create**.
