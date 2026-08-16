---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "Ex8H4nLSrf9oXqCCAFrIRQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:42.111946+00:00"
---

# Options

C options and related standards
:   The following options indicate that `c` files may be
    compiled with the corresponding standard. The default is
    `--c11`.

    - `--c11`
    - `--c90`
    - `--c99`

C++ options and related standards
:   The following options indicate that `c++` files may be
    compiled with the corresponding standard. The default is
    `--c++17`.

    - `--c++11`
    - `--c++14`
    - `--c++17`
    - `--c++98`

--all
:   The `--all` option enables checker types as defined in the
    *Coverity Command Reference*. These checker types include
    quality, security, and concurrency. When used with the
    `cov-make-library` command, the checkers and checker
    types are enabled to generate models for the enabled checkers. To choose
    specific checker types to model, use the options such as
    `--quality`, `--concurrency`,
    `--security`, and
    `--webapp-security`.

--checker-option <checker_name>:<option>[:<option_value>]
:   Passes the specified checker option to `cov-analyze` when
    invoking `cov-analyze` after the library has been built.

    Example:

    ```
    UNINIT:enable_deep_read_models:true
    ```

    Checker options and their default values are documented in the Coverity 2026.6.0 Checker Reference.

    CAUTION:

    The `cov-analyze` command allows
    `-co` as a shorthand form of this option, but
    `cov-make-library` already uses `-co`
    to designate the compiler, so don't confuse these option names.

--classpath <directories_or_jar_files>
:   [Java option] Lists directories or Jar files, which must be separated by
    a semi-colon (`;`) on the Windows platform, and by a
    colon (`:`) on other platforms. Like
    `javac`, `cov-make-library` searches
    these entries for bytecode with the referenced classes when attempting
    to resolve names in source files. See also the `--classpath`
    option to `cov-emit-java`. For
    `cov-make-library`, it is possible to use stubs.

--compiler <compiler>, -co <compiler>
:   [C/C++ option] Specifies a previously configured compiler (configured
    with `cov-configure``--compiler`) that is
    used to determine how to compile the files (using
    `cov-translate`). This is useful if you need to
    include standard headers. For example:

    ```
    > cov-configure --compiler ABC
    > cov-make-library --compiler ABC foo.c
    ```

--compiler-opt <opt>
:   [C/C++ option] Specify an option to the compiler specified by
    `--compiler` (or `cov-emit` is no
    compiler was specified). For instance, you can specify an include
    directory with `--compiler-opt -I --compiler-opt
    include_dir`

--concurrency
:   [C/C++ option] Use this option if you write a custom model using
    concurrency primitives.

--disable <CHECKER>
:   [C/C++ option. Deprecated for C# and Java.] Disables the creation of
    function models used by the specified checker.

    Note that this option disables a checker only if it is enabled by default
    *and not enabled in any other way*, for example, through a
    group enablement option such as `--all`.

--disable-default
:   [C/C++, C#, Java, Visual Basic option] Disables the creation of function models for *all*
    checkers, including Sigma checkers. Use options such as
    `--concurrency`, `--security`,
    `--quality`, and `--webapp-security`
    to choose a set of checkers for which to generate models.

    When using this option, you must also use an enablement option, such as
    `--quality` or `--security`. It is an
    error to use `--disable-default` without such an
    option.

--disable-webapp-security
:   [Java, C#, Visual Basic option] Disables the creation of models for Web application security
    checkers (for example, XSS and SQLI). You typically use this option when
    you only want to generate models for Java quality checkers. For a
    complete list of Web application security checkers, see the "Checker
    Enablement and Option Defaults by Language" table in the Coverity 2026.6.0 Checker Reference (HTML only).

    See also, `--webapp-security` and
    `--quality`.

--enable <CHECKER>
:   [C/C++ option. Deprecated for C# and Java.] Enables the creation of
    function models used by the specified checkers. If you want the
    specified checkers to check the source that uses your custom models, you
    must enable those checkers with this option.

    Important:
    The set of checkers enabled for `cov-make-library` must be the same as or a superset of the set of checkers used
    by any analysis that employs the models.
    You can't pick and choose checkers, or create multiple models for different subsets of checkers.

--enable-cgo-for-go-models
:   [Go option] Enables building Go models for code that contain C
    dependencies. These models are disabled by default.

    C code that is compiled as part of processing CGo dependencies will not
    be captured for analysis by `cov-make-library`.

    For code bases that contain CGo dependencies (in other words, Go code
    that imports the pseudo-package `"C"`): Your environment
    must be configured to successfully compile such code using the native Go
    compiler before you execute `cov-make-library` on your
    modeling code. This is required because the `cov-emit-go`
    command, the Go compiler, and the CGo tool, must access additional tools
    to process such code (they execute a C compiler and generate bindings
    for the compiled C functions).

    For more information about CGo support, see "Go compilers" in the Coverity 2026.6.0 Installation and Upgrade Guide.

--java
:   [Deprecated] Deprecated in version 7.0 because the command automatically
    determines the language based on the Java file extension.

--make-dc-config
:   [C/C++ only] Upgrades models for the deprecated SECURE_CODING checker to
    DC.CUSTOM_CHECKER checker configurations. Specifically, the option
    searches for `__coverity_secure_coding_function__` models
    in the source code and generates a JSON configuration file for a custom
    checker called DC.CUSTOM_CHECKER. The configuration file specifies
    function names and information found in the custom models.

    Example:

    ```
    > cov-make-library -of config.json --make-dc-config my_models.c
    ```

    To use the resulting configuration file in the analysis, you simply pass
    it through the `--dc-config` option.

    Example:

    ```
    > cov-analyze --dir <intermediate_dir> --dc-config config.json -en DC.CUSTOM_CHECKER
    ```

    The `--make-dc-config` option is also available to
    `cov-collect-models`.

--output-file <model-file>, -of <model-file>
:   Specify the name of the output model file. The default file name is
    `user_models.xmldb`, at
    `<install_dir>/config/`.

--quality
:   [C/C++, C#, Java, Visual Basic option] Generates models for quality checkers, including
    concurrency checkers. Use this option with
    `--disable-default` to generate models for only the
    quality checkers. For a list of quality checkers, see the "Checker
    Enablement and Option Defaults by Language" table in the Coverity 2026.6.0 Checker Reference (HTML only).

    See also, `--disable-default`,
    `--disable-webapp-security`, and
    `--webapp-security`.

--reference <referenced_assembly>
:   [C#, Visual Basic option] Specify a referenced assembly.

--security
:   [C/C++ option] Use this option if you write a custom model using
    security-related checkers such as TAINTED_DATA, TAINTED_STRING,
    STRING_SIZE, and STRING_NULL.

--security-file <license file>

-sf <license file>
:   Path to a valid Coverity Analysis license file. If not specified, this path is given by the
    `security_file` tag in the Coverity configuration or by
    license.dat (located in the Coverity Analysis
    <install_dir>/bin directory). A valid license
    file is required to run the analysis.

--webapp-security
:   [Web application security option] Generates models for Web application security checkers (for
    example, XSS and SQLI). Use this option with
    `--disable-default` to generate models for only the
    Web application security checkers. For a complete list of Web
    application security checkers, see the "Checker Enablement and Option
    Defaults by Language" table in the Coverity 2026.6.0 Checker Reference
    (HTML only).

    See also, `--disable-default`,
    `--disable-webapp-security`, and
    `--quality`.

## Shared options

--config <coverity_config.xml>

-c <coverity_config.xml>
:   Uses the specified configuration file instead of the default configuration
    file located at 
    <install_dir>/config/coverity_config.xml.

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
