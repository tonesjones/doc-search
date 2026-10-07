---
title: "To remove an engine so that Code Sight stops running it"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/to-remove-an-engine-so-that-code-sight-stops-running-it.html"
content_id: "eL9ConCQc3E0AQ5ExsrExA"
version: "2026.9.0"
section: "Authenticating to Servers in Code Sight"
scraped_at: "2026-10-06T23:39:51.464328+00:00"
---

# To remove an engine so that Code Sight stops running it

To remove a scan engine from Code Sight, you need to remove the engine from your system.

1. Close the development environment (IDE) from which you run Code Sight.
2. Navigate to the directory where it was installed, and delete the
   directory/folder that contains the Black Duck
   software-integrity engine you no longer want to use. 

   The default installation location depends on the operating system you are
   using. See the following table:

   | Platform | Location of directory/folder  where engines are installed | Directory/folder  for the particular engine |
   | --- | --- | --- |
   | Linux or Mac | /Users/<username>/      .blackduck/desktop/          controller/installedtools/ | blackduck/ |
   | coverity-analysis/ |
   | sigma/ |
   | Windows | C:\Users\<Username>\AppData\Roaming\      BlackDuck\desktop\          controller\installedtools\ | blackduck\ |
   | coverity-analysis\ |
   | sigma\ |

   Some sites install the desktop/ folder in a custom
   location. If you do not see it in the default location, consult your system
   administrator.
3. Restart the IDE.

   Now the Code Sight interface should indicate that you are connected only to the server for the engine that
   is still installed on your system.
