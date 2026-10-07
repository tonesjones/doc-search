---
title: "Code Sight QuickStart for Polaris issues"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-quickstart-for-polaris-issues.html"
content_id: "ShnEvEZzCthRz4E7Ecf~jA"
version: "2026.9.0"
section: "Polaris with Code Sight"
scraped_at: "2026-10-06T23:39:54.888129+00:00"
---

# Code Sight QuickStart for Polaris issues

Here is information to help you quickly get started using Code Sight, if you want to view issues from Polaris.

## 1. Display of Polaris issues

Remote Polaris issues are displayed in Team View.
Local Polaris issues (JetBrains IDEs, Visual Studio, and VS Code only) are displayed in Local View.

## 2. Authenticate to a Polaris server

After you have installed Code Sight, go to the appropriate Code Sight preferences.

- [image: image] In a JetBrains IDE (including IntelliJ),
  click the Preferences icon (or choose IntelliJ IDEA → Settings).
  In Eclipse, click the Preferences link (or choose Window → Preferences).
  In Visual Studio, click the Preferences link.
  Go to Black Duck Code Sight →
  Server Settings → Authentication. Choose the panel for Polaris.

  Figure 1. Example: Add a Polaris server
    
   [image: Sample dialog for adding a Polaris server]
- In the VS Code STATUS view, click the entry for a Polaris server.

  Figure 2. Server choices in VS Code
    
   [image: Server choices in the VS Code STATUS view]

Note:
The next steps are necessary for authenticating Polaris.
They are not necessary if you plan to run Polaris only in Local View (JetBrains IDEs, Visual Studio, and VS Code).

1. In the dialog’s URL field, enter the URL of the server you want to use.
2. In the Token field, enter the token value that will authenticate that server.
3. Click Test Connection.
4. If Test Connection reports that the server connected
   successfully, then click Apply (in JetBrains) or
   Save Settings (in Visual Stuio or VS Code).

## 3. Configure a source

To configure a source, go through the following steps:

1. Once you have applied the choice of a Polaris server, click Configure Source.

   Code Sight displays a “Select a Source” dialog, where you can specify which information you want
   to receive from the server.

   Figure 3. For Polaris
     
    [image: 'Select a Source' dialog for Polaris sources in Team View]

   (Example from IntelliJ)

   Click to choose an “Application”, then a “Project”, and then a “Branch”.

   Now Team View will display remote issues that Polaris detects from the selected source.

   For more information, see Sources configuration.
