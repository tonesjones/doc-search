---
title: "Detect in Jenkins Pipeline job"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/detect-in-jenkins-pipeline-job.html"
content_id: "Ha5H5ZKJ8geiusFjiOGtXg"
version: "11.5.1"
section: "Detect Integrations"
scraped_at: "2026-08-08T23:46:01.011175+00:00"
---

# Detect in Jenkins Pipeline job

In pipeline jobs there are only steps. You can generate the Detect pipeline step as follows.

1. Navigate to **Jenkins > New Item**.
2. In the **Enter an item name** field, type the name for your new Pipeline project.
3. Scroll down and click **Pipeline**.
4. Click **OK**.
5. On the resulting page, click the **Pipeline** tab.
6. To help you generate Pipeline syntax, in the **Pipeline** section, click **Pipeline Syntax** to access the **Pipeline Syntax** page.

   1. On the **Pipeline Syntax** page, click the **Sample Step** drop-down menu under **Steps**, and select **blackduck_detect: Blackduck Detect**

      1. Add some Detect properties.
      2. Click **Generate Pipeline Script**, and you will see a Pipeline Script statement that would call the step with that configuration. You may copy and paste the whole statement into your script, or pick up just the options you care about.
      3. **Optionally**, select the **Return status code** checkbox to return a status code.
      4. **Optionally**, select a **Custom download strategy** option.

Figure 1. Custom download strategy.
[image: Custom download strategy]

1. Add a Pipeline script and click **Save**.

The following is a simple example of a basic script.

Figure 2. Basic sample script.
[image: Sample script]

1. Run the build.
2. After completing the Jenkins Pipeline build with Detect, you can view the complete scan results in your Black Duck SCA instance.

**Note:** In Jenkins pipelines, there are no post-build actions because post-build actions are a Freestyle job concept.
