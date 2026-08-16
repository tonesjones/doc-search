---
title: "Modifying the default usage"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/modifying-the-default-usage.html"
content_id: "Bgx4883iSZnxR_xUKF8lzA"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:00.886424+00:00"
---

# Modifying the default usage

[HUB-17092]Usage indicates how a
component is intended to be included in the project when this version is released.

Possible usage values are:

- Statically Linked. A tightly-integrated component that is statically linked in
  and distributed with your project.
- Dynamically Linked. A moderately-integrated component that is dynamically linked
  in, such as with DLLs or .jar files.
- Source Code. Source code such as .java or .cpp files.
- Dev Tool / Excluded. Component will not be included in the released project. For
  example, a component that is used internally for building, development, or
  testing. Examples are unit tests, IDE files, or a compiler.
- Separate Work. Intended for loosely-integrated components. Your work is not
  derived from the component. To be considered a separate work, your application
  has its own executables, with no linking between the component and your
  application. An example is including the free Acrobat PDF Viewer with your
  distribution media.
- Implementation of Standard. Intended for cases where you implemented according to
  a standard. For example, a Java spec request that ships with your project.
- Merely Aggregated. Intended for components that your project does not use or
  depend upon in any way, although they may be on the same media. For example, a
  sample version of an unrelated product included with your distribution.
- Prerequisite. Intended for components that are required but not provided by your
  distribution.
- Unspecified. The usage for this component has not yet been determined.

In Black Duck version 2020.10.0, Black Duck introduced the UNSPECIFIED
usage value, which you can use as a default option instead of existing defaults to
eliminate confusion over whether the component is assigned a true usage value or a
default usage value. For example, if you use DYNAMICALLY_LINKED as the default usage
value, you might not be able to distinguish between components that have a true usage
value of DYNAMICALLY_LINKED and those components that are assigned the usage value by
default. By using UNSPECIFIED as the usage default, you know that you should take action
to assign a valid usage value when you see UNSPECIFIED assigned as the usage value.

The default usage is determined by match type: Snippets have a usage of Source Code while
all other match types are Dynamically Linked.

Black Duck uses the following variables so that you can change the
default usage for similar match types:

- BLACKDUCK_HUB_FILE_USAGE_DEFAULT. Defining a usage for this variable sets the
  default value for the following match types:
  - Binary
  - Exact Directory
  - Exact File
  - Files Added/Deleted
  - Files Modified
  - Partial
- BLACKDUCK_HUB_DEPENDENCY_USAGE_DEFAULT. Defining a usage for this variable sets the
  default value for the following match types:
  - File Dependency
  - Direct Dependency
  - Transitive Dependency
- BLACKDUCK_HUB_SOURCE_USAGE_DEFAULT. Defining a usage for this variable sets the
  default value for the following match types:
  - Snippet
- BLACKDUCK_HUB_MANUAL_USAGE_DEFAULT. Defining a usage for this variable sets the
  default value for the following match types:
  - Manually Added
  - Manually Identified
- BLACKDUCK_HUB_SHOW_UNMATCHED: Determines whether the unmatched component count is
  shown. The default is false (not shown).

## Match Types for bdio2 uploaded jsonld/bdio file

The default usage for these matches is Dynamically Linked.

- Direct Dependency Binary

- Transitive Dependency Binary

These are full-file matches same as the existing binary matches.

A single file can have multiple Transitive Dependency Binary matches, but only one
Direct Dependency Binary.

To configure different usage values:

1. Edit the `blackduck-config.env` file located in the
   `docker-swarm` directory to the new usage values by
   removing the comment icon (#) and entering a value. Use one of the usage
   values as shown in the file: SOURCE_CODE, STATICALLY_LINKED,
   DYNAMICALLY_LINKED, SEPARATE_WORK, IMPLEMENTATION_OF_STANDARD,
   DEV_TOOL_EXCLUDED, MERELY_AGGREGATED, PREREQUISITE, UNSPECIFIED

   For example, to change default usage for files to Unspecified:

   ```
   BLACKDUCK_HUB_FILE_USAGE_DEFAULT=UNSPECIFIED
   ```

   Note: If you enter the incorrect usage text, the original default value will still apply. A
   warning message will appear in the log files of the jobrunner
   container.

The modified usage values apply to any new scans or rescans.
