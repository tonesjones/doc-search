---
title: "Committing the issues to Coverity Connect"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/committing-the-issues-to-coverity-connect.html"
content_id: "c4~r2BnyCWkIv_aDEWFMCw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:25.628160+00:00"
---

# Committing the issues to Coverity Connect

Just as you can commit the output of the `cov-analyze` command to
Coverity Connect, you can also commit the issues that the Hello checker
finds.

**To commit issues found by Hello to Coverity Connect:**

1. Prepare Coverity Connect to receive the issues found by the Hello
   checker:

   1. StartCoverity Connect.

      The startup command is located in the Coverity Connect
      /bin directory:

      ```
      > cd <install_dir>/bin 
      > ./cov-start-im
      ```
   2. Log into Coverity Connect.
   3. Create a project that is configured with a Coverity Analysis
      stream for the C/C++ programming language.

      For example: `hello_stream` in the project
      `extend_examples`

   Note: If you need help with any of these steps, contact your Coverity Connect
   administrator.
2. Use Coverity to commit (push) the issues to Coverity
   Connect:

   ```
   > <install_dir>/bin/cov-commit-defects \
       --host server_hostname \
       --port port_number \
       --stream hello_stream \
       --user admin --dir int_dir
   ```

   This command produces output similar to the following on the console:

   ```
   Connecting to server sduke-t61p:9090
   2012-08-06 21:54:57 UTC - Committing 4 file descriptions...
   |0----------25-----------50----------75---------100|
   ****************************************************
   2012-08-06 21:54:57 UTC - Committing 4 source files...
   |0----------25-----------50----------75---------100|
   ****************************************************
   2012-08-06 21:54:56 UTC - Calculating 4 cross-references...
   |0----------25-----------50----------75---------100|
   ****************************************************
   2012-08-06 21:54:57 UTC - Committing 4 cross-references...
   |0----------25-----------50----------75---------100|
   ****************************************************
   2012-08-06 21:54:58 UTC - Committing 0 functions...
   2012-08-06 21:54:58 UTC - Committing 15 defect occurrences...
   |0----------25-----------50----------75---------100|
   ****************************************************
   2012-08-06 21:54:59 UTC - Committing 3 output files...
   |0----------25-----------50----------75---------100|
   ****************************************************
   New snapshot ID 10004 added.
   Elapsed time: 00:00:04
   ```
