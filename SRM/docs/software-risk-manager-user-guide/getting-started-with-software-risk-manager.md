---
title: "Getting Started with Software Risk Manager"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/getting-started-with-software-risk-manager.html"
content_id: "mgP9TMHGW4Kteo4yJmhOQg"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:02:47.793182+00:00"
content_hash: "5283a1981f4dcb79d57e4385450df377d6ef3a36958fcddde0b2fdc06154190d"
---

# Getting Started with Software Risk Manager

Software Risk Manager (SRM) is a complete application security posture management (ASPM)
solution. SRM enables you to set up policy-driven workflows to orchestrate AST tools
like Coverity and Black Duck, prioritize issues, and monitor compliance across your
software assets.

Software Risk Manager allows you to do the following with your AppSec data:

- Correlate results
- Prioritize vulnerabilities
- Track remediation
- Centralize risk visibility

SRM also provides issue tracking functionality as well as policy management
solutions.

## About This Guide

This guide provides descriptions of SRM functionality and instructions to maximize
SRM deployment. Additional information can be found in the following guides:

- *Software Risk
  Manager Installation Guide.* This guide provides
  instructions for installing and configuring Software Risk Manager on Windows
  and Linux platforms.
- *Software Risk
  Manager Plugins Guide.* This guide provides information
  and instructions for integrating Software Risk Manager with a variety of
  development tools and environments.
- *Software Risk Manager
  API Guide.* This guide documents the various REST
  resources provided by Software Risk Manager, which allows external
  applications and scripts to interface with SRM core functionality.
- *Black Duck Bridge CLI.* This guide explains how to run
  scans and receive results from the command line.

## Conventions Used in this Guide

The following conventions are used in this guide:

- **Page names.** The Software Risk Manager UI consists of a series of
  *pages.* The name of the page appears in the top-left corner of the
  screen. In this guide, the page name begins with a capital letter. For
  example, the Settings page.
- **Button names.** Tasks are performed by clicking buttons. The button
  name begins with a capital letter. For example, Click Save.
- **Icons.** Icons appear throughout the Software Risk Manager UI. Icons
  can provide a visual indication of a state or status, such as a policy
  violation. Icons can also serve as links to other pages. In this guide, the
  icons are indicated by the name of the icon, beginning with a capital
  letter. For example, Click the Settings icon.
- **Menu items.** Several pages in Software Risk Manager include sub-pages,
  which are listed as menu items along the top or left of the screen. A menu
  item begins with a capital letter. For example, Select License from the top
  menu.
- **Dropdown configuration options.** When working with certain elements,
  such as a project or finding, a configuration icon appears to the right of
  the page. The icon appears as three horizontal dots. Clicking this icon
  displays a dropdown list of options. Options appear in this guide by name,
  starting with a capital letter. For example, Click the project's dropdown
  configuration icon and select New Analysis.
- **Code strings and filenames.** Code strings and filenames are shown in a
  mono-spaced font. For example, Enter the following command: `run
  srm.install`

  Note: A command that is designated as "code" needs
  to be entered exactly as shown.

## Software Risk Manager Navigation

The Software Risk Manager UI consists of a series of pages, sub-pages, menus,
buttons, and so on. Each page includes common elements for navigation, as can be
seen the sample image below and the descriptions that follow.

[image: image]

The Software Risk Manager UI is structured around seven main pages:

- **Projects.** This page shows all the currently defined projects in
  Software Risk Manager.
- **Findings.** This page displays all the findings from a selected
  analysis.
- **Policies.** This page lists all the currently defined policies, policy
  violations, and other policy-related data
- **Integrations.** This page provides links to all the tool integrations
  supported by Software Risk Manager.
- **Reports.** This page provides a list of existing reports and allows you
  to create reports to automatically be run on a custom schedule based on
  saved filters from the Findings page.
- **Hosts.** This page lists the currently defined hosts and host-related
  data.
- **Settings.** This page provides links to sub-pages where you can
  configure SRM. The Settings page and sub-pages allow you configure users,
  define user groups, view server logs, and so on.

These pages are accessed by clicking their respective icons (links) in the SRM
navigation bar, as shown in the figure below.

[image: image]

Clicking an icon from the navigation bar opens the corresponding page. The name of
the page appears in the top left of the screen.

[image: image]

Menus, when available, appear along the left side of the page. Clicking a menu option
opens the corresponding page.

[image: image]

The dropdown configuration icon (three horizontal dots) is located to the right of a
particular entity, such as a project or a finding, and provides a dropdown list of
options.

[image: image]

The menu in the top right corner of the screen provides additional options and
information (from left to right):

- **Software version.** This is the version number of the Software Risk
  Manager installation.
- **In-app documentation.** Click the question mark icon to access the
  Software Risk Manager documentation set. Both PDF and web versions of the
  guides are available.
- **Plugin downloads.** Click the plugins download icon to display a list
  of plugin options you can download.
- **Settings.** Click the settings icon to access the Software Risk Manager
  visual log.
- **[username].** Click the username icon to access the My Settings page or
  to log out of Software Risk Manager.

[image: image]
