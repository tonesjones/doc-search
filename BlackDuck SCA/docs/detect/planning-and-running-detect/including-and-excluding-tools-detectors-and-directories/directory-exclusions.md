---
title: "Directory Exclusions"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/directory-exclusions.html"
content_id: "eDGv~IQXoFTLF1r_P8ws7g"
version: "11.5.1"
section: "Planning and running Detect"
scraped_at: "2026-08-08T23:44:35.132212+00:00"
---

# Directory Exclusions

Use detect.excluded.directories to exclude directories from search when looking for detectors, searching for files to binary scan when using property `detect.binary.scan.file.name.patterns`, and when finding paths to pass to the signature scanner as values for an '--exclude' flag.

## Exclude directories by name

This property accepts explicit directory names, as well as globbing-style wildcard patterns.
See configuring property wildcards for more info.

**Examples with a folder structure containing:**

- /projectRoot/foobar
- /projectRoot/bar
- /projectRoot/foo/bar
- /projectRoot/foo/bar2

| Value | Excluded at default exclusion depth | Not Excluded |
| --- | --- | --- |
| `foo` | `/projectRoot/foo` | `/projectRoot/foobar` & `/projectRoot/bar` |
| `*bar` | `/projectRoot/foo/bar`, `/projectRoot/bar` & `/projectRoot/foobar` | `/projectRoot/foo/bar2` |

## Exclude directories by path

This property accepts explicit paths relative to the project's root, or you may specify glob-style patterns.

Important:
When specifying path patterns:

- * Use '*' to match 0 or more directory name characters (will not cross directory boundaries).
- * Use '**' to match 0 or more directory path characters (will cross directory boundaries).

**Examples with a folder structure containing:**

- /projectRoot/foobar
- /projectRoot/bar
- /projectRoot/foo/bar
- /projectRoot/dir/foo
- /projectRoot/dir/foo/bar
- /projectRoot/directory/bar

| Value | Excluded at default exclusion depth | Not Excluded |
| --- | --- | --- |
| `foo/bar` | `/projectRoot/foo/bar` `/projectRoot/dir/foo/bar` | `/projectRoot/bar` `/projectRoot/dir/foo` `/projectRoot/foobar` `/projectRoot/directory/bar` |
| `**/foo/bar/` | `/projectRoot/foo/bar` `/projectRoot/dir/foo/bar` | `/projectRoot/foobar` `/projectRoot/bar` `/projectRoot/directory/bar` |
| `/projectRoot/d*/*` | None | All |

Detect uses FileSystem::getPatchMatcher and its glob syntax implementation to exclude path patterns. See [Oracle FileSystem::getPatchMatcher](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/nio/file/FileSystem.html#getPathMatcher(java.lang.String)) for more info.

Note: Exclusion depth is controlled by related properties. Unless the appropriate
search depth property is set to a value greater than, or equal to, the nesting level of the
target directory, a */foo/bar/* pattern will only exclude a root-level match.

By default, only root-level directories are excluded. To exclude directories at deeper levels,
you must configure the following properties:

- detect.excluded.directories.search.depth — controls exclusion depth for signature scanner
- detect.binary.scan.search.depth — controls exclusion depth for binary scan file matching

### Wildcards in relative path patterns

When excluding paths, if you want to use wildcards in an exclusion pattern for a relative path, there are some important rules.

Name-wildcards ('*'), unless appearing in a pattern that begins with path-wildcards ('**'), will only work if the pattern refers to one-level below the source path root.

To exclude /projectRoot/folder while scanning /projectRoot with the following structure:

**Examples with a folder structure containing:**

- /projectRoot/folder
- /projectRoot/folder/dir

| Value | Excluded at default exclusion depth | Not Excluded |
| --- | --- | --- |
| `f*` | `/projectRoot/folder` | NA |
| `folder/*` | NA | `/projectRoot/folder` or `/projectRoot/folder/dir` |
| `**folder/*` | `/projectRoot/folder/dir` | `/projectRoot/folder` |
| `*older/*` | NA | `/projectRoot/folder` or `/projectRoot/folder/dir` |
| `**/*older/*` | `/projectRoot/folder/dir` | `/projectRoot/folder` |

With the search depth set to 10 via the following properties:
`--detect.detector.search.depth=10`
`--detect.excluded.directories.search.depth=10`

| Value | Excluded at depth 10 | Not Excluded |
| --- | --- | --- |
| `f*` | `/projectRoot/folder` `/projectRoot/folder/dir` | NA |

### Related properties:

- detect.excluded.directories.defaults.disabled
- detect.excluded.directories.search.depth
- detect.binary.scan.file.name.patterns
