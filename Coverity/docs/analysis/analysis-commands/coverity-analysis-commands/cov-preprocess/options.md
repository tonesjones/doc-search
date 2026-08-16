---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "lRTIDTMKo0pGaJs6S_QWiA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:00.524938+00:00"
---

# Options

--config <coverity_config.xml>

-c <coverity_config.xml>
:   Uses the specified configuration file instead of the default configuration
    file located at 
    <install_dir>/config/coverity_config.xml.

--diff

-d
:   Preprocess the file with both the native compiler and with
    `cov-emit`, and then attempt to find relevant
    differences between the preprocessed files using some heuristics.

--diff-only
:   Determine the relevant differences between two files that are already
    preprocessed using some heuristics.

--dir <intermediate_directory>
:   Path name to an intermediate directory that is used to store the results of
    the build and analysis. This option is required.

-if <source_file>
:   Specify an input file that is preprocessed as if it were the file that was
    compiled.

--native
:   Preprocess with the native compiler instead of with
    `cov-emit`.

--no-lines

-n
:   Do not put #line directives in the preprocessed output file.

--no-retranslate

-nr
:   Do not re-translate the command line from the original compiler when
    attempting to preprocess with `cov-emit`. This can be
    faster, but it will not work with template compiler configurations.

--output-file <output-file>, -of <output_file>
:   Specify the path to and file name for the output file. Coverity recommends
    that you use this option instead of relying on the default output
    behavior.

--tu <translation_unit_id(s)>, -tu <translation_unit_id(s)>
:   A set of translation units (TUs), named by their numeric id attribute(s). A
    translation unit approximately maps to the output from a single run of a
    compiler. This option requires a comma-separated list of id(s), and
    `--tu` may be specified multiple times. The union of all
    these identifier sets is the set of TUs to operate on subsequently, for
    operations that work on TUs. It is an error if any of the specified IDs do
    not correspond to any existing translation unit.

## Shared options

--debug

-g
:   Turn on basic debugging output.

--ident
:   Displays the version of Coverity Analysis and build number.

--info
:   Displays certain internal information (useful for debugging), including the
    temporary directory, user name and host name, and process ID.

--tmpdir <tmp>

-t <tmp>
:   Specifies the temporary directory to use.

    - On UNIX, the default is `$TMPDIR`, or
      `/tmp` if that variable does not exist.
    - On Windows, the default is to use the temporary directory specified
      by the operating system.

--verbose <0, 1, 2, 3, 4>

-V <0, 1, 2, 3, 4>
:   Set the detail level of command messages. Higher is more verbose (more
    messages). Defaults to 1.
