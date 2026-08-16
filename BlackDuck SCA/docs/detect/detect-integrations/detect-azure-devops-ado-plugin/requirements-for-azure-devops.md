---
title: "Requirements for Azure DevOps"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/requirements-for-azure-devops.html"
content_id: "GlhfgisZkRYS~piYOmlAWw"
version: "11.5.1"
section: "Detect Integrations"
scraped_at: "2026-08-08T23:46:06.437741+00:00"
---

# Requirements for Azure DevOps

The following is a list of requirements for the Black Duck® Detect in Azure DevOps integration.

- Black Duck® SCA server.
  For the supported versions of Black Duck SCA, refer to [Black Duck Release Compatibility](https://documentation.blackduck.com/bundle/blackduck-compatibility/page/topics/Black-Duck-Release-Compatibility.html).
- Black Duck SCA API token to use with Azure.
- Azure DevOps Services or Azure DevOps Server 17 or later
- Java.
  OpenJDK versions 8 and 11 are supported. Other Java development kits may be compatible, but only OpenJDK is officially supported for Black Duck SCA.
- Access to the internet is required to download components from GitHub and other locations.

The Detect plugin for Azure DevOps is supported on the same operating systems and browsers as Black Duck SCA.

For scanning NuGet projects, verify that you have the NuGet tool installer set up in the build job definition.
For further information see [NuGet tool](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/tool/nuget?view=azure-devops&viewFallbackFrom=vsts%3Fview%3Dvsts)

You can get the Detect for Azure DevOps plugin at the [VisualStudio Marketplace](https://marketplace.visualstudio.com/items?itemName=blackduck.blackduck-detect).
