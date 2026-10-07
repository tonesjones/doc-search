---
title: "Creating a scan configuration"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/creating-a-scan-configuration.html"
content_id: "wj_4W6rJe1gqSFg7MhzK5w"
version: "2026.9.0"
section: "Viewing Issues in Code Sight"
scraped_at: "2026-10-06T23:39:51.947459+00:00"
---

# Creating a scan configuration

The Scan Configuration dialog (JetBrains, Eclipse and Visual Studio) or tab (VS Code) has controls for creating and managing scan configurations to be used with the Manual scan mode in Local View.

## In JetBrains IDEs, Eclipse, and Visual Studio

The list on the left shows scan configurations you have already created. Click the plus-sign icon to create a new scan configuration, or the minus-sign icon to delete a scan configuration that you have highlighted.

The fields on the right-hand side of the dialog depend on the type of scan you choose. Most give you a choice among existing options. The text in the Name field can be anything you enter.

Figure 1. The Scan Configuration dialog  
 [image: Dialog to create a scan configuration in IntelliJ]

When you click the plus-sign icon to create a new configuration, Code Sight displays a drop-down list that lets you choose the kind of scan that this will be.

Figure 2. Drop-down list to choose a scan type in IntelliJ  
 [image: Drop-down list presents options to choose the type of a new scan in IntelliJ]

## In VS Code

The left-hand column of the Scan Configuration tab shows buttons for managing configurations. The right-hand column shows the settings for a particular configuration.

Figure 3. The Scan Configuration tab  
 [image: Tab to create a scan configuration in VS Code]

- [image: image] When you click the plus-sign button to create a new configuration, Code Sight prompts you to choose the kind of scan that this will be.

  Figure 4. Buttons for choosing a scan type  
   [image: Buttons present options to choose the type of a new scan in VS Code]
- [image: image] You can also create a new configuration by clicking Copy scan configuration to copy and then paste the currently selected one. Code Sight appends “-copy” to the name of the new configuration.

The fields that display in the right-hand column depend on the type of scan you choose. Most give you a choice among existing options. The text in the Name field can be anything you enter.

## Configuration options for Coverity scans

When you choose a Coverity scan type, you choose how Code Sight runs a scan:

Coverity (.yaml, .json)
:   Code Sight runs the scan using the Coverity CLI, and obtains the scan configuration from a local YAML or JSON configuration file.

Coverity (.conf)
:   Code Sight runs the scan usinng the legacy `cov-run-desktop` command, and obtains the scan configuration from one or two coverity.conf files.

For more information, see Coverity scan configurations and custom scan settings

## Environment Variable Configuration in Code Sight

The Code Sight extension supports configuring environment variables at multiple levels to control the scan execution environment. You can define variables at the user level (applied to all scans across all projects), the workspace/project level (applied only to scans within the current workspace or project), or within individual scan configurations (applied only when that specific scan runs).

Environment variables configured in Code Sight are applied at scan time only — they affect the environment in which scan engines execute, but they do not modify the underlying Code Sight extension or IDE environment.

## Advanced options

This section of the Scan Configuration dialog or tab provides an interactive way to specify custom scan settings. Fields in this section are comparable to the choices you can specify using a project-specific coverity.conf file: See “Project-specific ‘coverity.conf’ files”.
