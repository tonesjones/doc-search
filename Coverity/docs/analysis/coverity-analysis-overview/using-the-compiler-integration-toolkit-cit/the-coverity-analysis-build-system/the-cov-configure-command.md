---
title: "The 'cov-configure' command"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-cov-configure-command.html"
content_id: "dgefKQU7657jT5KfC9foCw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:58.536871+00:00"
---

# The 'cov-configure' command

The `cov-configure` command can be used in two ways:

- template mode
- non-template mode

When used in template mode, the generation of a configuration for that compiler is
deferred until the compiler is used in the build. In either case, the following steps
describe an overview of the configuration generation process:

1. Determine required options.

   Identify any arguments that must be specified for the
   configuration to be valid. Certain compilers require that different
   configurations be generated depending on the presence of certain
   switches.

   For example, the GCC -m32 switch will cause the compiler to
   target a 32-bit platform, while -m64 will target a 64-bit platform.
   `cov-configure` will record these options in the
   configuration so the generated configuration will only be used when those
   options are specified. When using a compiler integration implementation using
   the Compiler Integration Toolkit (CIT), the required options must have the
   oa_required flag included in the switch specification in the compiler switch
   file (compiler_switches.dat). For more
   information, see The compiler switch file.
2. Test the compiler.

   Runs tests against the compiler to determine its behavior, for example,
   to determine type sizes and alignments. See Test tags for
   descriptions of the testing tags that you can set in the configuration
   file.
3. Determine include paths.

   cov-configure determines the include path in three ways and each
   involves opening standard C and C++ headers:

   - strace - Look at system calls to see what directories are searched. This is
     not supported on Windows systems.
   - dry run - `cov-configure` can parse include paths from the
     output of a sample compiler invocation. You can change this behavior with
     `<dryrun_switch>` and
     `<dryrun_parse>`.
   - preprocess - The most general solution is to preprocess the file and look
     for the `#line` directives which details where the files are
     located.

   For a C compiler, the test gives the compiler these files:
   stdio.h, stdarg.h

   For a C++
   compiler the test gives the compiler these file stdio.h,
   stdarg.h, cstdio,
   typeinfo, iostream,
   iostream.h, and limits. A Compiler
   Integration Toolkit (CIT) configuration can add additional files to the list of
   headers. For more information, see Additional configuration tags.
4. Determine macros:

   cov-configure determines macros in the following ways:
   - dump - Native compilers can dump intrinsically defined macros when they
     are invoked with certain switches. You can change this behavior with
     `<dump_macros_arg>`.
   - preprocess - Candidate macros are inserted into a file and the file is
     preprocessed to determine the macros value. Candidate macros are
     identified in two ways:
     1. Specified as part of the compiler implementation. Additional
        macro candidates can be added using the Compiler Integration
        Toolkit (CIT). For more information, see Additional configuration tags.
     2. System headers are scanned for potential macros.
5. Test the configuration

   Run tests against the configuration to see if it works correctly and
   then tailor them appropriately. Currently, the only test that is performed is to
   determine if `–no_stdarg_builtin` should be used or not.
