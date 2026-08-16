---
title: "The 'files' option"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-files-option.html"
content_id: "yrxlyp6LR_1VA7S6buy1Uw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:54.259207+00:00"
---

# The 'files' option

The `files` option allows you to include or exclude specific files or directories using glob patterns or regular expressions.

## Syntax (YAML format)

```
capture:
    files:
        include-glob: "*.java"
        exclude-glob: "*Test.java"
```

Glob patterns support `*` but not `**`, so more complex
file matching requires regex rather than a glob pattern. For a complete description of
glob patterns and regular expressions, and examples of how to use each in common
scenarios, see the configuration file
syntax or run `help config --syntax`.

## Available options

| Key | Description |
| --- | --- |
| `include-glob` | Glob pattern to include files. |
| `exclude-glob` | Glob pattern to exclude files. |
| `include-regex` | Regular expression to include files. |
| `exclude-regex` | Regular expression to exclude files. |
| `include-dirs` | List of directory names to include; for example, `["vendor"]`. |
| `include-list-file` | Path to a file that contains a list of source file paths to include, one per line. |
| `library-dirs` | Directories to search for dependencies. |
| `library-files` | Specific dependency files to include. |
| `webapp-archives` | Web application archives to capture. By default, all web applications are captured. Most users should not need any specific configuration for this. |
| `exclude-all-webapp-archives` | Configures whether to exclude capture of all webapp archives. Default: `false` |
| `emit-minified-js` | Configures whether to emit minified JavaScript. Default: `false` |

## Semantics for files in the project directory

Glob patterns, regular expressions, and default exclusions are only applied to the path relative to the project directory.
For example, if the project directory is /Users/jbloggs/Projects/my-project/, an `exclude-regex` such as `my-project\/.*` *would not*
result in all files in the project directory being excluded.
Similarly, a project directory of /Users/jbloggs/Projects/vendor/ would *also* not result in all files in the project directory being excluded,
even though vendor directories are excluded by default.

## Semantics for files outside of the project directory

For Analysis, build capture can capture files outside of the project directory.
For example, when capturing a Java project that uses Apache Maven, third-party JAR files might be captured in $HOME/.m2.
In this case, any `file` include and exclude patterns will apply to the full path to the file.
Because the include and exclude patterns apply to files both inside and outside the project directory, you need to take care to ensure that files aren't
accidentally excluded from capture.
