---
title: "Telemetry in Code Sight"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/telemetry-in-code-sight.html"
content_id: "JcP1maYt_vC8vUleXmYx3g"
version: "2026.9.0"
section: "General Information"
scraped_at: "2026-10-06T23:40:01.482545+00:00"
---

# Telemetry in Code Sight

When you run Code Sight, Black Duck Software, Inc. can collect usage and compliance data.
The data collected is completely anonymous.

For a detailed listing of metrics and statistics that are collected, please see our
[Use and Compliance Data Policy](https://www.blackduck.com/company/legal/use-compliance-data-policy.html).

Telemetry data collection is disabled until you explicitly enable it.

## Enabling or disabling telemetry

You can enable or disable telemetry data collection in any IDE.
If you choose to enable telemetry data collection in one IDE, it will be enabled for all IDEs on your system
that run Code Sight 2024.3.0 or a newer version.

You can also disable or enable telemetry globally, by changing your firewall settings.

**To enable or disable telemetry from within Code Sight:**

- When you start Code Sight, and have not yet chosen a telemetry setting, the extension prompts you to choose
  whether to enable telemetry data collection, or not.

  Figure 1. Telemetry prompt in IntelliJ
    
   [image: Telemetry prompt when starting Code Sight in IntelliJ]

  Figure 2. Telemetry prompt in VS Code
    
   [image: Telemetry prompt when starting Code Sight in VS Code]

After you choose a telemetry setting, you can change your choice later.
The interface depends on the IDE you use.

- **In Eclipse:**

  1. [image: image] In Code Sight, click the Preferences icon
     or on the menu bar, choose Window → Settings.
  2. In the Settings dialog, go to the Black Duck Code Sight → General panel,
     and then click the check box to either enable or disable telemetry data collection.
- **In IntelliJ and other JetBrains IDEs:**

  1. [image: image] In Code Sight, click the Preferences icon
     or on the menu bar, choose File → Settings.
  2. In the Settings dialog, go to the Black Duck Code Sight → General panel,
     and then click the check box to either enable or disable telemetry data collection.
- **In Visual Studio:**

  1. [image: image] In Code Sight, click the Preferences link
     or on the menu bar, choose Tools → Options.
  2. In the Options dialog, go to the Black Duck Code Sight → Other panel,
     and then click the check box to either enable or disable telemetry data collection.
- **In VS Code:**

  1. [image: Code Sight Settings icon]
     After you choose a telemetry setting, you can change your choice by going to the STATUS view,
     and then clicking Code Sight Settings.
  2. On the Settings tab, find the “Code Sight > Telemetry: Enablement” entry,
     and then click the check box to either enable or disable telemetry data collection.

**To enable or disable telemetry globally:**

Change your firewall settings to either allow or block the following URLs and port number:

| URL | Port |
| --- | --- |
| dc.applicationinsights.azure.com | 443 |
| dc.applicationinsights.microsoft.com | 443 |
| dc.services.visualstudio.com | 443 |
| *.in.applicationinsights.azure.com | 443 |
