---
title: "Command line clients"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/command-line-clients.html"
content_id: "PamErezYpVAdL40XeNNcUA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:40.761351+00:00"
---

# Command line clients

For scripting in the command line, users have a choice between the **Coverity CLI**
client and the **Bridge CLI** client.

## Coverity CLI client

The Coverity CLI is an alternative to using traditional Coverity Analysis commands.
After installing Coverity Analysis, you can invoke the Coverity CLI tool directly
from your terminal. Using the Coverity CLI allows you to:

- Scan a project without any knowledge about project contents.
- Understand which project files have been captured and which have not.

For details, see the Guide to the Coverity 2026.6.0 Point and Scan UI and the Coverity CLI, and more specifically the
section titled "Using the
Coverity CLI".

## Bridge CLI client

Bridge is useful when you want a unified CLI for
more than one of the security tools offered by Black Duck Software: Coverity
Connect, Coverity deployed in the cloud, Polaris,
Black Duck® SCA, Software Risk Manager.

Bridge does all the following:

- SAST and SCA scanning;
- Scan in synchronous or asynchronous (non-blocking) mode;
- Scan whenever new code is merged to a branch;
- Scan whenever a pull request is created or updated;
- Decorate pull requests with comments;
- Create automatic pull requests for new fixes ("Fix PRs") - Black Duck® SCA only;
- Generate a SARIF file;
- Post results to SCM (GitHub advanced security);
- Post results to any supported server (see the list of products above).

Note: Bridge can do any of the above in an air-gapped environment (with no
connectivity to the Internet).

For more information, see the [Black Duck® Bridge CLI](https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/bridge-product-overview.html)
documentation.

Note: We recommend automating with the Bridge
CLI Client because it’s the best way to get access to newer features and to have
a common interface for all our products.

We know that many customers rely on
the product-specific CLI clients, and if you happen to be looking for
information about those, they can be found here:

- [Detect](https://docs.blackduck.com/r/blackduck/latest/black-duck-documentation/black-duck-detect.html)
- [Coverity CLI](https://docs.blackduck.com/r/coverity/latest/coverity-documentation/using-the-coverity-cli.html)
