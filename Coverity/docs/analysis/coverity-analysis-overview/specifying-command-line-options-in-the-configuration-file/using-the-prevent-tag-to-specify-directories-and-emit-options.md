---
title: "Using the <prevent> tag to specify directories and emit options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-the-prevent-tag-to-specify-directories-and-emit-options.html"
content_id: "qCn51jk7OiB710T5AyDgYQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:01.346854+00:00"
---

# Using the <prevent> tag to specify directories and emit options

You can use the `<prevent>` tag (nested under the
`<coverity>` and `<config>` elements) to specify
directories and certain build options in the configuration file instead of specifying
them on the command line. Options that are specific to the build process reside under
the `<emit_options>` tag. Table 1 describes some common
configuration options and the equivalent command line option for each. If an option is
specified both on the command line to a command and also in
coverity_config.xml, the command line takes precedence.

Table 1. Options under the `<prevent>` tag in coverity_config.xml

| Tag | Description | Overriding command line option |
| --- | --- | --- |
| `<tmp_dir>` | The directory in which to place temporary files. | `tmpdir <dir>`  `-t <dir>` |
| `<dir>` | The top-level directory that Coverity Analysis uses to determine the emit and output directories. | `dir <dir>` |
| `<parse_error_threshold>` | A child of the `<emit_options>` tag. The percentage of units that must successfully compile for the `cov-build` command to not return error code 8, and to not generate a warning. If less than this percentage compiles, the `cov-build` command returns a warning and the 8 error code. The default value is 95. | `parse-error-threshold <percentage>` |
| `<preprocess_first>` | A child of the `<emit_options>` tag. If specified, the `cov-build` command tries to preprocess each file with the native compiler before sending it to `cov-emit`. This tag does not take a value. Use if the build fails because of errors in `cov-emit` preprocessing. | `preprocess-first` |
| `<no_diff>` | A child of the `<emit_options>` tag. Specify to disable automatic diagnostic of compilation failures by trying to find differences between preprocessed files. This tag does not take a value. | `no-diff` |
| `<return_emit_failures>` | A child of the `<emit_options>` tag. If specified, `cov-build` returns with an error code if an emit failure occurs. The return value is a combination (a binary OR) of the following flags:  - 1 – The build returned an error code. - 2 – The build terminated with an uncaught signal, such as a   segmentation fault. - 4 – No files were emitted. - 8 – Some files failed to compile. By default, if less than 95%   of the compilation units failed to compile, this error code is   returned. To change this percentage, use the   parse_error_threshold option.  Note that `cov-build` always returns an error code if your build fails. | `return-emit-failures` |
| `<chase_symlinks>` | A child of the `<emit_options>` tag. If specified, `cov-build` and `cov-translate` follow symbolic links when compiling files. For example, if you compile a file called foo.c, which is a symbolic link to the file bar.c, and foo.c has an error in it, the error report lists bar.c if you used this flag, otherwise foo.c. | `chase-symlinks` |
| `<emit_cmd_line_id>` | A child of the `<emit_options>` tag. If specified, `cov-build` and option, see The 'cov-translate' command in place of the native compiler. `cov-translate` emit different files for the same file built with different command-line options. By default, these commands only emit a file the first time it is compiled. See Getting linkage information. This tag does not take a value. | `emit-cmd-line-id` |

The tags described in Table 1
require a matching closing tag.

For example, see Figure 1.

Note: For `cov-analyze`, only the following XML tags are supported:

- `<tmp_dir>`
- `<dir>`

The following example modifies some common options.

Figure 1. XML configuration file example

```
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE coverity SYSTEM "coverity_config.dtd">
<coverity>

<!-- Version 1.0 -->
<cit_version>1</cit_version>
<config>

<prevent>
    <tmp_dir>/home/users/tests/temp</tmp_dir>
    <verbosity>2</verbosity>
    <emit_options>
        <emit_cmd_line_id/>
        <force_emit/>
        <return_emit_failures/>
        <chase_symlinks/>
    </emit_options>
</prevent>
</config>
</coverity>
```

Note: It is important to keep tags and their values on the same line. For example:

```
tmp_dir/home/user/tmp/data/tmp_dir
```

Using line breaks (as shown in the following example) can create pathnames with
unintended characters (such as carriage returns) or cause other problems.

```
tmp_dir/home/user/tmp/ 
data/tmp_dir
```
