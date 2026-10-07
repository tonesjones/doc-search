---
title: "Sources configuration"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/sources-configuration.html"
content_id: "w4SomROJr3JH1F~ZTiIpKA"
version: "2026.9.0"
section: "Code Sight: Preferences and Troubleshooting"
scraped_at: "2026-10-06T23:39:56.743212+00:00"
---

# Sources configuration

Shows controls for configuring the authorized networked software-integrity products.

Figure 1. Sources panel for server-based products
  
 [image: Panel that lists sources for server-based software-integrity products]

(Example from IntelliJ)

[image: image] Edit icon
:   Click to display the Select a Source dialog for the chosen server. See the section below.

Servers list
:   - ‘Server’ column

      Lists the servers for network products that have been authenticated.
    - ‘Source’ column

      For each server, lists the source-code project that has been chosen for analysis.

## “Select a Source” dialog

Figure 2. For a Coverity server
  
 [image: 'Select a Source' dialog for Coverity sources in Team View]

Figure 3. For Software Risk Manager
  
 [image: 'Select a Source' dialog for SRM sources in Team View]

Figure 4. For Polaris
  
 [image: 'Select a Source' dialog for Polaris sources in Team View]

(Examples from IntelliJ)

Note:
The columns in the “Select a Source” dialog depend on which kind of server you are configuring:

- For a Coverity server, the main source is called a “Project”,
  and a project can have one or more “Streams”.
- For a Software Risk Manager server, the main source is called a “Project”,
  and a project can have one or more “Branches”
- For a Polaris server, the main source is called an “Application”,
  an application can have one or more “Projects”,
  and a project can have one or more “Branches”.
