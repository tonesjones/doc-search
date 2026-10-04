---
title: "Using Bridge with compiled languages"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-bridge-with-compiled-languages.html"
content_id: "sz7~CMkUQuL7ivEPEjnOTw"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-10-04T23:28:26.797071+00:00"
content_hash: "4b6405a732f8f50084bba6ba428892e5214a4066454f6171e724504a2f2e38dd"
---

# Using Bridge with compiled languages

Black Duck platforms that use Coverity to perform SAST assessments (Polaris, Software Risk Manager and Coverity itself) require additional configuration for compiled languages to capture and analyze compilation processes by specifying build and clean commands.

Choose a configuration method from the decision table below to configure SAST scans for use with compiled languages in CI/CD pipelines:

Note: For equivalent Bridge CLI configuration please refer to the Coverity section in Bridge Options To Configure Tools.

| Configuration method | Description | Use when... |
| --- | --- | --- |
| Pipeline parameters | Include Bridge **build** and **clean** parameters in the workflow file. | Simplest method:  - No coverity.yml file is in use. - No additional Coverity configuration is required. |
| Configuration file | Coverity Configuration File (coverity.yml) that contains **build** and **clean** commands along with any other Coverity configurations. | - A coverity.yml file is already in use. - Additional Coverity configuration is required. |
| Pipeline args parameter | Pass the **clean** and **build** commands, and any other arguments needed, to the Coverity CLI in the workflow file. | - No coverity.yml file is in use. - Additional Coverity configuration is required. |

## Pipeline clean and build parameters

The simplest configuration is provided by specifying the clean and build parameters directly within the Black Duck Security Scan configuration.

This approach is recommended when a `coverity.yaml` file is not present and no additional Coverity configuration is required.

Table 1. Black Duck Security Scan Coverity clean and build parameters by platform

| Platform | Coverity clean parameter | Coverity build parameter |
| --- | --- | --- |
| - Azure - GitHub - Jenkins | `coverity_clean_command` | `coverity_build_command` |
| - Bitbucket - GitLab | `BRIDGE_COVERITY_CLEAN_COMMAND` | `BRIDGE_COVERITY_BUILD_COMMAND` |

**Example**:

```
name: coverity-action
on:
    push:
        branches: [main, master, develop, stage, release]
    pull_request:
        branches: [main, master, develop, stage, release]
    workflow_dispatch:
jobs:
    coverity:
        runs-on: ubuntu-latest
        steps:
            - name: Checkout Source
                uses: actions/checkout@v4
            - name: Setup Java JDK
                uses: actions/setup-java@v4
                with:
                java-version: 21
                distribution: temurin
                cache: maven
            - name: Coverity Scan
                uses: blackduck-inc/black-duck-security-scan@v2
                with:
                    ### SCANNING: Required fields
                    coverity_url: ${{ vars.COVERITY_URL }}
                    coverity_user: ${{ secrets.COVERITY_USER }}
                    coverity_passphrase: ${{ secrets.COVERITY_PASSPHRASE }}
          
                    ### POLICY ENFORCEMENT: Break build on full scan when encounter outstanding issues
                    coverity_policy_view: ${{ github.event_name != 'pull_request' && 'Outstanding Issues' || '' }}
          
                    ### PULL REQUEST COMMENTS:
                    coverity_prComment_enabled: true
          
                    # Required when PR comments is enabled
                    github_token: ${{ secrets.GITHUB_TOKEN }}
          
                    ### Perform local analysis with full toolkit
                    # coverity_local: true
          
                    ### COVERITY: Build commands for compiled languages
                    coverity_build_command: mvn -B -DskipTests package
                    coverity_clean_command: mvn -B clean
          
                    ## OPTIONAL DIAGNOSTICS: Upload logs as build artifact if true
                    include_diagnostics: false
```

## Coverity configuration file

Add **clean** and **build** commands to a **`coverity.yaml`** file if the file already exists and/or additional Coverity configuration options are required.

**Default coverity.yaml file location**

Bridge searches for a `coverity.yaml` file in the repository root by default. To use a different path, set the configuration parameter appropriate for your SCM platform (see table below).

Note: Bridge CLI 4.4.0 and later supports centralized configuration for SAST scans using a Coverity configuration file managed in the Polaris Web UI. Administrators upload the configuration file to Polaris. During a scan, Bridge CLI retrieves it and passes it to Coverity for analysis.

A locally specified configuration, using `coverity.config.path` or `--config` or `-c` in `coverity.args`, takes precedence over the centrally managed configuration.

If no configuration is available in Polaris or locally, Coverity uses the default CLI and analyzer behavior (see [default analysis documentation](https://docs.blackduck.com/access?ft:originId=f720d35c853c162f322ebf99909fe7c9/48a0a223f2d3132fc578c1a4f7c67eac.topic)).

Table 2. Configuration file path parameter by SCM platform

| SCM platform | Parameter |
| --- | --- |
| - Azure - GitHub - Jenkins | `coverity_config_path` |
| - Bitbucket - GitLab | `BRIDGE_COVERITY_CONFIG_PATH` |

**Example**:

```
capture:
    build:
        clean-command: mvn -B clean
        build-command: mvn -B -DskipTests package
```

Consult this [guide](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/b111ebf4ee3429ab6eea7cab4f88cbd5.topic) for further language examples.

## Pipeline Args parameter

CLI arguments can be passed to the Coverity CLI directly from the Black Duck Security Scan plugin using a configuration parameter. The configuration parameter is set as an argument string.

Use the pipeline **args** parameter to specify **build** and **clean** commands with additional Coverity configuration parameters.

Table 3. Black Duck Security Scan Coverity CLI arguments by platform

| Platform | Coverity CLI arguments parameter |
| --- | --- |
| - Azure - GitHub - Jenkins | `coverity_args` |
| - Bitbucket - GitLab | `BRIDGE_COVERITY_ARGS` |

**Example:**

```
name: coverity-action
on:
  push:
    branches: [main, master, develop, stage, release]
  pull_request:
    branches: [main, master, develop, stage, release]
  workflow_dispatch:
jobs:
  coverity:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Source
        uses: actions/checkout@v4
      - name: Setup Java JDK
        uses: actions/setup-java@v4
        with:
          java-version: 21
          distribution: temurin
          cache: maven
      - name: Coverity Scan
        uses: blackduck-inc/black-duck-security-scan@v2
        with:
          ### SCANNING: Required fields
          coverity_url: ${{ vars.COVERITY_URL }}
          coverity_user: ${{ secrets.COVERITY_USER }}
          coverity_passphrase: ${{ secrets.COVERITY_PASSPHRASE }}

          ### POLICY ENFORCEMENT: Break build on full scan when encountering outstanding issues
          coverity_policy_view: ${{ github.event_name != 'pull_request' && 'Outstanding Issues' || '' }}

          ### PULL REQUEST COMMENTS:
          coverity_prComment_enabled: true

          # Required when PR comments are enabled
          github_token: ${{ secrets.GITHUB_TOKEN }}

          ### COVERITY: Build Arguments for compiled languages
          coverity_args: -o capture.build.clean-command="mvn clean" -o capture.build.build-command="mvn -B -DskipTests package"

          ## OPTIONAL DIAGNOSTICS: Upload logs as build artifact if true
          include_diagnostics: false
```

## Useful resources

- [Coverity support matrix](https://docs.blackduck.com/access?ft:originId=f720d35c853c162f322ebf99909fe7c9/67c1db573f32f7968b154c184e8571a5.topic)
- [coverity.yaml examples](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/b111ebf4ee3429ab6eea7cab4f88cbd5.topic)
