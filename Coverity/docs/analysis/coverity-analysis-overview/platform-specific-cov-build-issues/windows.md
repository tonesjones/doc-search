---
title: "Windows"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/windows.html"
content_id: "J9RNEtdMDfqfdEzWJFLO8Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:10.697571+00:00"
---

# Windows

The `cov-build` command uses a different mechanism to capture compiler process
creation on Windows than on UNIX platforms. The Windows version of
`cov-build` runs the build command and its child processes in debug
mode. If your build system has problems running in debug mode, try using the
`--instrument` option with `cov-build`. This option
might be useful is for capturing a 32-bit `javac` compilation on 64-bit
Windows.

Some build systems on Windows are invoked from an integrated development environment
(IDE) such as Visual Studio. There are several ways of integrating Coverity Analysis
with an IDE:

- Invoke the IDE binary with the `cov-build` command wrapped around it. For
  Visual Studio 2005 and 2008, the IDE is typically invoked with the
  `devenv` command. For
  example:

  ```
  > cov-build --dir intermDir devenv
  ```

  After
  you run the command, perform the necessary actions in the IDE to perform the
  build and then exit the IDE. Because the `devenv` command
  runs the compiles, `cov-build` can capture the
  build.
- For Visual Studio 2010 and subsequent releases, the `devenv` command builds
  applications in a separate hosted instance of the `msbuild`
  tool.

  Analysis support for Visual Basic was introduced with Visual Studio
  2013.
- Use the command line to perform the build.

  Example using
  `devenv`:

  ```
  > cov-build --dir intermDir devenv solutionfile /build solutionconfig
  ```

  Example
  using
  `msbuild`:

  ```
  > cov-build --dir intermDir msbuild solutionfile /p:Configuration=Release
  ```
- Use the Visual C++ compiler directly (cl.exe) within a makefile and
  then run `make` or `nmake` with the
  `cov-build` command. This is the same process you would use
  to build with a compiler, such as gcc, on UNIX systems.
