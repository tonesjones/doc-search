---
title: "Get started with Black Duck Security Scan Plugin for Jenkins"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/get-started-with-black-duck-security-scan-plugin-for-jenkins.html"
content_id: "agoBKU5RlQQuyulDeyqdog"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:34.993561+00:00"
---

# Get started with Black Duck Security Scan Plugin for Jenkins

Black Duck Security Scan Plugin for Jenkins supports the following job types:

- Multibranch pipeline
- Freestyle
- Pipeline

Note: Multibranch and pipeline job types support both scripted and declarative syntax.

After completing the steps in this section, you will have a working pipeline job:

1. Install a branch source plugin (multibranch only).
2. Install the Black Duck Security Scan Plugin for Jenkins.
3. Configure the SCM Server in Jenkins.
4. Configure global settings in the Jenkins UI.
5. Configure a job in Jenkins:
   - Multibranch
   - Freestyle
   - Pipeline

## Install the branch source plugin

You will need to manually install the specific branch source plugin on your Jenkins instance.

Note: For a multibranch pipeline job, if you do not have a branch source plugin installed on your Jenkins instance, it will throw an error during the job execution.

To install the appropriate branch source plugin for Jenkins:

1. Navigate to Manage Jenkins and choose plugins.
2. Click the **Available Plugins** tab.
3. Check the box next to your Branch Source Plugin:
   - Bitbucket Branch Source Plugin
   - GitHub Branch Source Plugin
   - GitLab Branch Source Plugin

   Note: If the plugin is already installed on your system, it will not be listed on the Available tab.
4. Select **Download now and install after restart** (located near the bottom of the plugin list) to install the plug-in after the next Jenkins restart.
5. Restart Jenkins and navigate to **Manage Jenkins > Plugins > Installed** to verify that the plugin has been successfully installed.

## Install the Black Duck Security Scan Plugin for Jenkins

To install the Black Duck Security Scan Plugin for Jenkins:

1. Navigate to **Manage Jenkins** and then choose **plugins**.
2. Click the **Available Plugins** tab.
3. Select the checkbox next to **Black Duck Security Scan** plugin.

   Note: If the plugin is already installed on your system, you will not see it listed on the Available tab.
4. Near the bottom of the plugin list, select **Download now and install after restart** to install the plugin after the next Jenkins restart.
5. After restarting Jenkins, confirm that the plug-in is successfully installed by navigating to **Manage Jenkins**, then **Plugins**, then **Installed**. Verify that **Black Duck Security Scan** appears in the list.

## Configure the SCM server in Jenkins

To configure Jenkins to integrate with a Source Code Management (SCM) server:

1. Navigate to **Dashboard**.
2. Choose **Manage Jenkins**, and then choose **System**.
3. Follow the instructions below relevant to the Source Code Management (SCM) platform:

**GitHub**

1. Go to the **GitHub** section. Click the **Add GitHub Server** button and select the **GitHub server** from the drop down menu.
2. Configure the following settings for the GitHub server:
   1. Name
   2. API URL

   [image: Image showing the fields to configure in Jenkins for the GitHub server.]
3. Click the checkmark to select **Manage hooks**.
4. Select the credentials from the dropdown. If credentials have not been configured:
   1. Click the **Add** dropdown menu.
   2. Select **Kind > Username with password.**
   3. Provide a GitHub username and in the password field provide an access token.
5. Scroll to the bottom of the page, then click **Apply** and **Save**.

**GitLab**

1. Go to the **GitLab Servers** section. Click the **Add GitLab Server** button and select the **GitLab Server** option from the dropdown menu.
2. Configure the following settings for the GitLab server:
   1. Display Name
   2. Server URL
3. Click the checkmark to select **Manage Web Hooks**.
4. Select the credentials from the dropdown. If credentials have not been configured:
   1. Click the **Add** dropdown menu.
   2. Select **Kind > Username with password.**
   3. Provide a GitLab username and in the password field provide an access token.

   [image: Image showing the fields to configure in Jenkins for the GitLab server.]
5. Scroll to the bottom of the page, then click **Apply** and **Save**.

**Bitbucket**

1. Go to the **Bitbucket Endpoints** section. Click the **Add** button and select the **Bitbucket Server** option from the dropdown menu.

   [image: Image showing how to select Bitbucket Server as the endpoint.]
2. Configure the following settings (in Jenkins) for Bitbucket server:
   - Name
   - Server URL
   - Server Version (for the Bitbucket instance)

     [image: Image showing the fields to configure in Jenkins for the Bitbucket server.]
3. Click the checkmark to select **Manage hooks**. (Leave the other two boxes checked)
4. Select the credentials from the dropdown. If credentials have not been configured:
   1. Click the **Add** dropdown menu.
   2. Select **Kind > Username with password.**
   3. Provide a Bitbucket username and in the password field provide an access token.
5. In the **Webhook implementation to use** dropdown menu, select **Plugin**.
6. Scroll to the bottom of the page, then click **Apply** and **Save**.

## Configure global settings in the UI

Settings that are configured globally can be used in multiple pipelines. Any settings that all your pipelines will have in common should be set here, so that they only have to be set once. When one pipeline requires that an individual setting be different, you can set it in the jenkinsfile for that pipeline.

To configure global settings for the plugin:

1. Navigate to Dashboard, select Manage Jenkins, then select System.
2. Scroll down to the Black Duck Security Scan section and complete fields in that form for each product that you want to use.

   [image: image]

Note:

- "Username with password" and "Secret Text" are the only credential types supported.
- The credentials specified here will be used if no other credentials are provided in the Jenkinsfile.
