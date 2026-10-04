---
title: "Files and directories"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/files-and-directories.html"
content_id: "HZ56eqeQEx7vSS1NUCU5uQ"
version: "latest"
section: "Bridge CLI reference"
scraped_at: "2026-10-04T23:28:27.309591+00:00"
content_hash: "c64d9d6c63ba91963dee0763e8ca6d8b91b8faafda29de3742b1d28e1b14f897"
---

# Files and directories

Certain files and directories are created when you use the Bridge CLI client or any of the associated integrations.

## Location of logs and temp files

By default, the Bridge CLI writes logs and temporary files to `<current_working_directory>/.bridge`. You may change this default directory by using the `--home <directory_path>` option.

The following files and directories are found under the Bridge CLI home directory:

- `bridge.log`
- `diagnostics.json` file with `--diagnostics` option. See Logging and Diagnostics for details.
- Adapter directories and the corresponding `stdout` and `stderr` log files.
- Additional temporary files.

## Location of client scan tools

By default Bridge downloads client scan tools to `$HOME/.blackduck/bridge/tools` This includes the following client scan tools:

- Coverity
- Detect
- Sigma
- Signal

To change the download location for client scan tools use an absolute path with the `tool.install.directory` command or `BRIDGE_TOOL_INSTALL_DIRECTORY` environment variable.

**Using `tool.install.directory`**

```
bridge-cli --stage <e.g. --stage polaris> tool.install.directory=/opt/blackduck/tools <additional args>
```

**Using `BRIDGE_TOOL_INSTALL_DIRECTORY`**

```
export BRIDGE_TOOL_INSTALL_DIRECTORY=/opt/blackduck/tools
```
