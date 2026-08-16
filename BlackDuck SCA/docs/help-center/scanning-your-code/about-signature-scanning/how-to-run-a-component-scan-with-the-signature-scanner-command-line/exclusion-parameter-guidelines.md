---
title: "Exclusion Parameter Guidelines"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/exclusion-parameter-guidelines.html"
content_id: "17LjnEEbCzNltEhdyu8wvA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:39.299246+00:00"
---

# Exclusion Parameter Guidelines

The **--exclude** and **--exclude-from** parameters allow you to specify
directories to be excluded from signature scanning.
When using these parameters, follow these guidelines:

- **Single Directory Exclusion:** Use `--exclude <pattern>`
  to exclude a specific directory.
- **Multiple Directory Exclusions:** Use `--exclude-from
  <Filename>` to specify a file that lists multiple directories
  to exclude.
- **Automatically Excluded Items:** The scanner automatically excludes certain
  directories and files.

  | Excluded Directories | Excluded Files |
  | --- | --- |
  | - `CVS` - `.svn` - `.git` - `.hg` - `.bzr` - `__MACOSX` | - `.cvsignore` - `.git` - `.gitignore` - `.gitattributes` - `.gitmodules` - `.hgignore` - `.hgsub` - `.hgsubstate` - `.hgtags` - `.bzrignore` - `vssver.scc` - `.DS_Store` |
- **Exclusion Guidelines:** Follow specific rules regarding leading slashes,
  directory names, and file formats.

  - Leading and trailing forward slashes are required.

    For example, if you enter `exclude /directory`, a
    warning message will appear and the directory will not be excluded.
    If you enter `/directory` in the file, the directory
    will not be excluded.
  - Directory names cannot contain double asterisks (**).
  - Specify one directory per line in the file. Include the complete
    direct path. The path must be a relative path rather than an
    absolute path.
  - You cannot exclude archives or contents within archives.
- **Additional Methods:** There are two additional methods you can use to
  exclude directories from scanning:

  - Create an `ignore` file located in the
    `$HOME/config/blackduck` directory.

    Use this file to list excluded directories, relative to root. This option
    provides you with the ability to use one location to list all
    directories that need to be excluded.

    Lines in the `ignore` file must have the path from source
    root to the ignored directory, may have multiple subdirectories, and
    must have leading and trailing forward slashes (/).

    Create one of the following environment variables, as shown here,
    configured for Linux or Mac OS X:

    - ```
      export JAVA_TOOL_OPTIONS=" -Duser.home=<path>"
      ```

      The `.ignore` file must be located here:
      `<user.home>/.config/blackduck/ignore`
    - ```
      export XDG_CONFIG_HOME=<path>
      ```

      The `.ignore` file must be located here:
      `$XDG_CONFIG_HOME/blackduck/ignore`
    - ```
      export JAVA_TOOL_OPTIONS="-Dblackduck.scan.excludesFile=<path>/<file>"
      ```

      The `.ignore` file can be in any location and have
      any name.

    For Windows systems, use the Control Panel to access the Advanced System
    Settings dialog box to create the environment variables.
  - Create individual `.bdignore` files which can be located
    in any directory.

    Use this file to list the excluded subdirectories in the directory where
    the `.bdignore` file is located. You must create a
    `.bdignore` file in each directory that has
    subdirectories you want to exclude.

  You must also follow the exclusion guidelines as described above when using
  either of these methods.

  Tip: Use the **--debug** parameter when excluding directories to
  ensure that the scanner visited and excluded the directory.
