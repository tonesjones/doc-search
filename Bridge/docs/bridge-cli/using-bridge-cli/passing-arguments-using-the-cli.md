---
title: "Passing Arguments using the CLI"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/passing-arguments-using-the-cli.html"
content_id: "K_E1OK0VY_txDjPNqiqQGg"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:46:51.754097+00:00"
---

# Passing Arguments using the CLI

You can also pass arguments on the command line as an alternative to passing arguments
using a JSON file.

Here are the steps:

1. Create an access token in the web interface of the Black Duck security product you are integrating with.
2. Use environment variable(s) to pass sensitive information such as password or
   access token to Bridge CLI (recommended for security
   purposes). Bridge CLI automatically picks up values
   passed through these variables.
   - Example: `export
     BRIDGE_POLARIS_ACCESSTOKEN=<POLARIS_ACCESSTOKEN>`
3. Pass the necessary command line arguments as shown in the example below.

```
export BRIDGE_POLARIS_ACCESSTOKEN="<POLARIS_ACCESSTOKEN>"
bridge-cli --stage polaris polaris.project.name="<PROJECT_NAME>" \
polaris.application.name="<APPLICATION_NAME>" \
polaris.assessment.types=SAST,SCA \
polaris.serverurl="<POLARIS_SERVERURL>"
```

For a complete list of environment variables and command line arguments, see Complete list of Bridge arguments.

See Schema Resources and Extensions for Bridge CLI
resources.

For tool specific information and examples, see:

- Using Bridge CLI with Polaris
- Using Bridge CLI with Black Duck SCA
- Using Bridge CLI with Coverity
- Using Bridge CLI with Software Risk Manager (SRM)
