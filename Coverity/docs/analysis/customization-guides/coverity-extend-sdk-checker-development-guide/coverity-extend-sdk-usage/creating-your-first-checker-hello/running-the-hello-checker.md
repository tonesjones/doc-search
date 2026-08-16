---
title: "Running the hello checker"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/running-the-hello-checker.html"
content_id: "N0h6v62zpx_qSfKGjeGIug"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:24.324319+00:00"
---

# Running the hello checker

In this section, you run the Hello checker that you compiled in Compiling the hello checker. See Requirements before attempting to complete the steps in this section.

**To run the Hello checker:**

1. Create some sample input for the checker.

   You can save the following code as a file called
   HELLO/test1/hello.test.c:

   ```
   /*
     (c) 2017, Black Duck Software, Inc. All rights reserved worldwide.
     The information contained in this file is the proprietary and confidential
     information of Black Duck Software, Inc. and its licensors, and is supplied subject to,
     and may be used only by Black Duck customers in accordance with the terms and
     conditions of a previously executed license agreement between Black Duck and that
     customer.
   */
   // test1/hello.test.c
   // test input for 'hello' checker
   int foo()
   {
     int x = 1;
     x += 5;
     return x;
   }
   // EOF
   ```
2. Use Coverity to configure a compiler.

   To configure gcc and g++ compilers with Coverity Analysis:

   ```
   > cd <install_dir>/bin
   > ./cov-configure --gcc
   ```

   To configure the Microsoft C/C++ compiler `cl.exe` with
   Coverity Analysis:

   ```
   > cd <install_dir>\bin
   > cov-configure --msvc
   ```

   Note: The remaining steps in this section assume that you are using the Unix-based gcc compiler.
   If you are using a different compiler, configure it instead, and adjust the
   command lines to use the appropriate command-line syntax for that compiler and
   operating system. For guidance with the configuration of such compilers, see the
   Coverity Analysis 2026.6.0 User and Administrator Guide. For more complete information
   about compiler configuration, you can also refer to the Coverity Analysis 2026.6.0 User and Administrator Guide and the Coverity 2026.6.0 Command Reference documentation on the `cov-configure`.
   All of this documentation is available from
   <install_dir>/doc/en|ja|ko|zh-cn/index.html
   (where en contains the English-language documentation set
   for Coverity Analysis, and
   ja,
   `ko`, and `zh-cn`
   contain
   the
   Japanese-language,
   Korean-language, and Simplified Chinese-language
   documentation,
   respectively).
3. Use `cov-build` to intercept calls to the compiler and save its
   abstract syntax in the intermediate directory.

   On Unix:

   ```
   > cd HELLO
   > <install_dir>/bin/cov-build --dir int_dir gcc -c test1/hello.test.c
   ```

   On Windows:

   ```
   > <install_dir>\bin\cov-build --dir int_dir cl test1\hello.test.c
   ```

   Upon successful completion, this command prints the following output:

   ```
   [...]
   1 C/C++ compilation units (100%) are ready for analysis
   The cov-build utility completed successfully.
   ```

   This command creates a c/emit subdirectory (an emit directory) in your
   intermediate directory that contains the `cov-build` output:
   HELLO/int_dir/c/emit.

   For information about the `cov-build` command, see the Coverity 2026.6.0 Command Reference.
4. Use your Hello checker (`hello`) to analyze this intermediate
   directory:

   1. Copy the `hello` checker program into the Coverity
      Analysis
      bin directory.

      For example, on Unix:

      ```
      > cp hello <install_dir>/bin
      ```

      On Windows:

      ```
      > copy hello.exe <install_dir>\bin
      ```
   2. Run `hello` from your HELLO
      directory:

      ```
      > cd HELLO
      > <install_dir>/bin/hello --dir int_dir --force
      ```

      Note: The options to the `hello` checker are the same as those for the
      `cov-analyze` command.

      The output looks something like the following:

      ```
      Looking for translation units
      |0----------25-----------50----------75---------100|
      ****************************************************
      [STATUS] Computing links for 1 translation unit
      |0----------25-----------50----------75---------100|
      ****************************************************
      [STATUS] Computing virtual overrides
      |0----------25-----------50----------75---------100|
      ****************************************************
      [STATUS] Computing callgraph
      |0----------25-----------50----------75---------100|
      ****************************************************
      [STATUS] Topologically sorting 1 function
      |0----------25-----------50----------75---------100|
      ****************************************************
      [STATUS] Computing node costs
      |0----------25-----------50----------75---------100|
      ****************************************************
      [STATUS] Starting analysis run
      ANALYZE_TREE: "{...}"
      ANALYZE_TREE: "int x = 1"
      ANALYZE_TREE: "x"
      ANALYZE_TREE: "1"
      ANALYZE_TREE: "x = 1"
      ANALYZE_TREE: "x = 1;"
      ANALYZE_TREE: "int x = 1;"
      ANALYZE_TREE: "x"
      ANALYZE_TREE: "x"
      ANALYZE_TREE: "5"
      ANALYZE_TREE: "x + 5"
      ANALYZE_TREE: "x = x + 5"
      ANALYZE_TREE: "x += 5;"
      ANALYZE_TREE: "x"
      ANALYZE_TREE: "return x;"
      tree = S_return:
        loc = <file ID 0>:5:3-<file ID 0>:5:11
        expr = E_variable:
          type = int
          deepID = 2147483646
          var = x, type = int, dflags = {}
        isImplicit = 0
      ANALYZE_TREE: "<destruction for x>"
      |0----------25-----------50----------75---------100|
      ****************************************************
      Analysis summary report:
      ------------------------
      Files analyzed                  : 1
      Total LoC input to cov-analyze  : 2990
      Functions analyzed              : 1
      Paths analyzed                  : 1
      Time taken by Coverity analysis : 00:00:00
      Defect occurrences found        : 15 hello
      ```

Aside from the usual `cov-analyze` text, the output consists of one line
for each call to the ANALYZE_TREE function, showing the abstract
syntax tree that was passed to it.

The checker also creates
HELLO/int_dir/programming_language/output/hello.errors.xml,
containing that output in a format that can be committed to Coverity
Connect.
