---
title: "Quickstart: Polaris Bridge CLI in a GitHub workflow"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-polaris-bridge-cli-in-a-github-workflow.html"
content_id: "uoEvtoRlNAihuTseBI84ZQ"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:00.515586+00:00"
---

# Quickstart: Polaris Bridge CLI in a GitHub workflow

As an alternative to the [Black Duck Security Scan Action](https://github.com/marketplace/actions/black-duck-security-scan), the Bridge CLI can be downloaded and directly executed in a GitHub workflow. It has all the functionality of the action, but you must add a step to download the Bridge CLI from [repo.blackduck.com](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries).

To use the CLI directly from your workflow, you will have to pass the correct Bridge CLI execution commands directly inside the workflow. You also need to have the proper access credentials to download and use it. You can review the following documentation for instructions on use: Using Bridge CLI with Polaris.

Note: You can use Black Duck Security Scan Action (recommended) for your workflow instead of Bridge CLI by following the quickstart guide Quickstart: Black Duck Security Scan Action with Polaris

## Prerequisites

- In addition to a GitHub repository, you need Polaris access before you start this workflow.
- If the application doesn't already exist in Polaris, Bridge will try and create it before triggering a CI scan. If you have concurrent subscription / team member enabled, the application creation will be successful. If you have parallel subscription, application creation will fail.
- We recommend the following reading before you start:
  - GitHub prerequisites
  - Using the Black Duck Security Scan Action with Polaris
  - External issues
  - Pull request (PR) comments
  - Additional GitHub configuration
  - This micro-course: [Polaris: Using the Black Duck Security Scan GitHub Action](https://blackduck.skilljar.com/polaris-using-the-synopsys-github-action)

## Instructions

1. Create a GitHub token. See the micro-course tutorial in the prerequisites section above if you need instructions.

   Important: Confirm that the token has workflow read & write permissions. In GitHub, navigate to Project > Settings > Actions > General > Workflow Permissions.
2. Add the following variables (GitHub > Project > Settings > Secrets and Variables > Actions):

   | Variable | Type | Description | Example |
   | --- | --- | --- | --- |
   | `POLARIS_SERVERURL` | Variable | Polaris Server URL | `https://polaris.synopsys.com` (or `https://polaris.blackduck.com` after you [Migrate Polaris to the Black Duck domain](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/ee117187a16710bb1231f1919c97c0ed.topic)) |
   | `POLARIS_ACCESSTOKEN` | Secret | Polaris Access Token. You can use either an access token created in the Polaris UI or a service account token. | `REPLACE_WITH_YOUR_TOKEN` |
   | `BRIDGECLI_LINUX64` | Variable | Bridge CLI URL for Linux 64-bit runners. For other platforms, use the appropriate URL: `bridge-cli-bundle-macosx.zip` for Intel Mac or `bridge-cli-bundle-macos_arm.zip` for Apple Silicon Mac. | `https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip` |

   Warning: For security reasons please be sure to add `POLARIS_ACCESSTOKEN` as a secret to avoid exposing it in CI logs.

   Use the optional environment variables below to configure Bridge to report external repository issues. The environment variables can be uncommented in the workflow file example below.

   | Environment variable | Description | Example |
   | --- | --- | --- |
   | `BRIDGE_POLARIS_EXTERNALISSUES_CREATE` | Enable or disable creation of external issues in GitHub from scan findings. Set to `true` to enable. For more information, see External issues. | `true` or `false` |
   | `BRIDGE_POLARIS_EXTERNALISSUES_SEVERITIES` | Comma-separated list of severities for which external issues should be created. Default: `Critical,High` | `Critical,High,Medium,Low` |
   | `BRIDGE_POLARIS_EXTERNALISSUES_TYPES` | Comma-separated list of scan types for which external issues should be created. Accepted values: `SAST`, `SCA` | `SAST,SCA` |
   | `BRIDGE_POLARIS_EXTERNALISSUES_MAXCOUNT` | Set the maximum number number of issues that can be created. Default: `10` | `20` |
   | `BRIDGE_POLARIS_EXTERNALISSUES_GROUPSCAISSUES` | Set to `true` to group SCA issues by vulnerabilities of a component-version pair when creating repository issues. Set to `false` to create separate issues for each vulnerability. Default: `true`. | `true` |
3. Add a [coverity.yaml](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/cli/topics/options_reference.html) file in the project repository. (Uncompiled languages are detected and configured automatically).

   ```
   capture:
     build:
       clean-command: mvn -B clean
       build-command: mvn -B -DskipTests package
   ```

   Note: This example above uses maven and showcases the contents of coverity.yaml. You can use Maven but you can also substitute your own build and clean commands by following these instructions: [Configuring Coverity Thin Client for use with Bridge CLI and Polaris](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/3d79ddc1d59ccc31d9e8859e179b61e7.topic).
4. Create a new workflow (Actions > New Workflow > Setup a workflow yourself).

   Note: Please remember to substitute example variable values with your own desired values such as correct project branches, repository names, application name.

   Paste this example and please remember to change the applicable variable values with your own, such as: names of branches, project name, application name.

   ```
   # example workflow for Polaris scans using the Bridge CLI
   name: polaris-bridge-cli
   on:
     push:
       branches: [ main, master, develop, stage, release ]
     pull_request:
       branches: [ main, master, develop, stage, release ]
     workflow_dispatch:
   jobs:
     polaris:
       runs-on: ubuntu-latest
       env:
         BRIDGE_POLARIS_SERVERURL: ${{ secrets.POLARIS_SERVERURL }}
         BRIDGE_POLARIS_ACCESSTOKEN: ${{ secrets.POLARIS_ACCESSTOKEN }}
         BRIDGE_POLARIS_ASSESSMENT_TYPES: 'SAST,SCA'
         BRIDGE_POLARIS_APPLICATION_NAME: ${{ github.event.repository.name }}
         BRIDGE_POLARIS_PROJECT_NAME: ${{ github.event.repository.name }}
         BRIDGE_POLARIS_BRANCH_NAME: ${{ github.ref_name }}
       steps:
       - name: Checkout Source
         uses: actions/checkout@v3
       - name: Setup Java JDK
         uses: actions/setup-java@v3
         with:
           java-version: 17
           distribution: microsoft
           cache: maven
       - name: Polaris Full Scan
         if: ${{ github.event_name != 'pull_request' }}
         env:
           BRIDGE_POLARIS_FIXPR_ENABLED: true
           
           ## External Issues Parameters
           #
           # Uncomment environment variable below to create an issue for each scan finding
           # Defaults to false.
           # BRIDGE_POLARIS_EXTERNALISSUES_CREATE: true
           #
           # Uncomment environment variable below to filter issue creation by severity
           # Defaults to Critical,High
           # BRIDGE_POLARIS_EXTERNALISSUES_SEVERITIES: 'Critical,High'
           #
           # Uncomment environment variable below to filter issue creation by assessment type
           # BRIDGE_POLARIS_EXTERNALISSUES_TYPES: "SAST,SCA"
           #
           # Uncomment environment variable below to limit the number of issues created from
           # scan findings, Default limit is 10.
           # BRIDGE_POLARIS_EXTERNALISSUES_MAXCOUNT: 10
           #
           # Uncomment environment variable below to group sca issues by vulnerabilities of a
           # component version pair. Default is true.
           # BRIDGE_POLARIS_EXTERNALISSUES_GROUPSCAISSUES: true
           #
           ##
         run: |
           curl -fLsS -o bridge.zip ${{ vars.BRIDGECLI_LINUX64 }} && unzip -qo -d ${{runner.temp}} bridge.zip && rm -f bridge.zip
           ${{runner.temp}}/bridge-cli-bundle-linux64/bridge-cli --stage polaris \
           github.user.token=${{ secrets.GITHUB_TOKEN }}
       - name: Polaris PR Scan
         if: ${{ github.event_name == 'pull_request' }}
         run: |
           curl -fLsS -o bridge.zip ${{ vars.BRIDGECLI_LINUX64 }} && unzip -qo -d ${{runner.temp}} bridge.zip && rm -f bridge.zip
           ${{runner.temp}}/bridge-cli-bundle-linux64/bridge-cli --stage polaris \
               polaris.prcomment.enabled=true \
               polaris.branch.parent.name=${{ github.event.pull_request.base.ref }} \
               github.repository.branch.name=${{ github.event.pull_request.head.ref }} \
               github.repository.name=${{ github.event.repository.name }} \
               github.repository.owner.name=${{ github.repository_owner }} \
               github.repository.pull.number=${{ github.event.number }} \
               github.user.token=${{ secrets.GITHUB_TOKEN }}
   #    - name: Save Logs
   #      if: always()
   #      uses: actions/upload-artifact@v3
   #      with:
   #        name: bridge-logs
   #        path: ${{ github.workspace }}/.bridge
   ```

   This workflow automates security scanning for a repository using Polaris SAST and SCA analysis. The workflow runs on pushes and pull requests to specified branches and includes two distinct scan types: full scans for pushes and PR-specific scans with code review comments for pull requests.

   Fix pull requests are enabled to raise pull requests to upgrade dependencies for full scans of branches. See Fix pull requests (Fix PRs) and Using SCA Fix PRs with Bridge for further information and examples that demonstrate how to:
   - Configure order of preference for upgrade guidance
   - Raise Fix Pull Requests by severity
   - Enforce a maximum limit for the number of Fix Pull Requests created.

   The workflow includes optional parameters for external issues, which automatically create GitHub repository issues from scan findings, allowing developers to track and remediate security vulnerabilities directly in an existing GitHub workflow without switching to the Polaris UI.

   When enabled, external issues can be configured to filter by severity level and assessment type, group related SCA vulnerabilities, and limit the number of issues created per scan. For detailed instructions on configuring external issues, see Create external issues from Polaris scans.

   The following is a list of mandatory Bridge arguments used:

   | Variable | Type | Description | Example |
   | --- | --- | --- | --- |
   | `BRIDGE_POLARIS_APPLICATION_NAME` | Variable | Name of application in Polaris. If the application doesn't already exist in Polaris, Bridge will try to create it before triggering a CI scan. If you have concurrent subscription / team member enabled, the application creation will be successful. If you have parallel subscription, application creation will fail. | `YOUR_BRANCH_NAME` |
   | `BRIDGE_POLARIS_PROJECT_NAME` | Variable | The specified project is created on Polaris if it doesn't exist. If you don't want the project to be created, set `polaris.onboarding` to false. | `YOUR_PROJECT_NAME` |
   | `BRIDGE_POLARIS_ASSESSMENT_TYPES` | Variable | Comma separated values. For DAST configuration requirements, see Using Bridge With Polaris. | Accepted values: - `DAST` - `SAST` - `SCA` - `SCA,SAST` |
   | `BRIDGE_POLARIS_BRANCH_NAME` | Variable | Branch name in the Polaris server. If the branch does not exist, it creates the branch if `polaris.onboarding` is set to `true`. If `polaris.onboarding` is not enabled, the call will error out.  If a branch name is not provided, Bridge will error out and no tests will be created. | `YOUR_BRANCH_NAME` |

   Note: You can check out the Complete list of Bridge arguments.

### Windows PowerShell

Windows build agents use PowerShell instead of Bash and do not always have curl and/or unzip installed. The following can be used instead of curl and unzip in the above example.

```
      run: |
        Invoke-WebRequest -Uri ${{ vars.BRIDGECLI_WIN64 }} -OutFile bridge.zip
        Expand-Archive -Path bridge.zip -DestinationPath ${{ runner.temp }} -Force
        Remove-Item -Path bridge.zip -Force
        ${{ runner.temp }}/bridge-cli --verbose --stage polaris
```

## Useful resources

- [Polaris product documentation](https://polaris.blackduck.com/developer/default/)
- [Black Duck Security Scan Action Documentation](https://github.com/marketplace/actions/black-duck-security-scan)
- [Black Duck Security Scan Action Source](https://github.com/blackduck-inc/black-duck-security-scan)
- Bridge product overview
- [Bridge CLI Download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
