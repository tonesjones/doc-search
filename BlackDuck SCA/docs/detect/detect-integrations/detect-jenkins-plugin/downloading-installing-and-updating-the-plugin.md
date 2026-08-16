---
title: "Downloading, Installing, and Updating the Plugin"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/downloading-installing-and-updating-the-plugin.html"
content_id: "EPui4bTOMHllximjrmxrFA"
version: "11.5.1"
section: "Detect Integrations"
scraped_at: "2026-08-08T23:45:57.858406+00:00"
---

# Downloading, Installing, and Updating the Plugin

## Downloading and Installing a new instance

To install the Detect for Jenkins plugin, perform the following steps:

1. Navigate to **Manage Jenkins** > **Manage Plugins**.
2. Select the **Available** tab. (Note that if the plugin is already installed, it does not appear in the **Available** list.)
3. Select **Blackduck Detect**.
4. Click **Download now and install after restart**. This is the recommendation for installing the plugin.
5. After restarting Jenkins, confirm that the plugin is successfully installed by navigating to **Manage Jenkins** > **Manage Plugins > Installed**, and verify that **Synopsys Detect** displays in the list.

Detect plugin for Jenkins GitHub page [jenkinsci](https://github.com/jenkinsci/blackduck-detect-plugin).
Additional download locations listed in Download locations.

## Updating Synopsys Detect Jenkins plugin to Black Duck® Detect Jenkins plugin

For existing Synopsys Detect Jenkins plugin users, the Black Duck® Detect Jenkins plugin should be considered a fresh installation as the domain has changed.

- Take note of your existing system configuration and post-build setup before moving from the Detect Jenkins plugin to the Black Duck® Detect Jenkins plugin. You will need this information when configuring or reconfiguring your pipelines.

  - Configuration information can be located under your `JENKINS_HOME` directory.
- If you are utilizing a Detect Post Build Step, before upgrading to the Black Duck® Detect plugin, make sure to record the current configuration set in the configurable pipelines, for reuse.
- For Groovy, you will need to update the **Pipeline** script; under **Pipelines** > **Pipeline_Name** > **Configuration**, replacing the `synopsys_detect detectProperties:` portion of the script with `blackduck_detect detectProperties:`

  Example:

  ```
  node ('built-in') {

      stage ('Git - Checkout') {
      git 'https://github.com/yarnpkg/example-yarn-package.git'
      }
      stage ('Black Duck - Detect') {
      blackduck_detect detectProperties: '--blackduck.trust.cert=true --detect.wait.for.results=true', downloadStrategyOverride: [$class: 'ScriptOrJarDownloadStrategy']

      }
  }
  ```
- For the System Configuration and Black Duck® SCA, before upgrading to the Black Duck® Detect plugin, make sure to back up, or record the current configuration set for the Global Black Duck SCA URL and token that you have set in Manage Jenkins > Configure System > Black Duck® Detect section.
- If you are using Air Gap mode, before upgrading to the Black Duck® Detect plugin, make sure to save the current tool configuration that you have set in Manage Jenkins > Tools > Detect Air Gap mode.

## Updating the Black Duck® Detect for Jenkins plugin

You can update the Detect for Jenkins plugin when new versions are released.

1. Navigate to **Manage Jenkins** > **Manage Plugins**.
2. Click the **Updates** tab.
3. Select **Blackduck Detect**

   1. If there are updates for the Detect for Jenkins plugin, the updates display in the list. If there is not an available update, the Detect for Jenkins plugin does not display in this list.
   2. Alternatively, you can force Jenkins to check for plugin updates by clicking **Check now** on the **Updates** tab.
4. If there are updates, select the one you want, and click **Download now and install after restart**.
