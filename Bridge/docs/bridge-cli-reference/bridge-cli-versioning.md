---
title: "Bridge CLI versioning"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/bridge-cli-versioning.html"
content_id: "SFMWFXZ6gwFEM78yR_9iFg"
version: "latest"
section: "Bridge CLI reference"
scraped_at: "2026-08-08T23:47:33.237561+00:00"
---

# Bridge CLI versioning

Bridge CLI is distributed as a bundle that contains multiple workflows and binaries, each with its own version. As a result, logs and commands may display different version numbers, which is expected behavior.

Bridge CLI is not delivered as a standalone binary. Instead, it is distributed as a **self-contained bundle** that includes the Bridge CLI binary and workflows.

Each binary and workflow within the bundle is versioned independently. The bundle itself also has a version that represents the specific release of that collection of components.

## Why different versions may appear in logs

During execution, logs may display more than one version number. For example:

- The Bridge CLI bundle version (for example, `4.2.1`)
- The version of an individual workflow (for example, `3.0.555` for the Polaris workflow)

This does not indicate a version mismatch or installation problem. The bundle version identifies the overall Polaris release, while workflow and adapter versions identify the specific components being executed from within that bundle.

## Bundle versioning behavior

Bridge CLI bundles follow semantic versioning:

- **Major version** : Indicates breaking changes.
- **Minor version** : Introduces new features.
- **Patch version** : Delivers bug fixes or hotfixes.

A new bundle version is released whenever there are changes to workflows or the Bridge CLI binary itself.

The Bridge CLI binary version may remain unchanged between bundle releases if the update affects only workflows or adapters.

## Relationship between bundle version and component versions

A Bridge CLI bundle is immutable once released. Versions of the Bridge CLI binary and workflows included in the bundle do not change without releasing a new bundle version.

Compatibility and deprecation statements (for example, references to minimum supported Bridge versions) always refer to the **bundle version**, not to individual workflow or binary versions.

## Identifying the Bridge CLI bundle version

The bundle version can be identified using one or more of the following methods:

- The `versions.txt` file included in the root of the Bridge CLI bundle archive.
- The folder name or file name of the Bridge CLI bundle within the Bridge CLI [Black Duck repository](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/).
- The [`versions.txt`](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/) file present in the `latest` directory for the Bridge CLI bundle in the Black Duck repository.

## Available binaries and workflows

The Bridge CLI bundle provides the `list` command to list the binary tools and workflows. To list them, run:

```
bridge-cli --list
```

Example output:

```
Tools:
 - bridge-cli
 - file-replacer
Workflows:
 - bitbucket-pipe-executor
 - blackducksca
 - commenter
 - common
 - connect
 - coverity-tool
 - detect-tool
 - downloader
 - fixpr
 - gitlab-template-executor
 - issues-creator
 - list-languages
 - polaris
 - polaris-secure-tunnel
 - scm
 - signal
 - source-zipper
 - srm
```

Tools are standalone binaries included in the bundle. Workflows are the scanning and integration components that Bridge orchestrates when running security scans.

## Listing available versions for a binary or workflow

To list the available versions for a specific binary tool or workflow, pass the name as an argument to `--list`:

```
bridge-cli --list <workflow-or-binary-tool-name>
```

For example, to list available versions for the Polaris workflow:

```
bridge-cli --list polaris
```

Example output:

```
polaris
 - 3.0.555 (installed) "latest"
 - 3.0.552
 - 3.0.550
 ...
```

The `(installed)` label indicates the version currently present in the bundle. The `latest` label indicates the most recent available version.
