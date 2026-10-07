---
title: "Coverity scan configurations and custom scan settings"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/coverity-scan-configurations-and-custom-scan-settings.html"
content_id: "EnyUPfcRgbrSVY2uXLVh_Q"
version: "2026.9.0"
section: "Viewing Issues in Code Sight"
scraped_at: "2026-10-06T23:39:52.053143+00:00"
---

# Coverity scan configurations and custom scan settings

When you choose a Coverity scan type, you choose how Code Sight runs a scan.

## Using Coverity CLI options: Coverity (.yaml, .json)

If you choose Coverity (.yaml, .json), then Code Sight uses the Coverity CLI to run scans, and it uses the
CLI settings specified locally in a YAML or JSON file, coverity.yaml or coverity.json.

Important:
Unlike a coverity.conf file, the CLI-style Coverity configuration file (coverity.yaml or coverity.json)
*is not processed or read* by Code Sight itself.
However, when the Coverity CLI runs, if this file is present in the working directory, the Coverity Analysis will automatically use it.

This alternative is the recommended way to specify analysis options.

Here is an example of a simple configuration file that uses the JSON format:

```
{
    "version": 1,
    "capture": {
        "build": {
            "clean-command": "mvn clean",
            "build-command": "mvn install" 
        },
    },
}
```

In this sample configuration file, the user has specified clean and build commands, where the `"clean-command"` will be executed prior to using
`"build-command"` to capture the project.
Using the example, the project will be cleaned using Apache Maven (`"mvn clean"`) and then built using Maven as well (`"mvn install"`).

For more Coverity CLI options you can use in a configuration file, and descriptions of them, see
Options reference in the
*Guide to the Coverity Point and Scan UI and the Coverity CLI*.

## Using coverity.conf: Coverity (.conf)

If you choose Coverity (.conf), then Code Sight uses the command `cov-run-desktop` to run scans, and it uses the
configuration settings specified in one or two local coverity.conf files.

## Default configuration

If Code Sight can find no configuration file, it uses the choice you made before:
The Command-Line Interface in the case of Coverity (.yaml, .json) or
`cov-run-desktop` in the case of Coverity (.conf).
