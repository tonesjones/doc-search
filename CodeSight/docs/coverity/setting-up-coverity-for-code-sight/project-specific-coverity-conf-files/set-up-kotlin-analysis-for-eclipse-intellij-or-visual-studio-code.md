---
title: "Set up Kotlin analysis for Eclipse, IntelliJ, or Visual Studio Code"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/set-up-kotlin-analysis-for-eclipse-intellij-or-visual-studio-code.html"
content_id: "BQm8QI9B~ywaboSDUTktDA"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:53.094230+00:00"
---

# Set up Kotlin analysis for Eclipse, IntelliJ, or Visual Studio Code

While running Coverity Analysis 2022.12.0 or a later version of Coverity,
the Eclipse, IntelliJ, and VS Code development environments can analyze Kotlin source code.
Some additional setup is required.

In the configuration file that you use, add the string `"--kotlin"` to the compiler configuration settings.
In the same file, specify custom `build` and `clean` commands that are compatible with Kotlin.

The following code sample shows a bare-minimum JSON configuration file that can be used to analyze a Kotlin project:

```
{
    "type": "Coverity configuration",
    "format_version": 1,
    "format_minor_version": 7,
    "settings": {
        "cov_run_desktop": {       
            "build_cmd": ["gradle", "build"],
            "clean_cmd": ["gradle", "clean"]     
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

Attention:
In certain cases, when the Gradle® build files have been configured to override the
standard Kotlin compilation strategy, you might need to add the following option to the invocation of
the `build` command:

```
-Pkotlin.compiler.execution.strategy=in-process
```
