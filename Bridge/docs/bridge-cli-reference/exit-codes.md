---
title: "Exit codes"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/exit-codes.html"
content_id: "zOU23U2KJp8SsxjxXcSIJA"
version: "latest"
section: "Bridge CLI reference"
scraped_at: "2026-10-04T23:28:27.287557+00:00"
content_hash: "9a9fd19d8d017be0d53b515262e4ab574932f1239ee062c7bfc8d55cd37e49e5"
---

# Exit codes

## Exit codes reference

Bridge CLI returns the following exit codes depending on execution results. Any exit code other than `0` should be seen as a build-breaking condition in your CI/CD platform.

| Code | Code name | Description |
| --- | --- | --- |
| `0` | Normal | Bridge CLI exited without any errors. |
| `1` | UndefinedError | Undefined errors. Review the log file for details. |
| `2` | AdapterError | Bridge CLI received a non-0 exit code from an internal adapter. Review the log file for details. |
| `3` | ShutdownFailed | Bridge CLI failed to shut itself down after running the command. Review the log for details. |
| `8` | BridgeBuildBreak | The config option `bridge.break` is set to `true` but Bridge CLI is unable to enforce this. As a workaround, create a simple script to call Bridge CLI and implement build break logic in your script. |
| `9` | StartupFailed | Failed to initiate Bridge CLI. Review the log for details. |
