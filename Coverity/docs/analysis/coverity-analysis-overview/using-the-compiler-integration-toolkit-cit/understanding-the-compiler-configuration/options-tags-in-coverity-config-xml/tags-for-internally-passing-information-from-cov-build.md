---
title: "Tags for internally passing information from 'cov-build'"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tags-for-internally-passing-information-from-cov-build-.html"
content_id: "xkASgLmi1gjHLbfftHIWnw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:06.502120+00:00"
---

# Tags for internally passing information from 'cov-build'

These XML tags are used internally by `cov-build` to pass information to
`cov-translate`.

<cygpath>
:   Specifies the path in which Cygwin is installed. This does not appear in a configuration
    file.

<encoding>
:   Indicates what file encoding to use. This does not appear in a configuration file.

<encoding_rule>
:   Specifies file encodings on a per-file basis using regular expressions. Within
    `<encoding_rule>`, you use
    `<encoding>` to specify an encoding for files with
    names that match the regular expression you specify with
    `<path_regex>` or
    `<path_regex_icase>`, for example:

    ```
    <encoding_rule>
        <encoding>UTF-8</encoding>
        <path_regex>someFile\.c</path_regex>
    </encoding_rule>
    ```

    For case-insensitive regular expressions, you use
    `<path_regex_icase>`, for
    example:

    ```
    <encoding_rule>
        <encoding>Shift_JIS</encoding>
        <path_regex_icase>iregex</path_regex_icase>
    </encoding_rule>
    ```

    To use more than one regular expression
    to match multiple files that use a specific encoding, you can specify more
    than one `<path_regex>` and/or
    `<path_regex_icase>` under the same`<encoding_rule>`, for
    example:

    ```
    <encoding_rule>
        <encoding>EUC_JP</encoding>
        <path_regex>regex.*\.c</path_regex>
        <path_regex>regex2.*\.c</path_regex>
        <path_regex_icase>iregex.*\.c</path_regex_icase>
        <path_regex_icase>iregex2.*\.c</path_regex_icase>
    </encoding_rule>
    ```

    For each
    `<encoding_rule>`, it is necessary to specify an
    `<encoding>` tag and at least one
    `<path_regex>` or
    `<path_regex_icase>` tag.

    Note: Currently,
    Coverity does not support `<encoding_rule>` for Java,
    C#, and the Clang C/C++ compiler.
