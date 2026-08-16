---
title: "Jenkins Air Gap mode"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/jenkins-air-gap-mode.html"
content_id: "yMxJeo7itJ7NBDpGhzjE0w"
version: "11.5.1"
section: "Detect Integrations"
scraped_at: "2026-08-08T23:46:03.523163+00:00"
---

# Jenkins Air Gap mode

The Black Duck® Detect for Jenkins plugin enables you to configure an air gap option to run Detect.

Before you can see the **Detect Air Gap** option on the Global Tool Configuration page, you must install the Detect plugin.

Use the following process to make the **Detect Air Gap** option globally available when you're configuring a Detect job:

1. In Jenkins, Click **Manage Jenkins** on the left navigation and then click  **Global Tool Configuration**.
2. In the **Detect Air Gap** section, click **Add Detect Air Gap** and then complete the following:

   1. **Detect Air Gap Name**: A name for the air gap installation.
   2. **Installation directory**: The directory for the air gap installation files.
   3. **Install automatically**: Select this checkbox to enable Jenkins to install the air gap files on demand.

When you check this option, you have to configure an installer for this tool, where each installer defines how Jenkins will attempt to install this tool.

For a platform-dependent tool, multiple installer configurations enable you to run a different setup script depending on the agent environment, but for a platform-independent tool such as Ant, configuring multiple installers for a single tool wouldn't be suggested.

Figure 1. Air Gap mode.
[image: Air Gap mode]

1. Optionally, add another air gap version. You can use the **Add Installer** menu to choose other install methods such as **Run Batch Command** or **Run Shell Command**.
2. Click **Save**.
