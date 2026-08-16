---
title: "Troubleshooting Desktop Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/troubleshooting-desktop-analysis.html"
content_id: "gqnSYpdDSYQxH6r8almkvQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:35.565731+00:00"
---

# Troubleshooting Desktop Analysis

This troubleshooting section provides instructions for fixing the following common issues
with Desktop Analysis:

1. There is no
   captured compilation that contains the file
2. `PARSE_ERROR` reported in file to analyze
3. `WARNING:` compiler output does not exist
4. `[ERROR] No snapshot in stream "X" has analysis
   summaries...`
5. `Issues with HTTP client proxies`
6. Differences
   between Central and Desktop Analysis results
7. `cov-run-desktop --clean or --build`: "The system cannot find
   the file specified."

## Files not yet captured and not captured automatically

There are essentially three ways `cov-run-desktop` can
capture a file for analysis, and this error indicates that none of them
currently apply to the listed files. `cov-run-desktop`
cannot be sure which was intended to apply, so the user has to determine
that. The three capture methods are these:

- (a) Compiled under `cov-run-desktop --setup` or
  `--build`. This is the typical way of preparing
  `cov-run-desktop` to handle compiled source files.
- (b) Automatically captured using the filesystem capture configuration. Files for analysis
  that have not already been captured will be checked against filename patterns
  established in the filesystem capture configuration (part of the *compiler
  configuration*), such as glob *.js. When there is a
  match, such as foo.js, those files will be captured
  according the the relevant configuration.
- (c) Automatically compiled and captured with a *specific files* build script. (See
  Compiling files on demand for details.) If
  `specific_files_build_cmd` is specified in
  coverity.conf, files for analysis that have not already
  been captured, do not match any filesystem capture configuration, and match the
  `specific_files_regex` if specified, will be passed to that
  build script. If the script returns a failure code (non-zero), that will be
  reported to the `cov-run-desktop` user as a specific
  error.

Therefore, the resolution to this error (`not yet captured and not captured
automatically`) depends on which of these methods you expected to apply.
Method (b) below is the only choice for interpreted code (filesystem capture code),
including JavaScript, PHP, Python, Ruby, and Scala. Methods (a) and (c) are for
compiled code, including C, C++, Objective-C, C#, Java, and Kotlin. Method (a) is
the simpler and more typical of the two. If none of these apply, because a file is
not source code or not supported for Coverity desktop analysis, consider one of the
(n) solutions listed toward the end, below.

Troubleshooting method (a), compiling code under cov-run-desktop --setup or --build:
:   If you are expecting a file to have been captured already, the
    `cov-manage-emit` command can be used to help diagnose
    the cause. As a first step, run the following command to see a list of all
    the *primary source files* (PSFs) that were captured:

    ```
    cov-manage-emit --dir idir list
    ```

    A PSF is the "main" file of a translation unit (TU, also called a
    compilation unit), the file whose name is specified on the compiler
    command line. Other files that are implicitly read in order to compile
    the PSF, such as header files in C/C++ and other source and bytecode
    files in Java and C#, are "non-primary" source files.

    If you are
    trying to analyze a PSF, but it is not in the output of the list
    command, it means a compilation of that file was not captured.

    Solution (a1): Re-capture the build
    :   If the file to analyze was added since the last time you ran
        `cov-run-desktop --build`, it is necessary
        to re-run that command to capture a compilation of the new file.
        It is simplest to re-capture a full build, although it is also
        possible to just capture a compilation of that one file.

    Solution (a2): Configure another compiler
    :   Another reason a PSF might be missing is that its compilation
        was seen by `cov-build` but not recognized as a
        compilation at the time. The `cov-configure`
        command tells `cov-build` what commands to
        consider as compilers. Every compiler used in your build should
        be configured with `cov-configure`.

        Compiler
        configuration can be a complex process. The 
        idir/build-log.txt file
        contains information about what commands were seen and which
        were treated as a compilation. If examining that file is not
        sufficient to discover the cause of an uncaptured
        compilation command, contact Coverity Support for
        assistance.

    Solution (a3): Non-primary source files and record with source
    :   If the file you want to analyze is a non-PSF, such as a header
        file, then it is typically necessary to add
        `--record-with-source` to the
        `cov-run-desktop --build` command line.
        This causes the build to preprocess every translation unit and
        record all of the source files that are read, rather than just
        record the command line. Consequently,
        `cov-run-desktop` will be able to find a
        translation unit that includes a given header file, if one
        exists.

        The list of both primary and non-primary source files
        can be printed with the command:

        ```
        cov-manage-emit --dir idir --tu-pattern 'file(".")' print-source-files
        ```

        Here, the `--tu-pattern` is just a dummy
        pattern that matches all TUs, provided because
        print-source-files requires a pattern.

    Solution (a4): Specify a primary source file as well as a header
    :   Another tactic to analyze header files is to specify to
        `cov-run-desktop`
        *both* the header file to analyze and some PSF that
        includes that header file. `cov-run-desktop`
        will recognize the PSF, compile it, then notice that it includes
        the header. This is different from just analyzing the PSF,
        because `cov-run-desktop` only reports defects
        in files that are specified on the command line.

    Finally, detailed debugging of build capture with
    `cov-run-desktop` is possible by consulting the
    build-log.txt file and the
    output/cov-run-desktop-log.txt file in the
    intermediate directory, usually
    data-coverity/vN.N.N/idir.

Troubleshooting method (b), automatic filesystem capture:
:   Solution (b1): Configure filesystem capture
    :   Although the default compiler configuration used by
        `cov-run-desktop` includes standard
        configurations for all supported interpreted languages, if you
        have specified `compiler_configurations` in
        coverity.conf or a compiler
        configuration file with `--config`, these might
        not include filesystem capture. For example, to configure
        filesystem capture for Python *.py and PHP
        *.php, use this in
        coverity.conf (see Settings):

        ```
        "compiler_configurations": [
          {
            "cov_configure_args": ["--python"]
          },
          {
            "cov_configure_args": ["--php"]
          }
        ],
        ```

        Note: Although the naming can be
        misleading, for historical reasons, the configuration for
        filesystem capture is part of the "compiler
        configuration".

    Solution (b2): Expand file patterns for filesystem capture
    :   Suppose your project uses the convention of a .j extension for
        JavaScript files. The default configuration for JavaScript
        capture provided by `cov-run-desktop` looks for
        files matching *.js (and
        *.html and others). The following adds
        configuration for capturing *.j files as
        JavaScript:

        ```
        "add_compiler_configurations": [
          {
            "cov_configure_args": ["--comptype", "javascript", "--file-glob", "*.j"]
          }
        ],
        ```

        Note:
        `add_compiler_configurations` extends the
        default configuration for
        `cov-run-desktop`. Use
        `compiler_configurations` to replace
        it.

        Also refer to the `cov-configure`
        documentation in the Coverity 2026.6.0 Command Reference for
        more details.

    Solution (b3): Use a supported platform for the source language
    :   Coverity analysis of interpreted languages is not supported on some platforms. If you
        are using the default compiler configuration, this could explain
        why source files for some languages are not being captured.
        Providing an explicit configuration as in solution (b1) would
        cause `cov-configure` to report an error if a
        given filesystem capture language is not supported. You can also
        consult the "Supported platforms" section in the Coverity 2026.6.0 Installation and Upgrade Guide for more
        information.

    Also refer to the `cov-configure` documentation in the Coverity 2026.6.0 Command Reference for more details.

    Finally, detailed debugging of filesystem capture with
    `cov-run-desktop` is possible by
    consulting the autocapture-log.txt file
    and the output/cov-run-desktop-log.txt
    file in the intermediate directory, usually
    data-coverity/vN.N.N/idir.

Troubleshooting method (c), automatic compilation of specific files
:   If you do not see this line on the console before receiving the `not yet captured
    and not captured automatically`
    error:

    ```
    [STATUS] Attempting to compile files not known to the emit...
    ```

    then
    `cov-run-desktop` did not invoke the build script,
    either because none is configured or because no files were considered
    applicable.

    Solution (c1): Configure a `specific_files_build_cmd`
    :   See Compiling files on demand for details on
        configuring a custom build script.

    Solution (c2): Adjust `specific_files_regex` to match the file name
    :   If a file should be compiled by the build script and using
        `specific_files_regex` (recommended), make
        sure the regex matches that file name.

    If you do see this line on the console before receiving the
    `not yet captured and not captured automatically`
    error:

    ```
    [STATUS] Attempting to compile files not known to the emit...
    ```

    then
    `cov-run-desktop` did invoke the build script, and
    it reported success.

    Solution (c3): Specify a primary source file as well as a header
    :   Auto-compilation cannot typically handle an uncaptured header
        file when no primary file that includes it is part of the files
        for analysis. Consider including one, as in solution (a4)
        above.

    Solution (c4): Adjust `specific_files_regex` to match the file name (again)
    :   It is possible that some files were properly passed to the build
        script and some were not due to this.

    Solution (c5): Ensure that the build script always invokes the compiler
    :   If the build script is base on `make`, measures
        must be taken to ensure the compiler is always invoked, even if
        object files are newer than source files. One way to fix this is
        to have the script `touch` the source files
        before running `make`.

    Solution (c6): Configure the compiler
    :   Compilers used by the build script must be part of the compiler
        configuration. See solution (a2) above.

    Finally, detailed debugging of automatic compilation with
    `cov-run-desktop` is possible by consulting the
    autocompile-log.txt file and the
    output/cov-run-desktop-log.txt file in the
    intermediate directory, usually
    data-coverity/vN.N.N/idir.

    Possible
    solutions when none of method (a) through method (c) apply:

    - Solution (n1): Remove the file(s) from consideration, command
      line

      If a list of files was specified on the command line,
      remove the ones not to be analyzed.
    - Solution (n2): Remove the file(s) from consideration, SCM
      modified

      If using `--analyze-scm-modified`, use
      options `--ignore-modified-file-regex` and/or
      `--restrict-modified-file-regex`, or their
      coverity.conf equivalents, to exclude
      unanalyzable files by name or extension. Example
      coverity.conf
      addition:

      ```
      {
        // ... other settings ...
        "settings": {
          "cov_run_desktop": {
            // ADD the following:
            "restrict_modified_file_regex": "\\.(c|cpp|cc|java|cs)$"
          }
        }
      }
      ```
    - Solution (n3): Ignore uncapturable inputs (not recommended)

      If
      other solutions are impractical for eliminating uncapturable,
      unanalyzable files, or if you want a quick, temporary solution,
      you can specify `--ignore-uncapturable-inputs
      true` on the command line, or use the
      `ignore_uncapturable_inputs`
      coverity.conf setting.

Files not found
:   This generally indicates the user specified a path on the command line for a file to
    analyze, but the file was not found, either as an absolute path or relative to
    the current working directory.

    - Solution 1: Name a file that actually exists. Did you mistype the
      path?
    - Solution 2: Change to or specify the right directory

      If you want to
      analyze foo.c, but that is not in the current
      working directory, please change to that directory or include it in
      the specified path to foo.c.
    - Solution 3: Enable suffix matching (not recommended).

      Earlier versions
      of `cov-run-desktop` permitted specifying any path
      suffix of a file captured in the intermediate directory, regardless
      of the current working directory. To restore this functionality for
      backward compatibility, use `--allow-suffix-match` or
      `allow_suffix_match` in
      coverity.conf.

Unable to find or capture specified files
:   This message is only generated when using `--allow-suffix-match`, and
    indicates you either have a "file(s) not found" problem or a "file(s) not yet
    captured and not captured automatically" problem, but the nature of
    `--allow-suffix-match` doesn't allow the tool to distinguish
    the two. Refer to the troubleshooting guidance for those errors.

`PARSE_ERROR` reported in file to analyze
:   A `PARSE_ERROR` pseudo-defect is reported when the Coverity compiler is
    unable to compile a source file. It may be that the file contains an ordinary
    syntax error; generally, you should compile the file with your usual compiler to
    check for syntax errors before running Desktop Analysis.

    If there are no
    syntax errors detected by the usual compiler, a possible reason for a
    problem is that the compiler options for your build have changed — for
    instance, changing `-I` or `-D` flags for
    C/C++, or adding a `classpath` entry for java. In these
    cases, the solution is to re-capture a full build using
    `cov-run-desktop --build`.

    Another possibility
    is that you have encountered an incompatibility between that compiler and
    the Coverity compiler. In that case, the typical solution is to adjust the
    compiler configuration as defined with `cov-configure` to
    work around the problem. For more information, see "Configuring compilers for Coverity Analysis" in the Coverity Analysis 2026.6.0 User and Administrator Guide. In some cases, it may be necessary
    to contact Coverity Support for assistance.

`WARNING:` compiler output does not exist
:   This warning is caused, when analyzing Java code, by the absence of a
    .class file corresponding to some
    .java file that was selected for analysis. These
    .class files are used as input to the Java dynamic
    analysis which affects the XSS results for Java (see cov-security-da). To fix this, ensure
    that your usual compiler has run on the code first so it will generate the
    .class files, then run
    `cov-run-desktop`.

`[ERROR] No snapshot in stream "X" has analysis summaries...`
:   This error is caused by one of the following scenarios:

    - The reference stream (specified by the `--stream` option)
      does not contain any snapshots with analysis summaries.
    - The reference stream does contain one or more snapshots with analysis
      summaries, but their Code Version Date is more recent than the date
      specified to, or inferred by, the `cov-run-desktop`
      command (see `--reference-snapshot` in the Coverity 2026.6.0 Command Reference for information on how this is
      determined).

    To fix this, log in to Coverity Connect to identify a candidate
    reference snapshot, if one exists. It may be necessary to enable Desktop
    Analysis in stream configuration, and then commit a new
    snapshot.

    **To find a candidate reference snapshot:**

    1. In Coverity Connect, open a Snapshots view for
       your project (All In Project for example).
    2. Click the "gear" icon to edit the view settings, and open the
       Columns tab.
    3. Enable the Has Analysis Summaries and
       Code Version Date columns.
    4. Return to the Snapshots view. Any snapshot that
       has "True" in the Has Analysis Summaries column
       contains analysis summaries. Verify that your reference stream contains
       a snapshot with analysis summaries, and ensure that its Code Version
       Date is not more recent than the date specified by the
       `--reference-snapshot` option described in the Coverity 2026.6.0 Command Reference.

       For more information about Code
       Version Date, see the `cov-analyze` option,
       `--code-version-date`, also described in the Coverity 2026.6.0 Command Reference.

    If no candidate reference snapshot exists:

    1. Navigate to Configuration > Projects & Streams.
    2. Select the relevant stream, and click on the Desktop
       Analysis tab.
    3. Ensure that the Enable Desktop Analysis option is
       selected.
    4. Commit a new analysis to this stream. This will contain analysis
       summaries as long as the `cov-analyze --export-summaries`
       option is not explicitly set to `false`.

    If `--reference-snapshot scm` option is used:

    This
    issue may be caused if your codebase's last update date is before the
    reference snapshot was committed to the stream. To fix this:

    1. Update your codebase and push the changes (this will cause your SCM
       repository to be updated more recently than the reference snapshot).
    2. Re-run Desktop Analysis with `--reference-snapshot scm`.

Issues with HTTP client proxies
:   Desktop Analysis may fail or return inaccurate results when run on networks using HTTP
    client proxies. Specifically, issues are known to arise when the
    `http_proxy` environment variable is a machine name rather
    than an IP address, or when there are wildcards in the `no_proxy`
    environment variable.

Differences between Central and Desktop Analysis results
:   You may notice analysis results that differ slightly from your Central Analysis results.
    There are several reasons that this may occur; see Reasons for results differences.

`cov-run-desktop --clean or --build`: "The system cannot find the file specified."
:   On Windows platforms, you may find that a command that works in the
    cmd.exe shell does not work in
    `settings.cov_run_desktop.build_cmd` or
    `clean_cmd` in coverity.conf (or on the
    `cov-run-desktop --build` command line), as it fails with
    the error message, "The system cannot find the file specified."

    One possible
    reason is, unlike cmd.exe,
    `cov-run-desktop` does not automatically try file
    extensions other than ".exe". In particular, programs
    with extensions ".com", ".bat",
    and ".cmd" must be specified explicitly for
    `cov-run-desktop` to invoke them.
