---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "79znqoduHGk~uIdd0rIQZQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:08.362533+00:00"
---

# Options

@@<response_file>
:   Specify a response file that contains a list of additional command line
    arguments, such as a list of input files. Each line in the file is treated
    as one argument, regardless of spaces, quotes, etc. The file is read using
    the platform default character encoding. Using a response file is
    recommended when the list of input XML files is long or automatically
    generated.

    Optionally, you can choose a different encoding, by specifying it after the
    first "@". For example:

    ```
    cov-import-msvsca [OPTIONS] @UTF-16@my_response_file.txt
    ```

    You must use a supported Coverity encoding, listed under the `cov-build
    --encoding` option.

--append
:   Append issues to any issues that exist in the intermediate directory.

    - If `--append` is absent, all of the issues in the
      intermediate directory are deleted before importing and analysis
      summaries will not be captured.
    - If `--append` is present, issues are not deleted.

    See also `--output-tag`.

--codepage <identifier>
:   Specifies Microsoft code page source encoding. <identifier> is an
    integer represents the code page identifier, for example `--codepage
    1201`. For the list of code page identifiers, see <http://msdn.microsoft.com/en-us/library/windows/desktop/dd317756%28v=vs.85%29.aspx>.

    Source with a BOM will have the encoding auto-detected, even if
    `--codepage` or `--encoding` is specified.
    However, if you specify `--encoding`,
    `cov-import-msvsca` will log a warning recommending
    that you use `--codepage` instead.
    `--codepage` results in using the .NET mechanisms for
    decoding, which more closely mimic the Microsoft tools.

    You cannot use `--codepage` and `--encoding`
    together.

--dir <intermediate_directory>
:   Path name to an intermediate directory that is used to store the results of
    the build and analysis. This option is required.

--encoding <encoding_name>
:   Specify that source files are read using the named character encoding, such as
    `UTF-8`. The default is based on detection of byte-order
    marks and falling back on the operating environment default character
    encoding.

    Valid values are the ICU-supported encoding names:

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

--no-threshold-check
:   By default, if more than 10% of reported issues do not have file and line
    information because their referenced assemblies, their associated pdbs, or
    referenced source files (either from the MSVSCA XML file(s) or assembly pdb)
    are missing, then `cov-import-msvsca` will fail without
    importing any issues and print an informative error message that mentions
    `--no-threshold-check`. However, if
    `--no-threshold-check` is specified, these messages are
    just informative and are not treated as an error. The defects that depend on
    the missing information are omitted from the results and the remaining
    issues are imported normally.

--output-tag <name>
:   Specifies a non-default location within the intermediate directory for the
    results of one or more imports. The name can be anything you choose, using
    characters allowed in file names. When specified *without* the `--append` option, prior results
    found in this location are replaced. When specified *with*
    `--append`, new results are added to the result set.

--skip-unrecognized
:   By default, `cov-import-msvsca` fails if a specified input
    file is not in a recognized format or if the list of input files is empty.
    If `--skip-unrecognized` is specified, files in an
    unrecognized format are simply skipped with a warning, and the list of files
    can be empty. Thus, the translation of any input files in the recognized
    format proceeds normally, even if there are none.
