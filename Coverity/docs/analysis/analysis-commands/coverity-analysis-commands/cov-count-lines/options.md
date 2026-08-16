---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "Zey8ExnHBVM0fCaXpY7Z5w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:22.651994+00:00"
---

# Options

--code-identity-file <filename>
:   Creates a filename for a code base identity, stored as a
    `.cbi` file. The content of the `.cbi`
    file specifies the source files which are to be included and excluded from
    the analysis. When this option is specified, the
    `cov-count-lines` command line console output will also
    end with a hash of this file.

    For example:

    ```
     $ cov-count-lines --search . --third-party-regex files_to_exclude \
       --third-party-regex dir --code-identity-file my-example.cbi
     File: /path/to/source/example1.java; Analyzable lines: 8
     File: /path/to/source/example2.cc; Analyzable lines: 12
     File: /path/to/source/example3.cc; Analyzable lines: 14
     File: /path/to/source/example4.h; Analyzable lines: 4
     Total Analyzable Lines for Coverity Pricing: 38
     Code Base Identity Hash: 910b8f9b8699597dc0334ac3dc5af6fc0b61c7a95aa38edb553d63062088c2b9
    ```

    If you do not provide the full path to the `--search` option,
    a stack trace is produced as shown below

    ```
    cov-count-lines --search .
    filename-class.cpp:1866: assertion failed: getWithFilesystemStripped expects an absolute path name
    call stack backtrace:
    cov-count-lines linux64 2020.03
    0x448760
    0x4488c1
    0x44b84e
    0x44b94c
    0x465b88
    0x4222ed
    0x425614
    0x455295
    0x414745
    libc.so.6 linux64 2020.03
    0x21b97
    ```

    Once the identity hash has been generated, you can use it to create a license
    file. The `.cbi` file that has been created and saved will
    then be used to run `cov-analyze`.

    Note: Coverity recommends that you store the code identity file in your source
    control management (SCM) system. This prevents anyone else from changing the
    content of the code base after a license has been issued. The code identity
    file should only be updated when a Coverity license needs to be
    re-issued.

    See also, the cov-analyze version of
    `--code-identity-file`.

--file <filename>
:   Counts the lines in <filename>. You can use absolute or relative file/path
    names.

--list <file-list>
:   Specifies a text file (<file-list>), which contains one filename per line.
    The filenames can be absolute or relative, but relative filenames must be
    relative to the current working directory.

--search <path>
:   Searches for all source files in the specified path and its subdirectories, recursively. This
    option may be specified more than once. The absolute filenames found by
    `--search` are added to those specified with
    `--file` and `--list`.

    See also, `--search-extensions`.

--search-extensions <list of extensions>
:   Overrides the classification of what source files should or should not be
    counted. By default, all files that are recognized as an analyzable source
    will be counted. This option takes a comma-separated list of case-sensitive
    filename extensions. When specified, only files with these extensions will
    be counted.

    For example:

    ```
    c,c++,cc,cp,cpp,cs,cxx,h,h++,hh,hpp,htm,html,hxx,java,js,jsp,m,mm,php,php3,phtml,py,pyt,rb,rpy
    ```

--third-party-regex <regex>
:   Specifies a case-insensitive regular expression (regex) of absolute filenames to *exclude*
    from `--search` and to add (as exclusions) to the code
    identity file (see `--code-identity-file`). This option may
    be specified more than once. The regex uses Perl syntax and matches if it
    matches a substring.

    Note that these regexes can be used to exclude any files that should not be
    counted or reported for defects. These may include third-party files, test
    code, and generated code.

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
