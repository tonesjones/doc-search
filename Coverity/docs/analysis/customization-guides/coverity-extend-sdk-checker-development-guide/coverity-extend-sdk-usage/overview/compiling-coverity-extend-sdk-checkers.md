---
title: "Compiling Coverity Extend SDK checkers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/compiling-coverity-extend-sdk-checkers.html"
content_id: "OMlfbwJGTIbclK_dwtkpyw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:21.712999+00:00"
---

# Compiling Coverity Extend SDK checkers

The Coverity Extend SDK provides a few tools for compiling checkers:

- On Unix and Windows: The `build-checker` or, on Windows,
  `build-checker.bat` command. You will use this command to
  build the Hello checker sample in Creating your first checker: hello.

  <install_dir>/sdk/build-checker checker-name
  :   This command compiles a Coverity Extend SDK checker. It looks in the current
      directory for 
      checker_name.c or 
      checker_name.cpp, compiles it, and
      places the executable in the current directory. You can then run it
      as you would run `cov-analyze`. (For information
      about `cov-analyze`,
      see the Coverity 2026.6.0 Command Reference.)

      The `build-checker` command needs to be able to find the Coverity
      Extend SDK installation directory. If you copy the command
      from <install_dir>/sdk to another
      location, you must set environment variable PREVENT_ROOT to the root
      directory of the Coverity Extend SDK installation.

      For example, on Unix:

      ```
      export PREVENT_ROOT=<install_dir>/sdk
      ```

      For example, on Windows:

      ```
      set PREVENT_ROOT=<install_dir>/sdk
      ```
- `Makefile` in
  <install_dir>/sdk/samples compiles all the sample
  checkers located in <install_dir>/sdk/samples. You
  need to run `Makefile` from this directory. For example:

  ```
  > cd <install_dir>/sdk/samples
  > make
  ```

  CAUTION:

  When compiling on a Windows system, you must use the
  `make` command provided by GNU, *and* your system must
  be configured to use a POSIX shell. The Cygwin environment is one possible
  solution.

  The console output consists of a number of compile and link command lines. After
  successful completion, the console will print a message similar to the
  following:

  ```
  SUCCESS! Your checker has been compiled to ./whileloopassign
  ```
- On Unix only: Each sample checker subdirectory (for example,
  <install_dir>/sdk/samples/hello) includes a
  `Makefile` that is designed to compile just that checker.
  See Creating a Makefile for convenience.
