---
title: "Quickstart: Black Duck SCA Bridge CLI in a Bitbucket pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-black-duck-sca-bridge-cli-in-a-bitbucket-pipeline.html"
content_id: "7j8H5xerlHJ8jlahPYThjw"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:13.219120+00:00"
---

# Quickstart: Black Duck SCA Bridge CLI in a Bitbucket pipeline

As an alternative to the Black Duck Security Scan Pipe, the Bridge CLI can be downloaded and directly executed in a Bitbucket Pipeline. It has all the functionality of the Black Duck Security Scan Pipe, but requires an additional step to [download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/) the Bridge CLI.

To use the CLI directly from a pipeline, the correct Bridge CLI Black Duck parameters must be passed directly inside the workflow. Furthermore, appropriate access credentials are required to download and use it. Consult the overview page for further details and instructions on use.

Note: The Black Duck Security Scan Pipe (recommended) can be used for pipelines instead of Bridge CLI by following the quickstart guide. The Black Duck Security Scan Pipe has equivalent functionality and handles the Bridge CLI download and execution automatically.

To discover more about the Black Duck Security Scan Pipe and what it can do, take a look at the overview page.

## Prerequisites

- The following reading is recommended before starting this quickstart:

  - Bitbucket prerequisites
  - Pull Request comments
  - Fix Pull Requests
  - List Of mandatory and optional parameters for Black Duck SCA
  - Additional Bitbucket parameters
- Admin access to a Bitbucket repository.
- Access to a Black Duck SCA server configured with:
  - A Black Duck SCA role that allows creation of authentication tokens.
  - A Black Duck SCA API token with Read and Write access. This can be created by navigating to User Menu > My Profile from within Black Duck SCA.
- A Bitbucket Access Token is required to allow the pipeline to inject Pull Request review comments and raise Fix Pull Requests
- For security reasons, it is advisable to use [Bitbucket variables](https://support.atlassian.com/bitbucket-cloud/docs/variables-and-secrets/) with the `secured` option checked to store credentials and access tokens.
- Add the following variables and secured variables at the repository level (Repository Settings > Pipelines > Secrets and Variables or Workspace Settings > Workspace Variables > Add Variables)

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | `BRIDGE_BLACKDUCKSCA_URL` | Variable | Black Duck SCA Server URL | `https://blackduck.example.com` |
  | `BRIDGE_BLACKDUCKSCA_TOKEN` | Secured Variable | Black Duck SCA API Token | `REPLACE_WITH_YOUR_TOKEN` |
  | `BRIDGE_BITBUCKET_API_TOKEN` | Secured Variable | A Bitbucket Access Token required to inject Pull Request Comments and raise Fix Pull Requests | `REPLACE_WITH_YOUR_TOKEN` |
  | `BRIDGECLI_LINUX64` | Variable | Bridge CLI Download URL | <https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip> |
- The following Bridge CLI parameters are required to inject Pull Request comments and raise fix Pull Requests:

  | Parameter | Description | Value | Scan type |
  | --- | --- | --- | --- |
  | `blackducksca.fixpr.enabled` | Raise Fix PRs for detected issues | `true` | Full |
  | `blackducksca.automation.prcomment` | Enable PR comments | `true` | PR |
  | `bitbucket.project.repository.pull.number` | ID of PR with source code to scan | `$BITBUCKET_PR_ID` |

## Instructions

1. Add the following pipeline configuration to your repository at `bitbucket-pipelines.yml`.

   Note: For compiled languages, uncomment the build sections and image in the provided pipeline configuration. Adjust the build commands and image to align with project specific build tools and requirements, such as Maven, Gradle, or other build systems.

   ```
   # image: maven:3-eclipse-temurin-21
   pipelines:
     branches:
       '{main,master,develop,stage,release}':
         # - step:
         #  name: Build
         #  caches:
         #    - maven
         #  script:
         #    - mvn -B -DskipTests package
         - step:
             name: Black Duck Full Scan
             # caches:
             #   - maven
             script:
               - apt update && apt install -y curl unzip
               - curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d /tmp bridge.zip && rm -f bridge.zip
               - export DETECT_PROJECT_NAME=$BITBUCKET_REPO_SLUG
               - export DETECT_PROJECT_VERSION_NAME=$BITBUCKET_BRANCH
               - export DETECT_CODE_LOCATION_NAME=$BITBUCKET_REPO_SLUG-$BITBUCKET_BRANCH
               - /tmp/bridge-cli-bundle-linux64/bridge-cli --stage blackducksca
                   blackducksca.scan.full='true'
                   blackducksca.scan.failure.severities='BLOCKER'
                   blackducksca.fixpr.enabled='true'
                   blackducksca.reports.sarif.create='true'
                   bitbucket.workspace.id=$BITBUCKET_WORKSPACE
                   bitbucket.project.repository.name=$BITBUCKET_REPO_SLUG
                   bitbucket.project.repository.branch.name=$BITBUCKET_BRANCH
     pull-requests:
       '**':
         # - step:
         #  name: Build
         #  caches:
         #    - maven
         #  script:
         #    - mvn -B -DskipTests package
         - step:
             name: Black Duck PR Scan
             # caches:
             #   - maven
             script:
               - if [[ ! "${BITBUCKET_PR_DESTINATION_BRANCH}" =~ (main|master|develop|stage|release) ]]; then exit; fi
               - apt update && apt install -y curl unzip
               - curl -fLsS -o bridge.zip $BRIDGECLI_LINUX64 && unzip -qo -d /tmp bridge.zip && rm -f bridge.zip
               - export DETECT_PROJECT_NAME=$BITBUCKET_REPO_SLUG
               - export DETECT_PROJECT_VERSION_NAME=$BITBUCKET_PR_DESTINATION_BRANCH
               - export DETECT_CODE_LOCATION_NAME=$BITBUCKET_REPO_SLUG-$BITBUCKET_PR_DESTINATION_BRANCH
               - /tmp/bridge-cli-bundle-linux64/bridge-cli --stage blackducksca
                   blackducksca.scan.full='false'
                   blackducksca.scan.failure.severities='BLOCKER'
                   blackducksca.automation.prcomment='true'
                   bitbucket.workspace.id=$BITBUCKET_WORKSPACE
                   bitbucket.project.repository.name=$BITBUCKET_REPO_SLUG
                   bitbucket.project.repository.pull.number=$BITBUCKET_PR_ID
   ```

   The pipeline will download Bridge CLI from the URL contained in the `BRIDGECLI_LINUX64` environment variable for direct execution in the pipeline. One of the following Black Duck SCA scans will be triggered depending on the event type:
   - **Full Scan**: Triggered by push events to the specified branches (main, master, develop, stage, release). This scan:
     - Performs a complete SCA assessment of all dependencies
     - Creates a SARIF report for security findings
     - Enables fix Pull Request generation for vulnerable dependencies
     - Fails the build on BLOCKER severity vulnerabilities
   - **Pull Request Scan**: Triggered for Pull Request events targeting the specified branches. This scan:
     - Performs a differential analysis between the Pull Request and target branch
     - Automatically adds review comments for new vulnerabilities introduced in the Pull Request
     - Uses the target branch as the baseline for comparison
2. Run scans

   Once the pipeline is saved:
   1. **Trigger a full scan**: Push changes to a monitored branch (e.g., `main` or `develop`).
   2. **Enable Pull Request scanning**: Create a Pull Request targeting that branch. Pull Request scans will run for each push to the feature branch.
   3. **Review results**: Check for security scan comments added to the Pull Request.

   Example review comment: [image: Merge request review comments injected by SCA merge request scan]

## Useful resources

- [Black Duck product documentation](https://docs.blackduck.com/access?ft:originId=dad2192abc2e53d01fcee1313e1aa841/5bbb905bedd31850d3fe34d6407f0c43.topic&Version=latest)
- Bridge product overview
- [Bridge CLI download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
