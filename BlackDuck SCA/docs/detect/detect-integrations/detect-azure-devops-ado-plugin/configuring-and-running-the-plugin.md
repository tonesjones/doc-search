---
title: "Configuring and Running the Plugin"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/configuring-and-running-the-plugin.html"
content_id: "uAPcqiFYL0TGBKDDk0x89g"
version: "11.5.1"
section: "Detect Integrations"
scraped_at: "2026-08-08T23:46:08.514285+00:00"
---

# Configuring and Running the Plugin

After you install the plugin, you configure it in Pipeline task.

Configure your Black Duck® Detect for Azure DevOps plugin by adding configuration for your Black Duck SCA server and adding Detect arguments.

Figure 1. Configuring and running the plugin
[image: Configuring plugin]

## Configuring the plugin

1. Navigate to **Your Collection > Project > Pipelines > Tasks**. The plugin adds a new task of **Run Black Duck® Detect for your build**.
   You must add this task to your build queue.
2. Click **Run Detect for your build**, and the **Detect** panel displays on the right. In the **Detect** configuration panel, complete the following fields and options.
3. **Display name:** Type a unique name in this field. Note that the name you type here displays in the left panel; the default name is **Run Detect for your build**.
4. Click **+ New** to add a new **Black Duck SCA Service Endpoint** and then configure the details.
5. Click **+ New** to add a new **Black Duck SCA Proxy Service Endpoint** and then configure the details.
6. **Detect Version**: Version of the Detect binary to use. It is recommended to use the latest, but you can specify a version override if desired.
7. **Detect Run Mode:** Select the run mode. If you select **Use Air Gap**, a **Detect Air Gap Jar Directory Path** field opens in which you must specify the Detect air gap jar path.
8. **Detect Arguments**: Here you can include additional Detect* arguments; Detect picks up your build environment variables and your project variables. Use a new line or space to separate multiple arguments. Use double quotes to escape. You can use environment and build variables.

For more information on Detect arguments, refer to Properties.

- **Detect Folder**: The location to download the Detect jar or the location of an existing Detect jar. The default is the system temp directory. To specify a different directory, type the directory path and name in the field.

Windows agents require an absolute path when specifying Detect download location in the **Detect Folder** field.

- **Add Detect Task Summary**: Click this checkbox to add a summary of the Detect task to the build summary task.

In the user interface, fields with a red asterisk ( ***** ) are required. Some default values are provided, such as version.

**Note:** that the following fields belong to Azure DevOps, and are not part of the Black Duck® Detect plugin:

- Task version
- Display name
- Control Options
- Output Variables
