---
title: "GitLab prerequisites"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/gitlab-prerequisites.html"
content_id: "vEr4YZrSbEFnyYxynqSzzg"
version: "latest"
section: "GitLab Integrations"
scraped_at: "2026-08-08T23:48:04.709666+00:00"
---

# GitLab prerequisites

Before configuring Black Duck Security Scan Template into your GitLab pipeline, you must meet the following prerequisites.

## Basic requirements

- For self managed GitLab environments, PR comments and Fix PRs require GitLab 15.7 or Later.
- Starting with Bridge version 3.5.1, the Black Duck Security Scan Template now includes support for Linux ARM architectures.

## **GitLab runner setup options**

- GitLab Runner is an application that works with GitLab CI/CD to run jobs in a pipeline. To use GitLab Runner in your project, you must have the maintainer or owner role for the project.
- A GitLab runner can be self-managed or SaaS runners managed by GitLab. The choice of GitLab runner depends on the specific requirements and characteristics of the project. For example, self-managed runners are ideal when there is a need for tailored execution environments, such as: using specific hardware or software configurations, ensuring data security within a private network, or dynamically scaling resources to accommodate varying workloads efficiently. Conversely, SaaS runners offer quick and easy setup, eliminating the need for infrastructure configuration and management.
- A GitLab self-managed runner can be installed and used on GNU/Linux, macOS and Windows. For more details refer to: [Install GitLab Runner](https://docs.gitlab.com/runner/install/).
  - To set up project specific self-managed runner, go to (**Project Settings** → **CI/CD** → **Runners**) and configure.
  - During runner registration, choose executor as `shell`.
  - Pipelines that use a self-managed runner should be configured to include the GitLab Template as shown below:

    ```
    include:
      - remote: "https://gitlab.com/blackduck-inc/black-duck-security-scan/-/raw/main/templates/security_scan.yml"
    ```
- A GitLab SaaS runner is hosted and managed by GitLab:
  - Pipelines that use a SaaS runner should include the GitLab Template as shown below:

    ```
    include:
      - project: blackduck-inc/black-duck-security-scan
        ref: v2
        file: templates/security_scan.yml
    ```

    Note: Update the value for the `ref` key to specify the intended version.
- Ensure that curl and unzip package tools are installed for using self-managed/SaaS runner (Linux/Mac).
- The GitLab Template supports both Project runners and Shared runners (except Shared Mac Runners).

## Configure GitLab variables

- Sensitive data such as access tokens, user names, passwords and even URLs must be configured using GitLab variables.
- These can be added at the Project, Group or Global scopes (Global for self-managed GitLab instances only).
- To add variables, go to **Settings** → **CI/CD** → **Variables**. Be sure to mask passwords and tokens to avoid them being exposed in logs. For more details, see [GitLab CI/CD variables](https://docs.gitlab.com/ee/ci/variables).

## Configure GitLab user token

- `BRIDGE_GITLAB_USER_TOKEN` is required as input when running Black Duck SCA Fix PR, Black Duck SCA/Coverity PR Comment.
- Generate a Personal Access Token (PAT) from GitLab (**User Settings** → **Access Tokens**) and store it as a secret variable or store and fetch it from the vault.
- PAT must have **api** scope to perform Black Duck SCA Fix PR or Black Duck SCA/Coverity PR Comment. For more details, see [Personal access tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html).

## Create a `.gitlab-ci.yml` file

- Before running a pipeline using the GitLab Template, add a `.gitlab-ci.yml` file to your project by adding an `include` entry appropriate for the type of GitLab runner
- Push those changes and a GitLab runner picks up the job and initiates the pipeline.

## GitLab vulnerability reports

- The **Gitlab Ultimate** license is required in order to create SAST and SCA (dependency scanning) reports on GitLab. This is the case for both deployment models, GitLab Self-Managed and SaaS.
- You must have maintainer access to view the reports on the dashboard.
- Gitlab Vulnerability report is supported and verified for Gitlab SaaS.
- Gitlab Vulnerability report is not available for Pull request events.

## How to use GitLab vulnerability reports

- Set `BRIDGE_BLACKDUCKSCA_REPORTS_GITLAB_CREATE` or `BRIDGE_POLARIS_REPORTS_GITLAB_CREATE` to `true` to enable the respective reports.
- GitLab can only package artifacts located within the `$CI_PROJECT_DIR` directory. If `BRIDGE_POLARIS_REPORTS_GITLAB_DIR_PATH` is set outside `$CI_PROJECT_DIR`, the GitLab report will not be uploaded. (This is also the case for `BRIDGE_BLACKDUCKSCA_REPORTS_GITLAB_DIR_PATH`.)
- The default file names are `sca.json` for Blackduck SCA/Polaris SCA and `sast.json` for Polaris SAST, as set by Bridge.
- Ensure the directory path, along with the file name, is specified under **artifacts** in the `.gitlab-ci.yml` file. (Note: `dependency_scanning` refers to SCA.)

  **Default Example**

  ```
  artifacts:
      when: always
      reports:
          sast: $CI_PROJECT_DIR/.bridge/Polaris Gitlab Reports Generator/sast.json
          dependency_scanning: $CI_PROJECT_DIR/.bridge/Polaris Gitlab Reports Generator/sca.json
  ```

  **Custom Directory Example**

  ```
  artifacts:
      when: always
      reports:
          sast: $CI_PROJECT_DIR/custom_dir/sast.json
          dependency_scanning: $CI_PROJECT_DIR/custom_dir/sca.json
  ```
- Reports can be viewed on **Secure → Vulnerability Report/Security Dashboard** (from the Left side on the Gitlab menu).

Note:

- The Security Dashboard displays vulnerabilities from scans performed on the main or default branch only. Vulnerabilities can be viewed on specific Pipeline Job as well under the Security Tab. Vulnerabilities can be viewed on the MR summary page as well. For example, if Scan 1 identifies 10 vulnerabilities and 2 of them are resolved in Scan 2, the user must change the status of the resolved vulnerabilities to Resolved or False Positive. Otherwise, these vulnerabilities will continue to appear on the dashboard with the Needs Triage status.
- Identifiers are not aligned, even though CVE/CWE entries are sorted and placed at the beginning of the list during file creation (this behavior is controlled by GitLab). If two or more issues are reported by scanning tools, only the issue with the highest severity level will be displayed.
- The GitLab Vulnerability Report is not uploaded when policy violations appear in the scan that resulted in pipeline failure.
- If Bridge returns exit code `8`, and you want to generate a Gitlab Vulnerability report, you must set `MARK_BUILD_STATUS: 'success'` in the workflow file.
