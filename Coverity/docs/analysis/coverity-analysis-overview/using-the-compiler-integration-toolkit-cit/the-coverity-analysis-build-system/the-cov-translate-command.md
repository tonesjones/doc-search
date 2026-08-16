---
title: "The 'cov-translate' command"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-cov-translate-command.html"
content_id: "jD~sMdwg186IbSe_z1uFtA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:59.193953+00:00"
---

# The 'cov-translate' command

The `cov-translate` process takes a single invocation of the native
compiler and maps it into zero or more invocations of the Coverity compiler. The
following steps provide an overview of the `cov-translate` command
process:

1. Find the compiler configuration file that corresponds to the native compiler invocation. This
   involves finding a configuration with the same compiler name, the same compiler
   path, and the same required arguments. If such a configuration is not found, and the
   compiler was configured as a template, `cov-translate` will
   generate an appropriate configuration.
2. The native command line is then transformed into the Coverity compiler commands. All
   compilers tend to do similar things, so `cov-translate` is broken
   into phases. Each phase takes the command lines produced in the previous phase as
   input and produces transformed commands as output. Each phase has a default set of
   actions and will only appear in a configuration if needed by a particular compiler.

   Expand
   :   Expands the command line to contain all arguments. This usually means
       handling any text files that expand to command line arguments, native
       compiler configuration files, and environment variables. After this
       phase, all of the compiler switches should be on the command line.

   Post Expand
   :   If the results of transforming the command line in the Expand phase will
       result in a command line that is not valid for the native compiler, that
       portion of the transformation should be deferred to the Post Expand
       phase. The side effect of deferring transformation is that when
       preprocessing is attempted, or if the replay of a build occurs later,
       all of the files or environment elements might no longer be
       present.

   Pre-translate
   :   Maps the native compiler switches to the equivalent Coverity compiler
       switches, or drop the native compiler switches if they do not affect
       compilation behavior.

   Split
   :   Removes source files from the command line, splitting them into language
       groups. The default behavior performs the split based on the suffixes of
       the files.

   Translate
   :   This phase applies to actions that are not explicitly listed in any
       phases in the configuration XML. For example, the presence of
       <append_arg>-DFOO</append_arg> outside of any phase tags
       (such as <post_expand/>) appends `-DFOO` to the
       command line during the Translate phase. Also, part of this phase is the
       decision to skip command lines with arguments that you do not want to be
       emitted. For example, you might want to skip any invocations of the
       compiler that are only doing preprocessing.

   Post Translate
   :   Applies Coverity compiler command transformation that cannot be
       performed in the Translate phase.

   Source Translate
   :   Because the split phase removed source files from the command line,
       there is no opportunity to do command line transformations that are
       dependent on the name of the source file. For C/C++, this phase will be
       executed once for each source file to be compiled. For example, for GCC
       Precompiled header (PCH) file support, you can use this phase to append
       additional arguments if the source file is a C/C++ header file.

   Final Translate
   :   This translation phase is the last one before the arguments are passed
       to the Coverity compiler. This phase is reserved for the Coverity
       Support team to work around any command lines that are improperly
       handled by their implementations.
3. For the command lines produced by the phases of transformation, the Coverity compiler is then
   invoked unless `cov-build --record-only` is specified, in which
   case, Compiler Integration Toolkit (CIT) simply records the Coverity compiler
   command line for a later invocation as part of `cov-build
   --replay`.
