---
title: "Files configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/files-configuration.html"
content_id: "DjgA_71vD2edYYvYI215Rg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:03.351757+00:00"
---

# Files configuration

Use one or more of the following keys to specify the set of files to be captured.

For information about how globs and regexes work, see the configuration file syntax.

Note:
These settings apply to the capture of both compiled and non-compiled languages.

| Key | Type | Description |
| --- | --- | --- |
| `emit-minified-js` | Boolean | Specifies whether to enable capture of minified JavaScript files. |
| `exclude-glob` | string | A glob pattern that specifies the set of source files to exclude from capture. Note: Any *include* glob patterns and regular expressions are processed prior to handling *exclude* glob patterns and regular expressions.  Default: exclude nothing |
| `exclude-js` | Boolean | Specifies whether to skip emitting JavaScript files inside the web application archive. Default: `false` |
| `exclude-regex` | string | A regular expression that specifies the set of source files to exclude from capture. Note: Any *include* glob patterns and regular expressions are processed prior to handling *exclude* glob patterns and regular expressions.  Default: exclude nothing |
| `include-dirs` | array of strings | A list of directory base names to include for capture that would normally have been excluded. Default: Exclude directories named vendor/ or node_modules/, and directories whose names begin with a period (`.`). |
| `include-glob` | string | Glob pattern that specifies the set of source files to capture. **Default**: include everything. |
| `include-list-file` | string | A path to a file that contains a list of paths to the source files to capture. Path names in the list should be separated by newline (`"\n"`) characters. If include/exclude glob patterns or regular expressions are specified, these are applied to determine which of the files in the list are actually captured. |
| `include-regex` | string | A regular expression that specifies the set of source files to capture. Default: include everything. |
| `java-version` | string | Specifies the Java version to use when parsing and emitting Java source files with buildless capture. |
| `library-dirs` | array of strings | A list of directories to search in order to find dependencies to use during capture. |
| `library-files` | array of strings | A list of file dependencies to use during capture. |
| `webapp-archives` | array of Web-app archive configurations | This array specifies information about which Web-application archives should be captured. Default: Capture all Web-app archives |
| `exclude-all-webapp-archives` | Boolean | Configures whether to exclude capture of all webapp archives. Default: `false` |
