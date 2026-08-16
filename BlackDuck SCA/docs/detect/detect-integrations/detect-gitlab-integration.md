---
title: "Detect GitLab integration"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/detect-gitlab-integration.html"
content_id: "q8EtSsQ9h8iawGrJUdFTIw"
version: "11.5.1"
section: "Detect Integrations"
scraped_at: "2026-08-08T23:46:11.835243+00:00"
---

# Detect GitLab integration

Black Duck® Detect is designed to run in the native build environment of the project you want to scan. The following procedures provide guidance on setting up Detect with your GitLab continuous integration builds.

## Configuring with API tokens

The recommended way of configuring Detect from a GitLab pipeline is to use an API token. This is detailed as follows.

1. In Black Duck SCA, navigate to the profile of the user whose credentials are used to scan projects from the pipeline.
2. Scroll down to the **User Access Token** section, and complete the fields to create a new token.
3. Check both the **Read Access** and **Write Access** boxes.
4. Click **Generate.** Save or copy the displayed token.

   Figure 1. Creating the access token
   [image: Creating an access token]

## Configuring your environment variables

1. In the sidebar, navigate to **Settings**. Then select **CI/CD**.
2. Expand the **Secret variables** tab.

   Figure 2. Configuring the pipeline secrets
   [image: Configuring the pipeline secrets]
3. Create two environment variables:

   - BLACKDUCK_URL - URL of your Black Duck SCA installation.
   - BLACKDUCK_TOKEN - API token that you generated in Black Duck SCA.

   Note: You can make these variables protected. For additional information, refer to [Gitlab protected secret variables](https://gitlab.com/help/ci/variables/README#protected-secret-variables).
4. Configure Detect to be a script step in the *.gitlab-ci.yml* file of the project you want to scan. Then add the snippet for Detect.

   Ensure that the final line of the following command fits on a single command line.

   ```
   	image: java:8build:
   		stage: build
   		script:
   		- ./gradlew assemble
   	test:
   		stage: test
   		script:
   			- bash <(curl -s -L https://detect.blackduck.com/detect9.sh) --blackduck.url="${BLACKDUCK\_URL}" --blackduck.api.token="${BLACKDUCK\_TOKEN}" --blackduck.trust.cert=true --<any other flags>
   ```
5. Configure Detect as a script build step so GitLab can enforce build changes influenced by Detect. For example, checking for policy, failing builds according to policy, and others.
6. After you commit the change to *.gitlab-ci.yml,* the pipeline runs. After the build with Detect completes, you can view the complete scan results in your Black Duck SCA instance.

## Configuring with username and password

For improved security, it is recommended to use a revocable API token, as described in the preceding process, instead of storing an account password in GitLab settings.

1. In the sidebar project menu, navigate to **Settings** Then select **CI/CD**.
2. Expand the **Secret variables** tab.

   Figure 3. Configuring the pipeline secret variables
   [image: Configuring pipeline secret variables]
3. Create three environment variables:

   - BLACKDUCK_URL - URL of your Black Duck SCA installation.
   - BLACKDUCK_USERNAME - containing the username of the Black Duck SCA account to be used.
   - BLACKDUCK_PASSWORD - containing the password of the Black Duck SCA account to be used.

   Note: You can make these variables protected. For additional information, refer to [Gitlab protected secret variables](https://docs.gitlab.com/ee/ci/variables/#protect-a-cicd-variable).
4. Configure Detect to be a script step in the *.gitlab-ci.yml* file of the project you want to scan. Then add the snippet for Detect.

   Ensure that the final line of the following command fits on a single command line.

   ```
   	image: java:8build:
   		stage: build
   		script:
   		- ./gradlew assemble
   	test:
   		stage: test
   		script:
   			- bash <(curl -s -L <https://detect.blackduck.com/detect9.sh>) --blackduck.url="${BLACKDUCK\_URL}" --blackduck.hub.username="${BLACKDUCK\_USERNAME}" --blackduck.hub.password="${BLACKDUCK\_PASSWORD}" --blackduck.trust.cert=true --<any other flags>
   ```
5. Configure Detect as a script build step so GitLab can enforce build changes influenced by Detect. For example, checking for policy, failing builds according to policy, and others.
6. After you commit the change to *gitlab-ci.yml*, the pipeline runs. When the build with Detect completes, you can view the scan results in your Black Duck SCA instance.
