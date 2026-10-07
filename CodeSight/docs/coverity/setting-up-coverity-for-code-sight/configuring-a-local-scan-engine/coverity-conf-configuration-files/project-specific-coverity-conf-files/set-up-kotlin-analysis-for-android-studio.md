---
title: "Set up Kotlin analysis for Android Studio"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/set-up-kotlin-analysis-for-android-studio.html"
content_id: "rKSjIOLjh7mQtX~RWrKixw"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:53.050812+00:00"
---

# Set up Kotlin analysis for Android Studio

While running Coverity Analysis 2022.3.1 or a later version of Coverity,
the Android Studio development environment can analyze Kotlin source code and combined Kotlin/Java projects.
Some additional setup is required.

## Setting up Kotlin analysis

To enable Kotlin analysis in Android Studio, you must first run the `cov-configure --kotlin` command to enable the
build capture of Kotlin Android source and the filesystem capture of Android configuration files.

You also need to specify --fs-capture-search when you invoke the `cov-build` command.
Coverity will capture Kotlin Android files that are needed by the analysis, including the manifest
(AndroidManifest.xml) and the layout resource files.

No special flags are needed for the `cov-analyze` command, because Kotlin checkers are enabled by default.

## Setting up Kotlin/Java analysis

Run both `cov-configure --java` and `cov-configure --kotlin` to enable the build capture of both Java and Kotlin Android source
and the filesystem capture of Android configuration files. (Filesystem capture can be used as a fallback only for Java.)

Pass --fs-capture-search to the `cov-build` command.
Coverity will capture Java and Kotlin Android files that are needed by the analysis,
including the manifest (AndroidManifest.xml) and the layout resource files.

Specify --android-security when you invoke the `cov-analyze` command.

Note:
Coverity analyzes Java and Kotlin source code separately.

## A sample JSON configuration for both use cases

Here is an example of a JSON configuration file that meets the requirements for analyzing Kotlin and analyzing a Kotlin/Java combined project:

```
{
    "type": "Coverity configuration",
    "format_version": 1,
    "format_minor_version": 7,
    "settings": {
        "cov_run_desktop": {
            "build_cmd": ["./gradlew", "build"],
            "build_options": [
                "--fs-capture-search", "<project_directory>"
            ],
            "analysis_args":["--android-security"],
            "clean_cmd": ["./gradlew", "clean"]
        },
                
        "ide": {
            "build_strategy": "CUSTOM"
        },
        "add_compiler_configurations": [
             { "cov_configure_args": ["--kotlin"] }
        ]

    }
}
```
