---
title: "Setting up a license.dat file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-up-a-license.dat-file.html"
content_id: "jA7td4Ughecij_i9xrNSwQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:54.900390+00:00"
---

# Setting up a license.dat file

**To set up default licensing:**

1. Obtain a license file from Coverity - for that, open a Support
   case by logging in to the [Black Duck Community site](https://community.blackduck.com/s/contactsupport).
2. Verify that the license file is named license.dat. If it is
   not, rename it to license.dat.
3. Copy the license file to the <install_dir>/bin directory.

   Note: A missing license leads to a fatal `No
   license found` error when you attempt to analyze your code.

   On some Windows platforms, you might need to use
   administrative privileges when you copy the Coverity license to
   <install_dir>/bin. Due to file
   virtualization in some versions of Windows, it might look like
   license.dat is in <install_dir>/bin when it is not.

   Typically, you can set the administrative permission
   through an option in the right-click menu of the executable for the command interpreter
   (for example, Cmd.exe or Cygwin) or Windows Explorer.
