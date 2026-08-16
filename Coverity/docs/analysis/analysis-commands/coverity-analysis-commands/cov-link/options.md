---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "nULfRnJbZp48SZJpag~2IA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:37.419188+00:00"
---

# Options

## Input options

You must specify one of the following options. You must not use both together.

--collect, -co
:   Collects linkage information from all of the entries in an emit
    repository.

<link_file>
:   Specifies which source files are linked together. You can specify
    multiple link files.

## Filter options

These options are not required but can be specified multiple times.

--compile-arg <arg>, -a <arg>
:   Specify an argument that was given when compiling the files on the
    command line.

--compile-arg-regex <regex>, -r <regex>
:   Specify an argument that was given when compiling the specified files, as
    a Perl regular expression.

--no-compile-arg <arg>, -na <arg>
:   Specify an argument that was NOT given when compiling the files on the
    command line.

--no-compile-arg-regex <regex>, -nr <regex>
:   Specify an argument that does NOT match any argument given when compiling
    the files on the command line, as a Perl regular expression.

--source-file-regex <source_file_regex>, -s <source_file_regex>
:   Specify a portion of the source file pathname that was used during
    compilation, as a Perl regular expression. You can use a forward slash
    (`/`) as a directory separator in this string, for
    example `/proj1/` matches if `proj1` is a
    directory that is in the pathname. Note that on Windows, the matching is
    case-insensitive, and (`/`) is used as the directory
    separator (not `\`). You can specify this option more
    than once (as in `-s <source_file_regex> -s
    <source_file_regex`>). If there are several
    `-s` options, the source file's name only needs to
    match one of the specified expressions.

## Output options

You must specify one of the following options. You must not use both together.

--output-dir <output_dir>, -odir <output-dir>
:   Specifies an intermediate directory for the `cov-link`
    command to create. If you use this option, you must also use the
    `--dir` option to this command.

    Note that the `--dir` option to the
    `cov-analyze` command will use the specified
    `<output_dir>` as its value.

--output-file <output-file>, -of <output-file>
:   Specifies the pathname to the link file that is created. If you use
    `--collect`, any existing file with this name is
    replaced. If you specify `--source-file-regex`, any
    existing file with this name is appended to.

    If you use this option, you must also use the `--dir`
    option to this command.

## Shared options

--dir <intermediate_directory>
:   Path name to an intermediate directory that is used to store the results of
    the build and analysis. This option is required.

--ident
:   Displays the version of Coverity Analysis and build number.

--verbose <0, 1, 2, 3, 4>

-V <0, 1, 2, 3, 4>
:   Set the detail level of command messages. Higher is more verbose (more
    messages). Defaults to 1.
