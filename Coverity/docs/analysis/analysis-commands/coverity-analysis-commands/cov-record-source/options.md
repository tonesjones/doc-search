---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "bd5pFRTrcqlhJKk~aUmP2g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:04.402271+00:00"
---

# Options

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

--webapp-archive <archive_file_or_dir>

--war <archive_file_or_dir>

--ear <archive_file_or_dir>
:   See the `cov-emit-java --webapp-archive` option.
