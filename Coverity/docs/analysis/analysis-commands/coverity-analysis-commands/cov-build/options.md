---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "McX3wjTOwKMT7_laHCTdjA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:04.716943+00:00"
---

# Options

--add-arg <arg>
:   Specifies an `--add-arg <arg>` option to the
    `cov-translate` invocations that are launched by
    `cov-build`. See the description of this option
    in the `cov-translate` command
    documentation.

--append-log
:   Append a log of the current `cov-build` run to an
    existing build log file, instead of performing the default behavior,
    which is to overwrite the log file. For details about the file, see
    C, C++, C#, and Visual Basic build capture.

--auto-diff
:   **[C/C++ builds only]**

    Have `cov-translate` attempt to diff preprocessed
    files when a compilation fails. See the description of
    `--auto-diff` in cov-translate Options.

--bazel
:   **[Linux (64-bit), macOS, Windows (64-bit)]**

    Specifies that the build command that `cov-build` is
    wrapping is a Bazel build that uses the Coverity-Bazel integration
    to generate a build description that `cov-build` will
    use to replay the compilations locally. See "Building with
    Bazel" in Coverity Analysis 2026.6.0 User and Administrator Guide for
    more information about capturing a Bazel build and what platforms
    Bazel builds can be captured on.

--bazel-disable-module-workspace-agent
:   Prevent `cov-build --bazel` from injecting a Java agent into Bazel to
    automatically add the required information to allow the Coverity
    Bazel integration to function.

--bazel-extra-compile-mnemonic <extra mnemonic>
:   **[Linux (64-bit), macOS, Windows (64-bit)]**

    Specifies that Bazel actions with the mnemonic `<extra
    mnemonic>` should be treated as a compilation in any
    Bazel builds. Only works with the --bazel argument.
    This argument may be passed multiple times.

--bazel-extra-dep-type <extra dependency type>
:   **[Linux (64-bit), macOS, Windows (64-bit)]**

    Specifies that Bazel rule attributes named `<extra
    dependency type>` should be treated as a dependency type
    that may include targets relevant to capture in any Bazel builds.
    Only works with the --bazel argument. This argument
    may be passed multiple times.

--capture
:   Run the specified build command, and capture the actions and
    translation units in the
    `<intermediate_directory>` that is created by
    the `--initialize` option.

    Alternatively, a build system can directly invoke
    `cov-translate`, possibly in several concurrent
    processes.

    For C and C++ analysis, you can run concurrent, distributed builds
    across multiple machines with the `--capture` option
    if the `<intermediate_directory>` is located on an
    NFS partition. Distributed builds are only supported on Linux and
    Solaris systems.

--capture-ignore <program-name-with-extension>
:   **[Windows only]**

    When the `--instrument` option is **not** present:
    Use the `--capture-ignore` option to specify the base
    name (including the extension) of a program invoked by the native
    build that does not exit during the build, such as a service or a
    daemon. Otherwise `cov-build` will hang at the end of
    the native build waiting for these programs to terminate. The
    `cov-build` command is already aware of
    `NTVDM.EXE` and `MSPDBSVR.EXE`.
    The program name is case insensitive.

    When the `--instrument` option is present: Use the
    `--capture-ignore` option to specify the base
    name (including the extension) of a program invoked by the native
    build that should not be followed under `cov-build`.
    Note that any compiles launched by this process will not be seen.
    The program name is case insensitive.

--chase-symlinks
:   **[C/C++ builds only]**

    Follow symbolic links when determining filenames to report.

--chcmdline-type <type>
:   **[Deprecated]**

    This option is deprecated and has no effect. Do not use this
    option.

--coverity-response-file <response_file>
:   Specify a "response file" that contains a list of additional command
    line arguments, such as a list of input files. Each line in the file
    is treated as one argument, regardless of spaces, quotes, etc. The
    file is read using the platform default character encoding. The
    response file cannot contain the build command, either in full or in
    part.

--cygpath <path>
:   Specify the path to the directory, which contains the bin directory
    of the Cygwin installation, if it is not in the PATH environment
    variable.

--cygwin
:   **[C/C++ builds only]**

    On Windows, indicates that the build is done with Cygwin. This option
    allows Cygwin-style paths to be used in the native build command.
    However, you must use Windows-style paths for all Coverity Analysis
    commands.

--decomp-processes
:   Sets the number of processes to use when decompiling bytecode.

    If
    this value is not set, the number of processes is determined
    automatically.

--defer-decomp
:   Only records the decompilations of byte code during the build. It
    does not attempt to decompile and emit the byte code. Later,
    `cov-build` can be rerun with
    `--replay-decomp` to decompile and emit the byte
    code.

    See also, `--replay-decomp`.

--delete-stale-tus
:   Automatically deletes translation units that are created from source
    files that were renamed or removed. This capability is off by
    default. Use this command to perform an incremental build when you
    have deleted/renamed source files.

--desktop
:   The `--desktop` option can be used when running `cov-build` in
    preparation for Desktop Analysis. It behaves similarly to
    `--record-only` for C, C++ builds, disables
    bytecode decompilation in Java and C# builds, and does a full build
    for other languages.

    Please note that this option is supported for backward compatibility.
    The preferred method for capturing a build for Desktop Analysis is
    the `cov-run-desktop --build` option.

--dir <intermediate_directory>
:   Pathname to an intermediate directory that is used to store the
    results of the build and analysis.

    Either `--da-broker` or `--dir` must be
    specified. If you do not use `--dir`, Coverity
    recommends that you use `--log-dir` in addition to
    `--da-broker`.

--disable-aspnetcompiler
:   **[C# and Visual Basic builds only]**

    Disables the automatic invocation of
    `Aspnet_compiler.exe` for any ASP.NET 4 and
    earlier Web applications that are detected in the build. The output
    of `Aspnet_compiler.exe` is required by the C# and
    Visual Basic security checkers.

    Use this option if you are manually running
    `Aspnet_compiler.exe` as part of your native
    build or as part of your Coverity Analysis workflow. For further
    information, see "Running a security analysis on an ASP.NET Web
    application" in Coverity Analysis 2026.6.0 User and Administrator Guide.

--disable-cs-parse-error-recovery
:   Disables extra attempts to recover from problems parsing C# or Visual
    Basic source. Though this recovery process takes some extra time, it
    greatly reduces the impact of parsing problems in most cases. It
    works by attempting to emit subsets of the input files that would
    not otherwise reach the emit database.

    Typically, this option is needed only if the recovery process takes
    too long and becomes unmanageable. Note that unlike for Java, this
    mode is enabled by default for C# and Visual Basic because it uses a
    more efficient algorithm.

--disable-scan-transparency-data
:   Disables generation of data for *scan transparency*.

    For
    further information, see the --enable-scan-transparency-data
    option.

--emit-cmd-line-id
:   **[Deprecated]**

    This option is deprecated as of version 4.4.

--emit-complementary-info
:   Enables emitting of complementary information for compliance checkers
    such as MISRA checkers. Selecting this option results in a slower
    build capture but a faster analysis, and it should be applied when
    using compliance checkers. The default value is
    `--no-emit-complementary-info`

    Note: Enabling the `--emit-complementary-info` option
    prior to running an analysis is likely to turn up additional
    defects.

    Any analysis involving `--coding-standard-config`
    requires the information generated during `cov-build`
    when including the `--emit-complementary-info`
    option. The `cov-build` command will take longer, so
    this option should only be used when `cov-analyze` is
    used with `--coding-standard-config`.

    If `cov-build` did not include the
    `--emit-complementary-info` option and
    `cov-analyze` does include
    `--coding-standard-config`,
    `cov-analyze` automatically re-runs every
    `cov-emit` command (for the Translation Units to
    be analyzed). This excludes the native build and the
    `cov-translate` overhead, but it will add
    significant overhead to `cov-analyze`. Note that
    analysis will fail if the emit database does not include source;
    that is re-emit is not possible.

--emit-parse-errors
:   **[Deprecated]**

    This option is deprecated and has no effect.

--enable-scan-transparency-data
:   Enables generation of data for *scan transparency*.
:   When scan transparency is enabled, Coverity Analysis
    inspects the commands that were run during the build, and in the
    intermediate directory saves a list of binaries that might be compilers
    that weren't configured as such. This list is named
    scan-transparency/unconfigured-compilers.

    Scan transparency is enabled by default.

--encoding <enc>
:   **[C and C++ builds only]**

    Specifies the encoding of source files. Use this option when the source code
    contains non-ASCII characters so that Coverity Connect can display the code
    correctly. The default value is US-ASCII. Valid values are the ICU-supported
    encoding names:

    US-ASCII

    UTF-8

    UTF-16

    UTF-16BE
    :   UTF-16 Big-Endian

    UTF-16LE
    :   UTF-16 Little-Endian

    UTF-32

    UTF-32BE
    :   UTF-32 Big-Endian

    UTF-32LE
    :   UTF-32 Little-Endian

    ISO-8859-1
    :   Western European (Latin-1)

    ISO-8859-2
    :   Central European

    ISO-8859-3
    :   Maltese, Esperanto

    ISO-8859-4
    :   North European

    ISO-8859-5
    :   Cyrillic

    ISO-8859-6
    :   Arabic

    ISO-8859-7
    :   Greek

    ISO-8859-8
    :   Hebrew

    ISO-8859-9
    :   Turkish

    ISO-8859-10
    :   Nordic

    ISO-8859-13
    :   Baltic Rim

    ISO-8859-15
    :   Latin-9

    Shift_JIS
    :   Japanese

    EUC-JP
    :   Japanese

        Note: EUC-JP is now a valid output object encoding. See --output_object_encoding.

    ISO-2022-JP
    :   Japanese

    GB2312
    :   Chinese (EUC-CN)

    ISO-2022-CN
    :   Simplified Chinese

    Big5
    :   Traditional Chinese

    EUC-TW
    :   Taiwanese

    EUC-KR
    :   Korean

    ISO-2022-KR
    :   Korean

    KOI8-R
    :   Russian

    windows-1251
    :   Windows Cyrillic

    windows-1252
    :   Windows Latin-1

    windows-1256
    :   Windows Arabic

    Note: If your code is in SHIFT-JIS or EUC-JP, you must specify the
    `--output_object_encoding SHIFT-JIS` or
    `--output_object_encoding EUC-JP` option
    (respectively) for `cov-emit` in order to avoid
    receiving STRING_OVERFLOW false positives.

--finalize, -fin
:   **[C/C++ builds only]**

    Combines the build log and metrics from all the host machines that
    ran `cov-build` with the same
    `<intermediate_directory>`, and indicate any
    additional steps that are needed to prepare for a C and C++
    analysis.

    Do not specify a build command when using the
    `--finalize` option.

--force
:   Specifying this options causes the Coverity compiler to attempt all
    source files, including files that have already been emitted and
    whose timestamps have not changed. This is equivalent to
    `--force` in the respective compiler, for example
    `cov-emit`.

--initialize, -init
:   **[C/C++ builds only]**

    Creates the specified `<intermediate_directory>`
    that a set of subsequent builds will use. You can only use this
    option once, and without a build command, before a parallel
    build.

--instrument
:   **[Windows only]**

    **[Java, C, C++, C#, and Visual Basic builds only]**

    Use the instrumentation mode instead of the debugger. For certain
    builds, this configuration can significantly improve build times. In
    particular, parallel builds will benefit most from
    `--instrument`.

    **Known issues and workarounds:**

    - If Visual Studio (2010 or newer) is running
      `Tracker.exe`, `cov-build`
      will skip running `Tracker.exe` by default.
      (The rest of the build will remain unaffected.) This
      behavior can be disabled with the
      `--no-disable-tracker`
      option.

      Alternatively, you can set the environment
      variable `COVERITY_TRACKER_WHITELIST` to
      specify those `Tracker.exe` binaries that
      should **not** be disabled. This environment variable is
      a semi-colon delimited list. For
      example:

      ```
      COVERITY_TRACKER_WHITELIST="C:\path1\Tracker.exe;C:\path2\Tracker.exe"
      ```

      If
      the environment variable is set as in the example above, the
      `cov-build` command will not disable the
      Tracker when it is run from
      C:\path1\Tracker.exe or
      C:\path2\Tracker.exe.
    - If `Tracker.exe` is permitted to run, you may
      run into a few known issues, which are outlined below.

      - The template compiler configuration can cause link
        failures in the build. To work around this issue,
        you can take either of the following actions:

        - Generate a non-template compiler
          configuration.
        - Disable file tracking in your build. If you use
          `msbuild` to build, you can disable
          the tracker by adding
          `/p:TrackFileAccess=false` to your
          command line. If you use `devenv`
          to build, you need to add the configuration value
          to your solution/project files.
    - If Visual Studio (2010 or newer) is running
      `Tracker.exe`:

      - The `cov-build` command issues a
        warning if it detects
        `Tracker.exe`.
    - The capture DLL will still be loaded for persistent
      processes, even after `cov-build` exits. One
      such example of a process like this is
      `mspdbsvr.exe`, which is a special case
      that is automatically ignored. However, if you find another
      binary that persists, you can ignore it by adding
      `--capture-ignore foo.exe` to the
      `cov-build` command line. It is important
      to note, however, that you can only ignore the process if it
      does not start any compilations.
    - The `--instrument` argument is incompatible
      with the __COMPAT_LAYER environment variable. If your
      environment sets this variable, you must unset it to use
      `--instrument`.

--log-server
:   **[Windows only]**

    **[C/C++ builds only]**

    This argument allows `cov-build` to produce a
    consistent build log when using `--parallel-emit`.
    All output in the build log can be attributed to specific executions
    of each Coverity program. This is the default.

    This argument has no effect to and cannot be used in combination with
    `--instrument`. You will receive an error
    message.

--minimal-classpath-emit
:   Limits the group of emitted JAR files to those needed for compilation
    of the Java files. The default behavior without this option is to
    emit all the JAR files in the classpath regardless of whether they
    are referenced by a Java file in the compilation. This option can
    improve performance of Java builds with large numbers of unused JAR
    files on the classpath at the risk of not capturing all the
    dependencies of the those JAR files. For example if
    `A.java` references `A.jar`, which
    has dependencies on `B.jar`, this option will prevent
    `B.jar` from getting emitted even if
    `B.jar` is on the classpath.

--msbuild-shutdown-maxnodes <N>
:   **[Windows only]**

    For Visual Studio 2010 and newer: Specifies the maximum number of
    nodes that `cov-build` should attempt to shut down.
    Typically, this value is equal to the number of nodes that your
    Visual Studio project is configured to use. Use this option only if
    the default behavior is undesirably slow.

--name <name>
:   Tags a build with a name. This name can then be used can be used for
    translation unit pattern matching through the
    `cov-manage-emit``build_name`
    argument.

--no-banner
:   Suppresses the `cov-build` application name and version
    banner from the console output.

--no-disable-tracker
:   **[Windows only]**

    This option allows the user to force `cov-build
    --instrument` to run `Tracker.exe`. By
    default, if Visual Studio (2010 or newer) is running
    `Tracker.exe`, then `cov-build
    --instrument` will skip running the
    tracker executable. The `--no-disable-tracker` option
    allows the user to bypass this skip.

    Note: This option may cause build issues. See the *Known Issues and
    Workarounds* section under the `--instrument` option.

--no-emit-complementary-info
:   Disables emitting of complementary information for compliance
    checkers such as MISRA checkers.

--no-error-recovery
:   Disables source-level error recovery in the parser. This typically
    should only be used if error recovery is causing problems and you
    have been instructed to use this option by Coverity support.

--no-log-server
:   **[Windows only]**

    **[C/C++ builds only]**

    This argument forces `cov-build` to revert to its
    original behavior without the log server, with respect to the build
    log. This is only intended for use when issues arise using
    `--log-server`.

--no-msbuild-shutdown
:   **[Windows only]**

    For Visual Studio 2010 and newer: Disables shutdown of resident
    msbuilds that are created by the Microsoft Build Engine,
    `msbuild`. Use this option only if you know that
    you will not have any msbuild processes running, or if you kill the
    resident msbuilds through some other method.

--no-parallel-translate
:   **[C/C++ builds only]**

    Disables `cov-translate` parallelization. This will
    prevent `cov-translate` from running in parallel
    regardless of the degree of parallelization requested, either
    directly to `cov-build`,
    `cov-translate`, through configuration files, or
    native command line translation.

    This can also be added as a `cov-emit` argument in a
    configuration file (it is not actually passed to
    `cov-emit`). For example:

    ```
    <prepend_arg>--no-parallel-translate</prepend_arg>
    ```

--no-preprocess-next
:   **[C/C++ builds only]**

    Disables the `--preprocess-next` option.

--no-refilter, -nrf
:   **[C/C++ builds only]**

    When combined with `--replay`, calls
    `cov-emit` directly with the previously
    translated command line arguments, instead of calling
    `cov-translate` again (which is the default).

    This option does not work with MSVC PCH.

--no-security-da
:   Disables the dynamic analysis - that is, the execution of
    `cov-security-da`- that is typically run at the
    end of the build. The results of the dynamic analysis are used for a
    security analysis.

--original-capture
:   **[Non-Windows only]**

    Fall back to using the original build capture method. A new capture method was made
    the default in Coverity 2025.12.0, and this option
    switches back to using the previous method. May be useful to work around
    issues with the new capture method if they arise, but generally should not be
    necessary; please contact support if using this option solves an issue
    so that the new method can be improved.

--parallel-emit
:   **[Windows only]**

    **[C/C++ builds only]**

    This argument will allow `cov-emit` processes to run
    in parallel. For certain builds, this argument can significantly
    improve build times. This argument is enabled by default (see
    `--serial-emit`).

    This argument has no effect and cannot be used in combination with
    `--instrument`. You will receive an error
    message.

--parallel-translate <number_of_processes>
:   **[C/C++ builds only]**
:   This argument instructs `cov-translate` to run
    `cov-emit` in parallel when multiple files are seen
    on a single native compiler invocation. This is similar to the Microsoft
    Visual C and C++ `/MP` switch. Specify the
    `<number_of_processes>` to be greater than zero to
    explicitly set the number of processes to spawn in parallel, or zero to
    auto-detect based on the number of CPUs. When specified directly to
    either `cov-build` or `cov-translate`,
    this option will override any settings set in configuration files or
    translated through the native command line.

    This can also be added as
    a `cov-emit` argument in a configuration file (it is
    not actually passed to `cov-emit`). For
    example:

    ```
    <prepend_arg>--parallel-translate=4</prepend_arg>
    ```

--parse-error-threshold <percentage>
:   The percentage of translation units that must successfully compile
    for the `cov-build` command to not generate a
    warning. If less than this percentage compiles, the
    `cov-build` command will give a warning when the
    build completes. The default value is 95.

    Note: When used in conjunction with
    `--return-emit-failures`,
    `cov-build` will return error code
    `8`, in addition to generating the warning, if
    less than the specified percentage compiled.

--preprocess-first
:   **[C/C++ builds only]**

    Uses the native compiler to preprocess source files and then invokes
    `cov-emit` to compile the output of the native
    processor. By default, `cov-emit` (which is invoked
    by `cov-build`) otherwise tries to preprocess and
    parse each source file.

    Using this option can address some cases in which hard-to-diagnose
    causes for macro predefinitions are different, or for header files
    that cannot be found by `cov-emit`. Usually,
    `cov-configure` attempts to intelligently guess
    the native compiler's predefined macros and built-in include
    directories, but sometimes `cov-configure` guesses
    incorrectly. Using the `--preprocess-first` option
    circumvents the problem, but at the cost of losing macro information
    during analysis. Using `--preprocess-first` does not
    always work because it requires rewriting the native compiler
    command line, which the native compiler may or may not like.

    See also, `--preprocess-next`.

--preprocess-next
:   **[C/C++ builds only]**

    Attempts to use `cov-emit` to preprocess source files.
    If that attempt fails, or if `cov-emit` encounters a
    parse error, this option preprocesses the files with the native
    preprocessor, and invokes `cov-emit` to compile the
    output of the native processor. This offers the benefit of using the
    higher-fidelity `cov-emit` preprocessor, while also
    providing a fallback in case of errors.

    This option can be disabled with
    `--no-preprocess-next` (the latter has precedence
    over the former). See `--preprocess-first` for information
    about the effects of using the native preprocessor.

--record-only, -ro
:   **[C/C++ builds only]**

    Only record the compiles done during the build, do not attempt to
    parse and emit the code. Later, `cov-build` can be
    rerun with `--replay` to actually parse and emit the
    code.

    Note: Note that you must not relocate your intermediate directory
    (specified with `--dir`) between the
    `--record-only` and `--replay`
    steps. If you need to move your intermediate directory to a new
    location or separate machine, use
    `--record-with-source` and
    `--replay-from-emit`.

--record-with-source, -rws
:   **[C, C++, C#, Visual Basic, Java, and Kotlin builds only]**

    For C and C++, compiles translation units far enough to pull in all
    the `#include` files needed by the compilation, and
    store these in the emit. Later, you can rerun
    `cov-build` with
    `--replay-from-emit` to actually parse and emit
    the code. See the entry for `--replay-from-emit` for
    more information and examples.

    Note that for Kotlin, recording with source is not supported when
    capturing builds using custom compiler plugins.

    This argument has no effect to and cannot be used in combination with
    either `--preprocess-first` or
    `--preprocess-next`. You will receive an error
    message.

--replay, -rp
:   **[C/C++ builds only]**

    Replay the parse and emit steps that were previously recorded for a
    build in the given intermediate directory. If you specify this
    option, do not specify a build command. This option can be used to
    quickly update a previously emitted build if the source files have
    changed.

    Note: Note that you must not relocate your intermediate directory
    (specified with `--dir`) between the
    `--record-only` and `--replay`
    steps. If you need to move your intermediate directory to a new
    location or separate machine, use
    `--record-with-source` and
    `--replay-from-emit`.

--replay-decomp
:   Decompile translation units from byte code source contained within
    the emit directory. Replaying from the emit will have the same
    results, regardless of changes to the files in the filesystem
    (including deletion).

    See also, `--defer-decomp`.

--replay-failures, -rpf
:   **[C/C++ builds only]**
:   Only attempt to replay the emit for files that had parsing or other
    compilation failures.

--replay-from-emit, -rpfe
:   **[C, C++, C#, Visual Basic, Java, and Kotlin builds only]**

    Recompile translation units from source contained within the emit
    directory. Replaying from the emit will have the same results,
    regardless of changes to the files in the filesystem (including
    deletion).

    This can be used when translation units were added with normal
    `cov-build` processes (although this will have no
    real effect unless `--force` has been passed), or
    with translation units added with
    `--record-with-source`.

    The advantage of using `--record-with-source` and
    `--replay-from-emit` is that temporary files
    (such as created by #import) are captured in the emit, and so
    projects that use `#import` can be replayed, which
    they cannot with `--replay`. In addition, it is
    possible to transport the intermediate directory to a different
    computer/platform and replay it there.

    For example, you can record a build on Windows and transfer the
    intermediate directory to Linux and replay it there. (You will have
    to use `cov-manage-emit reset-host-name` to change
    the host.)

    This argument has no effect to and cannot be used in combination with
    either `--preprocess-first` or
    `--preprocess-next`. You will receive an error
    message.

--replay-processes <count>, -j <count>
:   Spawn up to *count* processes in parallel on a single machine
    for replay tasks.

    - When performing `--replay`,
      `cov-emit` processes are spawned. [C/C++
      builds only]
    - When performing `--bazel`,
      `cov-translate` processes are spawned.
      Compatible with all languages supported by the Bazel-Coverity
      integration. If -j is not specified, the build
      uses -j auto by default.
    - When performing `--replay-from-emit`, additional
      processes are spawned depending on the languages used.
      Compatible with all languages supported by the
      `--replay-from-emit` option.

    This option accepts the number of processes, or `auto`
    which sets the number of replay processes to the number of logical
    processors in the machine (`-j 0` is also accepted
    and is the same as `auto`).

--return-emit-failures
:   The `cov-build` command returns with an error code if
    an emit failure occurs. The return value is a combination (binary
    `OR`) of the following flags:

    - 1: The build returned an error code.
    - 2: The build terminated with an uncaught signal (for example,
      segmentation fault).
    - 4: No files were emitted.
    - 8: Some files failed to compile. By default, this error code
      is returned if fewer than 95% of the compilation units
      compiled successfully. You can change this percentage by
      using the `--parse-error-threshold`
      option.

    Note: The `cov-build` command always returns an error
    code if the native build fails.

--serial-emit
:   **[Windows only]**

    **[C, C++, C# and Visual Basic builds only]**

    This argument forces `cov-emit` processes to run in
    serial. This option is disabled by default (see
    `--parallel-emit`).

    This option has no effect and cannot be used in combination with
    `--instrument`. Attempts to use the two options
    together will result in an error message.

--system-encoding <enc>
:   **[C/C++ builds only]**
:   Specifies the encoding to use when interpreting command line arguments and file names. If
    not specified, a default system encoding is determined based on host OS
    configuration.

    See `--encoding` for a list of accepted
    encoding names.

    This option has no effect when used in
    conjunction with one of the `--replay` options.

## Shared options

--config <coverity_config.xml>

-c <coverity_config.xml>
:   Uses the specified configuration file instead of the default configuration
    file located at 
    <install_dir>/config/coverity_config.xml.

--debug

-g
:   Turn on basic debugging output.

--debug-flags <flag> [, <flag>, ...]
:   Controls the amount of debugging output produced during a build. These
    flags can be combined on the command line using a comma as a
    delimiter.

    Valid flags are `build`, `capture`,
    `translate`, `translate-phases`. For
    example, `--debug-flags build, translate`.

--ident
:   Displays the version of Coverity Analysis and build number.

--redirect stdout|stderr,<filename>

-rd stdout|stderr,<filename>
:   Redirects either the `stdout` or the `stderr`
    stream to the specified file.

--tmpdir <tmp>

-t <tmp>
:   Specifies the temporary directory to use.

    - On UNIX, the default is `$TMPDIR`, or
      `/tmp` if that variable does not exist.
    - On Windows, the default is to use the temporary directory specified
      by the operating system.

--treat-as-64bit <exe-name>
:   **[Deprecated]**

    This option is deprecated as of version 8.7 and has no effect.

--verbose <0, 1, 2, 3, 4>

-V <0, 1, 2, 3, 4>
:   Set the detail level of command messages. Higher is more verbose (more
    messages). Defaults to 1.
