---
title: "The hello checker source code"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-hello-checker-source-code.html"
content_id: "p9SqD~PeP7Q0GGQruU6kPg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:23.010194+00:00"
---

# The hello checker source code

In this section, you create a simple Coverity Extend SDK checker
(hello.cpp) designed to print every Abstract Syntax Tree (AST) that is passed into the
ANALYZE_TREE function. In subsequent sections, you will compile
and run this checker, then commit the issues that it finds in a code sample to
Coverity Connect.

To create the Hello checker:

1. Type or copy the following source code into a text editor:

   ```
   /*
     (c) 2017, Black Duck Software, Inc..  All rights reserved worldwide.
     The information contained in this file is the proprietary and confidential
     information of Black Duck Software, Inc.. and its licensors, and is supplied subject to,
     and may be used only by Black Duck customers in accordance with the terms and
     conditions of a previously executed license agreement between Black Duck and that
     customer.
   */
   // hello.c
   // trivial Extend checker
   #include "extend-lang.hpp"     // Extend API
   START_EXTEND_CHECKER( hello, simple );
   ANALYZE_TREE()
   {
     cout << "ANALYZE_TREE: " << CURRENT_TREE << endl;
     OUTPUT_ERROR("ANALYZE_TREE: " << CURRENT_TREE);
     ReturnPat ret;
     if( MATCH(ret) ) print_tree(CURRENT_TREE);
   }
   END_EXTEND_CHECKER();
   MAKE_MAIN( hello )
   // EOF
   ```

   The source code and makefile for this checker are located in the
   <install_dir>/sdk/samples/hello directory.

   Unlike the print_tree checker (see Examining nodes in the AST with print_tree), this checker restricts the level of information that is returned by using
   an `if` statement before calling `print_tree`.
2. Save this file as hello.cpp in a directory that is
   *outside* of the Coverity Extend SDK installation
   directory.

   For example: HELLO so that your checker source file is now called
   HELLO/hello.cpp

   Note: Saving the file inside of the installation directory can make the upgrade process for
   Coverity Extend SDK more difficult.
