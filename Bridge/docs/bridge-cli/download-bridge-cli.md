---
title: "Download Bridge CLI"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/download-bridge-cli.html"
content_id: "N6ht5MB9qNia93RVsekK1g"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:46:49.883825+00:00"
---

# Download Bridge CLI

## Bridge is now available in two flavors

- [Bridge CLI Bundle](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/)
- [Bridge CLI Thin Client](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-thin-client/latest/)

Note: The existing Bridge package has been renamed to Bridge CLI Bundle and includes all the features.

## Using Bridge CLI Bundle

1. Download the latest Bridge Bundle from [repo.blackduck.com](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/) or the Polaris
   UI.
   - If Bridge Bundle is downloaded from
     `repo.blackduck.com`, please verify the checksum.
     - Mac example:

       `cat ~/Downloads/bridge-cli-bundle-macos_arm.zip
       | openssl dgst -md5 -binary | openssl enc
       -base64`
     - Windows example:

       `type
       %USERPROFILE%\Downloads\bridge-cli-win64.zip |
       openssl dgst -md5 -binary | openssl enc
       -base64`
2. To install, simply unzip and add `bridge-cli` executable to your PATH or use absolute path to `bridge-cli` executable.
3. Run Bridge.

### Download Bridge CLI Bundle from the Polaris UI

To download the latest Bridge CLI Bundle from the Polaris UI, follow these steps:

1. Click **username** at the top right.
2. Select **Accounts**.
3. Select **Downloads**.
4. Choose the appropriate package for your operating system.

## **Using Bridge CLI Thin Client** – *New!*

Download the latest version of the Bridge CLI Thin Client from [repo.blackduck.com](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-thin-client/latest/). (Checksum verification examples are shown above.)

The Thin Client downloads the necessary features at runtime as it executes the workflow.
Here are some command examples:

1. To download the latest version of Polaris workflow, and run it:
   `bridge-cli --stage polaris --update`
2. To list all available and installed versions of Polaris workflows using list
   command: `bridge-cli --list polaris`
3. To list all available and installed versions workflows using list command:
   `bridge-cli --list`
4. To install a workflow:
   - To install the latest version of the Polaris workflow:
     `bridge-cli --install polaris`
   - To install a specific version of connect workflow:
     `bridge-cli --install connect@<version>`
5. To uninstall a workflow:`bridge-cli --uninstall
   polaris@<version>` would uninstall a specific version of
   Polaris workflow
6. To purge. In case you have multiple versions of different workflows
   installed, try running: `bridge-cli --purge`, and it will
   uninstall all old versions of each workflow, and just keep the latest
   versions
7. To use: `bridge-cli --use all@latest`. This will make sure
   Bridge updates itself to the latest version before running a workflow
8. A common example to have the latest of each workflow and Bridge binary would
   be: `bridge-cli --stage polaris --update --use
   all@latest`
9. To register the artifactory: `bridge-cli --register`
10. To update: `bridge-cli --diagnostics --update`
11. To check the version: `bridge-cli --version`

Note: The old Synopsys Black Duck product has been renamed to Black Duck SCA. To
address this name change, the Bridge CLI `--stage` parameter value has been
changed from `blackduck` to `blackducksca`. Bridge will error out if you use the
incorrect value.
