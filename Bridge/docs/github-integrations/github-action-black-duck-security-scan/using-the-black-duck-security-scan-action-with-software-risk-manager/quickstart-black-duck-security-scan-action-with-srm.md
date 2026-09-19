---
title: "Quickstart: Black Duck Security Scan Action with SRM"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-black-duck-security-scan-action-with-srm.html"
content_id: "k5FSWYxSWRa0gm_5FwCV~w"
version: "latest"
section: "GitHub Integrations"
scraped_at: "2026-08-08T23:47:49.577365+00:00"
---

# Quickstart: Black Duck Security Scan Action with SRM

This quickstart explains how to set up the Black Duck Security Scan Action to integrate with a SRM project to run a full scan, triggered by push and merge events on specified branches.

After the scan completes diagnostic logs will be exported as GitHub build artifacts.

Note: Scanning Pull Requests, injecting Pull Request review comments and creating SARIF reports is not currently supported for workflows that integrate the Black Duck Security Scan Action with Software Risk Manager.

## Prerequisites

- The following reading is recommended:
  - GitHub prerequisites
  - Using the Black Duck Security Scan Action with Software Risk Manager
  - Additional GitHub configuration
- Access to a GitHub repository with admin access.
- Access to a Software Risk Manager (SRM) server instance is required.
- If a Project is not specified, Bridge will try to create one before triggering a scan.
- Software Risk Manager uses Coverity to perform SAST assessments. Coverity requires additional configuration for compiled languages. For languages that use a build system (such as C++, Java, etc.), Coverity must be configured with build and clean commands to capture and analyze the build.
  - The instructions below use pipeline parameters to specify build and clean commands.
  - See Using Bridge with compiled languages for an explanation of the various methods available for configuring Bridge to integrate with Coverity to capture and analyze the build for compiled languages.

## Instructions

1. Create a SRM API Key. In SRM, navigate to User Menu, then My Profile. Ensure the token has read and write access.
2. In the GitHub repository, navigate to Settings, then Secrets and Variables, and then Actions. Add the variables in the following table. 

   | Variable | Type | Description | Example |
   | --- | --- | --- | --- |
   | `SRM_URL` | Variable | SRM Server URL | [https://srm.blackduck.com](https://server.blackduck.com/) |
   | `SRM_API_KEY` | Secret | SRM Authentication Token | `REPLACE_WITH_YOUR_TOKEN` |

   Note: Be sure to add tokens as secrets to avoid exposing them in CI logs.
3. Paste the example below into your workflow file.

   Note: For compiled languages, uncomment the build setup step (e.g., Setup Java JDK) and the `coverity_build_command` and `coverity_clean_command` parameters.

   ```
   name: CI-SRM-Basic
   on:
     push:
       branches: [main, master, develop, stage, release]
     workflow_dispatch:
   jobs:
     build:
       runs-on: [ubuntu-latest]
       steps:
         - name: Checkout Source
           uses: actions/checkout@v5
         # For compiled languages, uncomment and configure the build setup step below:
         # - name: Setup Java JDK
         #   uses: actions/setup-java@v4
         #   with:
         #     java-version: 21
         #     distribution: temurin
         #     cache: maven
         - name: SRM Scan
           uses: blackduck-inc/black-duck-security-scan@v2
           with:
             ### SCANNING: Required fields
             srm_url: ${{ vars.SRM_URL }}
             srm_apikey: ${{ secrets.SRM_API_KEY }}
             srm_assessment_types: "SCA,SAST"
             srm_project_name: ${{ github.event.repository.name }}
             srm_branch_name: ${{ github.ref_name }}
             srm_branch_parent: ${{ github.ref_name != github.event.repository.default_branch && github.event.repository.default_branch || '' }}
             
             ### COVERITY BUILD COMMANDS (uncomment and configure for compiled languages)
             # coverity_build_command: mvn -B -DskipTests package
             # coverity_clean_command: mvn -B clean
             
             ## OPTIONAL DIAGNOSTICS: Upload logs as build artifact if true
             include_diagnostics: false
   ```

   In the example above, the `on` block governs which events trigger the workflow. Once committed in the repository, this file will run the GitHub Action whenever there is a push event on the specified branches. Additionally, the `workflow_dispatch` event allows the action to be manually triggered from the repository, by navigating to **Actions**  then selecting the workflow name, and then clicking Run Workflow.

   Required and optional parameters are configured inside the `with` block.

   Note: The Black Duck Security Scan Action integrates with Software Risk Manager via Bridge CLI. Additional scan configuration options not available through the action's parameter set can be specified by defining relevant Bridge CLI environment variables within the workflow job.

   Set the `include_diagnostics` parameter to `true` to upload logs contained within the `.bridge` folder as GitHub artifacts.
4. Click Commit Changes

## Useful resources

- [Software Risk Manager Product Documentation](https://docs.blackduck.com/access?ft:originId=a7a2d5ea89b6a72cc0064ddb4822a898/eab099e1c0f476a7bddb3e1d5087369b.topic)
- [Black Duck Security Scan Action Documentation](https://github.com/marketplace/actions/black-duck-security-scan)
- [Black Duck Security Scan Action Source](https://github.com/blackduck-inc/black-duck-security-scan)
- Bridge product overview
- Using Bridge CLI
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
