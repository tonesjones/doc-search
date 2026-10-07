---
title: "QuickStart for the Code Sight Standard Edition"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/quickstart-for-the-code-sight-standard-edition.html"
content_id: "_DMZQLXS8S6kU19C6onudg"
version: "2026.9.0"
section: "Code Sight Standard Edition"
scraped_at: "2026-10-06T23:39:55.534495+00:00"
---

# QuickStart for the Code Sight Standard Edition

The Code Sight Standard Edition is set up so you can quickly register yourself,
download analysis engines, and begin scanning source.

## 1. Requirements

All the supported IDEs, [Eclipse](https://eclipseide.org/),
[Microsoft Visual Studio](https://visualstudio.microsoft.com/),
the [Microsoft Visual Studio Code](https://code.visualstudio.com/) editor
and the supported JetBrains IDEs, including [IntelliJ IDEA](https://www.jetbrains.com/idea/),
can run the Standard Edition.

## 2. Install Code Sight on your own system

If you need to, install Code Sight into your integrated development environment (IDE).
Black Duck Code Sight is available on these Marketplace sites:

- **Eclipse:** <https://marketplace.eclipse.org/content/code-sight-security>
- **JetBrains, including IntelliJ:** <https://plugins.jetbrains.com/plugin/25537-code-sight-security>
- **Visual Studio 2017:** <https://marketplace.visualstudio.com/items?itemName=blackduck.code-sight-vs2017>.
- **Visual Studio 2019:** <https://marketplace.visualstudio.com/items?itemName=blackduck.code-sight-vs2019>.
- **Visual Studio 2022:** <https://marketplace.visualstudio.com/items?itemName=blackduck.code-sight-vs2022>.
- **VS Code:** <https://marketplace.visualstudio.com/items?itemName=blackduck.code-sight-vscode>

If you need more detailed information, see:

- Installing Code Sight in Eclipse
- Installing Code Sight in IntelliJ
- Installing Code Sight in Visual Studio
- Installing Code Sight in Visual Studio Code

## 3. Register the Code Sight Standard Edition

When you launch Code Sight, it displays a tab that lets you register and then download the Code Sight Standard Edition.

Figure 1. Eclipse, IntelliJ (and other JetBrains IDEs), and Visual Studio: Tile for enabling the Standard Edition
  
 [image: Code Sight startup Eclipse and in JetBrains IDEs: Tile to enable Code Sight Standard Edition]

Figure 2. VS Code: Tab for enabling the Standard Edition (and other products)
  
 [image: Code Sight startup in VS Code: 'Choose a Product' tab]

If you have already obtained or been given a license for the Code Sight Standard Edition, you can click
Add License to enter the license’s path.

After you fill out the form and click Start Trial, Code Sight quickly installs free trials of
the Rapid Scan Static and Rapid Scan SCA engines.

The **Products and Licenses** panel (Eclipse, JetBrains, and Visual Studio) or
the **Choose a Product** tab (VS Code) also gives you the option of connecting to
your Coverity or Coverity on Polaris server, or to
your Black Duck SCA server, provided that your organization has
purchased the corresponding licenses.

## 4. Start scanning your source code

The controls for running Rapid Scan Staticm and Black Duck SCA
depend on which code-editing environment you use.

**When you run VS Code:**

1. [image: image] To see the Code Sight controls,
   click the icon in the margin that shows the Black Duck logo.
2. [image: image] When you click the Run Scan icon,
   Code Sight displays a drop-down list for you to choose a *scan configuration*.

   If no scan configuration has been created yet, Code Sight opens a dialog so you can create one.

   [image: image] Click Run Scan
   again to run a scan.

   [image: image] While a scan is running, you can click the
   Cancel icon to stop scanning.

   Figure 3. Scan-mode choices in VS Code
     
    [image: Drop-down menu to choose a scan mode]

   Alternatively, you can click the Mode label
   and choose Automatic Scan from the
   drop-down list. While auto-scan is enabled, Code Sight runs Rapid Scan Static on a single
   source file whenever you open a file or save it.

   For more details, see Local View and scan configurations.

**When you run a JetBrains IDE, including IntelliJ, Eclipse, or Visual Studio:**

Code Sight controls and notices appear in panels at the bottom of the editor’s window.

- [image: image] When
  you click the **Scan** icon, Code Sight allows you to
  initiate a scan. The available scan configurations are listed in a separate
  dropdown box next to the scan button, which must be accessed independently of
  the Scan icon.

  If no scan configuration has been created yet, Code Sight opens a dialog so you can create one.

  [image: image]
  Click Scan again to run a scan.

  [image: image] While a scan is running, you can click the
  Cancel icon to stop scanning.

  [image: image]

  Alternatively, you can click the Mode button labeled
  Auto. While auto-scan is enabled, Code Sight runs Rapid Scan Static on a
  single source file whenever you open a file or save it.
