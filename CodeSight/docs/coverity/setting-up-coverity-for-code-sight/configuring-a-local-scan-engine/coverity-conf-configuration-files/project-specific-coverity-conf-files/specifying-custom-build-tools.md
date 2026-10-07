---
title: "Specifying custom build tools"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/specifying-custom-build-tools.html"
content_id: "hnB_RY7Q4izY~w2wgiU3Rg"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:52.894531+00:00"
---

# Specifying custom build tools

To use build tools that differ from the standard tools used by your development environment,
specify these with a cov_run_desktop object in the configuration file your installation uses.

Here is a sample configuration file in JSON format that contains a
`cov_run_desktop` object:

```
{
    "type": "Coverity configuration",
    "format_version": 1,
    "format_minor_version": 7,
    "settings": {
        "cov_run_desktop": {
            "build_cmd": ["make", "all"],
            "clean_cmd": ["make", "clean"]
        },
        "ide": {
            "build_strategy": "CUSTOM"
        }
    }
}
```

This particular sample configuration sets up a project that uses the `make` build system.
In your own file, you would replace the `"build_cmd"` and `"clean_cmd"`
values with the names of the build and clean commands that your project actually uses.

For example, to use Apache Maven as your build tool, the `"cov_run_desktop"` fields would look like this:

```
        "cov_run_desktop": {
            "build_cmd": ["mvn", "compile"],
            "clean_cmd": ["mvn", "clean"]
        }
```

**Don’t forget:**
In the `"ide"` object, you must set `"build_strategy"`
to equal `"CUSTOM"`. If this field is missing, or is set to a different value,
Code Sight does not recognize the custom settings, or use the alternative tools you specified.
