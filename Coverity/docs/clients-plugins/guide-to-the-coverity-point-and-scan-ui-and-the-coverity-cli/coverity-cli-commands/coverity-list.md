---
title: "coverity list"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-list.html"
content_id: "ytanq0lyObHvHNZBXxhs2Q"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:34.916632+00:00"
---

# coverity list

List files that have been captured.

## Synopsis

```
coverity list [options]
coverity list (-h | --help)
```

## Description

The coverity list command lists files that have been captured to
the given intermediate directory by the coverity capture or
coverity scan command.

For each module found in the project directory, the coverity list
command shows information about files that were captured. In this context, a module
is a unit of functionality as defined by the build system. For instance, if Maven is
used for the project, each module is defined by a pom.xml
file.

For each module, the files that were captured are broken down by file family and then
by file type. For each file found in the project directory, the following
information is provided:

| Heading | Description |
| --- | --- |
| Filename | The name of the captured file. |
| Capture status | Indicates whether the corresponding file was captured and with what fidelity. There are four possible values for this heading:  - Succeeded: The file was successfully   captured. - Incomplete: The file was partially   captured; that is, there are parts of the file that   Coverity did not understand. - Failed: An attempt was made to capture   the file, but Coverity did not understand anything in   the file. - Ignored: The file was completely ignored; no attempt was made to   capture the file. Currently, files for C#, Dart, Java,   JavaScript/Typescript, PHP, Python, Ruby, Scala, and Swift   are supported, and if a build command was provided for   capture, files for C, C++, Objective-C, Objective-C++, and   Visual Basic are supported. That means if source files for   unsupported languages show up in the list   output, their status will be Ignored. |
| Code Lines | The number of lines of code in the file. |
| Notes | Additional relevant information about the file. |

The `coverity list` output looks like this:

```
...
Files for project file: /Users/jfitzpat/Projects/open-source/lunr.js/Makefile
  File family: Configuration
    File type: JSON
      Filename                          Capture Status Code Lines Notes
      .eslintrc.json                    Succeeded      74
      build/jsdoc.conf.json             Succeeded      10
      package-lock.json                 Succeeded      1636
      test/fixtures/stemming_vocab.json Succeeded      1
    File type: Markdown
      Filename        Capture Status Code Lines Notes
      CHANGELOG.md    Succeeded      158
      CONTRIBUTING.md Succeeded      12
      README.md       Succeeded      54
...
```

Capture might fail due to the following:

- For non-compiled files (Dart, JavaScript/Typescript, PHP, Python, Ruby, Scala, or
  configuration files): this means the effort to capture has failed. Call support
  for help.
- For compiled files: it means that files are unsupported (e.g., C or C++ with
  no build command), however you will still get analysis results.

  For Java or C# (or, with a build command, C, C++, Objective-C, Objective-C++, or Visual
  Basic), it means the compiler did not compile the files. The most likely
  reason is that the files are excluded from being compiled by the build
  system. If the files are in fact being compiled and not being captured,
  please call Support for assistance.

## Options

--project-dir project-dir-name
:   Project directory containing the source files to capture. If not
    specified, defaults to the current working directory

-h, --help
:   Displays the information in this section.

## Advanced Options

-c, --config file-name
:   The name of the configuration file to use. If not specified, defaults to
    coverity.yaml, coverity.yml,
    or coverity.json in
    project-dir.

    Guidance on creating and modifying configuration files is available in
    the form of a JSON schema in the docs directory at
    coverity-dir/doc/configuration-schema.json.

--dir <idir-name>
:   The name of the intermediate directory to use. If not specified, defaults to
    <project-dir>/idir.

–-compiler-config-file file-name
:   Custom compiler configuration to use.

-o, –-config-override key=val
:   Key and value to override in configuration.
