---
title: "Troubleshooting Coverity errors"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/troubleshooting-coverity-errors.html"
content_id: "f5qJcvAkPB9HCuaTC3v72A"
version: "latest"
section: "Troubleshooting"
scraped_at: "2026-08-08T23:49:08.327044+00:00"
---

# Troubleshooting Coverity errors

Use this information to resolve common Coverity errors that can occur when Bridge CLI runs scans against a Coverity Connect deployment.

These errors can occur when the Coverity analysis method selected by Bridge CLI does not match the target Coverity deployment, or when the required Coverity analysis tools are not available.

Bridge CLI determines the Coverity analysis method by the `coverity.local` setting:

- When `coverity.local=false` (default), Bridge CLI uses the thin client. Capture runs locally and analysis runs remotely using scan services.
- When `coverity.local=true`, Bridge CLI uses the full analysis client. Both capture and analysis run locally.

| Error | Cause | Solution |
| --- | --- | --- |
| ``` ERROR: Failed to retrieve tool information details Fetch tool information: received unexpected response status code '500' from Connect API ``` | Bridge CLI attempts to use the thin client, but the target Coverity Connect deployment does not have scan services enabled.  Because scan services are not available, the server cannot provide the thin client tools that Bridge CLI is trying to download and use. | Set `coverity.local` to `true` in the Bridge CLI configuration. |
| ``` ERROR: Download descriptor for Coverity tool were not found in the Coverity Connect server: https://coverity.server.com ``` | Bridge CLI is configured to use the full analysis client.  Bridge CLI attempts to download the full analysis client from the Coverity Connect server. If the required installers are not available, the download fails. | To resolve this issue, use one of the following options:   - Make the Coverity full analysis client installer available by copying the appropriate .sh or .exe installer file to `<connect_install_dir>/server/base/webapps/downloads` on the Coverity Connect server. - If the Coverity full analysis client is already installed on the build system, set `coverity.install.directory` to the installation path. |
