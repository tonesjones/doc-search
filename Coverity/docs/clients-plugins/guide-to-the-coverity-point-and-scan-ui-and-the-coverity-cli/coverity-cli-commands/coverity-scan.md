---
title: "coverity scan"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-scan.html"
content_id: "JK8bakuqlZ27pIFOD1eK_w"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:35.654161+00:00"
---

# coverity scan

Capture, analyze, and get a link to the analysis results.

## Synopsis

```
coverity scan [options] [-- <build-command>...]
coverity scan [options] --local <results-path> [-- <build-command>...]
coverity scan (-h | --help)
```

## Description

The coverity scan command executes a capture and an analysis, and
uploads the results to the Connect server or saves results to a local directory.

This command requires either a configuration file or use of the --local
option, depending on where the analysis results are saved.

- For local analysis results, use the --local option.
- To commit results to Connect, use the Coverity configuration file to specify
  the Connect instance where to commit. You may specify the configuration file
  using the --config option, otherwise the file
  project-dir
  /coverity.yaml is used by default.

## Options

--archive-file <file-name>
:   Archive file (zip or tar.gz) containing the code to scan. If `--project-dir` is also specified,
    the archive is extracted to that path instead of to a folder with the same name as the archive.

-- build-command
:   Optional. A command used to capture the project by monitoring the build
    process for compiler invocations and then replaying them using the
    appropriate Coverity compiler. In other words, this is equivalent to
    doing the following, where mvn -DskipTests -DskipITs clean
    install is the build command:

    ```
    cov-build --dir idir mvn -DskipTests -DskipITs clean install
    ```

-h, --help
:   Displays the information in this section.

--project-dir <project-dir>
:   Project directory containing the code to scan.
    If not specified, defaults to the current working directory.

--scm-branch <branch>
:   When this option is specified, the command will use the <branch> branch for the given Git
    repository. If the repository folder does not exist, a `git
    clone` with the specified branch will be performed. If the folder
    already exists, the `git fetch`, `git checkout
    <branch>`, and `git pull` commands will be
    executed to retrieve the latest changes.

    This option has to be used together
    with `--scm-url`.

    At most one of
    `--scm-branch` and `--scm-revision` may be
    used. Specifying both `--scm-branch` and
    `--scm-revision` produces an error message

--scm-revision <revision>
:   When this option is specified, the command will use the <revision> revision for the given
    Git repository. If the repository folder does not exist, a `git
    clone` with the specified revision will be performed. If the folder
    already exists, the `git fetch` and `git checkout
    <revision>` commands will be executed to retrieve the specified
    revision.

    This option has to be used together with
    `--scm-url`.

    At most one of
    `--scm-branch` and `--scm-revision` may be
    used. Specifying both `--scm-branch` and
    `--scm-revision` produces an error message.

--scm-url <scm_url>
:   Specifies a URL for a source repository that contains the code to scan.

    The format of the URL is specific to each SCM system and must be
    accepted by the SCM system in use. Supported SCM systems: Git.

    Examples
    of Git URLs:

    - `/srv/git/project.git`
    - `git://example.com/group/project.git`
    - `https://github.com/example/project.git`
    - `git@github.com:example/project.git`
    - `ssh://git@github.com:example/project.git`

    If `--project-dir` is also specified, the repository is
    cloned to that path instead of to a folder with the same name as the repo.
    If the folder already exists, the latest changes are pulled instead of
    cloned. If a branch or revision is specified via
    `--scm-branch` or `--scm-revision`,
    respectively, that branch or revsion will be either cloned or pulled as
    necessary.

## Advanced Options

--compiler-config-file file-name
:   Custom compiler configuration to use.

--config, -c file-name
:   The name of the configuration file to use. If not specified, defaults to
    coverity.yaml, coverity.yml,
    or coverity.json in
    project-dir.

    See also -o option below.

    Guidance on creating and modifying configuration files is available in
    the form of a JSON schema in the docs directory at
    coverity-dir/doc/configuration-schema.json.

--cra
:   Enable EU Cyber Resilience Act (CRA) analysis mode.

--dir <idir-name>
:   The name of the intermediate directory to use. If not specified, defaults to
    <project-dir>/idir.

--disable-build-command-inference
:   Disable build command inference during capture.

--exclude-language lang
:   Language to exclude from capture. You may specify this option multiple
    times, but you may not also use the --language
    option

    By default all supported languages are included.

--file-exclude-glob glob
:   Exclude glob pattern to use when capturing files outside of a build.

--file-exclude-regex regex
:   Exclude the files defined by the specified regex when capturing files
    outside of a build.

--file-include-glob glob
:   Include glob pattern to use when capturing files outside of a build.

--file-include-regex regex
:   Include the files defined by the specified regex when capturing files
    outside of a build.

--incremental
:   Capture source files that were added or changed since the previous capture.

--language lang
:   Language to capture. You may specify this option multiple times, but you
    may not also use the --exclude-language option

    By default all supported languages are included.

--library-dir dir
:   Name of a library directory to look for dependencies to use during capture.
    You may specify this option multiple times.

--library-file file
:   Name of a library file to use as a dependency during capture. You may
    specify this option multiple times.

--local-format format
:   Specifies the format in which to save results: Must equal either `"html` (the default) or `"json"`.

--local-only
:   Force analysis results to be committed to the local filesystem.

--local results-path-name
:   Save analysis results to the specified local directory or file. For HTML format, this must
    specify a directory. For JSON format, this must be a file name.

    Note: When
    you invoke `coverity scan` and either the
    `--local` option is specified or
    `commit.local` is present in the configuration file
    (for example, coverity.yaml), then Coverity commits to both Coverity Connect
    *and* the local file or directory.

-o, --config-override key=val
:   Key and value to override in configuration.

–-pool-size <size>
:   Pool size to use when `analyze.location=connect` in
    coverity.yaml, which means that the scan is
    performed in the cloud.

    For a Thin Client analysis performed in the cloud, use this optional
    parameter to specify a scan job node pool size to use for a scan
    (analysis) in the cloud. Valid values are `"small"`,
    `"medium"`, `"large"`,
    `"extralarge"`, and custom pools. If you use a custom
    node pool, obtain the name of the node pool from the Coverity cloud
    administrator. See also Initiating a scan in the cloud.

--reset-cache <item>
:   Remove the given cached item.

--upload-artifacts <value>
:   Artifacts to upload following a scan when `analyze.location=connect` in
    coverity.yaml, which means that the scan is
    performed in the cloud. Valid values are `"All"` (the
    default), `"LogsOnly"`, `"None"`, and
    `"OnFailure"`. See also Initiating a scan in the cloud.
