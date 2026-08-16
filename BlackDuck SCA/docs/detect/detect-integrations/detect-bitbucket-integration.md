---
title: "Detect Bitbucket integration"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/detect-bitbucket-integration.html"
content_id: "ZoOsd~2_NgcPIOvlk42PMg"
version: "11.5.1"
section: "Detect Integrations"
scraped_at: "2026-08-08T23:46:12.611303+00:00"
---

# Detect Bitbucket integration

Black Duck® Detect consolidates several scanning utilities and tools and can be used to scan artifacts in a [Bitbucket pipeline](https://bitbucket.org/product/features/pipelines). The following procedures provide guidance on setting up Detect with your Bitbucket continuous integration builds.

## Prerequisites

Integration with BitBucket requires a fully configured instance of Detect and compatible instance of Java. For prerequisite information refer to Requirements and release information

## Configuring with API tokens

The recommended way of configuring Detect with a Bitbucket pipeline is to use an API token.

1. In Black Duck SCA, navigate to the profile of the user whose credentials are used to scan projects from the pipeline.
2. Scroll down to the **User Access Token** section, and complete the fields to create a new token.
3. Check both the **Read Access** and **Write Access** boxes.
4. Click  **Generate.** Save or copy the displayed token.

   Figure 1. Creating the access token
   [image: Creating an access token]

## Configuring Detect for Bitbucket with an API token

This section describes how to run Detect with Bitbucket pipelines using an API token.

1. On the project's Bitbucket page, navigate to **Settings** and then click **Repository Variables** in the left navigation under **Pipelines**.

   Figure 2. Configuring the pipeline with an access token
   [image: Configuring with an access token]
2. Create the following environment variables:

   - BLACKDUCK_URL - URL of your Black Duck SCA environment.
   - BLACKDUCK_TOKEN - API token that you generated in Black Duck SCA.
3. Add the following snippet to the `bitbucket-pipelines.yml` file:

```
bash <(curl -s -L https://detect.blackduck.com/detect11.sh) --blackduck.url="${BLACKDUCK_URL}" 
--blackduck.api.token="${BLACKDUCK_TOKEN}" --blackduck.trust.cert=true --<any other flags>
```

The resulting pipeline YAML file may appear with content similar to the following:

```
# This is a sample build configuration for Java (Maven).
# Check our guides at https://confluence.atlassian.com/x/zd-5Mw for more examples.
# Only use spaces to indent your .yml configuration.
# -----
# You can specify a custom docker image from Docker Hub as your build environment.
image: maven:3.3.9
  
pipelines:
  default:
    - step:
        caches:
          - maven
        script: # Modify the commands below to build your repository.
          - mvn -B verify # -B batch mode makes Maven less verbose
          - mvn clean package
        artifacts:
          - target/**
    - step:
        name: detect
        script:
          - bash <(curl -s -L https://detect.blackduck.com/detect11.sh) --blackduck.url="${BLACKDUCK_URL}" --blackduck.api.token="${BLACKDUCK_TOKEN} --blackduck.trust.cert=true"
```

Important: Configure Detect as a command after the code-build step as it relies on access to the code tree and the build environment.

When you commit the modified YAML file, the build is triggered. After the pipeline build with Detect completes, you can view the complete scan results in your Black Duck SCA instance. For additional information and properties for Detect, refer to Detect properties for more details.
