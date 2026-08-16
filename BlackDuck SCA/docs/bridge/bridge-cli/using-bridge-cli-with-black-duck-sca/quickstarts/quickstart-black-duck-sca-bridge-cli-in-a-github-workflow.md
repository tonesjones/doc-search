---
title: "Quickstart: Black Duck SCA Bridge CLI in a GitHub workflow"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-black-duck-sca-bridge-cli-in-a-github-workflow.html"
content_id: "FTbnmGEIkHdZaZnu67Cf5g"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:14.178899+00:00"
---

# Quickstart: Black Duck SCA Bridge CLI in a GitHub workflow

As an alternative to the [Black Duck Security Scan Action](https://github.com/marketplace/actions/black-duck-security-scan), the Bridge CLI can be downloaded and directly executed in a GitHub Actions workflow. It has all the functionality of the action, but requires an additional step to [download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/) the Bridge CLI.

To use the CLI directly from a pipeline, the correct Bridge CLI Black Duck® SCA parameters must be passed directly inside the workflow. Furthermore, appropriate access credentials are required to download and use it. Consult the overview page for further details and instructions on use.

Note: The Black Duck Security Scan Action (recommended) can be used for workflows instead of Bridge CLI by following the quickstart guide. The plugin has equivalent functionality and handles the Bridge CLI download and execution automatically.

To discover more about the GitHub Action and what it can do, take a look at the overview page.

## Prerequisites

- The following reading is recommended before starting this quickstart:

  - GitHub prerequisites
  - Pull Request comments
  - Fix pull requests (Fix PRs)
  - External issues
  - List of mandatory and optional parameters for Black Duck SCA
  - Additional GitHub parameters
- Admin access to a GitHub repository.
- Access to a Black Duck SCA server configured with:
  - A Black Duck SCA role that allows creation of authentication tokens.
  - A Black Duck SCA API token with Read and Write access. This can be created by navigating to User Menu > My Profile from within Black Duck SCA.
- A GitHub Personal Access Token. The default `secrets.GITHUB_TOKEN` is recommended to allow the pipeline to inject Pull Request review comments and raise fix Pull Requests.
- For security reasons, it is advisable to use [GitHub Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions) and [Variables](https://docs.github.com/en/actions/learn-github-actions/variables) to store credentials and access tokens.
- Add the following variables and secrets at the repository or organization level (Settings > Secrets and Variables > Actions)

  | Variable | Type | Description | Example |
  | --- | --- | --- | --- |
  | `BLACKDUCK_URL` | Variable | Black Duck SCA Server URL | `https://blackduck.example.com` |
  | `BLACKDUCK_API_TOKEN` | Secret | Black Duck SCA API Token | `REPLACE_WITH_YOUR_TOKEN` |
  | `BRIDGECLI_LINUX64` | Variable | Bridge CLI URL | <https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip> |
- The following Bridge CLI parameters are required to inject Pull Request comments and raise fix Pull Requests:

  | Parameter | Description | Value | Scan type |
  | --- | --- | --- | --- |
  | `blackducksca.fixpr.enabled` | Raise Fix PRs | `true` | Full |
  | `blackducksca.automation.prcomment` | Enable PR comments | `true` | PR |
  | `github.repository.pull.number` | ID of PR to scan | `${{ github.event.number }}` |
- Use the optional environment variables below to configure Bridge to report external repository issues. The environment variables can be uncommented in the workflow file example below.

  | Environment variable | Description | Example |
  | --- | --- | --- |
  | `BRIDGE_BLACKDUCKSCA_EXTERNALISSUES_CREATE` | Enable or disable creation of external issues in GitHub from scan findings. Set to `true` to enable. For more information, see External issues. | `true` or `false` |
  | `BRIDGE_BLACKDUCKSCA_EXTERNALISSUES_SEVERITIES` | Comma-separated list of severities for which external issues should be created. Default: `Critical, High` | `Critical, High, Medium,Low` |
  | `BRIDGE_BLACKDUCKSCA_EXTERNALISSUES_MAXCOUNT` | Set the maximum number number of issues that can be created. Default: `10` | `20` |
  | `BRIDGE_BLACKDUCKSCA_EXTERNALISSUES_GROUPSCAISSUES` | Set to `true` to group SCA issues by vulnerabilities of a component-version pair when creating repository issues. Set to `false` to create separate issues for each vulnerability. Default: `true`. | `true` |

## Instructions

1. Add the following workflow to your repository at `.github/workflows/blackduck-sca.yml`.

   Note: For compiled languages, uncomment the Setup Java JDK and Maven Build steps. Adjust the build commands to align with project specific build tools and requirements, such as Maven, Gradle, or other build systems.

   ```
   name: bd-bridge-cli
   on:
     push:
       branches: [ main, master, develop, stage, release ]
     pull_request:
       branches: [ main, master, develop, stage, release ]
     workflow_dispatch:
   jobs:
     blackduck:
       runs-on: ubuntu-latest
       env:
         BRIDGE_BLACKDUCKSCA_URL: ${{ vars.BLACKDUCK_URL }}
         BRIDGE_BLACKDUCKSCA_TOKEN: ${{ secrets.BLACKDUCK_API_TOKEN }}
         BRIDGE_GITHUB_USER_TOKEN: ${{ secrets.GITHUB_TOKEN }}
         BRIDGE_GITHUB_REPOSITORY_OWNER_NAME: ${{ github.repository_owner }}
         BRIDGE_GITHUB_REPOSITORY_NAME: ${{ github.event.repository.name }}
         BRIDGE_GITHUB_REPOSITORY_BRANCH_NAME: ${{ github.ref_name }}
       steps:
       - name: Checkout Source
         uses: actions/checkout@v4
       # Uncomment the Setup Java JDK step below for compiled languages
       # - name: Setup Java JDK
       #   uses: actions/setup-java@v4
       #   with:
       #     java-version: 21
       #     distribution: temurin
       #     cache: maven
       # Uncomment the Maven Build step below for compiled languages
       # - name: Maven Build
       #   run: mvn -B -DskipTests package
       - name: Black Duck SCA Full Scan
         if: ${{ github.event_name != 'pull_request' }}
         env:
           DETECT_PROJECT_NAME: ${{ github.event.repository.name }}
           DETECT_PROJECT_VERSION_NAME: ${{ github.ref_name }}
           DETECT_CODE_LOCATION_NAME: ${{ github.event.repository.name }}-${{ github.ref_name }}
   	    ## External Issues Parameters
           #
           # Uncomment environment variable below to create an issue for each scan finding
           # Defaults to false.
           # BRIDGE_BLACKDUCKSCA_EXTERNALISSUES_CREATE: true
           #
           # Uncomment environment variable below to filter issue creation by severity
           # Defaults to Critical,High
           # BRIDGE_BLACKDUCKSCA_EXTERNALISSUES_SEVERITIES: 'Critical,High'
           #
           # Uncomment environment variable below to limit the number of issues created from
           # scan findings, Default limit is 10.
           # BRIDGE_BLACKDUCKSCA_EXTERNALISSUES_MAXCOUNT: 10
           #
           # Uncomment environment variable below to group sca issues by vulnerabilities of a
           # component version pair. Default is true.
           # BRIDGE_BLACKDUCKSCA_EXTERNALISSUES_GROUPSCAISSUES: true
           #
           ##
         run: |
           curl -fLsS -o bridge.zip ${{ vars.BRIDGECLI_LINUX64 }} && unzip -qo -d ${{ runner.temp }} bridge.zip && rm -f bridge.zip
           ${{ runner.temp }}/bridge-cli-bundle-linux64/bridge-cli --stage blackducksca \
               blackducksca.scan.full=true \
               blackducksca.scan.failure.severities=BLOCKER \
               blackducksca.fixpr.enabled=true \
               blackducksca.reports.sarif.create=true
       - name: Black Duck SCA PR Scan
         if: ${{ github.event_name == 'pull_request' }}
         env:
           DETECT_PROJECT_NAME: ${{ github.event.repository.name }}
           DETECT_PROJECT_VERSION_NAME: ${{ github.base_ref }}
           DETECT_CODE_LOCATION_NAME: ${{ github.event.repository.name }}-${{ github.base_ref }}
         run: |
           curl -fLsS -o bridge.zip ${{ vars.BRIDGECLI_LINUX64 }} && unzip -qo -d ${{ runner.temp }} bridge.zip && rm -f bridge.zip
           ${{ runner.temp }}/bridge-cli-bundle-linux64/bridge-cli --stage blackducksca \
               blackducksca.scan.full=false \
               blackducksca.automation.prcomment=true \
               github.repository.pull.number=${{ github.event.number }}
   #    - name: Save Logs
   #      if: always()
   #      uses: actions/upload-artifact@v4
   #      with:
   #        name: bridge-logs
   #        path: ${{ github.workspace }}/.bridge
   #        include-hidden-files: true
   ```

   The pipeline will download Bridge CLI from the URL contained in the `BRIDGECLI_LINUX64` environment variable for direct execution in the pipeline. One of the following Black Duck SCA scans will be triggered depending on the event type:
   - **Full Scan**: Triggered by push events to the specified branches (main, master, develop, stage, release). This scan:
     - Performs a complete SCA assessment of all dependencies
     - The workflow includes optional parameters for external issues, which automatically create GitHub repository issues from scan findings, allowing developers to track and remediate security vulnerabilities directly in an existing GitHub workflow without switching to the Black Duck® SCA UI.

       When enabled, external issues can be configured to filter by severity level and assessment type, group related SCA vulnerabilities, and limit the number of issues created per scan. For detailed instructions on configuring external issues, see Create external issues from Black Duck SCA scans.
     - Creates a SARIF report for security findings
     - Enables fix Pull Request generation for vulnerable dependencies
     - Fails the build on BLOCKER severity vulnerabilities
   - **Pull Request Scan**: Triggered for Pull Request events targeting the specified branches. This scan:
     - Performs a differential analysis between the Pull Request and target branch
     - Automatically adds review comments for new issues introduced in the Pull Request
     - Uses the target branch as the baseline for comparison

   Note: To enable diagnostic logging, uncomment the "Save Logs" step at the end of the workflow. This will upload Bridge CLI logs as workflow artifacts for troubleshooting purposes.
2. Run scans

   Once the pipeline is saved:
   1. **Trigger a full scan**: Push changes to a monitored branch (e.g., `main` or `develop`).
   2. **Enable Pull Request scanning**: Create a Pull Request targeting that branch. Pull Request scans will run for each push to the feature branch.
   3. **Review results**: Check for security scan comments added to the Pull Request.

   Example review comment: [image: PR review comments injected by SCA PR scan]

## Useful resources

- [Black Duck product documentation](https://docs.blackduck.com/access?ft:originId=dad2192abc2e53d01fcee1313e1aa841/5bbb905bedd31850d3fe34d6407f0c43.topic&Version=latest)
- Bridge product overview
- [Bridge CLI download](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
