---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "Xym6TRKxjH2IBDUvbxSs9w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:18.272726+00:00"
---

# Options

--
:   Indicate the end of `cov-configure` options. Following this
    option, you can specify additional compiler options. For example, GNU
    compiler installations that use a non-standard path to the cpp0 preprocessor
    require the additional GNU -B option to specify its path:

    ```
    > cov-configure --compiler gcc -- -B/home/coverity/gcc-cpp0-location/bin
    ```

    If your build explicitly uses the GNU compiler on the command line with
    either the `-m32` or `-64` option, also supply
    the option to the `cov-configure` command. For example:

    ```
    > cov-configure --compiler gcc -- -m32
    ```

--compiler <name>, -co <name>
:   Specify the compiler to configure. If the compiler <name> is not in the
    PATH, specify the full pathname to the compiler. To specify additional
    compiler options, use `--` followed by the options, for
    example:

    ```
    > cov-configure --comptype gcc --compiler C:\Mingw\bin\gcc.exe -- -D__STDC__
    ```

--comptype <type>, -p <type>
:   Specify the type of compiler to configure. In many cases,
    `cov-configure` guesses the compiler type based on the
    `--compiler` argument, but if the name of your compiler
    is non-standard, specify `--comptype`.

    As a general rule, never configure a compiler as a C++ compiler. Do so only
    in the case of a particular problem that you are trying to work around. If
    you configure a compiler as a C compiler, `cov-configure`
    will automatically take care of the C++ case.

    To see a full list of supported compiler types, run the
    `cov-configure`
    `--list-compiler-types` option.

    For information about configuring compilers, see the Coverity Analysis 2026.6.0 User and Administrator Guide.

--coverity-response-file <response_file>
:   Specify a "response file" that contains a list of additional command line
    arguments, such as a list of input files. Each line in the file is treated
    as one argument, regardless of spaces, quotes, etc. The file is read using
    the platform default character encoding.

--dart
:   [buildless capture option] Configures buildless capture for Dart source code.

--delete-compiler-config
:   This option accepts a compiler configuration by an absolute path or a path
    relative to the top-level configuration file. Only configurations specified
    in the top-level configuration will be deleted, otherwise this command has
    no effect.

    **Example**: Top-level configuration file,
    `conf/config.xml` contains three configurations:

    1. template-gcc-config-0
    2. template-msvc-config-0
    3. template-javac-config-0

       The following example will remove the configuration
       template-gcc-config-0, leaving the remaining two configurations
       untouched.

       ```
       cov-configure --delete-compiler-config template-gcc-config-0 \
          -c conf/conf.xml
       ```

--file-glob <pattern>
:   [buildless capture only] Used in conjunction with
    `--comptype` to specify a glob pattern to match for
    source files of the specified type. This option allows you to customize the
    predefined file-include patterns (including also those for friend compilers) that are used
    when you specify one of the language-specific options (such as
    `--java` or `--javascript`).

    For example, the following command creates a configuration for JavaScript
    that captures only files with a `.js` extension:

    ```
    > cov-configure --comptype javascript --file-glob '*.js'
    ```

    Note that the glob pattern will only match on filenames, not on directories
    or path information.

    The glob expression is matched against the filename using case insensitive
    matching.

    Do not use the `--file-regex` with
    this option.

    You will receive a warning if you specify a pattern that is identical to one
    that in a previously generated configuration file for an interpreted
    language or friend compiler.

--file-regex <pattern>
:   [buildless capture only] Used in conjunction with
    `--comptype` to specify a regex pattern to match for
    source files of the specified type. This option allows you to customize the
    predefined file-include patterns (including also those for friend compilers) that are used
    when you specify one of the language-specific options (such as
    `--java` or `--javascript`).

    For example, the following command creates a configuration for JavaScript
    that captures only files with a `.js` extension:

    ```
    > cov-configure --comptype javascript --file-regex '^.*\.js$'
    ```

    Note that the regular expression will only match on filenames, not on
    directories or path information.

    The regular expression is matched against the filename using case insensitive
    matching.

    Do not use the `--file-glob` with
    this option.

    You will receive a warning if you specify a pattern that is identical to one
    that in a previously generated configuration file for an interpreted
    language or friend compiler.

--force
:   Generate the configuration even if the compiler specified does not behave as
    expected for a compiler of the specified type.

--fs-library-path <path/to/the/library>
:   [Java buildless capture option] For Java buildless capture, the
    `--fs-library-path` option is added to the class and
    source paths of the Java compiler. Specifying this option is the equivalent
    to passing the `--classpath <path/to/lib>` argument and
    `--sourcepath <path/to/lib>` as command line options
    to the Java compiler.

    For example, the following command adds classes,
    `some.jar`, and `extrasrc` to the Java
    compiler's class and source paths (in this
    order):

    ```
    cov-configure --config config.xml \
       --java-buildless \
       --fs-library-path path/to/classes \
       --fs-library-path path/to/some.jar \
       --fs-library-path path/to/extrasrc
    ```

    [If you need to modify the
    class and source paths for different `cov-build` invocations, use
    the `cov-build` variant for `--fs-library-path`
    instead.] [You can also avoid modifying the paths with each build by using the
    `cov-configure` variant. This extends them only once in your
    configuration or installation.]

    [JavaScript, PHP, and Python filesystem
    capture only] Specifies third-party library locations for JavaScript Node.js
    `require` modules, ECMAScript 6 module imports,
    JavaScript HTML `script src=` includes, and HANA XSC
    libraries imported with `$.import`. PHP
    `include`/`include_once`/`require`/`require_once`
    and Python imports. By default, the `cov-build` command
    resolves these inclusions and imports relative to the source file doing the
    inclusion/import (according to language specific rules). The
    `cov-build` command also attempts to resolve them
    relative to directories passed to the `--fs-library-path`
    option.

    Passing directories to the `cov-configure`
    `--fs-library-path` option stores them in the configuration
    (for use with any `cov-build` command that uses that
    configuration). If you need to specify different libraries for different
    `cov-build` invocations, use the
    `cov-build` variant of `--fs-library-path`
    instead.

    For example, the following command adds `lib3`
    and `lib4` as additional library paths (searched in that
    order):

    ```
    cov-configure --config config.xml \
       --javascript \
       --fs-library-path lib3 \
       --fs-library-path lib4
    ```

    The search for the library file is
    permissive: If the search does not find the library at a relative path
    specified by this option, a second search for the filename alone (excluding
    the specified path) will run.

--javascript
:   [buildless capture only] Configures buildless capture for JavaScript source
    code. Also associates files ending in `.htm`,
    `.html`, `.js`, `.jsx`,
    `.ts`, `.tsx`, and `.vue`
    with a configuration for JavaScript so they can be saved in the intermediate
    directory.

    This configuration automatically excludes files that match the following
    regular expressions:

    - `//node_modules//`
    - `//jquery[^//]*[.]js$`
    - `//[^//]*-vsdoc[.]js$`

    See also, `--fs-library-path`, `--no-html`,
    `--no-jsp`, `--no-jsx`,
    `--no-typescript`, and `--no-vue`.

--list-compiler-types , -lsct
:   Generates a list of the supported compiler types. Usage:

    ```
    cov-configure --list-compiler-types
    ```

--list-configured-compilers <output>, -lscc <output>
:   Lists the configured compilers defined in your
    `<install_dir>/config/coverity_config.xml` file.
    The `output` option defines which output format you want the
    compiler configuration information displayed. It must one of:

    - `csv`
    - `json`
    - `text`

    Each format displays the following categories for each configured compiler:

    - Configuration name
    - Configuration path ("json" format only)
    - Compiler type
    - Compiler
    - Template configuration
    - Enabled options/required arguments

      Template configurations have "Config Args" while instantiated
      configurations have "Required Args". "Config Args" are used to probe
      the compiler along with any "Required Args" when instantiating a
      template configuration.

    If the value for any field cannot be determined (for example, if an option is
    not defined in the configuration file), "null" is printed in that field
    instead.

    The "json" format displays the configuration name AND the full path to the
    configuration in the `"Config Name"` and `"Config
    Path` elements. The following example shows the `"json"`
    format:

    ```
        {
            "Config Name"   : "template-gcc-config-0",
            "Config Path"   : "C:\\cygwin\\tmp\\template-gcc-config-0",
            "Compiler Type" : "gcc",
            "Compiler"      : "gcc",
            "Is Template?"  : "yes",
            "Config Args"   : "-DBAR"
        },
    ```

    The `"text"` and `"csv"` formats show only the directory and configuration names
    (not the full path).

    The following example shows the `"text"` and `"csv"` formats (they are
    identical):

    ```
        Config Name, CompType, Compiler, Template?, Config/Required Args
        -----------, --------, --------, ---------, --------------------
        template-gcc-config-0,gcc,gcc,yes,null
        template-gcc-config-1,gcc,g++,yes,null
        template-javac-config-0,javac,javac,yes,null
        template-java-config-0,java,java,yes,null
        template-apt-config-0,apt,apt,yes,null
    ```

    Note that in real usage, $prevent$ and $REAL_CC$ are actual paths.

--list-required-arguments, -lsra
:   Outputs a list of all the potential required arguments for a given compiler.
    Pass the `--compiler` or `--comptype`
    arguments to specify the compiler type on which you want
    `list-required-arguments` to operate.

--no-android
:   [buildless capture option] Disables the buildless capture of Java Android
    files. The default behavior for the Java template configuration is to enable
    the buildless capture of Java Android files that are needed by the
    analysis, including the manifest (`AndroidManifest.xml`) and
    the layout resource files.

    This option is valid only when either the `--java` option or
    `--java-buildless` option is also specified.

--no-capture-config-files
:   This option disables the buildless capture of miscellaneous configuration
    files. By default, when the Dart, Java, JavaScript, PHP, Python, or Scala
    templates are configured for buildless capture, they will also capture any
    smaller files that aren't media file types. The
    --no-capture-config-files option overrides this default
    behavior. Typical files that are captured this way include XML files, .plist
    files, framework configuration files, and other kinds of textual
    configuration files. Capturing these files aids Coverity Analysis in
    understanding application and framework configuration. It also enables
    various checkers (including user-defined
    TEXT.CUSTOM_CHECKER checkers) to run on them and to
    report any potential defects.
    You can limit which specific configuration files are captured by using the --file-include-glob or file-include-regex option with the
    `coverity capture` CLI command.

    Note: We do not recommend using this option for anything outside of
    troubleshooting scenarios, or unless advanced tuning is required for your
    deployment.

--no-header-scan
:   Disables performing a header scan for macro candidates during probing of a
    compiler.

--no-html
:   [buildless capture option] Disables the buildless capture of HTML files.
    The default behavior for the JavaScript template configuration is to enable
    the buildless capture and HTML compilation of files with the
    `*.htm` and `*.html` filename
    extensions.

    This option is valid only when the `--javascript` or
    `--typescript` option is also specified.

--no-javascript
:   [buildless capture option] Disables the buildless capture of JavaScript
    files. The default behavior for the TypeScript template configuration is to
    enable the buildless capture and JavaScript compilation of files with the
    `*.js`, `*.xsjs`,
    `*.xsjlib`, and `*.map` filename
    extensions.

    This option is valid only when the `--typescript` option is
    also specified.

--no-jsp
:   [buildless capture option] Disables the buildless capture of JavaServer
    Pages (JSPs). The default behavior for the Java template configuration is to
    enable the buildless capture and JSP compilation of files with the
    `.jsp` and `.jspx` filename
    extensions.

    This option is only valid when either the `--java` option or
    `--java-buildless` option is also specified.

--no-jsx
:   [buildless capture option] Disables the buildless capture of JSX files. The
    default behavior for the JavaScript template configuration is to enable the
    buildless capture and JSX compilation of files with the
    `*.jsx` filename extension.

    This option is valid only when the `--javascript` or
    `--typescript` option is also specified.

--no-typescript
:   [buildless capture option] Disables the buildless capture of TypeScript
    files. The default behavior for the JavaScript template configuration is to
    enable the buildless capture and TypeScript compilation of files with the
    `*.ts`, `*.tsx`, and
    `tsconfig.json` filename extensions.

    This option is valid only when the `--javascript` option is
    also specified.

--no-vue
:   [buildless capture option] Disables the buildless capture of Vue.js Single
    File Component files. The default behavior for the JavaScript template
    configuration is to enable the buildless capture and compilation of files
    with the `*.vue` filename extension.

    This option is valid only when the `--javascript` or
    `--typescript` option is also specified.

--php
:   [buildless capture option] Configures buildless capture for PHP source code. For supported
    versions of the PHP language, see "Language support" in Coverity Analysis 2026.6.0 User and Administrator Guide.

--python
:   [buildless capture option] Configures buildless capture for Python source
    code. For supported versions of the Python language, see "Language support" in Coverity Analysis 2026.6.0 User and Administrator Guide.

--ruby
:   [buildless capture option] Configures buildless capture for Ruby source
    code. For supported versions of the Ruby language, see "Language support" in Coverity Analysis 2026.6.0 User and Administrator Guide.

--scala
:   [buildless capture option] Configures buildless capture for Scala source code.

--template, -tm
:   Provides a template configuration for building with a related set of
    compilers. The necessary compiler configurations are generated with the
    required arguments as needed during the build process. For example, if a g++
    command that specified `-m64` was encountered, a g++
    configuration would be generated specifying the `-m64`
    argument.

    If you specify this flag, the argument to `--compiler` is a
    name of the compiler without a path. Do not use the
    `--version` option with this option.

    Note:
    Certain compilers don't require you to use the --template option.
    See "Options to specify languages".

--template-dir <directory_path>, -td <directory_path>
:   [Compiler Integration Toolkit (CIT) option] Specifies a template directory
    for custom Compiler Integration Toolkit (CIT) templates that override
    templates found in the default location. This option makes it possible to
    use custom templates without the need to modify anything in the default
    template directory. Multiple `--template-dir` options are
    allowed with directories specified in order of decreasing priority.

--version <version>, -v <version>
:   For C/C++, specify the compiler version. In many cases, `cov-configure` will
    guess the compiler version for you. For Microsoft Visual C/C++, the version
    is of the form "1310".

    For Java, values match valid source levels to the `javac`
    compiler: '1.4', '1.5', '5', '1.6', '6', '1.7', '7'.

    For Python, by default, version 3 of the Python language is assumed, which is the only
    version currently supported.

--xml-option <option>
:   Adds user-specified XML to `coverity_config.xml`. This option
    is useful for adding items to the file without using an editor.

    **Usage**

    ```
    --xml-option=[tag][@<language>]:value
    ```

    - [tag] is the basic XML tag to be added, for example,
      `add_arg`.
    - [@language] specifies that the switch is only to be added for compiler variants with the
      given language. Valid values are: `C, C++, Java, CS, ObjC,
      ObjC++`, or `NC` (where
      `NC` stands for "Not Compiled" and applies to
      Dart, JavaScript, PHP, Python, Ruby, and Scala). If this specifier
      is omitted, then the tag will be added for all compiler types being
      configured.
    - **value** is the value contained within the tag. This can be any
      value, including arbitrary XML.

    Simple example:

    ```
    --xml-option=append_arg:-Ihello
    ```

    Simple example in C config only:

    ```
    --xml-option=append_arg@C:-Ihello
    ```

    Arbitrary XML: `--xml-option` allows any number of XML
    elements. See example below, quoted as required for Windows:

    ```
    --xml-option=:"<append_arg>-Ihello</append_arg><append_arg>--ppp_translator</append_arg>"
    ```

    Arbitrary XML in C++:

    ```
    --xml-option=@C++:"<append_arg>-Ihello</append_arg>"
    ```

## C/C++ options

--cygpath <path>
:   Specify the path to the directory, which contains the bin directory of
    the Cygwin installation, if it is not in the PATH environment
    variable.

--cygwin
:   On Windows, indicates that Cygwin is necessary for a GCC compiler. The
    `cov-configure` command can detect if Cygwin is
    necessary without this, but you can use this option to force Cygwin if
    needed.

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

--redirect stdout|stderr,<filename>

-rd stdout|stderr,<filename>
:   Redirects either the `stdout` or the `stderr`
    stream to the specified file.

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
