---
title: "Using Bridge CLI with Coverity"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-bridge-cli-with-coverity.html"
content_id: "aQUbyCwfvaXW3nOBHZz2yg"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:17.486245+00:00"
---

# Using Bridge CLI with Coverity

As a Coverity customer, you can use Bridge CLI to automate SAST scanning in your CI/CD pipeline.

Note: You can use Bridge CLI with both on-prem Coverity Connect as well as Coverity cloud deployment. Details below.

Use the decision table below to learn more:

| Howto | Documentation |
| --- | --- |
| Integrate Bridge CLI With Coverity | - Running Coverity scans using a JSON file - Running Coverity scans using the command line |
| Authenticate with Coverity Connect Using Auth Key | - Using auth keys with Bridge |
| Raise Fail Pull Requests with Coverity with comments added for security issues detected according to specific levels of impact | - Using Fail Pull Requests With Coverity - Creating Coverity Fail Pull Requests |

For more information, see Complete list of Bridge CLI arguments.

Note: As an alternative to Bridge CLI, you can also use GitHub Action – Black Duck Security Scan, GitLab – Black Duck Security Scan Template or Azure DevOps – Black Duck Security Scan Extension for Azure DevOps.

## Running Coverity scans using a JSON file

Pass sensitive information such as username and password using environmental variables, and run Bridge CLI and pass the JSON file using the `--input` command line option.

Here is the example command line:

```
export BRIDGE_COVERITY_CONNECT_USER_NAME="<COV_USER>"
export BRIDGE_COVERITY_CONNECT_USER_PASSWORD="<COVERITY_PASSPHRASE>"
bridge-cli --stage connect --input input.json
```

Here's an example `input.json` file that you can use with on-prem Coverity Connect:

```
{
  "data": 
    {
        "coverity": 
        {
             "connect": {
                    "url": "<CONNECT_URL>",
                        "project":{
                        "name": "<PROJECT_NAME>"
                    },
                    "stream": {
                        "name": "<STREAM_NAME>"  
                    },
                    "policy": {
                        "view": "<View Name / Id>"
                    }
                },
            "local": true
        }
    }
}
```

Here is an example `input.json` file that you can use with Coverity cloud deployment:

```
{
  "data": 
    {
        "coverity": 
        {
             "connect": {
                    "url": "<CONNECT_URL>",
                        "project":{
                        "name": "<PROJECT_NAME>"
                    },
                    "stream": {
                        "name": "<STREAM_NAME>"  
                    },
                    "policy": {
                        "view": "<View Name / Id>"
                    }
            }
        }
    }
}
```

The above examples use the following:

- `BRIDGE_COVERITY_CONNECT_USER_NAME` and `BRIDGE_COVERITY_CONNECT_USER_PASSWORD` environment variables to pass sensitive information such as password or access token to Bridge CLI (recommended for security purposes). Note that Bridge CLI automatically picks up values passed through these environment variables.
- `--stage` to specify the Black Duck security product you are integrating with.
- `coverity.connect.url` for Coverity Connect URL.
- `coverity.connect.project.name` for project on Coverity Connect. Project will be created if it doesn't exist.
- `coverity.connect.stream.name` for stream on Coverity Connect. Stream will be created if it doesn't exist.
- `coverity.connect.policy.view` for policy view to be used by Bridge CLI to decide if the CI pipeline should be failed or not.
- `coverity.local` to let Bridge CLI know if this is an on-prem Coverity Connect or a Coverity cloud deployment.

## Running Coverity scans using the command line

Instead of using a JSON file, you can pass arguments on the command line.

Here are the example commands that you can use with on-prem Coverity Connect:

```
export BRIDGE_COVERITY_CONNECT_USER_NAME=<COV_USER>
export BRIDGE_COVERITY_CONNECT_USER_PASSWORD=<COVERITY_PASSPHRASE>
bridge-cli --stage connect \ 
  coverity.connect.url=<COVERITY_URL> \
  coverity.connect.project.name=<COVERITY_PROJECT> \ 
  coverity.connect.stream.name=<COVERITY_STREAM> \ 
  coverity.connect.policy.view=<COVERITY_VIEW_NAME> \ 
  coverity.local=true
```

Here are the example commands that you can use with Coverity cloud deployment:

```
export BRIDGE_COVERITY_CONNECT_USER_NAME=<COV_USER>
export BRIDGE_COVERITY_CONNECT_USER_PASSWORD=<COVERITY_PASSPHRASE>
bridge-cli --stage connect \ 
   coverity.connect.url=<COVERITY_URL> \
   coverity.connect.project.name=<COVERITY_PROJECT> \ 
   coverity.connect.stream.name=<COVERITY_STREAM> \ 
   coverity.connect.policy.view=<COVERITY_VIEW_NAME>
```

The above examples use the following:

- `BRIDGE_COVERITY_CONNECT_USER_NAME` and `BRIDGE_COVERITY_CONNECT_USER_PASSWORD` environment variables to pass sensitive information such as password or access token to Bridge CLI (recommended for security purposes). Note that Bridge CLI automatically picks up values passed through these environment variables.
- `--stage` to specify the Black Duck security product you are integrating with.
- `coverity.connect.url` for Coverity Connect URL.
- `coverity.connect.project.name` for project on Coverity Connect. Project will be created if it doesn't exist.
- `coverity.connect.stream.name` for stream on Coverity Connect. Stream will be created if it doesn't exist.
- `coverity.connect.policy.view` for Coverity policy view to be used by Bridge CLI to decide if the CI pipeline should be failed or not.
- `coverity.local` to let Bridge CLI know if this is an on-prem Coverity Connect or a Coverity cloud deployment.

Note: If you are using Coverity Cloud Deployment version 2023.6 or newer, note that Bridge CLI uses the default version of the Thin Client as configured on the Coverity cloud server. To use a specific version of Thin Client, pass the `version` argument. For more details, refer to Coverity Connect table in the Complete list of Bridge CLI arguments.

For more details, see the Complete List of Bridge CLI Arguments.

## Using auth keys with Bridge

For Coverity Connect workflows, you need to provide the user name and password as input to Bridge. Coverity Connect provides a way for users to generate the auth keys, which can be used for authentication / access to Connect APIs. Although Bridge does not support accepting an auth key file as input, you can still use the auth key with Bridge by passing it directly in the CLI.

- Generate auth keys from Coverity Connect - ( [Black Duck Documentation Portal](https://docs.blackduck.com/access?ft:originId=coverity-docs-latest_en-US/Chunk1186420026.html)).
- Open generated auth key file, read the key field from it, and pass it as the password to Bridge.

## Creating Coverity Fail Pull Requests

Coverity security scans can be configured to automatically fail Pull Request scans when security issues are detected according to specified levels of impact. Integrating this capability into CI/CD pipelines prevents high-impact security vulnerabilities from entering the production codebase. Visit Using Fail Pull Requests With Coverity page to learn more.

Note: When both `coverity.prcomment.enabled` and `coverity.connect.policy.view` are configured for a Coverity PR scan, the `coverity.connect.policy.view` setting will be ignored, and PR comments will be generated only for new issues that match the specified impact filter (`coverity.prcomment.impacts`).

The `coverity.prcomment.enabled` and `coverity.prcomment.impacts` parameters are used to configure the Pull Request comments feature. Command usage is documented in the Complete List Of Bridge Commands page.

To create Coverity Fail Pull Requests:

- Set `coverity.prcomment.enabled` to `true`
- Use `coverity.prcomment.impacts` to define an Impact levels filter. If new issues are detected in the Coverity Pull Request that match the filter then:
  - The Pull Request scan and the build will be marked as failed.
  - Matching issues will be uploaded to Coverity Server
  - Comments will be added to the Pull Request for matching issues.
- Pass source code repository token as shown in the example below:
  - `github.user.token` for GitHub
  - `gitlab.user.token` for GitLab
  - `azure.user.token` for Azure DevOps
- Pass additional options as necessary

Below is an example that uses an `input.json` file. Pass access tokens using environmental variables:

```
export BRIDGE_COVERITY_CONNECT_USER_NAME="<COV_USER>"
export BRIDGE_COVERITY_CONNECT_USER_PASSWORD="<COVERITY_PASSPHRASE>"
export GITHUB_USER_TOKEN=<GITHUB_USER_TOKEN>
```

Create an input file as follows:

```
{
    "data": {
        "coverity": {
            "connect": {
                "url": "<CONNECT_URL>",
                "project": {
                    "name": "<PROJECT_NAME>"
                },
                "stream": {
                    "name": "<STREAM_NAME>"
                },
                "policy": {
                    "view": "<View Name/ID>"
                }
            },
            "github": {
                "repository": {
                    "name": "<GitHub Repo Name>",
                    "owner": {
                        "name": "<GitHub Owner Name>"
                    },
                    "branch": {
                        "name": "<Branch Name>"
                    },
                    "pull": {
                        "number": <Pull Request Number>
                    }
                }
            },
            "prcomment": {
                "enabled": true,
                "impacts": ["High"]
            }
        }
    }
}
```

The command line equivalent is:

```
export BRIDGE_COVERITY_CONNECT_USER_NAME="<COV_USER>"
export BRIDGE_COVERITY_CONNECT_USER_PASSWORD="<COVERITY_PASSPHRASE>"
export GITHUB_USER_TOKEN=<GITHUB_USER_TOKEN>

bridge --connect.url="<CONNECT_URL>" \
       --connect.project.name="<PROJECT_NAME>" \
       --connect.stream.name="<STREAM_NAME>" \
       --connect.policy.view="<View Name/ID>" \
       --github.repository.name="<GitHub Repo Name>" \
       --github.repository.owner.name="<GitHub Owner Name>" \
       --github.repository.branch.name="<Branch Name>" \
       --github.repository.pull.number=<Pull Request Number> \
       --prcomment.enabled=true \
       --prcomment.impacts="High"
```

It can be observed from the examples above that the `coverity.prcomment.enabled` parameter is set to `true` and a high impact level filter is configured for `coverity.prcomment.impacts`. Subsequently, the following actions are performed by Bridge when new high impact issues are detected by a Coverity Pull Request scan:

- Pull Request comments are added for high impact issues.
- New high impact issues are uploaded to the Coverity Server (CNC and Connect).
- The Pull Request scan fails if high impact issues are detected and the build is marked as failed.
