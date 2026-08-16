---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "cs3l38vYhqHg5f0X6Vzy6A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:37.409830+00:00"
---

# Options

--add-modules modules
:   [Java9+ only] Allows you to specify the name of one or more modules in a
    comma-delimited list. These modules are added to the set of observable root
    modules. The default root modules may vary by JDK, and are defined by the
    module declaration in the java.se JDK module.

--add-exports module-name/package-name=target-module
:   [Java 9+ only] Allows you to specify that the package-name
    in module-name is exported explicitly to the
    target-module. The effect of this option is the same
    as declaring an `exports` clause in the module declaration
    for the module-name.

    This option can be specified more than once if multiple add-exports options
    are required.

--add-reads module-name=target-modules
:   [Java 9+ only] Allows you to to specify additional read edges between
    module-name and one or more target module names in a
    comma-delimited list. Note that in the context of the Java module system,
    `reads` is synonymous with `requires`, so
    the effect of this option is the same as declaring `requires`
    clauses in the module declaration.

    This option can be specified more than once if multiple add-reads options are
    required.

--android-apk Android_APK_file
:   [Used for Coverity Extend SDK checkers that analyze Android applications]
    Identifies an Android APK file that is associated with a specified input
    file and read by custom Extend SDK checkers that are built for Android
    analysis.

    Requirement: When using this option, you must also specify an `--input-file`
    option to this command. For information about custom Android checker
    development, see "Reporting events and defects on input files" in Coverity Extend SDK 2026.6.0 Checker Development Guide.

--auto project_directory
:   [Not supported for module-based code in Java 9+] Allows you to specify a
    directory where source (*.java), input Jar files
    (*.jar), and compiler outputs
    (*.class) can be found. If you set this option,
    `cov-emit-java` will recursively search for these
    items.

    Note that `--auto project_directory` is
    functionally equivalent to the following:

    ```
    --findsource project_directory 
    --findjars project_directory
    --compiler-outputs project_directory
    ```

    If necessary, you can specify `--findsource`,
    `--findjars`, or `--compiler-outputs`
    options along with the `--auto` option. This sort of
    specification might be useful if you have a simple project that requires
    specific Ant or JDK dependencies.

    Example:

    ```
    cov-emit-java --dir <intermediate_directory> --auto $PROJECT_ROOT --findjars $ANT_HOME:$JAVA_HOME
    ```

--bootclasspath directories_or_jar_files
:   Allows you to specify a list of directories or Jar files, which must be
    separated by a semi-colon (`;`) on the Windows platform, and
    by a colon (`:`) on other platforms. Classes specified
    through the `--bootclasspath` are emitted, but the bodies of
    their methods are not, because `cov-emit-java` expects to
    have models for them. Coverity Analysis for Java comes with models for the
    entire Java Runtime Environment (JRE) and Android SDK, which should address
    all cases.

    Like `javac`, `cov-emit-java` searches
    these entries for bytecode with the referenced classes when attempting to
    resolve names in source files. The directories/jar files are searched in the
    order specified in directories_or_jar_files.

    Generally, you do not need to specify this option because
    `cov-emit-java` selects the bootclasspath of the JRE
    that comes with Coverity Analysis for Java. However, if you are compiling
    code against a non-standard JRE, one that is not API-compatible with the
    standard JRE, then you might need to use this option.

--classpath directories_or_jar_files
:   Allows you to specify a list of directories or Jar files. The list must be formatted as follows:

    - Windows: separate entries with a semi-colon.
    - Other platforms: separate entries with a colon.
    - The wild card (`*`) in classpath is supported.

      The
      wildcard will find all Jar files in the given directory (ie:
      `foo/*` finds all jars in
      foo/).

    Like `javac`, `cov-emit-java` searches
    these entries for bytecode with the referenced classes when attempting to
    resolve names in source files. The directories/jar files are searched in the
    order specified in directories_or_jar_files. Since
    Coverity Analysis analyzes these class files, it is better, when possible,
    to specify the implementations that are loaded at runtime rather than the
    stubs that are used for compilation.

    Note: Note that
    directories specified with `--classpath` will only be
    searched for Jar files if the wildcard is used. Otherwise, directories
    will be searched only for bytecode.

    If a directory
    (foo/) may contain bytecode *as well
    as* Jar files, you should include both
    "`foo/`" AND "`foo/*`" in your
    arguments to `--classpath`.

    The `cov-emit-java` command captures the same bytecode in
    Jar files referenced on the classpath that `java` or
    `javac` find (that is, bytecode where the package name
    matches the directory within the Jar file).

    The `cov-emit-java` command respects the
    Class-Path entry in Jar manifests.

    If the `--classpath` option is not specified, the current
    directory will be used as the default classpath.

    The `cov-emit-java` command is not affected by the CLASSPATH
    environment variable.

    Note: When loading certain jar files, `cov-emit-java` can consume more than 10GB
    of memory. This can cause out-of-memory failures on low-memory systems,
    including 32-bit systems in general.

--compiler-outputs class_files_or_directories
:   Captures a list of class files that have debug symbols for subsequent analysis by the Java Web
    application security dynamic analyzer.

    The list contains class files separated by the classpath separator (colon or
    semi-colon). Any directories in the list will be recursively searched for
    class files. Compiler outputs should be specified on the same command line
    as the source code from which they were compiled. Subsequent invocations of
    `cov-emit-java` on the same source files will replace
    the compiler outputs from the previous invocation with those of the new
    invocation.

    Jar files passed to `--compiler-outputs` will have their
    contained class files included. Directories passed to
    `--compiler-outputs` will not have their contained Jar
    files included.

    Note: Do not pass obfuscated bytecode to this option.

--dir <intermediate_dir>
:   Identifies the intermediate directory into which this command emits source
    files and referenced assemblies. An error occurs if the specified
    intermediate directory exists but is not valid, or if the directory does not
    exist and cannot be created.

    This option is required.

--encoding character_encoding
:   Applies the specified character encoding to all source files processed by
    this invocation of `cov-emit-java`. Defaults to UTF-8. This
    default might not be the same one that `javac` uses.

    Supports the following encodings (note that these differ from what
    `javac` supports):

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

    MacRoman
    :   The `cov-emit-java` treats MacRoman as
        Macintosh.

    Note: Some other unsupported encoding names might be supported if a known alias
    is supported. For example, the Java canonical x-EUC-TW is mapped to
    EUC-TW.

    The `cov-emit-java` command attempts to
    tolerate encoding errors and logs a warning when it finds bytes that
    cannot be decoded.

--findears <directory_list>
:   [Java Web application option] Searches the specified directories recursively
    for EAR (Enterprise Archive) files and adds the ones that it finds to the
    emit in the intermediate directory. The directory list must be separated by
    a semi-colon (;) on the Windows platform, and by a colon (:) on other
    platforms.

    In most cases, Coverity recommends that you use only one
    of these related options (`--findwars`,
    `--findwars-unpacked`, `--findears`, or
    `--findears-unpacked`). The option should match the final packaged
    `web-app` format. Otherwise, the search might find and emit unwanted
    temporary build artifacts.

    Note: The Web application directories should not contain
    obfuscated classes.

--findears-unpacked <directory_list>
:   [Java Web application option] Searches the specified directories recursively
    for unpacked web-app root directories and add the ones
    that it finds to the emit in the intermediate directory. The
    web-app root directories are identified by the
    presence of a META-INF/application.xml file. The
    directory list must be separated by a semi-colon (;) on the Windows
    platform, and by a colon (:) on other platforms.

    In most cases, Coverity recommends that you use only one
    of these related options (`--findwars`,
    `--findwars-unpacked`, `--findears`, or
    `--findears-unpacked`). The option should match the final packaged
    `web-app` format. Otherwise, the search might find and emit unwanted
    temporary build artifacts.

    Note: The Web application directories should not contain
    obfuscated classes.

--findjars <Jar_containing_directories>
:   [Java Web application option] Allows you to specify a list of directories, which must be
    separated by a semi-colon (`;`) on the Windows platform, and
    by a colon (`:`) on other platforms. The
    `cov-emit-java` command searches these directories
    recursively for Jar files and adds the ones that it finds to the classpath.
    The directories are searched in the order specified in
    <Jar_containing_directories>.

    Note that this option can result in an error if the number of Jar files
    exceeds the limit on the number of open files that is allowed by your
    operating system.

--findsource <source_directories>
:   Lists directories, which must be separated by a semi-colon
    (`;`) on the Windows platform, and by a colon
    (`:`) on other platforms. The
    `cov-emit-java` command searches these directories
    recursively for source files. It process the source files that it finds as
    if they were specified directly on the `cov-emit-java`
    command line.

--findwars <directory_list>
:   [Java Web application option] Searches the specified directories recursively
    for WAR (Web application archive) files and adds the ones that it finds to
    the emit in the intermediate directory. The directory list must be separated
    by a semi-colon (;) on the Windows platform, and by a colon (:) on other
    platforms.

    In most cases, Coverity recommends that you use only one
    of these related options (`--findwars`,
    `--findwars-unpacked`, `--findears`, or
    `--findears-unpacked`). The option should match the final packaged
    `web-app` format. Otherwise, the search might find and emit unwanted
    temporary build artifacts.

    Note: The Web application directories should not contain
    obfuscated classes.

    See also `--webapp-archive` and `--findwars-unpacked`.

--findwars-unpacked <directory_list>
:   [Java Web application option] Searches the specified directories recursively
    for unpacked web-app root directories and adds the ones
    that it finds to the emit. The web-app root directories
    are identified by the presence of a WEB-INF/web.xml
    file. The directory list must be separated by a semi-colon (;) on the
    Windows platform, and by a colon (:) on other platforms.

    In most cases, Coverity recommends that you use only one
    of these related options (`--findwars`,
    `--findwars-unpacked`, `--findears`, or
    `--findears-unpacked`). The option should match the final packaged
    `web-app` format. Otherwise, the search might find and emit unwanted
    temporary build artifacts.

    Note: The Web application directories should not contain
    obfuscated classes.

    See also `--webapp-archive` and `--findwars`.

--force
:   Disables incremental compilation by forcing the command
    to compile and generate output for all source files, including files that have
    already been compiled and are present in the Intermediate Directory and whose
    timestamps has not changed.

--help

-h
:   Prints a usage message to the command console, then exits.

--ignore-sccs
:   Ignores all directories named SCCS. This is useful for
    version control systems that store metadata with .java,
    .jar, and .class extensions in
    directories named SCCS.

--input-file <resource_file>
:   [Used for Coverity Extend SDK checkers that analyze Android applications]
    Identifies a resource file, typically a
    AndroidManifest.xml file, that can be read by
    custom Extend SDK checkers built for Android analysis. This option can be
    specified multiple times on the command line.

    Requirement: When using this option, you must also specify the
    `--android-apk` option. For information about custom
    Android checker development, see "Reporting events and defects on input files" in
    Coverity Extend SDK 2026.6.0 Checker Development Guide.

--javac-version
:   Identifies which implementation's bugs to emulate. Oracle Javac is the
    standard, but there are places where Oracle Javac does not conform to the
    specification and Eclipse does. To accommodate this, Eclipse attempts to
    implement Oracle bugs and ties it to the `--javac-version`
    switch. If the `--source` option is explicitly defined, then
    the `--javac-version` option is set to the same value. If the
    `--javac-version` option is explicitly defined, then the
    `--source` option is set to the same value. If both
    options are defined, then they work with the values that they are explicitly
    set to. The default value is 1.8.

    Note: Versions older than 1.8 for this option are not supported.

--jvm-max-mem
:   [Java Web application security option] Sets the value of the JVM that is used
    for invoking the Jasper engine for JSP compilation. The option accepts an
    integer that specifies a number of megabytes (MB). The default value is
    1024.

--kotlin-jvm
:   Enables the compilation of Kotlin source code instead of Java source code.
    The `cov-emit-java` command can be used to capture bytecode
    written in either Java or Kotlin.

--limit-modules module-names
:   [Java 9+ only] Allows you to specify the name of one or more modules in a
    comma-delimited list. The observable modules will then be restricted to the
    transitive closure of those specified in the limit-modules option, in
    addition to any modules specified by the `--add-modules`
    option.

--lombok-jar
:   Set this option to the location of the lombok jar file when running
    `cov-emit-java` on files that use Lombok.

--minimal-classpath-emit
:   Limits the group of emitted JAR files to those needed for compilation of the
    Java files. The default behavior without this option is to emit all the JAR
    files in the classpath regardless of whether they are referenced by a Java
    file in the compilation. This option can improve performance of Java builds
    with large numbers of unused JAR files on the classpath at the risk of not
    capturing all the dependencies of the those JAR files. For example if
    A.java references A.jar, which
    has dependencies on B.jar, this option will prevent
    B.jar from getting emitted even if
    B.jar is on the classpath.

--module-path directories_or_jar_or_jmod_files
:   [Java 9+ only] This option allows you to specify a list of directories, JAR
    files, or JMOD files, which must be separated by a semi-colon (;) on the
    Windows platform, and by a colon (:) on other platforms.

--module-source-path directory
:   [Java 9+ only] This option allows you to specify where to find source files
    for multiple modules.

--no-compiler-outputs
:   Indicates that the `--compiler-outputs` option is intentionally unspecified. Use
    of this option is not recommended because the dynamic analysis for Java Web
    application security relies on a compiler output specification. Without
    emitting compiler outputs, you can expect to see false positive XSS
    reports.

    It is an error to run `cov-emit-java` without exactly one of
    the following options: `--no-compiler-outputs` or
    `--compiler-outputs`.

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
    cov-emit-java [OPTIONS] @UTF-16@my_response_file.txt
    ```

    You must use a supported Coverity encoding, listed under the `cov-build
    --encoding` option.

--skip-emit-war-javascript-source
:   [Java Web application option] Skip capture of JavaScript source code embedded
    in a Web application archive (`.WAR` file,
    `.EAR` file, or equivalent unpacked directory).

--skip-war-sanity-check
:   [Java Web application option] Suppresses a failure in the case that the emit
    process determines that expected contents of the Web application (web-app)
    archives are missing.

    This option overrides the following sanity check on each WAR file or Web
    application directory on the command line:

    - The check that each contains a /WEB-INF
      directory and /WEB-INF/web.xml file.

    This option overrides the following sanity check on the set of all Web
    application archives or directories on the same command line:

    - The check that the Web applications do not contain enough
      (>20%) of the classes captured during build capture or manual
      `cov-emit-java` invocations.

    These checks are designed to catch cases where someone passes the wrong items
    to `--webapp-archive`. Turn off this check *only if* you
    are certain that you are passing the correct Web application files or
    directories to `cov-emit-java`, despite the warnings.

    For additional details, see `--webapp-archive` and --skip-webapp-sanity-check.

--source Java_version
:   Identifies which version of the Java language to emulate. For example,
    `--source=1.8` will allow
    `cov-emit-java` to handle lambda expressions and other
    features that appeared in Java 8. If `--source` is explicitly
    defined, then the `--javac-version` is implicitly set to the
    same value. If `--javac-version` is explicitly defined, then
    the `--source` option is implicitly set to the same value. If
    both are explicitly defined, then both have the value they are explicitly
    set to. The default value is 1.8.

    Note: Versions older than 1.8 for this option are not supported.

--sourcepath source_directories
:   Lists directories, which must be separated by a semi-colon
    (`;`) on the Windows platform, and by a colon
    (`:`) on other platforms. Like `javac`,
    the `cov-emit-java` command searches these directories for
    source files that contain referenced classes. If no
    `--sourcepath` is provided, the sourcepath will default
    to the expanded classpath.

--system directory | none
:   [Java 9+ only] Allows you to specify the location of the JRE or JDK to pull system libraries
    from. This is the replacement for the bootclasspath in Java 9+. For more
    information on how system libraries are used during analysis, see the
    `--bootclasspath directories_or_jar_files` option.

--use-fe <front end>
:   As of Coverity 2023.9.0, the --use-fe option does nothing. It has been deprecated, and will be removed in a future release.
    It was formerly used to allow users to specify either the `edg` (EDG) or `ecj` (Eclipse) front end,
    but EDG is no longer maintained and does not work with any code that targets Java 9 or newer.
    Specifying a value of `edg` results in a warning, and `cov-emit-java` will use Eclipse anyway.

--webapp-archive archive_file_or_dir, --war archive_file_or_dir, --ear archive_file_or_dir
:   [Java Web application option] The `--webapp-archive` and
    `--war` options store the contents of the specified Web
    Archive (WAR, .war) file, Enterprise Archive (EAR,
    .ear), or directory with the unpacked contents of
    either to the intermediate directory (emit repository) and prepares them for
    analysis. For these two options, the `cov-emit-java`
    command inspects the file or directory that is provided as argument and it
    guesses its type, based on the presence of WEB-INF (for WAR) or META-INF
    (for EAR), falling back to WAR by default. The `--ear` is
    similar, but it only interprets its argument as an EAR.

    These options can be passed multiple times to store and analyze multiple
    archives.

    Note: You need to emit any JSP files so that the analysis can find and report defects in them,
    particularly XSS issues. The build capture does not emit JSP files (which
    are typically compiled at runtime).

    The preferred method to emit JSPs is
    to use this option to capture the Web application archive(s) that
    contain them. The advantage of this approach is that the archives also
    include compilation dependencies and important configuration files.

    Another method to emit JSPs is with buildless capture. See the
    `coverity
    capture` documentation. This method is appropriate if
    the JSPs are not packaged into a Web application archive file. This
    includes Spring Boot "Fat JARs" and other deployment systems that do not
    include JSP source for runtime compilation.

    Because these two methods are complementary, care should be taken to
    avoid emitting redundant copies of the same JSP files. To exclude
    specific filesystem paths, see `coverity capture --file-exclude-regex`.
    To disable the buildless capture of JSPs, see `cov-configure
    --no-jsp`.

    In addition to JSP files, JavaScript files embedded inside Web
    application archives are emitted.

    Example:

    ```
    cov-emit-java --dir my/intermediate/dir 
                  --webapp-archive path/to/webapp.war
                  --webapp-archive path/to/webapp2.war
    ```

    You can also specify a list of directories to search for WAR or EAR files (or
    unpacked directories) using one of the following options to this command:
    `--findwars`, `--findwars-unpacked`,
    `--findears`, or `--findears-unpacked`.

    After using this option, you can run an analysis with the
    --webapp-security option
    to `cov-analyze`.
    See "Running a security analysis on a Java Web application" in
    Coverity Analysis 2026.6.0 User and Administrator Guide.

    See also `--findwars` and `--findwars-unpacked`.

--verbose <0, 1, 2, 3, 4>

-V <0, 1, 2, 3, 4>
:   Set the detail level of command messages. Higher is more verbose (more
    messages). Defaults to 1.
