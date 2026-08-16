---
title: "Default exclusions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/default-exclusions.html"
content_id: "uOCg2KViqgQlrim4e9SdzQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:54.906223+00:00"
---

# Default exclusions

By default, Coverity excludes certain files and directories from capture.
These default exclusions apply *only* to files inside the project directory.

These are the files and directories that are excluded by default:

- Files in directories with the following names:
  - vendor/
  - node_modules/
  - __MACOSX
- Files in hidden directories (directories whose name begins with a .), except that:
  - .terraform/ directories *are not* excluded.
- Files in a Carthage/ directory provided a Cartfile is present.
- Files in a Pods/ directory provided a Podfile is present.

## Overriding defaults

You can override these default exclusions by using the following `files` option key values:

- `include-glob` or `include-regex`

  To expliciitly include matching files.
- `include-dirs`

  To include specific directory names that would otherwise be excluded.

## Example

To include files from a normally excluded vendor/ directory:

```
capture:
    files:
        include-dirs:
            - vendor
```
