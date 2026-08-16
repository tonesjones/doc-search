---
title: "Connect Code Sight to Polaris"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/connect-code-sight-to-polaris.html"
content_id: "u044TqFWChDjKBIafTJESQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:38.145052+00:00"
content_hash: "b581ab436fbdeb3bdc2db41ad66be4b9547d2fbef13ec89faeae17b7936992a7"
---

# Connect Code Sight to Polaris

Connect Code Sight to Polaris to view issues in Team View, or run tests on Polaris from your IDE.

## Overview

An active Polaris subscription grants you access to Code Sight, an extension that runs in popular IDEs.

Once you install and configure Code Sight, you can:

- View Polaris issues in your IDE (in Team View) with Android Studio, IntelliJ and other JetBrains IDEs, Visual Studio, and VS Code.
- Run tests on Polaris from your IDE with Android Studio, IntelliJ and other JetBrains IDEs, and VS Code.

Find supported IDEs (and IDE versions) on the [Code Sight support matrix](https://docs.blackduck.com/access?ft:originId=e5be419b9a362d8c0118eeab3a8ee157/76437dcf1b2163b1d95d535625579578.topic&Version=latest).

Important: You must upgrade Code Sight to version 2025.4.0 or newer by November 24, 2026 to avoid errors. See [Migrate Polaris to the Black Duck domain](migrate-polaris-to-the-black-duck-domain.md) for more information.

## Install and configure Code Sight

To install Code Sight and connect it to Polaris, follow these steps:

1. Follow the instructions in the Code Sight documentation to install Code Sight.

   - [Installing Code Sight in IntelliJ](https://docs.blackduck.com/access?ft:originId=e5be419b9a362d8c0118eeab3a8ee157/61ebd240d0606ccc90da047f2684a878.topic&Version=latest)
   - [Installing Code Sight in Visual Studio](https://docs.blackduck.com/access?ft:originId=e5be419b9a362d8c0118eeab3a8ee157/11bfe00c691a2a41f48dfb2bdd094b68.topic&Version=latest)
   - [Installing Code Sight in Visual Studio Code](https://docs.blackduck.com/access?ft:originId=e5be419b9a362d8c0118eeab3a8ee157/543f3fbc30f75ac2edbd9c0e124731c7.topic&Version=latest)
2. Sign into Polaris and make an access token.

   Note: See [Make an access token](make-an-access-token.md) for more information.
3. Follow the instructions in the Code Sight documentation ([Code Sight QuickStart for Polaris issues](https://docs.blackduck.com/access?ft:originId=e5be419b9a362d8c0118eeab3a8ee157/f44dd6c3f8ba288eb1358d651b6e8fe2.topic&Version=latest)) to add your Polaris URL and access token to Code Sight's settings. Then, configure one or more sources (branches in SAST & SCA projects in Polaris) to retrieve issues from.

   Note: Retrieving DAST issues from Polaris is not supported.

## View Polaris issues in your IDE (in Team View)

After you connect Code Sight to Polaris, SAST and SCA issues captured in Polaris appear in Code Sight, in Team View.

1. If you haven't done so already, Install and configure Code Sight.
2. After you configure a source, find SAST and SCA issues from Polaris in Team View.

   Note: See [Viewing Polaris issues on the server](https://docs.blackduck.com/access?ft:originId=e5be419b9a362d8c0118eeab3a8ee157/4d16cb74014c2be1ba527d7f925ffb18.topic&Version=latest) in the Code Sight documentation for more information.

## Run tests on Polaris from your IDE

After you connect Code Sight to Polaris, you can run tests from from Android Studio, IntelliJ and other JetBrains IDEs, and VS Code. Doing so allows you to incrementally validate changes you make, without affecting your project's primary branch.

### Before you proceed

Before you run tests with Code Sight, please note:

- Running tests with Code Sight is supported in Android Studio, IntelliJ and other JetBrains IDEs, and VS Code.
- When you run a test from your IDE (using Code Sight), Code Sight creates a branch in Polaris. The names of branches created by Code Sight include `CodeSight_` and the email address of the user the branch was created for (for example, `CodeSight_user@domain.com`).

  Important: The branches Code Sight creates are not compatible with SCM integrations.
- Your permissions in Polaris must allow you to run tests. You cannot test projects in applications that you only have observer-level access to.

  Note: See [Roles and permissions](../reference/roles-and-permissions.md) for more information.

### Run tests on Polaris from your IDE

Follow these steps to run a test on Polaris with Code Sight:

1. If you haven't done so already, Install and configure Code Sight.
2. Follow the instructions in the Code Sight documentation to:
   1. [Create a scan configuration](https://docs.blackduck.com/access?ft:originId=e5be419b9a362d8c0118eeab3a8ee157/399bd9b1087c2b940b21d9e765e91a9b.topic&Version=latest).

      Important: `build` and `clean` commands in a scan configuration's advanced settings will override `build` and `clean` commands in your project's coverity.yaml file.
   2. [Run a scan](https://docs.blackduck.com/access?ft:originId=e5be419b9a362d8c0118eeab3a8ee157/241bd3f8f1796c6ec1551742bd7c7a9f.topic&Version=latest).
3. View issues from local tests in Local View.

   Tip: Compare the list of issues under Local View with the list under Team View to validate changes as you remediate issues — even before you commit your changes.

### Monitor tests in Polaris

Monitor tests you run with Code Sight on the Tests page.

Note: By default, tests run with Code Sight are hidden on the Tests page. Select IDE with the Test Mode filter to show tests run with Code Sight.

  
 [image: tests show ide mode]
