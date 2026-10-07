---
title: "To clean up the Code Sight configuration files (IntelliJ)"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/to-clean-up-the-code-sight-configuration-files-intellij-.html"
content_id: "Z4Nlzy3ildDf_PglCseMJQ"
version: "2026.9.0"
section: "Installing Code Sight"
scraped_at: "2026-10-06T23:39:50.315788+00:00"
---

# To clean up the Code Sight configuration files (IntelliJ)

Code Sight saves information in a folder with a number of configuration files. After
you uninstall the plug-in, you might want to remove this. There is also a file that saves
the current state of the plug-in.

1. Open a command window or terminal.
2. Remove the Black Duck desktop/ folder. The default location of this
   directory/folder depends on the operating system you are using. See the following table:

   | Platform | Location of Desktop directory/folder |
   | --- | --- |
   | Linux or Mac | /Users/<username>/.blackduck/desktop/ |
   | Windows | C:\Users\<Username>\AppData\Roaming\BlackDuck\desktop\ |

   Some sites install the desktop/ folder in a custom location.
   If it is not in the default location, consult your system administrator.
3. Remove the code_sight_state.xml files.

   Code Sight generates a code_sight_state.xml file for *each source-code project*
   that you scan.
   Each of these files is saved in a directory/folder named .idea/,
   which is created inside the project folder for each project (code base) that you analyze by using
   Code Sight within IntelliJ.
4. Remove the code_sight_plugin_state.xml files.

   There is one of these for each JetBrains IDE that you have installed. The default
   location depends on the operating system that you use. See the following table:

   | Platform | Location of Desktop directory/folder |
   | --- | --- |
   | Linux | ~/.config/JetBrains/<product><version>/config/options |
   | Mac | ~/Library/Application Support/JetBrains/<product><version>/config/options |
   | Windows | %APPDATA%\JetBrains\<product><version>\config\options\ |
