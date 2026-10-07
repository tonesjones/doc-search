---
title: "Code Sight QuickStart for Software Risk Manager issues"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-quickstart-for-software-risk-manager-issues.html"
content_id: "yoA2pgOLt9WfHRGz9BZAhQ"
version: "2026.9.0"
section: "Software Risk Manager with Code Sight"
scraped_at: "2026-10-06T23:39:55.300422+00:00"
---

# Code Sight QuickStart for Software Risk Manager issues

Here is information to help you quickly get started using Code Sight, if you want to view issues from the Software Risk Manager.

## 1. Requirements

Software Risk Manager issues are displayed in Team View, which for the Software Risk Manager is available
in these development environments: IntelliJ and other JetBrains IDEs, Microsoft Visual Studio, and VS Code.

## 2. Add a Software Risk Manager server

After you have installed Code Sight, go to the appropriate Code Sight preferences.

- [image: image] In IntelliJ, click the Preferences icon
  (or choose IntelliJ IDEA → Settings). In Visual Studio, click the Preferences link
  (or choose Tools → Options).

  Go to Black Duck Code Sight →
  Server Settings → Authentication. Choose the panel for Software Risk Manager.

  Figure 1. Authentication controls for Software Risk Manager (IntelliJ)
    
   [image: IntelliJ: SRM authentication panel]
- In the VS Code STATUS view, click the entry for a Software Risk Manager server.

  Figure 2. Server choices in VS Code
    
   [image: Server choices in the VS Code STATUS view]

## 3. Configure the Software Risk Manager server

To configure the server, go through the following steps:

1. In the dialog’s URL field, enter the URL of the server you want to use.
2. In the Token field, enter the token value that will authenticate that server.
3. Click Test Connection.
4. If Test Connection reports that the server connected successfully, then in Visual Studio or VS Code,
   click Save Settings.

   In IntelliJ, you need to proceed to the next step to configure a source, and then click Apply.
5. Once you have chosen a Software Risk Manager server, click Configure Source.

   Code Sight displays a “Select a Source” dialog, where you can specify which information you want
   to receive from the server.

   Figure 3. For Software Risk Manager
     
    [image: 'Select a Source' dialog for SRM sources in Team View]

   (Example from IntelliJ)

   Click to choose a “Project”, and then choose a “Branch”.

   For more information, see Sources configuration.
