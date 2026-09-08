---
title: "Back Up and Restore Prerequisites"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/back-up-and-restore-prerequisites.html"
content_id: "cIew8G81vS~NEGUt4dvZqw"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:09.883939+00:00"
content_hash: "b632acf885d1af321e1aadb6ba70cd37fa6a3e584dc773b41c9cf57597362350"
---

# Back Up and Restore Prerequisites

The Software Risk Manager backup and restore scripts depend on [PowerShell
Core](https://github.com/PowerShell/PowerShell#get-powershell), which can be installed on macOS, Linux, and Windows.

When running the backup and restore scripts, make sure you're either in a PowerShell Core
terminal environment or the command begins with `pwsh` so it's run by
PowerShell Core.

## Windows Prerequisites

Ensure you can run PowerShell Core scripts on Windows by switching your PowerShell
Execution Policy to RemoteSigned (recommended) or Unrestricted. You must run the
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned` command from an
elevated/administrator Command Prompt.
