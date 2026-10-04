---
title: "Requirements for Azure DevOps"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/requirements-for-azure-devops.html"
content_id: "GlhfgisZkRYS~piYOmlAWw"
version: "12.0.0"
section: "Detect Integrations"
scraped_at: "2026-10-04T23:33:23.614304+00:00"
content_hash: "d7e1b558299d740e120a8340eb24dd2c94cc481a404b69f420c6956828781d4e"
---

# Requirements for Azure DevOps

The following is a list of requirements for the Black Duck® Detect in Azure DevOps integration.

- Black Duck® SCA server.
  For the supported versions of Black Duck SCA, refer to [Black Duck Release Compatibility](https://docs.blackduck.com/r/blackduck/black-duck-compatibility-reference/black-duck-sca-release-compatibility.html).
- Black Duck SCA API token to use with Azure.
- Azure DevOps Services or Azure DevOps Server 17 or later
- Java: OpenJDK 64-bit version 11, 13, 14, 15, 16, 17, or 21. If using Java 11: 11.0.5 or higher is required.

  Note: Other Java development kits may be compatible, but only OpenJDK is officially supported.
- Access to the internet is required to download components from GitHub and other locations.

The Detect plugin for Azure DevOps is supported on the same operating systems and browsers as Black Duck SCA.

For scanning NuGet projects, verify that you have the NuGet tool installer set up in the build job definition.
For further information see [NuGet tool](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/tool/nuget?view=azure-devops&viewFallbackFrom=vsts%3Fview%3Dvsts)

You can get the Detect for Azure DevOps plugin at the [VisualStudio Marketplace](https://marketplace.visualstudio.com/items?itemName=blackduck.blackduck-detect).
