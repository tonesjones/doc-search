---
title: "Using Bridge CLI with Software Risk Manager (SRM)"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-bridge-cli-with-software-risk-manager-srm-.html"
content_id: "3SlkM2ZuAE6KeyGWJy1OBQ"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:47:24.532178+00:00"
---

# Using Bridge CLI with Software Risk Manager (SRM)

As a Software Risk Manager (SRM) customer, you can use Bridge CLI to automate SCA and SAST scanning in your CI pipeline.

## Running SRM scans with a JSON file

Pass sensitive information such as username and token using environmental variables, and run Bridge CLI and pass the JSON file using the `--input` command line option.

After passing sensitive data using environmental variables (`$ export BRIDGE_SRM_APIKEY=$SRM_APIKEY`) for security reasons, pass in your JSON file. Here's an example command loading the `input.json` file:

```
bridge-cli --stage srm --input input.json
```

Here is the `input.json` file:

```
{
    "data": {
      "srm": {
        "url": "<SRM URL>",
        "project": {
          "name": "SRM_PROJECT"
        },
        "assessment": {
          "types": [
             "sast",
             "sca"
          ]
        }
         
      },
      "coverity": {
        "execution": {
          "path": "/Users/johndoe/bridge-install-dir/srm-coverity/cov-thin-client-macosx-2023.6.1/bin/coverity"
        }
      }
    }
  }
```

For a complete list of environment variables and command line arguments, see Complete list of Bridge arguments.

## Running SRM scans on the command line

Instead of using a JSON file, you can pass all arguments on the command line.

Here is a command line example for SRM:

```
bridge-cli --stage srm \
srm.url="<SRM URL>" \
srm.project.name="SRM_PROJECT" \
srm.assessment.types=SAST,SCA \
coverity.execution.path="/Users/johndoe/bridge-install-dir/srm-coverity/cov-thin-client-macosx-2023.6.1/bin/coverity"
```

`bridge-cli` indicates you're running the Bridge CLI CLI. The `--stage` flag specifies a group of adapters to run. `srm` indicates you are running the command with SRM.

`srm.project.name` sets the resource to the value `SRM_PROJECT`, invokes the proper adapters to run scans with, and lists the proper scanning server URL. (If this project does not already exit, Bridge CLI will create it.)

Pass arrays using comma separated values (CSV). For example: `srm.assessment.types=SAST,SCA`.

`srm.assessment.types` specifies whether to run `SAST`) or `SCA` scans, or both.

## Running SRM in Air Gap mode

To run Bridge CLI in air gap mode (no connectivity to the Internet):

1. Download the latest/supported version of Detect jar at either:
   - `<home>/.bridge/blackduck` (default location), *or*
   - A location configured using `<tool.install.directory>/blackduck` to override the default.
2. Set air gap to true, by either:
   - Passing on the command line (`network.airgap=true`):

     ```
     bridge-cli --stage srm \
     srm.url="<SRM URL>" \
     srm.project.name="SRM_PROJECT" \
     srm.assessment.types=SAST,SCA \
     coverity.execution.path="/Users/johndoe/bridge-install-dir/srm-coverity/cov-thin-client-macosx-2023.6.1/bin/coverity"
     network.airgap=true
     ```

     *or*
   - Passing it as an argument in your JSON input file:

     ```
     {
         "data": {
             "srm": {
                 …
             },
             "network": {
                 "airgap": true
             }
         }
     }
     ```

For a complete list of environment variables and command line arguments, see Complete list of Bridge CLI arguments.
