---
title: "Installing Coverity Thin Client on a client system"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/installing-coverity-thin-client-on-a-client-system.html"
content_id: "~dHYkuBMc8AdnN880ggRBA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:28.554365+00:00"
---

# Installing Coverity Thin Client on a client system

This section describes how to install the Coverity Connect Thin Client using either the
Coverity Connect UI or the `curl` command.

Note:

The 2024.6.0 release now enforces ranges of support between Coverity and Thin Client.
Scans will not run with versions of Thin Client that are not supported by the
Coverity version deployed in the cloud. If you have an unsupported version of Thin
Client on your client system and you attempt to run a scan using the unsupported
Thin Client version, the capture and any build might succeed, however the analysis
will fail. In the event of a failure, you might need to install a supported version
as described in this section, and/or contact your Coverity cloud deployment
administrator.

## Using the Coverity Connect UI

To download and install the Thin Client using the Coverity Connect UI, follow these
steps:

1. On the client system, log into the Coverity Connect UI.
2. Navigate to the Downloads page: Help > Downloads.

   [image: image]
3. On the Downloads page, under Desktop Plug-ins, select the
   Thin Client tab. For example:

   [image: image]

   Note: The Select a thin client window
   lists Thin Client versions that are supported with the Coverity version that
   is deployed in Kubernetes in the cloud.
4. On the Thin Client tab, you can download the Thin Client installer using the UI
   as follows:

   1. Expand the Tools List. You will see the available Thin Client
      installers.
   2. Select a Thin Client installer for the desired Thin Client version and
      client platform. For example, to install Thin Client version 2026.6.0 on a Linux64
      system:

      `cov-thin-client-linux64-2026.6.0`
   3. Click Download. The Thin Client package
      downloads.
5. Update the `PATH` variable with the Thin Client analysis
   executable path that contains the analysis executable. For example, in
   Linux:

   ```
   export PATH=$PATH:$RUNNER_TEMP/bin
   ```

## Using the `curl` command

Alternatively, for example in an automated environment, you can download the Thin Client tools
files using a `curl` command. To download and install the Thin Client
using `curl`:

```
curl -fLOsS $COV_URL/api/v2/scans/downloads/cov-thin-client-<platform>-<version>.tar.gz | tar -C $RUNNER_TEMP -xzf -
export PATH=$PATH:$RUNNER_TEMP/bin
```

where:

- `COV_URL` specifies the URL of the Coverity root directory.
- `<platform>` is the platform type, for example
  `linux64`.
- `<version>` is the Thin Client version; use
  `default` for the default version.
- `RUNNER_TEMP` specifies the directory in which the executable
  file is installed.

**Examples:**

- To download and install version 2026.6.0 for a Linux64
  system:

  ```
  curl -fLOsS $COV_URL/api/v2/scans/downloads/cov-thin-client-linux64-2026.6.0.tar.gz | tar -C $RUNNER_TEMP -xzf -
  export PATH=$PATH:$RUNNER_TEMP/bin
  ```
- To download and install the default version for a Linux64
  system:

  ```
  curl -fLOsS $COV_URL/api/v2/scans/downloads/cov-thin-client-linux64-default.tar.gz | tar -xzf -
  export PATH=$PATH:$RUNNER_TEMP/bin
  ```
