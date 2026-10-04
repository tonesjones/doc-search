---
title: "Exclude files from SAST scans"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/exclude-files-from-sast-scans.html"
content_id: "ueQZXEHhm6pihfoXwypNvA"
version: "latest"
section: "How-to"
scraped_at: "2026-10-04T23:28:24.943506+00:00"
content_hash: "fb4e810096f42970fa7fd2ee1e481d0d94bb464ccb0153037d602bbb3a5b69ad"
---

# Exclude files from SAST scans

Excluding files and directories from a scan can reduce noise and improve scan performance.

**Contents**

- When should I exclude files from SAST scans?
- How do I exclude files and directories from a source archive uploaded to Polaris?
- How do I exclude files and directories from SAST analysis?
- How should I write exclusion patterns in coverity.yaml?
- How do I write cross-platform exclusion patterns?
- What YAML formatting mistakes should I avoid?
- How do I verify that exclusions are working?

## When should I exclude files from SAST scans?

Common use cases for excluding files and directories include:

- Excluding generated code
- Excluding third-party or vendor-managed code
- Excluding test projects that are outside the desired scan scope
- Reducing scan duration
- Preventing findings from code that is not maintained by the development team

## How do I exclude files and directories from a source archive uploaded to Polaris?

Bridge can be configured to create a project source archive and upload it to Polaris for remote capture, and analysis. This only applies when the source upload feature is enabled:

```
polaris.test.sast.location=remote
```

Configure file exclusions using:

```
project.source.excludes="generated/**,node_modules/**"
```

The `project.source.excludes` parameter accepts gitignore patterns, not file paths. Files and directories matching the configured patterns are excluded from the source archive uploaded to Polaris and are not included in the analysis.

For supported pattern syntax, see the [Git ignore documentation](https://git-scm.com/docs/gitignore).

## How do I exclude files and directories from SAST analysis?

Coverity is used by Polaris, Black Duck® Software Risk Manager™ and Coverity Connect to capture source files for analysis using build capture or buildless capture. Files and directories can be excluded from SAST analysis using `coverity.yaml`, regardless of which capture method is used.

CAUTION:

Excluding files and directories from capture can cause files that depend on the excluded content to be incompletely analyzed. This may lead to false positives or false negatives. Only exclude files and directories that are not compiled into production, or that are not required to build or analyze production code.

**Recommended: Exclude files using exclude-regex**

Use `exclude-regex` within the `capture: files` section of `coverity.yaml` to exclude files and directories from analysis. This configuration applies to both build capture and buildless capture workflows.

The `exclude-regex` option uses Google RE2 regular expression syntax. For supported pattern syntax, see the [RE2 syntax documentation](https://github.com/google/re2/wiki/Syntax).

Note: By default Bridge downloads the latest available version of Coverity. If using Coverity versions earlier than 2025.9.0, `capture.files` exclusions apply only to files captured by buildless capture. To exclude files from build capture in earlier versions, use `skip_file` within a `cov-configure` compiler configuration.

When using build capture, `exclude-regex` is evaluated against the source file paths supplied to Coverity during compilation. The exact paths depend on how the build system is configured. For example, if a Maven build compiles files from both `src/main/java` and `project/src/main/java`, exclusion patterns are matched against those paths.

```
capture:
  build:
    clean-command: mvn clean
    build-command: mvn -B -DskipTests -DskipITs install

  files:
    exclude-regex: "(^|/)src/main/java/excluded(/|$)"
```

In the example above the following files and directories would be matched by this pattern:

```
src/main/java/excluded/ForwardNullExcludeExample.java
project/src/main/java/excluded/ForwardNullExcludeExample.java
src/main/java/excluded
```

Further guidance and examples on writing exclusion patterns in coverity.yaml is provided below.

**Coverity versions earlier than 2025.9.0: Exclude files using skip_file**

Using the latest available Coverity version is recommended whenever possible.

For Coverity versions earlier than 2025.9.0, `exclude-regex` can be used to exclude files discovered during buildless capture, but it does not exclude files captured during build capture. In these environments, use `skip_file` when a build-capture exclusion is required.

This can be relevant when using older Coverity versions, for example through Polaris Multi Version support.

`skip_file` is a compiler configuration option that requires:

- a language specifier
- a Perl-compatible regular expression

For languages such as Java, source files are often compiled as a group rather than individually. As a result, excluding a file with skip_file might not have the intended effect if the file is required for compilation to succeed. The same consideration applies to other languages and build systems that compile multiple source files together.

For example, the following configuration excludes files located under `src/main/java/excluded` during Java build capture:

```
capture:
  build:
    clean-command: mvn clean
    build-command: mvn -B -DskipTests -DskipITs install

  compiler-configuration:
    cov-configure:
      - ["--java", "--xml-option=skip_file:.*/src/main/java/excluded/.*"]
```

For supported pattern syntax, see the [Perl regular expression documentation](https://perldoc.perl.org/perlre).

For a complete list of supported language specifiers, see [invoking cov-configure](https://docs.blackduck.com/r/coverity/2026.3/coverity-documentation/synopsis.html?tocId=AVreAcGmvj2jWaEjpgtnbw) in the Coverity Documentation.

## How should I write exclusion patterns in coverity.yaml?

Use an exclusion pattern that clearly matches the intended file or directory path. Avoid broad patterns that can match unrelated paths.

Recommended example:

```
capture:
  files:
    exclude-regex: '(^|/)src/main/java/excluded(/|$)'
```

This regular expression excludes the `src/main/java/excluded` directory and any files below that directory.

The pattern works as follows:

- `(^|/)` matches either the start of the path or a path separator before `src`.
- `src/main/java/excluded` matches the directory path to exclude.
- `(/|$)` matches either a path separator after `excluded` or the end of the path.

This helps avoid uncertainty about whether the file path evaluated by Coverity starts with a leading slash.

Examples matched by this pattern:

```
src/main/java/excluded/ForwardNullExcludeExample.java
project/src/main/java/excluded/ForwardNullExcludeExample.java
src/main/java/excluded
```

Examples not matched by this pattern:

```
src/main/java/not-excluded/ForwardNullExcludeExample.java
src/main/java/excluded-files/ForwardNullExcludeExample.java
src/test/java/excluded/ForwardNullExcludeExample.java
```

Avoid using only a bare directory name unless broader matching is intended.

```
capture:
  files:
    exclude-regex: 'excluded'
```

For example, it can match:

```
src/main/java/excluded/ForwardNullExcludeExample.java
src/main/java/excluded-files/ForwardNullExcludeExample.java
```

Use a directory-boundary pattern when the exclusion should apply only to a specific directory.

## How do I write cross-platform exclusion patterns?

`exclude-regex` is agnostic to the path separator used by the operating system. Using forwarded slashes (/) in exclusion patterns is recommended since they are easier to read and do not require the escaping often needed when using backslashes.

## What YAML formatting mistakes should I avoid?

Quote regular expression values in YAML. Regular expressions often contain characters that also have meaning in YAML, such as `*`, `|`, and `\`. Quoting the value helps ensure that the YAML parser passes the intended regular expression to Coverity.

Preferred:

```
capture:
  files:
    exclude-regex: '(^|/)src/main/java/excluded(/|$)'
```

Be careful with the `|` character. It has different meanings depending on where it appears:

- In a regular expression, `|` means "or".
- In YAML, `|` starts a multiline literal block.
- In YAML, `|-` starts a multiline literal block and removes the final trailing newline.
- In YAML, `>` starts a folded multiline value, where line breaks can be converted to spaces.

Avoid YAML block scalar syntax for `exclude-regex` unless you have verified how the final value is parsed.

Avoid this unless verified:

```
capture:
  files:
    exclude-regex: >
      .*[/\\]test[/\\].*|
      .*[/\\]generated[/\\].*
```

Prefer a single-line value:

```
capture:
  files:
    exclude-regex: '.*[/\\]test[/\\].*|.*[/\\]generated[/\\].*'
```

When using `|` as a regular expression operator, avoid unintended spaces around it. Spaces are treated as part of the regular expression and can change which files are excluded.

Preferred:

```
capture:
  files:
    exclude-regex: '.*[/\\]test[/\\].*|.*[/\\]generated[/\\].*'
```

Avoid unintended spaces:

```
capture:
  files:
    exclude-regex: '.*[/\\]test[/\\].*| .*[/\\]generated[/\\].*'
```

In the second example, the space after `|` becomes part of the second alternative. As a result, the expression may not match paths that would otherwise be excluded.

## How do I verify that exclusions are working?

To verify exclusions:

1. For Polaris source upload scans, inspect the generated source archive located in the `.bridge/project_source_zipper` folder to confirm that excluded files and directories are not included.
2. Confirm that issues are not reported for the excluded files or directories in the web UI of the Black Duck product, e.g. Coverity Connect, Polaris or Software Risk Manager (SRM).

Using the correct exclusion mechanism helps reduce scan scope, improve performance, and focus analysis on the code that matters most.
