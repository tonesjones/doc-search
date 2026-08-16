---
title: "Compiling the hello checker"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/compiling-the-hello-checker.html"
content_id: "~6uwzApYomaMg1xGyIO4dA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:23.662486+00:00"
---

# Compiling the hello checker

In this section, you compile the Hello checker that you built in The hello checker source code.

To compile the Hello checker:

1. Go to your HELLO directory, and invoke
   `build-checker`:

   ```
   > cd HELLO
   > <install_dir>/sdk/build-checker hello
   ```

   Note that the argument is hello, not hello.cpp.

   install_dir is the Coverity Analysis root
   directory.

   After printing the compilation and linking command line, this build command prints the
   following:

   ```
   SUCCESS! Your checker has been compiled to ./hello
   ```

   If an error occurs, set your PATH. See 
   `build-checker`
    in Compiling Coverity Extend SDK checkers.

   Note: On Unix, you can run the makefile for the sample checker instead of running
   `build-checker`. This file is located in the
   <install_dir>/sdk/samples/hello directory.

   On
   Windows, if you see the following error when compiling your checker, you
   must either restart your console as an administrator or make a copy of the
   samples
   directory:

   ```
   C:/Program Files/Coverity/Coverity Static Analysis/sdk/compiler/bin/ld.exe:
    cannot open output file hello.exe: Permission denied
    collect2: ld returned 1 exit status
    ERROR: Checker "hello" did not successfully compile.
   ```
2. Locate the following output in your HELLO directory:

   - hello (on Unix)
   - hello.exe (on Windows)

   This output is the checker program, which supports a command-line interface similar to
   `cov-analyze`, except that it can only run one checker.
   (For information about `cov-analyze`,
   see the Coverity 2026.6.0 Command Reference.)
