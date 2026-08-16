---
title: "Non-filtered sub-commands"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/non-filtered-sub-commands.html"
content_id: "AzdQACeBXNHfUCNp_57fMQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:47.424431+00:00"
---

# Non-filtered sub-commands

These sub-commands cannot be filtered with translation unit options.

add-other-hosts
:   Adds all translation units from emit repositories in the current intermediate
    directory but associated with host names other than the current one. In
    general, an intermediate directory can contain several emits, each
    associated with a specific host name. This option copies all of the TUs from
    emits associated with other hosts into the emit associated with the current
    host. This sub-command can be used to aggregate the results of a distributed
    build into a single intermediate directory.

add-scm-annotations --input <input_file>
:   Adds the SCM annotations for the source files in the specified input file to
    the source files in the intermediate directory. The input file can be the
    output file of the `cov-manage-emit dump-scm-annotations`
    option or the `cov-extract-scm`.

    This option reads input from standard input when <input_file> is "-".
    Otherwise, it reads from the specified file.

    Note: If you pipe the output of `cov-extract-scm`directly to
    `cov-manage-emit`, for
    example:

    ```
    cov-extract-scm --input input.txt --output - | 
    cov-manage-emit --dir idir add-scm-annotations --input -
    ```

    This
    will always generate at least one error and the first line of output
    will read `Extracting SCM data for ### files`.

check-compatible
:   Checks if an emit version is compatible with the current Coverity Analysis
    tools. For example:

    ```
    cov-manage-emit --dir idir check-compatible
    ```

    This option returns 0 if it is compatible, 1 if it is not compatible, and 2+
    if there is an error.

check-integrity
:   Checks database integrity. If this check fails, print errors to stdout and
    exits with a non-zero code. Otherwise, exits with 0.

delete-bytecode
:   Removes all file contents from the database. This is useful if you need to
    provide an intermediate directory to Coverity technical support and want to
    make sure that source code is excluded.

delete-scm-annotations
:   Removes all SCM annotations from the database. This is useful if you need to
    provide an intermediate directory to Coverity technical support and want to
    make sure that SCM data is excluded.

delete-source
:   Removes only source contents, including all webapp archive files (JSP, XML,
    and so forth). This option does not remove Java class, JAR files, or .NET
    bytecode. This is useful if you need to provide an intermediate directory to
    Coverity technical support and want to make sure that the source content is
    excluded.

dump-scm-annotations --output <output_file>
:   Output all SCM annotations stored in the intermediate directory. This command
    creates a cache of the SCM annotations that is intended to be reapplied in
    the future using add-scm-annotations.

    This option places output on a standard output when <output_file> is
    "-". Otherwise, it outputs to the specified file.

export-json-build <options>
:   Exports a captured build to a JSON file for later use with
    import-json-build.

    Required options for `export-json-build`:

    - `--output-file <filename>, -of
      <filename>`

      Specify the path to and file name for the JSON file to be
      exported.

    Optional options for `export-json-build`:

    - `--schema-version <value>`

      Specifies the schema version to use for the JSON file. See the output
      of `cov-manage-emit list-json-schema-versions` for
      a listing of valid values, as well as details about version
      differences. If not specified, the latest schema version will be
      used.
    - `--strip-path <path>` 

      Strips the prefix for the exported file
      names and paths in the exported JSON file. This may be specified
      multiple times, but only the first matching strip path for any given
      path will be stripped. Accordingly, specify multiple strip paths
      from most specific to least for best results.

import-json-build <options>
:   Imports a JSON build file, which can be generated via the
    `export-json-build` sub-command, to the intermediate
    directory specified to `cov-manage-emit`. Note that the
    imported directory will not be useful for analysis results until at least a
    partial capture has been performed *after* the import. This option is
    primarily used in combination with `cov-run-desktop` to
    enable `cov-run-desktop` to work without requiring a full
    native build capture.

    Required options for `import-json-build`:

    - `--input-file <filename>, -if
      <filename>`

      Specify the path to and file name for the exported JSON file to
      import.

    Optional options for `import-json-build`:

    - `--compilation-log <log file>` 

      Specify a log file to dump
      diagnostic output from this command to. If this is not specified,
      then the output from the `import-json-build`
      command goes to stdout.
    - `--parallel <number of processes>, -j <number of
      processes`>

      Specify the number of `cov-translate` processes to
      use simultaneously for the import. Note that 'auto' can be specified
      to allow `cov-manage-emit` to automatically
      determine the number of processes to use based on the detected
      hardware.

list-builds
:   Reports total number of successful and failed builds.

list-compiled-classes
:   Lists the classes contained in the emit that have been compiled. Use with `--java`
    or `--cs` to limit the results to one of the languages. The
    output is CSV-formatted and written to standard output and is designed to be
    specified into the `cov-build --java-instrument-classes
    <filename>` command.

    The CSV file format has two columns:

    - Column 1 - The name of the class.
    - Column 2 - The full path to the source file for the class.

    This sub-command applies only to Java and .NET, not to C/C++.

list-functions-v1
:   Lists the functions in the intermediate directory. The valid command line
    options are:

    - `--function-pattern <pattern>` 

      Restrict output to only those
      functions which match <pattern>. <pattern> follows the
      syntax described in the Translation unit pattern matching section, however the following predicates are used instead of the
      predicates described in that section:

      - `mangled_name(regex)`: The
        function is included if its mangled name matches the given
        regex.
      - `unmangled_name(regex)`:
        The function is included if its unmangled name matches the
        given regex.
      - `filename(regex)`: The
        function is included if it is in a file whose stripped name
        matches the given regex.
    - `--output-fields <fields>` 

      Specifies the fields for each function
      to include in the output. `<fields>` is a
      comma-separated list of keywords from among the following:

      - `mangled_name`: The mangled name of the
        function.
      - `unmangled_name`: The unmangled name of the
        function.
      - `filename`: The name of the file containing
        the function.
      - `default`: The default output fields. This is
        equivalent to
        "`mangled_name,unmangled_name,filename`",
        and is the default if the `--output-fields`
        option is not specified.

      Output is in CSV format by default, unless the
      `--json` option is given. Each line except the
      first corresponds to a function, and contains the output fields in
      the order specified. The first line is a header indicating the field
      names.
    - `--json`

      Output in JSON format. The output is a JSON array, where each element
      corresponds to a function. Each element of this array is an object
      whose name/value pairs correspond to the specified
      `--output-fields`.
    - `--strip-path <path>`

      The path prefixes to strip before evaluating file names. Normally
      this is not required, but it can be used to override the default
      path.

list-json-schema-versions
:   List valid `schema-version` values for use with
    `export-json-build`. A brief description of version
    differences will accompany each value.

list-scm-known <command_options>
:   Lists the files contained in the emit that have corresponding SCM data
    included in the emit. The valid command line options are:

    - `--output <output_file>`

      The list is written to standard output when <output_file>
      is the dash character ("-"). Otherwise, the list is written to
      the specified file.
    - `--filename-regex <regex>`

      Includes a file for consideration if the regular expression
      (regex) matches the name of the file; this is not
      case-sensitive.

      For the purpose of turning a file name into a string that can
      then be matched against a regex, the following normalizations
      are applied:

      - The name is made absolute, including the drive letter on
        Windows systems.
      - The forward-slash character ("/") separates name
        components.
      - When no drive letter is present, the name begins with a
        forward-slash character ("/"); otherwise, a
        forward-slash character ("/") follows the drive
        letter.
    - `--count`

      Reports the number of files that would have been reported. If used with
      `--filename-regex`, it reports the number of
      matching files only.

list-scm-unknown <command_options>
:   Lists the source files contained in the intermediate directory that do not
    have corresponding SCM annotations included in the intermediate directory.
    The valid command line options are:

    - `--output <output_file>`

      The list is written to standard output when <output_file>
      is the dash character ("-"). Otherwise, the list is written to
      the specified file.
    - `--filename-regex <regex>`

      Includes a file for consideration if the regular expression
      (regex) matches the name of the file; this is not
      case-sensitive.

      For the purpose of turning a file name into a string that can
      then be matched against a regex, the following normalizations
      are applied:

      - The name is made absolute, including the drive letter on
        Windows systems.
      - The forward-slash character ("/") separates name
        components.
      - When no drive letter is present, the name begins with a
        forward-slash character ("/"); otherwise, a
        forward-slash character ("/") follows the drive
        letter.
    - `--count`

      Reports the number of files that would have been reported. If used with
      `--filename-regex`, it reports the number of
      matching files only.

query-build-id
:   Outputs the current build ID for this intermediate directory.

repair
:   Repairs database integrity. This operation might cause data loss, such as
    discarding translation units that are damaged.

reset-host-name
:   If the specified intermediate directory has data associated with a single
    host name other than the current host name, changes the host name associated
    with the emit database to the current host name.

set-build-id
:   Sets the build ID of the specified intermediate directory. The valid command
    line options are:

    --build-id <build-id>
    :   Set the build ID of the specified intermediate directory to
        <build-id>.

    --build-id-file <build-id-file>
    :   <build-id-file> is a file containing a build ID. Set the
        build ID of the specified intermediate directory to the value
        contained by this file.
