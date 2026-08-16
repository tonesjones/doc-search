---
title: "Troubleshooting build problems"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/troubleshooting-build-problems.html"
content_id: "04HXBRWvm_AHle~uQyY9uw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:08.133306+00:00"
---

# Troubleshooting build problems

The build-log.txt file is generated but there are no COMPILING lines and no "Emit for file complete" messages.
:   Potential causes:

    - The compiler is not configured properly in
      coverity_config.xml. Common problems include:
      - A syntax error in the coverity_config.xml
        file. It must be a valid XML file according to the DTD
        <install_dir>/dtd/coverity_config.dtd.
        Look carefully at the initial output to the terminal when
        `cov-build` is invoked. Consider using an
        XML syntax or schema validator such as
        `xmllint` to make sure that the file is
        valid.
      - The configured path name of a compiler is empty or missing, in
        the comp_dir tag. This field should identify the actual path
        name for the configured compiler, although any executed
        compilation with the same command name is analyzed as if it were
        the configured version. If incompatible versions are in use, you
        can configure them with a template, or you can separately
        configure each pathname that is in use.

The build stops before all files have been compiled.
:   Potential causes:

    - The native build is failing. The `cov-build` command
      relies on the native build to be able to complete the compile. The
      `cov-build` command cannot proceed beyond the
      native build. On many build systems, there is a way to keep compiling
      files even when an error occurs. For example, the -i flag to
      `make` forces `make` to ignore any
      errors during the build. Coverity Analysis does not require a 100%
      complete build to produce good results.
    - The `cov-build` command could be interfering with the
      native build. Contact Coverity support for assistance.

Some or all files give compiler error messages in build-log.txt.
:   Potential causes:

    - The compiler translator or options are not configured properly. If you
      manually modified or generated the
      coverity_config.xml file, reread Using Coverity Analysis configuration files in the analysis. The most common problem is a mismatch between the predefined macros
      in nodefs.h and the predefined macros supplied by
      the build's compiler. Consider using the
      `cov-configure` command to generate a configuration
      file automatically. Make sure to specify the compiler version.
    - Some of the macro suppressions in nodefs.h are
      causing parsing problems. Consider removing the offending predefine in
      nodefs.h if the offending nodef is not
      required. For C++, a prototype declaration might need to be added to
      nodefs.h.
    - The pre-include directories are not set properly. The build compiler has
      a list of built-in directories to search to find include files. The
      include_dir and sysinclude_dir options in
      coverity_config.xml need to reflect these
      built-in search paths. Note that the include_dir has precedence over
      sysinclude_dir, and that and parsing might change in "system" headers.
      Both are searched whether "" or <> is used. The
      `cov-configure` command automatically finds these
      search paths for most compilers.
    - The `cov-emit` command is not able to parse the source
      code. There are some non-standard, compiler-specific constructs that
      `cov-emit` might not be able to parse correctly.
      For a detailed discussion of the potential problems and solutions, see
      Configuring compilers for Coverity Analysis.

I am using `clearmake` and the Coverity build only seems to compile a small subset of my source files.
:   Potential causes:

    The `clean` command with `clearmake`
    generally does not cause a subsequent invocation to re-build all of the
    source files in the build with the compiler. The Coverity build system looks
    for invocations of the compiler to decide which source files to analyze, so
    any `clearmake` optimizations that circumvent actually
    running the compiler will interfere with the Coverity build. In particular,
    you must:

    1. Delete all of the object files that correspond to the source files that
       you want to compile.
    2. Turn off *winking* by specifying the appropriate option to
       `clearmake`.
