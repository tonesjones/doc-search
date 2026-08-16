---
title: "Translation unit sub-commands with optional filtering"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/translation-unit-sub-commands-with-optional-filtering.html"
content_id: "ZNTzl5kjzRDHo86RXozVBA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:48.159453+00:00"
---

# Translation unit sub-commands with optional filtering

The following filtering sub-commands work on translation units. By default, all translation
units are included in the results. You can optionally restrict the translation units
used in these operations with the `--tu` and/or
`--tu-pattern` options.

The options for listing emit
database information and recompiling also support restricting the translation units with the
`--tu` and/or `--tu-pattern` options.

add <int_dir>
:   Add (copy) all translation units from a specified intermediate directory
    (`<int_dir>`) into the current one (the one
    specified with the `--dir` option). If `--tu`
    and/or `--tu-pattern` are specified, then those filters are
    interpreted as applying to the source emit, and only the matching subset is
    copied.

    CAUTION:

    Combining intermediate directories can cause defect reports to appear
    or disappear, because the information in one intermediate directory can affect the
    information in another.

link-file <out_file>
:   Create a file (`<out_file>`) with a description of the specified translation
    units as a link file, which can be used as input to
    `cov-link`.

list
:   List all translation units in the intermediate directory. Each translation
    unit is identified by its numeric ID, which is listed along with its primary
    source file name.

list-capture-invocations
:   For each emitted translation unit (TU) and link unit (LU) that is not
    filtered-out by command line options, this command produces JSON formatted
    UTF-8 encoded output that describes the captured build invocations, recorded
    process invocations, cov-emit and/or
    cov-emit-link invocations generated for each
    compilation or linker action, and select input and output files and their
    kind (for example, C source file, object file, static library).

    **Command syntax**

    ```
    cov-manage-emit <GENERAL OPTIONS> list-capture-invocations <COMMAND OPTIONS>
    ```

    where `<COMMAND OPTIONS>` specific to this command
    are:

    - --no-process-details

      Omit all cov-build,
      cov-translate,
      cov-emit-
      * process invocation details. This option
      reduces the output to translation units, link units, and their
      associated files.

    **Output format**

    The JSON output is a single object that contains members with values that
    denote metadata (type, version information), process invocation, TU or LU
    data. The root object members are:

    - `type:` A constant string that contains "Coverity
      Capture Invocations". For
      example:

      ```
      "type": "Coverity Capture Invocations"
      ```
    - `version:` A string that contains the Coverity version
      that produced the JSON file. For
      example:

      ```
      "version": "2021.06"
      ```
    - `files:` An array that associates IDs with paths used
      to name a file or directory. Both case-normalized and case-preserved
      paths are provided. For example:

      ```
      "files": [
        {
          "id": 1,
          "case-normalized": "/path/to/file.cpp",
          "case-preserved": "/Path/to/File.cpp"
        }
      ]
      ```
    - `environment-variables:` An array that associates IDs
      with names and values for environment variables. For
      example:

      ```
      "environment-variables": [
        {
          "id": 1,
          "name": "VAR",
          "value": "Value"
        }
      ]
      ```
    - `environment-variable-blocks:` An array that
      associates IDs with sets of environment variable IDs. Processes
      spawned with the same set of environment variables share an
      environment variable block. For
      example:

      ```
      "environment-variable-blocks": [
        {
          "id": 1,
          "environment-variable-ids": [ 1, 2, 6 ]
        }
      ]
      ```
    - `cov-build-invocations:` An array that associates IDs
      with build process invocations. For
      example:

      ```
      "cov-build-invocations": [
        {
          "id": 1,
          "process-invocation": {
            "hostname": "skippy",
            "pid": 1234,
            "start-time": "2021-03-15T11:35:12Z",
            "end-time": "2021-03-15T11:35:14Z",
            "exit-code": 0,
            "platform": "Linux x86_64",
            "username": "sadie",
            "command-line": [ "cov-build", "--dir", "covint", "make" ],
            "working-directory-id": 1,
            "environment-variable-block-id": 1,
          }
        }
      ]
      ```
    - `cov-translate-invocations:` An array that associates
      IDs with `cov-translate` process invocations. For
      example:

      ```
      "cov-translate-invocations": [
        {
          "id": 1,
          "process-invocation": { ... }
        }
      ]
      ```
    - `cov-emit-invocations:` An array that associates IDs
      with `cov-emit` or
      `cov-internal-emit-clang` process invocations.
      For example:

      ```
      "cov-emit-invocations": [
        {
          "id": 1,
          "process-invocation": { ... }
        }
      ]
      ```
    - `cov-emit-cs-invocations:` An array that associates
      IDs with `cov-emit-cs` invocations.
    - `cov-emit-fortran-invocations:` An array that
      associates IDs with `cov-emit-fortran`
      invocations.
    - `cov-emit-go-invocations:` An array that associates
      IDs with `cov-emit-go` invocations.
    - `cov-emit-java-invocations:` An array that associates
      IDs with `cov-emit-java` invocations.
    - `cov-emit-rust-invocations:` An array that associates
      IDs with `cov-emit-rust` invocations.
    - `other-emit-invocations:` An array that associates IDs
      with `cov-emit-misc` invocations.
    - `cov-emit-link-invocations:` An array that associates
      IDs with `cov-emit-link` process invocations. For
      example:

      ```
      "cov-emit-link-invocations": [
        {
          "id": 1,
          "process-invocation": { ... }
        }
      ]
      ```
    - `translation-units:` An array that associates IDs with
      sets of properties that describe translation units, including
      associated process invocations and input files. For
      example:

      ```
      "translation-units": [
        {
          "id": 1,
          "cov-build-invocation-id": 1,
          "cov-translate-invocation-id": 1,
          "cov-emit-invocation-id": 1,
          "emit-failed": false,
          "kind": "C++",
          "primary-file-id": 1,
          "input-files": [
            {
              "file-id": 1,
              "kind": "source file",
              "implicit": false
            }
          ]
        }
      ]
      ```
    - `link-units:` An array that associates IDs with sets
      of properties that describe link units, including associated process
      invocations, link unit types, and input files. For
      example:

      ```
      "link-units": [
        {
          "id": 1,
          "cov-build-invocation-id": 1,
          "cov-translate-invocation-id": 1,
          "cov-emit-link-invocation-id": 1,
          "emit-failed": false,
          "kind": "object library",
          "primary-file-id": 1,
          "input-files": [
            {
              "file-id": 1,
              "kind": "object file",
              "implicit": false
            }
          ]
        }
      ]
      ```
    - `metrics:` An object with members that contain build
      capture statistics. For example:

      ```
      "metrics": {
        "tu-count": 500,
        "tu-failures": 3,
        "lu-count": 10,
        "lu-failures": 0
      }
      ```

list-json
:   List all translation units in the intermediate directory as a
    standards-compliant JSON array. The translation units are identified by a
    numeric ID, which is listed along with the following fields:

    - `id:` The unique numeric translation unit ID.
    - `primaryFilename:` The primary source file name.
    - `primaryFileSizeInBytes:` The size of the primary
      source file in bytes.
    - `primaryFileHash:` MD5 hash of the contents of the
      primary source file.
    - `language:` String describing the translation unit
      language.
    - `userLanguage:` The user-specified translation unit
      language.
    - `hasASTs:` Boolean. 'true' if the intermediate
      directory contains an AST for this translation unit, otherwise
      'false'.

    Example output:

    ```
    [
      {
        "id" : 1,
        "primaryFilename" : "/home/build/project/tu1.cpp”,
        "primaryFileSizeInBytes" : 92,
        "primaryFileHash" : "6f700a28a47e79cddff8fba60cac7098",
        "language" : "C++”,
        "userLanguage" : "C++”,
        "hasASTs" : true
      },
      {
        "id" : 2,
        "primaryFilename" : "c:/project/stdafx.cpp",
        "primaryFileSizeInBytes" : 122,
        "primaryFileHash" : "3827e3e7426ce0bdebb7e51c94d2a680",
        "language" : "C++",
        "userLanguage" : "C++",
        "hasASTs" : false
      }
    ]
    ```

    Note: The output of this command may contain additional attributes that are not
    documented here. For maximum interoperability, please ignore any attribute
    that is not documented.

extract-files --output-dir <dir> [--strip-path <path>]... {--regex <regex> | <filename>...}
:   Extracts files present in the emit directory to the specified output
    directory.

    The original directory, optionally stripped by any `--strip-path arguments`,
    will be made relative to the specified output directory (on Windows, the
    drive letter, if any, is always removed). Specify the files to extract by
    including either a regular expression or a list of file names. If you
    include the `--regex` option, all files whose name matches
    the given regular expression are extracted: for this purpose, the file names
    are represented using a `'/'` separator. If a *TU*
    filter (`--tu`, `--tu-pattern`) is provided,
    only files referenced by the filtered TUs are included.
