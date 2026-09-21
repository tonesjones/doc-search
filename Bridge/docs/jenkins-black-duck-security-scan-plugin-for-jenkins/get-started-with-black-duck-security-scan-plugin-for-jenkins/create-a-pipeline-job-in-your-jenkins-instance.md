---
title: "Create a pipeline job in your Jenkins instance"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/create-a-pipeline-job-in-your-jenkins-instance.html"
content_id: "CTM6UmVhuMa7WiKO_UN~2g"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:36.848848+00:00"
---

# Create a pipeline job in your Jenkins instance

Note: Only normal scanning is supported through pipeline.

To create a pipeline job:

1. Select the New Item.
2. Enter a name for the item.
3. Select Pipeline.

   If the Pipeline option is unavailable, you'll need to go back and install the Jenkins Pipeline plug-in.
4. Click OK.

## Configure the pipeline job

To configure the pipeline job:

1. Go to the Pipeline section on your job's configuration page and do one of the following:
   - Choose **Pipeline script** and insert your script.
   - Choose **Pipeline script from SCM** from the definition dropdown menu, then follow the instructions below.
2. Select Git from the dropdown menu.
3. Enter the Repository URL.
4. Select your credentials from the dropdown menu.

   If you haven't configured your credentials, do the following:
   1. Click the Add dropdown menu.
   2. Select **Kind > Username with password**.
   3. Provide your scm username and enter your access token in the password field.
5. Enter your branch name for the Branch Specifier field.
6. Accept the default values.
7. Click Apply, then Save.
8. Click Build Now to build your pipeline job.

Note:

1. PR comment is not supported through pipeline.
2. `coverity_project_name` and `coverity_stream_name` are mandatory parameters for pipeline.

## Generate pipeline syntax

To generate syntax for your pipeline:

1. Navigate to **Dashboard > JOB NAME.**
2. Click on **Pipeline Syntax** from the sidebar.
3. Go to the **Steps** section.
4. Select **security_scan: Black Duck Security Scan** from the Sample Step dropdown menu.
5. Complete the necessary fields in the form.
6. Click **Generate Pipeline Script**.
7. Copy the generated pipeline script to your Jenkinsfile.
8. Store the Jenkinsfile at the root level in your repository.

Note: Even if you have set all your configurations globally, you may need to add additional configurations to your Jenkinsfile. For more information, see the following:

- Using the Black Duck Security Scan Plugin with Black Duck SCA
- Using the Black Duck Security Scan Plugin with Coverity
- Using the Black Duck Security Scan Plugin with Polaris
