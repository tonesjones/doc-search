---
title: "Approved signature lists"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/approved-signature-lists.html"
content_id: "bJ1t7uZ9C4EMMPdfaffr8A"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:48.625820+00:00"
---

# Approved signature lists

As the Signature Scanner examines files, it generates “signatures” of the files and sends
SHA-1 and clean SHA-1 signatures to Black Duck's web application. Black Duck filters
these signatures based on the individual file matching parameters (if selected) and/or
allowed signature lists, which you can create. Black Duck then sends the signatures to
the Black Duck KnowledgeBase (KB) web service to identify the open source software
contained in the your scanned code.

You can create an allowed signature list for SHA-1 and/or clean SHA-1 file extensions.
Each list is optional and works independently of the other list.

To create a list of approved signatures::

- Use one or both of the following parameters in the Signature Scanner:
  - **--binaryAllowedList** *x, y, x* where *x*, *y*, *z* are the approved
    file extensions for SHA-1 (binary) files.
  - **--sourceAllowedList** *a, b, c* where *a*, *b*, *c*, are the approved
    file extensions for clean SHA-1 (source code) files.
- Create an environment variable. The following example is for SHA-1 and clean
  SHA-1 signatures for Linux or Mac OS X.

  ```
  export JAVA_TOOL_OPTIONS="-Dblackduck.scan.cli.BinaryAllowedList=x,y,z -Dblackduck.scan.cli.SourceAllowedList=a,b,c"
  ```

  For Windows systems, use the Control Panel to access the Advanced System Settings
  dialog box to create the environment variable.

If you enable individual file matching (using the**--individualFileMatching**
parameter) in Signature Scanner
*and* create list(s) of allowed signatures, the outcome depends on the option you
select:

- **source** option
  - *Replaces* the existing file extension for the **source** option with the list of file
    extensions from your clean SHA-1 signature list
    (**sourceAllowedList**).
  - Does *not* use the list of file extensions from your SHA-1 signature list
    **binaryAllowedList** .
- **binary** option
  - Replaces the existing list of file extensions used for the **binary** option with the list of
    file extensions from your SHA-1 signature list
    (**binaryAllowedList**).
  - Does *not* use the list of file extensions from your clean SHA-1 signature list
    (**sourceAllowedList**).
- **all** option
  - Matches with all file extensions.
- **both** option
  - *Only* uses the file extensions from your SHA-1 and clean SHA-1 signature list (
    **binaryAllowedList**  and **sourceAllowedList**).
