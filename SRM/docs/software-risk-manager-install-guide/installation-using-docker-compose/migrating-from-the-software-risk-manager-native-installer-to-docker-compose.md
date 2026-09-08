---
title: "Migrating from the Software Risk Manager Native Installer to Docker Compose"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/migrating-from-the-software-risk-manager-native-installer-to-docker-compose.html"
content_id: "J4CqEaegq2UqikfPApcKlw"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:13.562045+00:00"
content_hash: "e9f3ebce298ca5e4e175dae4d1443b225c4859fc214ff52d6dd7485601955f8e"
---

# Migrating from the Software Risk Manager Native Installer to Docker Compose

Refer to the sections below to migrate your data from a system created by the Software Risk
Manager Installer to your Docker Compose instance. The version you are running with Docker
Compose must equal the version number of the system whose data you want to migrate. If
necessary, upgrade your systems to a matching version.

## Prerequisites

The Software Risk Manager migration script depends on [PowerShell
Core](https://github.com/PowerShell/PowerShell#get-powershell), which can be installed on macOS, Linux, and Windows. However, the target
system you're migrating data to should have successfully gone through the installation
process.

## Windows Prerequisites

Ensure you can run PowerShell Core scripts on Windows by switching your PowerShell
Execution Policy to `RemoteSigned` (recommended) or
`Unrestricted`. You must run the `Set-ExecutionPolicy
-ExecutionPolicy RemoteSigned` command from an elevated/administrator Command
Prompt.

## Migration Paths

For more information on migration, see the following:

- Migration Without an External
  Database
- Migration With an External
  Database
