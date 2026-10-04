---
title: "Passing Arguments using environment variables"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/passing-arguments-using-environment-variables.html"
content_id: "9dlLegLeeUU0Vr2OHp95~g"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-10-04T23:28:24.990245+00:00"
content_hash: "bd358e5857bdce7b02ad87c81b74fe477a7d7487918877514697e4ea92326e9f"
---

# Passing Arguments using environment variables

Command-line arguments can also be specified using environment variables

To configure a command-line argument as an environment variable:

1. Add the prefix `BRIDGE_`.
2. Convert the property name to uppercase.
3. Replace periods (`.`) with underscores (`_`).

The equivalent environment variable for `polaris.accesstoken` is shown in the table below for Linux, macOS, Windows, and PowerShell.

| Platform | Example |
| --- | --- |
| Linux | ``` export BRIDGE_POLARIS_ACCESSTOKEN=MyAccessToken ``` |
| macOS | ``` export BRIDGE_POLARIS_ACCESSTOKEN=MyAccessToken ``` |
| Windows | ``` set BRIDGE_POLARIS_ACCESSTOKEN=MyAccessToken ``` |
| PowerShell | ``` $env:BRIDGE_POLARIS_ACCESSTOKEN="MyAccessToken" ``` |
