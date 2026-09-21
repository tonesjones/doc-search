---
title: "Create a multibranch pipeline job in your Jenkins instance"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/create-a-multibranch-pipeline-job-in-your-jenkins-instance.html"
content_id: "qyeJCmOFIODUwLZsaRPs6g"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:35.607099+00:00"
---

# Create a multibranch pipeline job in your Jenkins instance

To create the Multibranch Pipeline, do the following:

1. Click to the New Item.
2. Enter an item name.
3. Select Multibranch Pipeline.

   If you don't see Multibranch
   Pipeline as an option, then the Jenkins Pipeline plugin
   hasn't been installed. (The Jenkins Pipeline plugin is a
   prerequisite.)
4. Click OK.

## Configure the multibranch pipeline job

To configure the job:

1. Navigate to your job's configuration page and select Bitbucket from the
   Branch Sources section.
2. Select your Bitbucket Server from the Bitbucket Server dropdown menu.
3. Select your credentials.
4. Enter the Owner Name.

   Use the project key from your Bitbucket
   repo.
5. Enter the Repository Name and accept all the default values.
6. Determine which branches to scan.

   CAUTION:

   During the first-time
   job configuration, Jenkins triggers a scan on all branches by default,
   if a jenkinsfile exists in the root directory. If you only want to scan
   one branch after saving your configuration, see the section on
   restricting scanning below before you click Apply and Save.
7. Click Apply, then Save.

## Restrict scanning to one branch, if needed

To restrict a scan to one branch:

1. Find the Property strategy dropdown menu in the Branch Sources section and
   select **All branches get the same properties**.
2. Click Add property (which is located below the Property strategy
   field).
3. Click Suppress automatic SCM triggering.
4. Enter your branch name in the **Branch names to automatically build**
   field.

   If you want to include several branches, you can use
   regex.
5. Select For matching branches schedule all builds (nothing is
   suppressed) from the Suppression strategy dropdown
   menu.
6. Click Apply, then Save.

Later on, you may need to delete the Suppress automatic SCM
triggering property to trigger scan on other branches by clicking Scan
Multibranch Pipeline Now on the job.

## Generate pipeline syntax

To generate syntax for your multibranch pipeline:

1. Navigate to **Dashboard > JOBNAME > Branches/Pull Requests**.
2. Click on the **BRANCH NAME** or **PULL REQUEST**.
3. Click on **Pipeline Syntax** from the sidebar.
4. Go to the **Steps** section.
5. Select **security_scan: Black Duck Security Scan** from the Sample Step
   dropdown menu.
6. Complete the necessary fields in the form.
7. Click Generate Pipeline Script.
8. Copy the generated pipeline script to your Jenkinsfile.
9. Store the Jenkinsfile at the root level in your repository.
