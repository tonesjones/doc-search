---
title: "Capturing a specific set of files"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/capturing-a-specific-set-of-files.html"
content_id: "qovVZOVqu5ZLLa0rlPUQPg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:55.539855+00:00"
---

# Capturing a specific set of files

The `files` option's `include-list-file` setting allows you to specify a file that contains a list of source file paths to include in the capture.
Each line in the file should represent a single file path.

For example, suppose you have a file named file-list.txt with the following contents:

```
src/main/java/com/example/App.java
src/main/java/com/example/Utils.java
```

... then your configuration would look like this:

```
capture:
    files:
        include-list-file: file-list.txt
```

You can combine this configuration with other include/exclude patterns, as needed.

## Verifying that the correct set of files has been captured

You can use the `coverity list` command to verify what has been captured.
When you configure file inclusions and exclusions, we strongly recommended that you run `coverity capture` and then `coverity list`
to confirm that the set of files that were captured matches your expectations.

Globs and regular expressions can be tricky to specify correctly.
Using `coverity list` is an effective way to ensure that the right set of files will be analyzed.
