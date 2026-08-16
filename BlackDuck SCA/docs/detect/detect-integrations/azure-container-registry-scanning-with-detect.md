---
title: "Azure Container Registry scanning with Detect"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/azure-container-registry-scanning-with-detect.html"
content_id: "BqTGgOhNYhycyakYl8VBaA"
version: "11.5.1"
section: "Detect Integrations"
scraped_at: "2026-08-08T23:46:13.231254+00:00"
---

# Azure Container Registry scanning with Detect

Black Duck® Detect supports scanning images stored in the Azure Container Registry (ACR). Image scan results are sent to your dedicated Black Duck SCA instance providing vulnerability, license, and operational risk results on the open source software components identified in the ECR image.

There are two ways that you can use Detect to scan container images in ACR:

- Using an Azure DevOps Pipeline, see Azure DevOps (ADO) Plugin
- Using Detect on a local workstation

## Prerequisites

Azure Container Registry Scanning requires a fully configured instance of Detect.

For prerequisite information refer to Requirements and release information

## Detect ACR scanning on a local workstation

Before you can scan images in ACR using Detect, ensure that you satisfy the following requirements:

- One or more container images stored in ACR.

  - For more information about publishing and storing images in ACR, refer to the [container registry topic about pushing images](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-get-started-docker-cli).
- Azure CLI is installed
- Docker is installed

Tip: To run Detect, you will need to provide login credentials for your Black Duck SCA
server by adding the following arguments to the command line:

- `--blackduck.url={your [bd_product_short] server URL}`
- `--blackduck.api.token={your [bd_product_short] access token}`

To locally scan container images stored in ECR, follow these steps:

1. Authenticate with ACR.The *az acr login* command generates an authentication token and authenticates with your registry.

**Generate Docker Login for ECR (Linux)**

`az acr login --name <acrName>`

2. Invoke Detect, and provide the following paramaters at a minimum.

**Detect - Scanning Images**

```
bash <(curl -s -L https:‎ //detect.blackduck.com/detect11.sh) \
--blackduck.url=<URL> \
--blackduck.api.token=<token> \
--detect.docker.image=<Image URI> \
--detect.project.name=<Project Name>
```

### Invoking Detect as a script to scan a Docker image stored in ACR

If you would rather run Detect as a script than an extension, follow these steps:

In this example, follow the steps to create your first application using the [Azure Portal.](https://docs.microsoft.com/en-us/azure/devops/pipelines/get-started-azure-devops-project?view=vsts)

From the available options, select: **Node.js sample app > Simple Node.js app > Web App for Containers.**

You must authenticate with ACR; refer to [Authenticate with Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-authentication).

Start in **Pipelines > Library** inside Azure DevOps.

1. Refer to [Variable Groups for Builds and Releases](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/variable-groups?view=vsts) page for how to create a Variable Group.

2. Create a variable group for your Black Duck SCA instance:

- blackduck.url (value is the url of your Black Duck SCA instance).
- blackduck.api.token (value is your generated API token, secret).

3. Create a second variable group for your ACR Credentials:

- acr.username (value is your ACR username).
- acr.password (value is your ACR password).

4. Access your build(CI) pipeline by expanding the **Pipelines** sidebar item, and then choosing **Builds**.

5. Select the Pipeline you want to add Detect to, then click **Edit**.

6. Link your variable groups by following the steps in [Use a Variable Group](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/variable-groups?view=vsts#use-a-variable-group).

7. Add a Pipeline task for running Detect:

- After you click **Edit**, the **Tasks** screen of your CI Pipeline opens.
- In the **Build** task, click the plus (**+**) sign to add a new task.
- Use the search bar to search for bash.
- Click **Add** to add the step to your pipeline.

8. Configure the bash step to run after the image has been pushed to ACR.

- Select to run an inline script.
- Reference the following example for the script to run Detect.

```
#/bin/bash
#Log in to ACR using the configured Variable Group
docker login <registryname>.azurecr.io -u $(acr.username) -p $(acr.password)
#Call Detect, passing the Docker Image location
bash <(curl -s -L https:‎ //detect.blackduck.com/detect11.sh) \
--blackduck.url=$(blackduck.url) \
--blackduck.api.token=$(blackduck.api.token) \ 
--detect.docker.image=<registryname>.azurecr.io/<containername>:$(Build.BuildId) \ 
--detect.project.name=$(Build.DefinitionName) \ 
--detect.project.version.name=$(Build.BuildNumber)
```

9. Save and Queue the Pipeline, and then view the Pipeline Run Results.

10. View Scan Results in your instance of Black Duck SCA.
