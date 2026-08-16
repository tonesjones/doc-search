---
title: "coverity capture"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-capture.html"
content_id: "9yyxFGddblNscTwF_ducZA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:57.242465+00:00"
---

# coverity capture

Capture source files for analysis.

## Synopsis

```
coverity capture [options] [-- <build-command>...]
coverity capture (-h | --help)
```

## Description

The coverity capture command captures source files inside the
given project directory to prepare them for analysis.

## Options

--archive-file <archive-file>
:   An archive file (zip or tar.gz) containing
    the code to capture. If --project-dir is also specified, the archive is extracted
    to that path instead of to a folder with the same name as the archive.

-- build-command
:   Optional. A command used to capture the project by monitoring the build process for
    compiler invocations and then replaying them using the appropriate Coverity
    compiler. In other words, this is equivalent to doing the following, where
    mvn -DskipTests clean install is the build command.

    ```
    coverity capture --dir idir -- mvn -DskipTests clean install
    ```

-h, --help
:   Displays the information in this section.

--project-dir project-dir-name
:   Project directory containing the source files to capture. If not
    specified, defaults to the current working directory.

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
:   Specifies a URL for a source repository that contains the code to capture.

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

--local results-dir-name
:   Complete analysis locally and save the results to the specified
    directory.

-o, --config-override key=val
:   Key and value to override in configuration.
