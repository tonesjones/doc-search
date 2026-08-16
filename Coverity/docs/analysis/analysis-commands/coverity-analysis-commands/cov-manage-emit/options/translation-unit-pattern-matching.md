---
title: "Translation unit pattern matching"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/translation-unit-pattern-matching.html"
content_id: "let6Hl4HhiGJ4zTEEDs_lA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:51.474647+00:00"
---

# Translation unit pattern matching

The argument to `--tu-pattern` is a string that acts as a filter on
translation units. Alternatively, to use a file name for a pattern, specify
`@filename`. Each pattern in this file must be
on a separate line.

To get useful information about the translation units in an emit repository, use the
list sub-command.

A pattern has the following syntax:

```
[!] function("regex"|'regex') [|| function("regex")] 
    [&& function("regex")]
```

When combining patterns, the precedence from lowest to highest, is OR
(`||`), AND (`&&`), and NEG
(`!`). OR and AND are left-associative. You can use parentheses to
group expressions to override precedence or associativity. The `regex` is
a Perl regular expression. A backslash in a quoted string is interpreted as a regular
expression metacharacter, and not as a string literal metacharacter. You can use single
or double quotes to pass the string properly from the shell to the command. The Perl
`regex` is used for partial matches; for full matches use the
beginning of line (`^`) and end of line (`$`) symbols.

Detailed examples can be found in Coverity Analysis > Coverity Analysis Usage > Analysis with
Coverity Checkers > Setting up Coverity Analysis for a production environment >
Integrating Coverity Analysis into a build system > Integrating Coverity Analysis into the build environment
> Getting linkage information.
.

The values for function for where to apply the regular expression
are:

all
:   No argument. Matches all compilations. Used when all TUs desired and
    tu-pattern required.

arg
:   Matches if the `regex` matches any of the native compiler
    command line elements, including the native compiler executable itself.

build_arg:
:   Matches if the `regex` matches any argument to
    `cov-build`, including the `cov-build`
    executable name.

build_name("regex")
:   Matches if `cov-build` --name name
    compiled the translation unit and name is matched by
    regex.

cov_emit_arg
:   Matches if the `regex` matches any argument to the Coverity
    compiler front end, such as `cov-emit`, including the
    executable name.

file
:   Matches if the `regex` matches the name of the primary source
    file. For the purpose of turning a file name into a string that can then be
    matched against a `regex`, the following normalizations are
    applied:

    - The name is converted to an absolute pathname. On Windows, this
      includes the drive letter.
    - On Windows, all letters are lower-cased, including the drive
      letter (this applies to all names in translation units created
      on Windows).
    - The forward-slash character (`/`) separates name
      components.
    - When no drive letter is present, the name begins with
      `/`; otherwise, a `/` follows
      the drive letter.

    For example:

    ```
    --tu-pattern "file('test\.c$')"
    ```

failure
:   No argument. Matches if the compilation was unsuccessful (exit code != 0).
    Used by `cov-build --replay-failures`.

'had_recoverable_errors("true")' list
:   Returns a list (`list`) of the names of files that reported recoverable errors during the build.

    **Example of invoking this option, and the output it generates:**

    ```
    cov-manage-emit --dir idir --tu-pattern 'had_recoverable_errors("true")' list 
    Looking for translation units
    |0----------25-----------50----------75---------100|
    ****************************************************
    Translation unit:
    1 -> /test/rec/t.c (recoverable errors)
    ```

header
:   Matches if the `regex` matches the name of any header file,
    which is defined to be a source file included in the TU other than the
    primary source file.

lang("lang")
:   The lang pattern matches TUs with one of the following specified language patterns:

    - C
    - C++
    - C#
    - CUDA
    - Dart
    - .NET bytecode
    - Fortran
    - Go
    - HTML
    - Java
    - JavaScript
    - JSX
    - JVM bytecode
    - Kotlin
    - Objective-C
    - Objective-C++
    - PHP
    - Python 3
    - Ruby
    - Rust
    - Scala
    - Swift
    - Text
    - TypeScript
    - Visual Basic
    - Vue.js SFC

link_file
:   The `regex` is not interpreted as a regular expression, but
    rather as the name of a file, which should be the output of
    `cov-link` (or `cov-manage-emit
    link_file`).

success
:   No argument. Matches if the compilation was successful (exit code = 0).
