---
title: "Create a freestyle job in your Jenkins instance"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/create-a-freestyle-job-in-your-jenkins-instance.html"
content_id: "s0cFs4NcgZBNWwua7O2EqQ"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:36.228284+00:00"
---

# Create a freestyle job in your Jenkins instance

Jenkins Freestyle projects provide a UI-based approach to configuring build jobs without requiring Jenkinsfile scripting.

The Black Duck Security Scan Plugin provides the following features for use in Jenkins Freestyle projects:

- Provides UI fields for configuring scans for Black Duck® SCA, Coverity, Polaris or Software Risk Manager.
- Uses the server URL and access token from the Black Duck Security Scan Configuration page based on the selected product for scanning.

## Limitations

Using freestyle jobs with the Black Duck Security Scan Plugin has the following limitations:

| Limitation | Description |
| --- | --- |
| Unsupported features | The following features are unsupported:  - Pull request comments - Fix pull requests   Note: For enterprise applications, Multibranch Pipelines are **recommended** with support for Pull Request scans and fix Pull Requests |
| URL server and token override | The global server URL and access token parameters for a Black Duck product configured in the Black Duck Security Scan Plugin **cannot** be overridden in a pipeline job. |

Note: The following UI fields are mandatory when using a Coverity build step in a Black Duck Security Scan Plugin freestyle job:

- Project Name
- Stream Name

## Create a freestyle project

To create a Jenkins Freestyle Project:

1. Select New Item from the top left menu displayed in the Jenkins Dashboard.
2. Enter an item name.
3. Select Freestyle project.
4. Click OK.

## Configure a freestyle job

To configure a freestyle job for Black Duck Security Scan Plugin:

1. Go to the Source Code Management section on your job's configuration page and select Git.
2. Enter the Repository URL.
3. Select your credentials from the dropdown menu. If you haven't configured your credentials, do the following:
   1. Click the Add dropdown menu.
   2. Select Kind > Username with password .
   3. Provide your scm username and enter your access token in the password field.
4. Enter your branch name in the Branch Specifier field.
5. Accept the default values for Source Code Management.
6. (Optional) To restrict which node this project runs on, selectRestrict where this project can be run and provide your agent label as Label Expression .
7. Click Add build step in the Build Steps section.
8. Select Black Duck Security Scan from the dropdown menu.
9. Select the security product from the Select Security Product dropdown menu and complete the required UI fields for that product.
10. Click Apply and Save.
11. Click Build Now to build the freestyle job.
