---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "yG44As8XM5UxJuW6ZTGOcg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:08.626686+00:00"
---

# Options

--dir <intermediate_directory>
:   Path name to an intermediate directory that is used to store the results of
    the build and analysis. This option is required.

--input <file.xmldb>, -if <file.xmldb>
:   Instead of reading models from an intermediate directory, use this input
    file. This option can be used more than once. If you specify multiple input
    files, the models in them are merged together and placed into the output
    file. Models from input files that are specified first have precedence over
    those in files that are specified later.

--make-dc-config
:   [C/C++ only] For a description, see the --make-dc-config option to
    `cov-make-library`.

--output-file <file.xmldb>, -of <file.xmldb>
:   The path name for the file to store the collected models.

    By default, using this option will append to the output file if the output
    file already exists. For example, the following command appends a new
    `model-1l.xmdb` file to the `all-models`
    collection

    ```
    $ cov-collect-models --input model-1.xmldb --output-file all-models.xmldb
    ```

--output-tag <name>
:   Use this option if you used it when generating analysis results. See the
    --output-tag option to
    `cov-analyze`.

--text
:   Output the models as text. This format is far less efficient than the
    standard `.xmldb` format, but is easier to debug.

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
