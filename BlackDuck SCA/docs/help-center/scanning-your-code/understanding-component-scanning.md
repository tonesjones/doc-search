---
title: "Understanding Component Scanning"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/understanding-component-scanning.html"
content_id: "7Y9PO5z66fExOZgbxpwbCg"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:26.698993+00:00"
---

# Understanding Component Scanning

Black Duck Component Scanning is scanning functionality that provides an automated way to determine the set of open source software components that make up a software project. Component Scanning helps organizations manage their use of open source by identifying and cataloging components in order to provide additional metadata such as license, vulnerability, and project health for those components. Component Scanning lets users use the scanner to scan software artifacts on their local computers, which automatically generates a BOM that can be linked to a specific project in Black Duck.

Black Duck Component Scanning can extract the following archive types:

- AR
- ARJ
- CPIO
- DUMP
- TAR
- RPM
- ZIP
- 7z

Archives may optionally be compressed using any of the following compression algorithms:

- Bzip2
- Gzip
- Pack200
- XZ
- LZMA
- Snappy
- Z (compress)
- DEFLATE

During the component scan, Component Scanning examines similarities and differences between large clusters of files and can find:

- Exact matches to unmodified archives and directories of open source.
- Fuzzy matches to modified archives and directories of open source.

It scans an arbitrary file system directory or archive and matches to known components in the Black Duck KnowledgeBase (KB).

The core concept behind component scanning and discovery is the ability to compare the signatures of artifacts in the repository with the signatures of all OSS components in the Black Duck KB and quickly recognize a match. The recognition can be fuzzy—it does not need to be an exact match to be recognized. When there are multiple possible matches, Component Scanning determines the preferred match.

Component Scanning can discover and identify code that is:

- **Unmodified**: A collection of files that have not changed since they were released by the open source project.
- **Renamed**: A collection of files that have been renamed without other modification.
- **Compressed and/or recompiled**: Jars that have been compressed and/or recompiled after they were released by the open source project.
- **Modified or rebundled**: For example, with a jar:
  - Class files from more than one component jar combined into a single jar
  - Class files added to or deleted from a component jar
  - Nested component jars with jar files added or deleted

Component Scanning classifies each match based on how it was made:

- **Exact**: Component Scanning identified the set of files as an exact match to a component in Black Duck KB.
- **File Dependency**. Component Scanning identified a match via a file dependency.
- **Files Modified**: Component Scanning identified a fuzzy match to a component in Black Duck KB, where some of the files were modified. Sometimes this is a match to a previous or subsequent version of the component, which may have been missing from Black Duck KB at the time that the match was made.
- **Files Added/Deleted & Modified:** The component scan identified a fuzzy match to a component in Black Duck KB This can happen when:
  - An OSS component is matched, but some of the files associated with the component have been added, deleted, or modified. This can be a match to a previous or a subsequent version of the component, which may have been missing from Black Duck KB at the time of the match.
  - A component is only matched against a common directory structure (structure-only), but because a significant number of components share this structure, Black Duck KB may propose a match that has very little similarity to the scanned component.
  - A component is only matched against a common directory structure, but because proprietary or third-party code can share a common directory structure with components, Black Duck KB may propose a match that has very little similarity to the scanned code.

  The Black Duck KB contains a 'blacklist' of very common, non-unique, directory tree structures. For example, many components include a directory that contains three subdirectories: 'css', 'img', and 'js'. This structure has been blacklisted, so that Black Duck KB will not propose irrelevant matches.

## Supported languages

For the current list of supported languages, refer to the list of supported languages shown in the [Black Duck Detect documentation](https://docs.blackduck.com/p/detect).

Component Scanning currently supports the ability to identify components containing Java binaries, JavaScript, or C (C, C++, C#) binaries and source code and Ruby, Python, Scala, Objective C, Swift; PHP, R, Go, Erlang, and Perl.

For example, scanning can identify open source components based on directories that contain C, C++, or C# source files (i.e., files with the following extensions: .c, .c++, .cc, .cpp, .cs, .cxx, .h, .hh, .hpp, .hxx, .h++, .idl, .rc). That is to say, collections of these files (or partial collections) that are re-used from their original OSS packages with similar directory structures will be matched. As noted above, some files in these collections may be modified, added or removed, and matching will still occur.

## Individual file matching

Individual file matching refers to identifying a component based on the checksum of a single file. However, enabling this feature does not guarantee that every file within an open-source library in the Knowledge Base (KB) will match to its corresponding component. Various factors, including code reuse and the organization of files within the repository, can influence the matching process. Therefore, while individual file matching is a powerful tool, the results may vary based on the specific files being scanned.

Prior to Black Duck 2020.2.0, for a small set of file extensions (`.js`, `.apklib`, `.bin`, `.dll`, `.exe`, `.o`, and `.so`), regular signature scanning matched files to components based upon a checksum match to the one file. Unfortunately, this matching was not always accurate and produced a fair amount of false positives that required you to spend additional effort reviewing and adjusting the BOM. Therefore, individual file matching is no longer the default behavior and instead is an optional capability as of the Black Duck 2020.2.0 release.

This may cause some components to drop off your BOM, which may or may not be desired. Therefore, in the Black Duck 2020.2.0 release, Black Duck provides parameters in the scanning tools so that you can re-enable individual file matching. Refer to the command line parameters for the Signature Scanner CLI and Black Duck Detect documentation for more information.

## ISO files

[HUB-9111] The Signature Scanner cannot scan an ISO file: you must first mount the file to your local file system and then scan the file system.

## Supported package managers

[HUB-8391] Refer to the [Black Duck Detect documentation](https://documentation.blackduck.com/bundle/detect) for a list of supported package managers.

## Scanning tools

Download, install, and scan using one of the following tools:

- Black Duck Detect. [Black Duck Detect](https://documentation.blackduck.com/bundle/detect) is the recommended scanning tool for Black Duck.
- Black Duck Detect Desktop
- Command line  (CLI) version of Signature Scanner.

Tip: Review the Scanning Best Practices Guide for information on the best practices for scanning.
