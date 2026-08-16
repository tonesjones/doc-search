---
title: "Point and Scan, the Coverity CLI, and file usage"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/point-and-scan-the-coverity-cli-and-file-usage.html"
content_id: "Bu0KMRr~JRbhLKCLA9jwnw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:44.639742+00:00"
---

# Point and Scan, the Coverity CLI, and file usage

Point and Scan and the Coverity CLI can identify the following types of files:

| File Type | Description |
| --- | --- |
| Project | A project file: For example, Maven pom.xml, Gradle build.gradle, and so forth. |
| Source | The file contains source code for a particular programming language. For example, sourceCode.java is expected to contain Java source code. |
| Binary | A binary file containing executable code. For example, binaryCode.jar is expected to contain executable code. |
| Configuration | A configuration file: For example, a YAML file or a JSON file. |
| Text | A text file: For example, README.txt. |
| Unknown | The file classification does not fall into one of the other listed categories. |

Note:
The number of issues for JavaScript code that you can discover using the Coverity CLI might exceed the number you would discover
using the `cov-build --war` command. This could be because the
default Coverity configuration ignores the dist directory and its
contents. The Coverity CLI is intended to capture and report as much as possible; you
can limit what is captured if there is too much noise.

Important:
When using the Coverity CLI, file inclusions and exclusions apply *only* to files captured by scanning the file system.
Files that are captured by observing a build process are *always* captured.
For example, if the Coverity CLI is invoked by a command line such as `coverity scan -- make`, any files that are observed to be compiled by the
`make` command will be captured regardless of which directory they are in or of the presence of any specified file inclusions or exclusions.
