---
title: "Options: Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options-analysis.html"
content_id: "UCuKOcgZuXlTKn8OL~jFLg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:32.475768+00:00"
---

# Options: Analysis

--allow-unmerged-emits
:   By default, the analysis fails if an intermediate directory contains emits of
    builds from multiple hosts. Specify this option to disable error checking
    and permit the analysis to continue in these cases.

    If you use `cov-manage-emit add-other-hosts` to associate
    all emit repositories in the current intermediate directory with the current
    host, `--allow-unmerged-emits` is not needed to continue the
    analysis.

--append
:   Append defects from the last analysis run to the defects from this run.

    By default, each analysis run includes individual checker-result files, the
    analysis summary file, and a metrics file. The `--append`
    option adds analysis results to the individual checker-result and summary
    files, but leaves the metrics file unchanged. So when you use the
    `--append` option, the metrics file will reflect the
    initial analysis without incremental analysis results for subsequent
    analyses that use the `--append` option.

    The `--append` option is intended for appending issues found
    by custom Extend SDK checkers (see Coverity Extend SDK 2026.6.0 Checker Development Guide)
    and for importing issues by the 
    `cov-import-results`
     and 
    `cov-import-msvsca`
     commands. This option does not allow multiple
    `cov-analyze` commands with standard checkers to write
    results into the same intermediate directory. To analyze a mixed-language
    code base, use a single `cov-analyze` invocation.

    When this option is used with the `--output-tag` option,
    `--append` applies to the output location that is
    specified through `--output-tag`.

--cluster-config <host-config-file>
:   When used with `cov-analyze`, the
    `--cluster-config` option specifies a configuration that
    uses multiple hosts, in order to distribute analysis among more than one
    server.

    For example, `--cluster-config` can specify an
    `"ssh-config"` file (in JSON format). The file describes
    the configuration of one or more SSH-based remote worker systems. See the
    section "Using remote worker jobs to manage resource constraints"
    in the Coverity Analysis 2026.6.0 User and Administrator Guide.

--code-identity-file <file>
:   The name of a code identity file, when required by the license. This file
    contains information about which files to include and/or exclude from line
    counts and analysis, as well as a signature of the licensed code base. The
    inclusions and exclusions are based on settings to --search, --search-extensions, and --third-party-regex in 
    `cov-count-lines`
    . The code identity file should match the signature indicated by the
    optional string parameter `cbi_hash` in the license file.

    When required by the license, `cov-analyze` searches for a
    matching file with a cbi extension in the following
    locations:

    - The directory from which `cov-analyze` is
      invoked.
    - The bin/ subdirectory of the Coverity Analysis
      installation directory.
    - The file specified by `--code-identity-file` (if
      provided).

    Note that for licenses requiring a code identity file, `--strip-path` must be
    provided. See also the `--code-identity_file` option to
    `cov-count-lines`.

--code-version-date <date>
:   For Desktop Analysis, use this option to specify the date of the source code.
    This date is used for impact analysis. If possible, it is recommended to use
    the SCM checkout date of the code being analyzed.

    If this option is not specified, the products will use the latest invocation
    timestamp of `cov-build` as stored in the intermediate
    directory. If that is not available, then the current date and time are used
    instead.

    This option is required when analyzing historical versions of your source
    code.

    The value of date must follow one of the following
    formats:

    - `YYYY-MM-DD` - Specifies a date. Midnight, local
      time zone.
    - `YYYY-MM-DD[ T]hh:mm(:ss)?` - Specifies a date and
      time of day. Local time zone.
    - `YYYY-MM-DD[ T]hh:mm(:ss)?Z` - Specifies a date
      and time. *Z* is the zone designator
      for the zero UTC offset, also known as "Zulu time".
    - `YYYY-MM-DD[ T]hh:mm(:ss)?[+-]hh:mm` - Specifies
      the date, time, and time zone. The offset
      (`[+-]`) explicitly sets the time zone.

    Note: Dates before 1970 are not allowed.

    **Examples:**

    ```
    2019-07-01                Midnight on July 1, 2019, local time zone
    2019-07-01 13:00          1pm on July 1, 2019, local time zone
    2019-07-01T13:00:30       30 sec after 1pm on July 1, 2019, local time zone
    2019-07-01 13:00Z         1pm on July 1, 2019, UTC time zone
    2019-07-01 13:00-07:00    1pm on July 1, 2019, Pacific Daylight Time
    2019-07-01T13:00-08:00    1pm on July 1, 2019, Pacific Standard Time
    2019-07-01T13:00+09:00    1pm on July 1, 2019, Japan Standard Time
    ```

--cra
:   Enable EU Cyber Resilience Act (CRA) analysis mode.

--derived-model-file <derived_file.xmldb>
:   [Deprecated as of version 7.7.0] This option will be removed and replaced in
    a future release. Use --model-file instead.

--dir <intermediate_directory>
:   Path name to an intermediate directory that is used to store the results of
    the build and analysis. This option is required.

--disable-scan-transparency-data
:   Disables generation of data for *scan transparency*.

    For further information, see
    the `--enable-scan-transparency-data` option.

--enable-constraint-fpp
:   Enables additional filtering of potential defects by using an additional
    false-path pruner (FPP). This option can increase the analysis time up to
    20% (normally much less), but decrease the number of false positives that
    occur along infeasible paths. Because this FPP uses a different method for
    pruning false positives, it is possible that a very small number of true
    positives are pruned as well.

    Note that use of this option requires an *additional* 200MB of memory
    per worker.

    Starting in version 7.0, this option applies to C, C++, C#, Visual Basic, and
    Java.

--enable-scan-transparency-data
:   Enables generation of data for *scan transparency*.

    When scan transparency is enabled, Coverity Analysis gathers information that can help with improving configuration,
    such as which functions might need user models or which defect annotations were unused.
    For more information, see "Enabling collection of scan transparency data"
    in the Coverity Platform 2026.6.0 User and Administrator Guide.

    Scan transparency is enabled by default.

--export-summaries <true|false>
:   Collects function summary data for the analysis. The collected data provides
    interprocedural analysis information for Desktop Analysis users, and must be
    committed to any stream that is used by Desktop Analysis.

    This option is `true` by default.

--force
:   Turns off incremental analysis. This setting forces a full re-analysis of the
    source, even if the source file or other source files on which it depends
    have not changed since it was previously analyzed.

--hibernate-config
:   Specifies a directory that contains Hibernate mapping XML files, if
    applicable. Pertains to the "HIBERNATE_BAD_HASHCODE" checker (see the Coverity 2026.6.0 Checker Reference for details).

--ignore-deviated-findings
:   Set this option to prevent reporting defects that are deviated with
    annotations.

    Any defects or false positives annotated using the #pragma Coverity
    compliance directive will be suppressed and will not be reported by Coverity
    Connect. *All* recorded deviations in the current project version are
    then written to a CSV file. For more information see "Annotating compliance deviations" in the Customizing Coverity book.

--jobs <number-of-workers> | auto | max<number-of-workers>

-j <number-of-workers> | auto | max<number-of-workers>
:   Allows you to control the number of analysis workers that run in parallel,
    subject to any limits specified by your license. Starting in version 7.6.0,
    the need to use this option should be rare because the default typically
    sets the appropriate number of workers to use for your hardware, license,
    and analysis task. Note that the default for this option varies by
    license.

    - Default for a non-FlexNet license (license.dat):
      `--jobs` auto
    - Default for a FlexNet license: -`-jobs max8`

    In general, the analysis runs faster with more threads, but the scalability
    of that speed increase depends on the kind of analysis, the code
    language(s), and other properties of the code base. In general, analysis of
    C code parallelizes best, followed by C++, followed by C#, Visual Basic, and
    Java quality analysis, followed by Web application security analysis, which
    is largely not parallelized.

    This option must specify one of the following values:

    - `<number-of-workers>`: Specifies number of analysis workers
      to run in parallel.

      Example: `--jobs 8`

      The specified number of workers is not allowed to exceed suggested limits for
      your hardware unless you also use the --override-worker-limit option.
    - `auto`: Automatically determines the number of workers to use.
      Hardware detection through `--jobs` auto attempts to optimize for
      the case where the analysis has full or nearly-full use of the machine's
      computational resources (memory and CPU). If that is not the case, you should
      consider setting -j explicitly, for example, where the analysis occupies one of
      several "executors" on a continuous integration server.

      Example: `--jobs auto`

      If `--jobs auto` is set, the analysis will determine the number of
      workers to run based on the minimum of the following:

      - The largest number of workers that keeps the recommended minimum physical
        memory requirements below the actual physical memory of the machine.
      - The number of logical CPUs, or virtual cores, on the machine. This is the
        number of threads or processes that the operating system can schedule
        simultaneously on the hardware.
      - Six (6) times the number of "physical" CPU cores, when known.
      - 48: Coverity has not found performance improvements from using more than
        48 workers, and using more might reach limits on open file descriptors,
        and so on.
      - The number permitted by the license or available for FlexNet
        checkout.

      Detection of memory and logical CPUs should work on all analysis platforms, but
      detection might fail or produce incorrect results in some virtualization
      environments.

      This value is not compatible with the `--override-worker-limit`
      option.
    - `max<number-of-workers>`: Limits the number of analysis
      workers that can run in parallel based on the maximum you set and the amount of
      memory and number of cores that are available.

      Example: `--jobs max8`

      This value is not compatible with the `--override-worker-limit`
      option.

    See "Parallel analysis" in the Coverity Analysis 2026.6.0 User and Administrator Guide for
    guidance.

    For backward compatibility, the `--j
    <number-of-workers>` syntax is still supported in this
    release.

--max-loop <num>
:   Limits the maximum number of times that loops are traversed. The default
    limit is 32, which should be encountered rarely. -1 means unlimited.

--max-mem <value>
:   Sets the maximum amount of memory, in megabytes, that a single analysis
    worker process will use for the core analysis. The total memory required is
    approximately the product of the `--max-mem` and
    `-j` options. The default value is 512.

    The worker will use some additional memory for miscellaneous purposes, and
    even more memory if you use `--enable-constraint-fpp` or
    enable INTEGER_OVERFLOW.

    The analysis will reject a setting that is too large for the available
    physical memory and number of workers.

    On 32-bit Windows systems, do not set <value> to more than 512
    megabytes.

    Note: An out-of-memory error indicates that the analysis is trying to use more memory than is
    available to the system. If an out-of-memory error occurs, use the
    `--max-mem` option to *decrease* the amount of
    memory that the analysis is allowed to use.

    Note that JVM
    `max-mem` options work in the opposite way. So it is
    necessary to *increase* (not decrease) the max-mem for
    out-of-memory errors related to the JVM. In this case, it is possible
    that the system will run out of memory in the JVM.

--no-log
:   Disables logging.

--one-tu-per-psf <true|false>
:   When set to true, analyzes exactly one translation unit (TU) found for a
    given primary source file (psf) name. If there is more than one TU for a
    primary source file, the analysis will pick a single TU using an algorithm
    that is intended to ensure consistency between analysis runs. However, if
    the build command lines change, the analysis might make different choices
    and the results might vary, even though the code appears to be unchanged. A
    false value enables analysis of all TUs, regardless of primary source file
    duplication. The default value is `true`.

--output-tag <name>
:   Specifies a non-default location within the intermediate directory for the results of one or more
    analyses. The name can be anything you choose, using characters allowed in
    file names. When specified *without* the `--append
    option`, prior results found in that location are replaced. When
    specified *with*
    `--append`, new results are added to the result set.

--override-worker-limit
:   Allows you to specify a value to `-j` that is greater than the recommended value.
    This option can be useful when the license allows more workers than the
    number of cores in the machine.

--path-log-threshold <number>
:   If a function has more than <number> paths, this count is output to the
    log file.

--paths <number>
:   Sets the upper limit on the number of paths to traverse for each function.
    Default is 5000.

--preview
:   This option has been deprecated. For backwards compatibility, this option
    enables the same checkers that it used to.

--print-paths
:   Prints the number of paths explored for each analyzed function.

@@<response_file>
:   Specify a response file that contains a list of additional command line
    arguments, such as a list of files for analysis. Each line in the file is
    treated as one argument, regardless of spaces, quotes, etc. The file is read
    using the platform default character encoding. Using a response file is
    recommended when the list of input XML files is long or automatically
    generated.

    Optionally, you can choose a different encoding, by specifying it after the
    first "@". For example:

    ```
    cov-analyze [OPTIONS] @UTF-16@my_response_file.txt
    ```

    You must use a supported Coverity encoding, listed under the 
    `cov-build --encoding`
     option.

--security-file <license file>

-sf <license file>
:   Path to a valid Coverity Analysis license file. If not specified, this path is given by the
    `security_file` tag in the Coverity configuration or by
    license.dat (located in the Coverity Analysis
    <install_dir>/bin directory). A valid license
    file is required to run the analysis.

--strip-path <path>

-s <path>
:   Strips leading directory names from file paths that
    appear in error messages and in references to your source files.

    The leading portion of the path is omitted if it matches a value
    specified by this option. For example, if the actual full path name of a
    file is /test/me/sourceFile.c, and
    `--strip-path /test` is specified, then the name
    attribute for the file becomes
    /me/sourceFile.c.

    The `--strip-path string` can include more than one
    directory name. Also, you can specify the `--strip-path`
    option multiple times. If more than one `--strip-path` is
    present, Coverity uses the longest of these. (Coverity does not attempt
    to use more than one of the specified path prefixes.)

    For example, suppose that you specify the following:

    ```
    --strip-path /a --strip-path /b --strip-path /b/c
    ```

    ... then `--strip-path` would condense paths in the
    following way:

    Table 1. Results of using `--strip-path`

    | Original path | Stripped path | Notes |
    | --- | --- | --- |
    | a/fname | /fname |  |
    | a/b/fname | /b/fname | In this case, /b was not a leading directory name in the path. |
    | b/fname | /fname |  |
    | b/c/fname | /fname |  |

    Important: We recommend using this option for a number of
    reasons:

    - Failure to use this option can result in poor Coverity Connect
      performance, triage issues related to component maps, an
      unnecessary increase the size of the Coverity Connect database,
      and even incorrect LOC counts.
    - This option shortens paths that Coverity Connect displays. It
      also allows your deployment to be more portable if you need to
      move it to a new machine in the future.
    - In addition, using this option during the analysis, rather than
      when committing the analysis results to Coverity Connect, can
      enhance end-to-end performance of the path stripping process
      itself.

    Linux example:

    ```
    > cov-analyze --dir myDir --strip-path=`pwd`
    ```

    Windows example:

    ```
    > cov-analyze --dir myDir --strip-path=%cd%
    ```

    In the less common case, the option should specify the root of your build
    tree.

--ticker-mode <mode>
:   Set the mode of the progress bar ticker. The available modes are:

    none
    :   No progress bar is displayed.

    no-spin
    :   Only the print stars are displayed; the spinning bar is
        not.

    spin
    :   This is the default mode. Stars with a spinning bar at the
        end are displayed. Each file, function, or defect committed
        corresponds to steps of spin.

--tu <translation_unit_id(s)>

-tu <translation_unit_id(s)>
:   Limits the scope of `cov-analyze` to a set of translation
    units (TUs), named by their numeric ID attribute(s). A translation unit
    approximately maps to the output from a single run of a compiler.

    This option requires a comma-separated list of id(s), and
    `--tu` can be specified multiple times. The union of all
    these identifier sets is the set of TUs to operate on subsequently, for
    operations that work on TUs.

    Even when using the `--tu` or `--tu-pattern`
    options, you must specify the `--analyze-node-modules` option
    in order to analyze translation units in node_modules.

    It is an error if any of the specified IDs do not correspond to any existing
    translation unit. To get the IDs for translation units, use the
    `cov-manage-emit`
    list
    sub-command.

    You can use the `--tu` and `--tu-pattern`
    options together.

--tu-pattern <translation_unit_pattern>

-tp <translation_unit_pattern>
:   Limits the scope of `cov-analyze` to a set of translation
    units specified with a translation unit pattern. The
    `--tu-pattern` option can be specified multiple times.
    Matching TU sets are unioned together across all patterns.

    Both `--tu` and `--tu-pattern` can be specified
    on a single command line. The final set of TUs operated upon includes a
    given TU if it matches any specified translation unit pattern or its ID is
    listed explicitly as an argument to `--tu`.

    Even when using the `--tu` or `--tu-pattern`
    options, you must specify the `--analyze-node-modules` option
    in order to analyze translation units in node_modules.

    It is an error if at least one `--tu-pattern` argument is
    specified but no translation unit matches any of the specified patterns.

    You can get useful information on TUs by using the
    `cov-manage-emit`
    list
    sub-command.

    See Translation unit matching for more information. Detailed examples can also be found in
    Coverity Analysis > Coverity Analysis Usage > Analysis with
    Coverity Checkers > Setting up Coverity Analysis for a production environment >
    Integrating Coverity Analysis into a build system > Integrating Coverity Analysis into the build environment
    > Getting linkage information.

--user-model-file <user_file.xmldb>
:   [Deprecated as of version 7.7.0] This option will be removed and replaced in
    a future release. Use --model-file instead.

--wait-for-license
:   Indicates that if a license cannot be obtained from the license server,
    `cov-analyze` must wait until a license becomes
    available. After a license becomes available, `cov-analyze`
    acquires it and proceeds with the analysis. This option is ignored if
    `cov-analyze` does not use a floating-node license.
