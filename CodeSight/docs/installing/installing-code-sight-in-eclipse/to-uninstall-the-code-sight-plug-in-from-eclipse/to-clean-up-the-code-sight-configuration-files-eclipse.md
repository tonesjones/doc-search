---
title: "To clean up the Code Sight configuration files (Eclipse)"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/to-clean-up-the-code-sight-configuration-files-eclipse-.html"
content_id: "Y2TfDxeQZUsLxvgBQwXBbg"
version: "2026.9.0"
section: "Installing Code Sight"
scraped_at: "2026-10-06T23:39:49.973376+00:00"
---

# To clean up the Code Sight configuration files (Eclipse)

Code Sight saves information in a folder with a number of configuration files. After
you uninstall the plug-in, you might want to remove this. There is also a file that saves
the current state of the plug-in.

1. Open a command window or terminal.
2. Remove the Black Duck desktop/ folder. The default location of this directory/folder depends on the operating system you are using.
   See the following table:

   | Platform | Location of Desktop directory/folder |
   | --- | --- |
   | Linux or Mac | /Users/<username>/.blackduck/desktop/ |
   | Windows | C:\Users\<Username>\AppData\Roaming\BlackDuck\desktop\ |

   Some sites install the desktop/ folder in a custom location.
   If it is not in the default location, consult your system administrator.
3. Remove the file code_sight_state.xml.

   This file is saved in the directory/folder named eclipse-workspace/.metadata/.plugins/com.codesight.eclipse/.
