---
title: "CovRunDesktopSettings"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/covrundesktopsettings.html"
content_id: "dVtpfmmK0lLktDSafz9ojw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:17.892547+00:00"
---

# CovRunDesktopSettings

The `CovRunDesktopSettings` class carries settings specific to the
`cov-run-desktop` program. It has the following attributes:

allow_suffix_match?: bool
:   When true, `cov-run-desktop` behaves as if
    `--allow-suffix-match` were passed on the command line.
    This option is only recommended for enhanced backward compatibility.

analysis_args?: string[]
:   Arguments that `cov-run-desktop` should treat as if they appeared on its
    command line with the purpose of altering the behavior of the underlying
    analysis. This can be used to cause desktop analysis to use different
    options from the full, central analysis, although that is not the
    recommended usage.

    If relative file names appear in these arguments, they
    will be interpreted as relative to the code_base_dir.

build_cmd?: string[]
:   A command line, as a sequence of shell words, that will invoke a build. This is run by
    "`cov-run-desktop --build`".

build_encoding?: string
:   A string to use as the argument to `cov-build --encoding` during build
    capture. The source_encoding option is preferred if all source code uses the
    same character encoding, but this option takes precedence for build capture
    when both are specified.

build_record_with_source?: bool
:   When true, `--record-with-source` is passed to `cov-build`.
    The default is `false`.

build_options?: string[]
:   A sequence of additional option words to pass to `cov-build`. The sequence
    of words must form a valid option and argument sequence for
    `cov-build`.

    For example:

    ```
        "build_options": [
            "--encoding", "UTF-8",               
            "--append-log",
            "--capture-ignore", "NTVDM.EXE"
          ]
    ```

checkers?: <Checkers>
:   `Checkers` then defines 
    `CheckerSettings`
     specific to the operation of cov-run-desktop.

    An example of the
    checkers and extend_checkers class is:

    ```
    {
      // other cov-run-desktop settings...
      "checkers": {
        "ARRAY_VS_SINGLETON": {
          // inherit enabled value from tools or stream by not specifying the "enabled" property
          "options": {
            "stat_cutoff": 7
          }
        },
        "BAD_FREE": {
          "enabled": false
        }
      },
      "extend_checkers": {
        "MY_CUSTOM_CHECKER": {
          "enabled": true,
          "options": {
            "O": 3
          }
        }
      }
    }
    ```

clean_cmd?: string[]
:   A command line (word sequence) that will clean the build. This is used by
    "`cov-run-desktop --clean`".

coding_standard_configs?: string[]
:   This accepts a list of strings, since this option can be specified multiple times on the
    command line. Provides the path(s) to configuration file(s) for a coding
    standard to run as part of the analysis. This option is required to enable
    C/C++ MISRA analysis. It can also be used for enabling other standards, such
    as CERT-C and AUTOSAR, see the description of the
    `--coding-standard-config` option to the
    `cov-analyze` command for more information.

extend_checkers?: <Checkers>
:   `Checkers` then defines 
    `CheckerSettings`
     specific to the operation of
    `cov-run-desktop`.

fs_capture_build_options?: string[]
:   Like build_options but used when `cov-run-desktop` invokes
    `cov-build` to automatically capture files with
    filesystem capture.

    Note:
    The `fs_capture_build_options` setting has been deprecated, and support for it will be
    discontinued in a future release of Coverity Analysis.

ignore_all_files_regex?: regex
:   A regex to be treated like the argument to `cov-run-desktop
    --ignore-all-files-regex`. This is meant for use with all modes
    (`--analyze-captured-source`, `--analyze-scm-modified`,
    or explicit file list) in order to exclude certain files from the analysis scope.

    Note: The files matching this regex may still be included if they are referenced
    from other files included in the analysis scope.

ignore_modified_file_regex?: regex
:   A regex to be treated like the argument to `cov-run-desktop
    --ignore-modified-file-regex`. This is meant for use with the
    `--analyze-scm-modified` switch in order to avoid trying
    to analyze things that are not actually source code files.

ignore_uncapturable_inputs?: bool
:   Corresponds to the `--ignore-uncapturable-inputs` option to
    `cov-run-desktop`. This option is not recommended for
    general use because it can hide errors that would be revealed in the process
    of more thoughtful configuration.

restrict_all_files_regex?: regex
:   A regex to be treated like the argument to `cov-run-desktop
    --restrict-all-files-regex`. This is meant for use with all modes
    (`--analyze-captured-source`, `--analyze-scm-modified`,
    or explicit file list) in order to avoid trying to exclude certain files from the analysis scope.

    Note: The files matching this regex may still be included if they are referenced
    from other files included in the analysis scope.

restrict_modified_file_regex?: regex
:   A regex to be treated like the argument to `cov-run-desktop
    --restrict-modified-file-regex`. This is meant for use with the
    `--analyze-scm-modified` switch in order to avoid trying
    to analyze things that are not actually source code files.

reference_snapshot?: string
:   Corresponds to the `cov-run-desktop --reference-snapshot` option.

    The
    default value is "idir-date".

source_encoding?: string
:   A string to use as the argument to `cov-build --encoding`, both during
    build capture and filesystem capture.

specific_files_build_cmd?: string[]
:   Specifies a command, typically a custom script, that can compile uncaptured files on
    demand. The command will be executed with `$(code_base_dir)`
    as the current directory and source files added to the end of the command,
    as paths relative to that directory or as absolute paths. See "Compiling
    files on demand" for details.

specific_files_build_options?: string[]
:   Like build_options but used when `cov-run-desktop` invokes
    `cov-build` with the
    `specific_files_build_cmd`. When unspecified, any
    settings in `build_options` are used.

specific_files_regex?: regex
:   When specified, specifies a pattern that files must match in order to attempt
    auto-compilation with `specific_files_build_cmd`. For
    example, if the command can only compile C and C++, the regex might be
    `\\.(c|cpp)$` to avoid attempting to compile header files
    or source code from other languages. When this option is unspecified, all
    specified files for analysis not previously captured with build capture and
    not captured with filesystem capture will be passed to
    `specific_files_build_cmd`. See "Compiling files on
    demand" for details.
