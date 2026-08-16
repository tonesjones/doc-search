---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "Lv9mV8CLZZNnTWLJFdsUOA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:16.701031+00:00"
---

# Description

The `cov-configure` command creates a configuration for a compiler (or
compiler family) and/or a scripting language, such as JavaScript. Choices in this
configuration file impact buildless capture.

The `--config` option specifies the name of the configuration file. By
default, if no other configuration file or directory is specified, the configuration is
created at <install_dir>/config/coverity_config.xml. Each
invocation of the `cov-configure` command adds a given compiler's
configuration in its own subdirectory under the directory that contains the output
configuration file. Within each compiler's configuration subdirectory, the
coverity_config.xml file contains an include directive for that
compiler-specific configuration.

Note:
On some Windows platforms, you might need to use Windows administrative privileges
when you run `cov-configure`.

Typically, you can set the
administrative permission through an option in the right-click menu of the
executable for the command interpreter (for example, `Cmd.exe` or
Cygwin) or Windows Explorer.

## Options to specify languages

The following table shows shortcut options that tell `cov-configure` which language to configure for analysis.
Languages shown in this table generate a template without requiring you to use the --template option.
For other languages, use --template with the --compiler and --comptype options.

Table 1. Language shortcut options

| Option | Compiler configuration | Filesystem configuration |
| --- | --- | --- |
| --apex | - | APEX configuration files |
| --clang | `clang`, `clang++` | - |
| --cs | `csc` | - |
| --cuda | `nvcc` | - |
| --dart | - | Dart configuration files |
| --gcc | `gcc`/`g++` | - |
| --go | `go` | `-` |
| --java | `java`, `javac`, `javaw` | Android configuration files, JAR, JSP |
| --java-buildless | - | Android configuration files, JSP |
| --javascript | - | HTML, TypeScript, JSX, VUE |
| --kotlin | `java`, `javaw`, `kotlin`, `kotlinc` | Android `kotlin-module` |
| --msvc | `cl` | - |
| --php | - | PHP configuration files |
| --python | - | Python configuration files |
| --ruby | - | Ruby configuration files |
| --rust | cargo |  |
| --scala | - | Scala configuration files |
| --typescript | - | HTML, JavaScript, JSX, TypeScript, VUE configuration files |
| --vb | `vbc` | - |

## Friend compilers

The configuration templates for certain languages automatically configure "friend compilers",
which tell `cov-build` to capture additional files for related applications in the configured language.
For example, `cov-configure --javascript`
automatically configures the capture of HTML files with the file-include pattern *.(htm|html).
In a similar way, `cov-configure --java` automatically configures the capture of
Android configuration files (with a file-include pattern of *.xml) and JSP configuration files
(with a file-include pattern of *.(jsp|jspx)).

The following table summarizes the "friend" file types associated with particular languages:

Table 2. Friend file types

| Buildless capture type | Friend file types | Notes |
| --- | --- | --- |
| Android | *.layout.*xml, *.AndroidManifest.xml, *.gradlew, *.gradlew.bat |  |
| APEX | *.cls, *.tgr, *.page |  |
| C# | *.cs |  |
| Dart | *.dart |  |
| Fortran | *.for, *.fpp, *.ftn, *.f77, *.f90, *.f90, *.f95, *.f2003, *.f2008, *.f2017 |  |
| Go | go.mod |  |
| HTML | *.htm, *.html |  |
| Jakarta Server Pages | *.jsp, *.jspx |  |
| Java | *.java |  |
| JavaScript | *.js, *.xsjs, *.xsjslib, *.cjs, *.mjs, *.map | JavaScript is a special case. See the Default Files for JavaScript Coverity Analysis Compilers table for additional file patterns configured by `cov-configure --javascript`. |
| JavaScript Syntax | *.jsx |  |
| Kotlin | *.kotlin_module |  |
| PHP | *.php, *.php1, *.php2, *.php3, *.php4, *.php5, *.php6, *.php7, *.php8, *.php9, *.phtml |  |
| Python | *.py, *.py3 |  |
| Ruby | *.rb, *.Gemfile |  |
| Rust | *.rs, Cargo.toml |  |
| Scala | `*.scala` |  |
| TypeScript | *.ts, *.tsx, *.cts, *.mts, *.tsconfig.json |  |
| VUE | *.vue |  |

Note:
The option --no-capture-config-files suppresses capture of the friend file types.

## Buildless capture configurations

A buildless capture configuration (for languages like Dart, Java, JavaScript, PHP, Python,
Ruby, or Scala) can be generated using template files that are provided. For
example, the following command uses the default template to generate a configuration
for Python:

```
cov-configure --python --config my-python-config.xml
```

The generated configuration specifies a set of file-include and -exclude patterns.
These file-include patterns define which files will be captured (or excluded) when
the code is captured for analysis. The configuration also associates the include
patterns with their corresponding Coverity analysis compiler. The
`coverity capture` CLI command then uses the configuration file to
determine the set of files it will emit during buildless capture.

The include and exclude patterns are matched with case-insensitive matching.

The sample command above, using the default Python template, generates a
configuration with a file-include pattern of `*.py`, and associates
these files with the Python compiler.
When you invoke `coverity capture`, the Coverity CLI recursively searches the project directory for files that
match the *.py file name pattern and emits those files so they will be analyzed.

The following table shows these default file-include patterns and their associated compilers
for JavaScript. For other languages (Dart, Java, Python, PHP, Ruby, Scala) you can
refer to the default configuration templates.

Table 3. Default Files for JavaScript Coverity Analysis Compilers

| Language | File Types |
| --- | --- |
| `--javascript` | *.js, *.xsjs, *.xsjlib, *.map - JavaScript compiler |
| *.html, *.htm - HTML compiler (unless `--no-html`) |
| *.vue - Vue.js Single File Component compiler (unless `--no-vue`) |
| *.ts, *.tsx, tsconfig.json - Typescript compiler (unless `--no-typescript`) |
| *.jsx - JSX compiler (unless `--no-jsx`) |
| `--typescript` | Alias for `--javascript`, with support for a `--no-javascript` option to suppress capture of `*.js`, `*.xsjs`, `*.xsjlib`, and `*.map` files. |

You can further customize the default capture configurations by using the
`--file-glob` or `--file-regex` options to extend
the list of file-include patterns.

To add a new filename extension for HTML files—for example, `.ihtm`—you could execute the following command lines:

```
cov-configure --javascript -config my-js-config.xml
cov-configure --comptype html --file-glob "*.ihtm" --config my-fs-config.xml
```

You can also create a custom configuration from scratch, without using or altering
the default templates. To do so, use `--file-glob` or
`--file-regex` in conjunction with `-comptype`.
For example, you might go through the following steps:

1. `cov-configure --comptype php --file-glob "*.php(5|7)" -c new-php-config.xml`
2. `cov-configure --comptype php --file-glob "*.phtml" -c new-php-config.xml`

For more details, see the descriptions of the --file-regex,
--file-glob, and --comptype options.
