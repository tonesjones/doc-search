---
title: "Exclude files or directories from Coverity Analysis"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/exclude-files-or-directories-from-coverity-analysis.html"
content_id: "e4STs7do8dI3bnOisOv6uQ"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:52.995174+00:00"
---

# Exclude files or directories from Coverity Analysis

You can exclude files or directories from Coverity Analysis scans.

CAUTION:

This functionality applies when using the Coverity tools and not when using Polaris scans.

There are two ways to exclude files or directories from a Coverity Analysis scan, as the following sections describe.

## • Use your configuration file

Add the following `"settings"` section to the configuration file.
Here is an example in JSON format:

```
{
    "type": "Coverity configuration",
    "format_version": 1,
    "format_minor_version": 7,
    "settings": {
        "cov_run_desktop": {
            "ignore_all_files_regex":"<regex>"
        }
    }
}
```

## • Use the Advanced options for your Coverity scan configuration

Add the option string to the Coverity section of the Advanced section of the
Scan Configuration dialog (IntelliJ) or tab (VS Code).

Figure 1. `--ignore-all-files-regex` option in a Coverity scan configuration for IntelliJ
  
 [image: Advanced scan configuration for Coverity showing the --ignore-all-files-regex option (IntelliJ)]

Figure 2. `--ignore-all-files-regex` option in a Coverity scan configuration for VS Code
  
 [image: Advanced scan configuration for Coverity showing the --ignore-all-files-regex option (VS Code)]

## The regular expression

In either case, the format of the string represented by `<regex>` depends on the
operating system that you use:

Linus or macOS
:   Here is an example:

    `.*/<folder_name>/.*`

Windows
:   Here is an example:

    `.*\\\\<folder_name>\\\\.*`
