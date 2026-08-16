---
title: "Running Black Duck® Detect in Jenkins"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/running-black-duck-detect-in-jenkins.html"
content_id: "G2WQimZfpS_iSzHZSdF7lg"
version: "11.5.1"
section: "Detect Integrations"
scraped_at: "2026-08-08T23:45:59.951867+00:00"
---

# Running Black Duck® Detect in Jenkins

By default, Detect for Jenkins downloads either the latest Detect shell script when run on a UNIX node, or PowerShell script when it's run on a Windows node, to the Jenkins tools directory, and then executes that script. Note that you can also use the JAR option to run Detect.

The Detect PowerShell or shell script is downloaded once and placed in the Detect working directory. If you want to force the plugin to fetch the latest script, clear out the Detect directory in your Jenkins tools directory.

# **JAR option**

If you do not want to download Detect, you can manually put the JAR on the node where you want Detect to run and specify the DETECT_JAR environment variable that points to your provided JAR, and that JAR will be executed instead.

To use the JAR option, perform the following steps:

1. Navigate to **Dashboard > Manage Jenkins > Configure System > Global properties > Environment variables**.
2. Click **Add**.
3. Set an environment variable with the following properties:

   1. **Name**: `DETECT_JAR`.
   2. **Value:** `<path to the Detect jar file on your Jenkins node>`.

**Note:** When your build runs, Jenkins looks for configured environment variables, and if it locates DETECT_JAR, it uses that instead of pulling the latest Detect shell script.

## Air Gap option

Detect can be configured to run in an air gap fashion, see: Air Gap.

In freestyle and Pipeline jobs, you can toggle between the different modes for running Detect in the plugin such as pulling the Detect.jar from scripts or $DETECT_JAR_PATH, or from a specified Tool Installation.

## Running Detect in a job

You can run Detect as a post-build action or a Pipeline step.

### Pipeline step

You can configure the scan as a pipeline step in a Pipeline job.

Refer to the pipeline example

### Post-build actions

You can configure the scan as a post-build action in a freestyle job. You can have multiple post-build actions, but only one Detect post-build action.

Refer to the freestyle example.

## DSL considerations

The Detect for Jenkins plugin provides Dynamic DSL for both freestyle steps and pipeline steps. Read more at [Dynamic DSL](https://github.com/jenkinsci/job-dsl-plugin/wiki/Dynamic-DSL).

**Note:** that versions 1.83 and later of the DSL plugin do not support the Detect for Jenkins plugin pipeline steps.
