---
title: "Integrating Coverity Analysis into a build system"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/integrating-coverity-analysis-into-a-build-system.html"
content_id: "RfxurH01corkXbYL4Qz76Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:57.665568+00:00"
---

# Integrating Coverity Analysis into a build system

Using a C/C++ code base as an example, Figure 1
shows how many build systems interact with the compiler. The build system calls an
`exec`-type function to run the compiler process. The compiler
process reads in the source files and produces binary object files.

Figure 1. A typical build system
[image: image]

There are two standard ways of integrating Coverity Analysis into this kind of build
system. One way, shown in Figure 2, uses the
`cov-build` command (described in Integrating Coverity Analysis into the build environment—'cov-build') to automatically detect invocations of the compiler. This method usually requires no
changes to the build system itself. Instead, it relies on "wrapping" the build system so
that Coverity Analysis can piggyback on the compiler invocations. The native build
system is invoked by the `cov-build` command, which sets up the
operating environment such that calls to `exec`-type functions made by
the dynamically-linked build process are intercepted by the Coverity Analysis
`capture` stub library. The capture library calls the
`cov-translate` command to translate the compiler command-line
arguments to the command line arguments of the Coverity Analysis engine (also called the
Coverity compiler). The Coverity compiler then parses the file and outputs a binary form
of the source file into the intermediate directory, where it is read later by the
analysis step. After the Coverity compiler finishes, the capture library continues to
run the normal compiler that generates the .o files. You must run
the actual compiler in addition to the Coverity compiler because many build processes
build dependencies and build-related programs during the build itself. The disadvantage
of this method is that it requires a longer compile time because each source file is
parsed and compiled once with the regular compiler, and a second time by the Coverity
compiler. But, the build system itself does not change, and no Coverity Analysis related
changes need be maintained.

Figure 2. Coverity Analysis integration using the `cov-build`
command
[image: image]

Figure 3 shows an alternative Coverity Analysis
integration method that relies on modifications to the build targets of the build system
itself. Most build systems have the notion of a debug build target and a production
build target. Similarly, another build target can be added to invoke the
`cov-translate` command, or even the Coverity compiler directly
(with the `cov-emit` command), to parse the code and generate the
intermediate data. This method requires the build administrator to maintain the changes
to ensure that they continue to work when the build steps change. The common
`make` utility makes it possible to perform this form of
integration by changing a single variable, such as CC. The Coverity
Analysis translator can be configured to understand the command-line arguments for a
variety of compilers, so the arguments to the compiler usually do not need to be
changed. For more information about this integration method, see Alternative build command: 'cov-translate'.

Figure 3. Coverity Analysis integration by modifying build targets
[image: image]

The rest of this chapter describes how to use Coverity Analysis to perform
these two types of integration.

- The intermediate directory
- Integrating Coverity Analysis into the build environment—'cov-build'
- Alternative build command: 'cov-translate'
- Running parallel builds
