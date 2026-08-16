---
title: "The capture: Examples"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-capture-examples.html"
content_id: "NBHk1dXcCA7f4nf_YPmc4Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:52.885178+00:00"
---

# The capture: Examples

To capture sources, from the source code directory run either the Coverity CLI `coverity capture` command
or the `cov-build` command.

## For compiled languages or scripts and interpreted code

Invoke `coverity capture` as follows:

```
> coverity capture -- <BUILD_COMMAND>
```

If you are not able to build the project, or are looking to capture scripts and interpreted code only, you can use the Coverity CLI
without specifying a build command. The Coverity CLI will attempt to infer the right build command where this is possible.
For example:

```
> coverity capture
```

Keep in mind that this alternative might produce less accurate results than when you specify a particular build command.
Also, some languages might not be supported: For more information see the "Buildless capture support?" column in the
"Support matrix" table of the Guide to the Coverity 2026.6.0 Point and Scan UI and the Coverity CLI.

If you want to capture certain languages only, you can specify the specific languages that you want to analyze.
For example:

```
> coverity capture --language java
```

If you want to capture only compiled languages, you can use `cov-build` instead of the Coverity CLI:

```
> cov-build --dir <intermediate_directory> <BUILD_COMMAND>
```

## For JavaScript capture

If you have both minified and non-minified versions of the same library in your source, capture only the non-minified version.
However, if only the minified version is available, you should capture it. You can use the --file-exclude-regex option or the
--file-exclude-glob option of the Coverity CLI `coverity capture` command for this purpose.

Although defects will be reported in third-party code when it is not minified, and those defects might not be actionable, supporting evidence
for defects in your code can only be shown in non-minified code.

## For capturing directly from a `git` repository

Use the --scm-url option. For example:

```
> coverity capture --scm-url git@mygit.internal.example.com:myrepo.git
```

## Notation

Examples in this section use the following notation for values to passed to the command options:

- `<BUILD_COMMAND>` is the command you use to invoke your compiler
  (for example, `gcc` or `javac`) on source code,
  such as Java and C++. For important recommendations, see
  The capture: Further notes on build capture.
- <intermediate_directory> specifies a name that
  you designate for the directory that will store an intermediate
  representation of the code base that you are building or emitting.
  If that name does not exist already, the command will create the intermediate directory with the name you specify.
  This directory can contain data for all the supported programming languages.
