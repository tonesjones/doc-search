---
title: "How do I enable Coverity (SAST) scans within Visual Studio Code?"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/how-do-i-enable-coverity-sast-scans-within-visual-studio-code-.html"
content_id: "KCyUX37XWBWKguAGN2Vy~w"
version: "2026.9.0"
section: "Installing Code Sight"
scraped_at: "2026-10-06T23:39:50.801800+00:00"
---

# How do I enable Coverity (SAST) scans within Visual Studio Code?

To scan source with Coverity in VS Code, scripted languages need no additional setup,
but compiled languages need to be configured in a configuration file.

Note:
This topic applies only to Coverity scans.
Rapid Scan Static can scan source code and text-based metadata without any additional setup.

- If you want Coverity to scan code in an interpreted language (that is, a scripted language such as JavaScript or Python), then no setup is required.
- If you want Coverity to scan code in a compiled language (such as C, C++, Java, and so on), then a
  a configuration file needs to be set up so that it specifies the particular build and clean tools used by your project.

  For instructions on how to do so, please see the section that follows.

## Setting up build tools for Visual Studio Code

Visual Studio Code is characterized as a “source-code editor” rather than
an “integrated development environment”.
As such, it does not have built-in build tools.
To run Code Sight as an extension to VS Code, and have it scan compiled languages, you need to first
specify the build and clean commands that Coverity Analysis will use.

**Be aware:**
VS Code requires this custom configuration only for compiled languages.
However, if you add this JSON code to the configuration file, the newly specified build tools will be used by
*any* Code Sight extension or plug-in that employs this confiiguration file.
The configuration change overrides any IDE’s default build and clean commands.

To set up the tools, add a `"settings"` field to the configuration file.
The `"settings"` field should contain, in turn, two fields:

1. A `"cov_run_desktop"`
   field that specifies the build and clean commands to use.
2. An `"ide"` field with a `"build_strategy"`
   field set to `"CUSTOM"`.

Here is a JSON code example of such a `"settings"` field:

```
    "settings" : {
        "cov_run_desktop" : {
            "build_cmd" : ["make", "all"],
            "clean_cmd" : ["make", "clean"]
        },
        "ide" : {
            "build_strategy" : "CUSTOM"
        }
    }
```

... Which tells Coverity Desktop to build a project with the `make all` command, and to
clean up after a build with the `make clean` command.

To build a project using Apache Maven instead of `make`, you could use
the following `"cov_run_desktop"` settings:

```
    "settings" : {
        "cov_run_desktop" : {
            "build_cmd" : ["mvn", "compile"],
            "clean_cmd" : ["mvn", "clean"]
        },
        "ide" : {
            "build_strategy" : "CUSTOM"
        }
    }
```

For a complete example of such a configuration file, see
Specifying custom build tools.
