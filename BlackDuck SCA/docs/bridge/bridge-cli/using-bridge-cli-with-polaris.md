---
title: "Using Bridge CLI with Polaris"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-bridge-cli-with-polaris.html"
content_id: "DB3mniWSJB2WPCpqg3ByGA"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:46:56.985780+00:00"
---

# Using Bridge CLI with Polaris

As a Polaris customer, you can use Bridge CLI to automate SAST, SCA and DAST scanning in your CI pipeline.

Requirements for integrating Bridge with Polaris are specified in Polaris prerequisites.

You can use Bridge CLI to run Polaris scans in the following two ways:

- Running Polaris scans with a JSON file
- Running Polaris scans on the command line

Details about configuring your scans:

- Exporting a SARIF file
- Source code upload scan
- Local analysis scan
- SCA configuration requirements
- Additional SAST configuration requirements
- DAST configuration requirements

For a complete list of configuration options, see Complete list of Bridge arguments.

As an alternative to Bridge CLI, you can also use GitHub Action – Black Duck Security Scan, GitLab – Black Duck Security Scan Template or Azure DevOps – Black Duck Security Scan Extension for Azure DevOps.

## Running Polaris scans with a JSON file

Bridge CLI for Polaris uses Coverity for SAST scans and Black Duck for SCA scans under the hood. Depending on the task, you may need to pass additional SAST and SCA options.

Pass sensitive access token information using the `BRIDGE_POLARIS_ACCESSTOKEN` environment variable, and run Bridge and pass the JSON file using the `--input` command line option.

Note: The `BRIDGE_POLARIS_ACCESSTOKEN` environment variable accepts both user access tokens (created in the Polaris UI) and service account tokens.

Here is a command line example for Polaris:

```
export BRIDGE_POLARIS_ACCESSTOKEN=<POLARIS_ACCESSTOKEN>
bridge-cli --stage polaris --input input.json
```

The above example uses the following:

- `BRIDGE_POLARIS_ACCESSTOKEN` environment variable to pass sensitive information such as password or access token to Bridge CLI (recommended for security purposes). Note that Bridge CLI automatically picks up values passed through these environment variables. Both user access tokens and service account tokens can be used with this environment variable.
- `--stage` argument to specify the Black Duck security product you are integrating with.

Here is the `input.json` file:

```
{
    "data": {
        "polaris": {
            "application": {
                "name": "<APPLICATION_NAME>"
            },
            "project": {
                "name": "<PROJECT_NAME>"
            },
            "branch": {
                "name": "<BRANCH_NAME>"
            },
            "assessment": {
                "types": ["SCA"]
            },
            "test": {
                "sca": {
                    "type": "<TEST_TYPE>"
                }
            },
            "serverUrl": "<POLARIS_URL>"
        }
    }
}
```

Note: Replace `<TEST_TYPE>` with `SCA-SIGNATURE` to run a signature scan or with `SCA-PACKAGE` to explicitly run a package scan. You may also run both scan types in the same pipeline. When both scans are run, Bridge will create two tests on Polaris. One test is created for the Package Manager Scan, and another is created for the Signature Scan.

- **Default value:** `SCA-PACKAGE`
- Run both scan types: `SCA-PACKAGE,SCA-SIGNATURE`

The above JSON file uses the following:

- `polaris.serverurl` for Polaris URL.
- `polaris.application.name` for Polaris Application to use. Note that if the application doesn't already exist in Polaris, Bridge will try to create it before triggering a CI scan. If you have concurrent subscription / team member enabled, the application creation will be successful. If you have parallel subscription, application creation will fail.
- `polaris.project.name` for Polaris Project to use. If the project doesn’t exist on Polaris, it’ll be created. If you don’t want the project to be created, set `polaris.onboarding` to `false`.
- `polaris.branch.name` branch name in the Polaris server. Bridge will error out if a branch name is not provided. If branch doesn’t exist in Polaris, Bridge will create the branch. If you don’t want the branch to be created in Polaris, set `polaris.onboarding` to `false`.
- `polaris.assessment.types` specifies the type of scan to be run: `SAST` or `SCA` or `SAST,SCA` or `DAST`.

For a complete list of environment variables and command line arguments, see Complete list of Bridge arguments.

For additional SAST-specific details, see Additional SAST configuration requirements.

For additional DAST-specific details, see DAST configuration requirements.

## Running Polaris scans on the command line

Instead of using a JSON file, you can pass all arguments via the command line.

Here is a command line example for Polaris:

```
export BRIDGE_POLARIS_ACCESSTOKEN=<POLARIS_ACCESSTOKEN>
bridge-cli --stage polaris polaris.project.name="<PROJECT_NAME>" \
polaris.branch.name="<BRANCH_NAME>" \
polaris.application.name="<APPLICATION_NAME>" \
polaris.assessment.types=SAST,SCA \
polaris.serverurl="<SERVERURL>"
```

The above example uses the following:

- `BRIDGE_POLARIS_ACCESSTOKEN` environment variable to pass sensitive information such as password or access token to Bridge CLI (recommended for security purposes). Note that Bridge CLI automatically picks up values passed through these environment variables. Both user access tokens and service account tokens can be used with this environment variable.
- `--stage` argument to specify the Black Duck security product you are integrating with.
- `polaris.serverurl` for Polaris URL.
- `polaris.application.name` for Polaris Application to use. Note that the specified application must exist on Polaris with appropriate entitlements.
- `polaris.project.name` for Polaris Project to use. If the project doesn’t exist on Polaris, it’ll be created. If you don’t want the project to be created, set `polaris.onboarding` to `false`.
- `polaris.branch.name` branch name in the Polaris server. Bridge will error out if a branch name is not provided. If branch doesn’t exist in Polaris, Bridge will create the branch. If you don’t want the branch to be created in Polaris, set `polaris.onboarding` to `false`.
- `polaris.assessment.types` specifies the type of scan to be run: `SAST` or `SCA` or `SAST,SCA` or `DAST`.

To run scans against a specific branch, pass `polaris.branch.name="<BRANCH.NAME>"`. If the branch does not exist and `polaris.onboarding` is set to `true`, the branch will be created. If the branch does not exist and `polaris.onboarding` is set to `false`, the call will error out.

To add comments to pull requests, pass `polaris.prcomment.enabled` as `true`. You must pass `polaris.branch.name` and `polaris.branch.parent.name`, along with other required options in Complete list of Bridge arguments. By default, Bridge adds comments for Critical and High Severity issues. You can change the severity level by passing `polaris.prcomment.severities`.

Note: For GitHub users only, Bridge reads parent branch name from `github.branch.parent.name`. All other users must specify parent branch name using this option.

For a complete list of environment variables and command line arguments, see Complete list of Bridge arguments.

For additional SAST-specific details, see Additional SAST configuration requirements.

For additional DAST-specific details, see DAST configuration requirements.

## Exporting a SARIF file

Bridge CLI allows you to export findings in a SARIF file. Here is a command line example for Polaris:

```
export BRIDGE_POLARIS_ACCESSTOKEN=<POLARIS_ACCESSTOKEN>
bridge-cli --stage polaris --input input.json
```

Here is the `input.json` file:

```
{
    "data": {
        "polaris": {
            "application": {
                "name": "<APPLICATION_NAME>"
            },
            "project": {
                "name": "<PROJECT_NAME>"
            },
            "branch": {
                "name": "<BRANCH_NAME>"
            },
            "assessment": {
                "types": [
                    "SCA",
                    "SAST"
                ]
            },
            "serverUrl": "<SERVER_URL>",
            "reports": {
                "sarif": {
                    "create": true,
                    "groupSCAIssues": true,
                    "file": {
                        "path": "<FILE_PATH>"
                    },
                    "issue": {
                        "types": ["SCA", "SAST"]
                    },
                    "severities": ["CRITICAL", "HIGH"]
                }
            }
        }
    }
}
```

Note: SARIF report creation is only supported for non MR/PR scans. Set "polaris.reports.sarif.create" to "true", and a SARIF file will be created.

## Source code upload scan

Bridge CLI allows you to upload source code to Polaris, and then scan it with Polaris (mimicking the process a user would follow in the Polaris UI).

Here is the `input.json` file:

```
{
    "data": {
        "polaris": {
            "application": {
                "name": "<APPLICATION_NAME>"
            },
            "project": {
                "name": "<PROJECT_NAME>"
            },
            "branch": {
                "name": "<BRANCH_NAME>"
            },
            "assessment": {
                "types": ["SAST","SCA"]
            },
            "test": {
                "sca": {
                    "location": "remote"
                },
                "sast": {
                    "location": "remote"
                }
            },
            "serverUrl": "<POLARIS_URL>"
        }
    }
}
```

In the example above the `polaris.test.sca` and `polaris.test.sast` parameters have been configured with a value of `remote` to specify that source code should be uploaded to the Polaris platform for scanning and analysis.

## Local analysis scan

Bridge CLI allows source code to be captured and analyzed locally, e.g. within the local CI/CD environment, with scan results uploaded to Polaris. This functionality is particularly valuable in sectors like military and defense, where protecting confidential data and code from unauthorized access is crucial. By enhancing control over compliance with regulatory requirements, organizations can ensure adherence to security standards.

Note: Local analysis is currently only available for SAST assessments.

Local Analysis downloads the Sigma, Polaris Snippet Generator and Coverity Analysis tools to the local environment in addition to the Coverity Analysis license file.

Here is the `input.json` file:

```
{
    "data": {
        "polaris": {
            "application": {
                "name": "<APPLICATION_NAME>"
            },
            "project": {
                "name": "<PROJECT_NAME>"
            },
            "branch": {
                "name": "<BRANCH_NAME>"
            },
            "assessment": {
                "types": ["SAST", "SCA"]
            },
            "test": {
                "sast": {
                    "location": "local"
                }
            },
            "serverUrl": "<POLARIS_URL>"
        }
    }
}
```

In the example above the `polaris.test.sast.location` parameter has been configured with a value of `local` to specify that source code should be captured and analyzed in the local environment. Scan results are then uploaded to Polaris.

The equivalent command line example is:

```
bridge-cli --stage polaris polaris.project.name="<PROJECT_NAME>" \
    polaris.branch.name="<BRANCH_NAME>" \
    polaris.application.name="<APPLICATION_NAME>" \
    polaris.serverurl="<SERVER_URL>" \
    polaris.assessment.types="SAST,SCA" \
    polaris.test.sast.location="local"
```

## SCA configuration requirements

- It is important to run SCA scans as a post-build step to ensure consistent results for a project’s transitive dependencies. If you run a SAST scan with Auto Capture/File Capture prior to running an SCA scan, then you must run a build prior to running SCA. Additionally, if you run SCA alone, then you must run a build prior to running the scan.
- In addition to running scans, you can also optionally configure Bridge CLI to create fix pull requests for SCA issues. Currently, only NPM is supported.

## Additional SAST configuration requirements

A `coverity.yml` configuration file is required for

- Static analysis of compiled languages like C/C++, C# and Java.
- Optimizing static analysis when results are unsatisfactory.

Certain Coverity Connect scans on Polaris require configuration of additional capture settings using a `coverity.yaml` file.

See [Configuring Coverity Thin Client for use with Bridge CLI and Polaris](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/3d79ddc1d59ccc31d9e8859e179b61e7.topic) in the Black Duck® Developer Portal for more information.

## DAST configuration requirements

Before you can start DAST tests with Bridge, you must create a DAST project in Polaris (using the Polaris UI). Bridge will not create DAST projects in Polaris. See [Create and test DAST projects for web applications and APIs](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/0512dbec44b6eba533ecfced82de0f4c.topic) and  [Secure Tunnels With fAST Dynamic](https://blackduck.skilljar.com/polaris-secure-tunnels-with-fast-dynamic?utm_source=docsportal&utm_medium=banner&utm_campaign=pol_academypromo) for more information.

After you create a DAST project in Polaris, use `polaris.assessment.types=DAST` to start a DAST test.

Note: The `DAST` assessment type cannot be combined with other assessment types (`SAST` and/or `SCA`).

An example command you can use to start a DAST test is shown below:

```
bridge-cli --stage polaris \
     \
  polaris.serverUrl="<SERVER_URL>" \
    " \
  polaris.assessment.types="DAST" \
    " \
  polaris.application.name="<APPLICATION_NAME>" \
     \
  polaris.project.name="<PROJECT_NAME>"
```

Note: When you start a DAST test of an internal web application or API using the Bridge CLI, Bridge establishes a secure tunnel automatically (provided your system meets the requirements for Polaris Secure Tunnel).

With Bridge 4.3.0 and later the user can create a secure tunnel from the Polaris Web UI and associate it with a DAST application/project. Bridge CLI determines which tunnel to use via the application and project name.
