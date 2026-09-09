---
title: "Analyses Overview"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/analyses-overview.html"
content_id: "VAac_BTM9oMYu_j2h17G8A"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:35.034353+00:00"
content_hash: "8f77d3a7e7cf861cc896be331bddb01ab546565440cecbea1b33d36b583728bb"
---

# Analyses Overview

When the Scan Farm has been configured, Software Risk Manager can automatically run
Coverity SAST and Black Duck SCA scans. Software Risk Manager also comes with bundled
open source [tools](https://www.blackduck.com/integrations.html#logoWall6) to scan a wide variety of applications.
Supported languages and expected inputs for the built-in open source scanners are
described in the Built-in Open Source Code
Scanners and the Built-in Open
Source Dependency Scanners sections. In addition to the bundled tools,
Software Risk Manager can import the results of several commercial and open source
tools. The supported tools and generic input formats are described in the Importing Scan Results section. There are
a number of different options to configure and run analyses for Software Risk Manager:
manually using the web interface, Jenkins plugins, or automatically (such as from your
continuous integration server) using the API or using Black Duck Bridge CLI. These are
all detailed in the Starting Analyses
section.

## Incremental Analysis

Software Risk Manager performs analyses incrementally. This means that as new
analysis inputs (files) are added to a project, any findings associated with them
are added to the project.

The life of a finding is tied to the inputs in which it was reported. When the last
input contributing to a finding is archived, the finding itself is marked as "Gone"
and hidden by default (see Findings View
Options).

Analysis inputs can be archived manually or automatically. For more information on
archival, see Auto-Archival.
