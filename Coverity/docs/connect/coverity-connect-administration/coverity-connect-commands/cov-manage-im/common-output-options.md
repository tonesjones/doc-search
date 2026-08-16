---
title: "Common OUTPUT options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/common-output-options.html"
content_id: "WY8lHYusMxamWo7wqyg5Iw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:37.923882+00:00"
---

# Common OUTPUT options

The following OUTPUT options are common to all modes.

--fields
:   Specify the fields to output with a `--show OPERATION` option.
    The list of fields are specified as a comma-separated value (CSV) list.

    To display a list of field names that are valid for a given mode, use
    `--show`
    `--output` fields in that mode. For example:

    ```
    > cov-manage-im --mode projects --show --output fields
    ```

    The following examples generate a comma-separated list of the values in the
    specified fields.

    ```
    > cov-manage-im --mode projects \ 
        --show --fields project,description,creation-date,last-modified-date
    ```

    ```
    > cov-manage-im --mode projects  \
        --show --output streams --fields project,stream-name,is-stream-linked
    ```

    ```
    > cov-manage-im --mode streams \ 
        --show --fields stream,language,description
    ```

    ```
    > cov-manage-im --mode defects --stream MySampleStream \ 
        --show --fields action,cid,checker
    ```

    The order in which the fields are specified in the CSV list is the order in
    which they display. The same field can be listed multiple times.

--no-headers|-nh
:   Do not print field headers with `--show` operation.

--separator sep
:   Use sep to separate CSV values instead of a comma.

--output-file|-of file
:   Write output to a file named by file.
