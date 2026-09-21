---
title: "Bridge CLI"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/bridge-cli.html"
content_id: "XXWcReElxhPsW9A9y8RBYQ"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:46:49.278317+00:00"
---

# Bridge CLI

Bridge CLI serves as the foundation for all Bridge CI/CD integrations, using Coverity and Detect to support SAST and SCA assessments. Bridge CLI provides a single, unified interface for automating testing with Black Duck software products and is designed to facilitate testing on virtually any platform where tests are automated.

The Bridge CLI client is can be used to script testing with any Black Duck product on virtually any testing platform. It's an ideal solution wherever you want to automate Black Duck Software products and an off-the-shelf Black Duck Security scan plug-in is not available.

## Use cases

- The Bridge CLI full bundle can perform all Bridge capabilities in an air-gapped environment, with no connectivity to the Internet.
- For applications built on a CI/CD platform where the Black Duck Security Scan is not available as a ready-to-use plug-in, the Bridge CLI client can be used directly within CI/CD pipeline jobs to provide equivalent features. This approach makes the Black Duck Security Scan capabilities available on virtually any automation platform.

## Downloads

The following Bridge CLI distributions are available for download:

- **Full bundle**: Includes all necessary components and dependencies for comprehensive security scanning. This distribution is suitable for environments where complete offline operation is required, such as air-gapped networks or systems with limited internet connectivity. The full bundle can be downloaded from [repo.blackduck.com](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/). Polaris users can also download the full bundle from the Polaris UI by: Select Username from top right menu > Account > Downloads > Select package appropriate for operating system.
- **Thin client bundle**: Provides a lightweight distribution that downloads required components on demand during execution. This distribution is suited to cloud-based CI/CD environments, containerized deployments and scenarios where storage space is limited. The thin client supports faster initial deployment with dynamic component retrieval and can be downloaded from [repo.blackduck.com](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-thin-client/latest/).

## How Bridge works

Bridge CLI is a command-line utility that can be downloaded and used on a local host or within CI/CD platforms. This is the recommended approach when there is no Black Duck Security Scan plugin available for the Source Code Management (SCM) system.

The Bridge CLI client uses Coverity and Black Duck® Detect under the hood, providing a single, unified interface for automating all testing with Black Duck Software products. Bridge is designed to bring testing to virtually any platform where tests are automated.

[image: Bridge CLI Integration With Black Duck Platforms]

Configurations for Coverity and Detect can be customized to fine-tune testing. Examples of configuration include:

- Setting up Coverity to work with a specific compiler, such as GCC.
- Configuring Detect search depth within the source folder.

All functionalities available through Coverity and Detectcan also be accessed by passing commands to these tools via Bridge CLI, providing a consistent automation entry point for Black Duck security testing.

**Related Links**  

- Download Bridge CLI
- Files and directories
- Bridge support matrix
