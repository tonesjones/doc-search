---
title: "Point and Scan and the CLI Support matrix"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/point-and-scan-and-the-cli-support-matrix.html"
content_id: "Cv8d_Z1yNTzIjpI~FYNUAw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:23.794974+00:00"
---

# Point and Scan and the CLI Support matrix

Point and Scan and the Coverity CLI support the following platforms and languages:

| Language | Operating system and architecture | Build capture support? | Buildless capture support? | Thin client support? |
| --- | --- | --- | --- | --- |
| Apex | All | N/A | yes | yes |
| C/C++ | All | yes | - | yes |
| Objective-C/C++ | macOS Intel, macOS on Apple silicon,  Linux Intel 64-bit, Windows Intel 64-bit only | yes | - | yes |
| C# | Linux Intel 64-bit, Windows Intel 64-bit only | yes | yes | yes |
| Dart | All | N/A | yes | yes |
| Go | All | yes | yes | yes |
| Java | All | yes | yes | yes |
| JavaScript/TypeScript | All | N/A | yes | yes |
| Kotlin | macOS Intel, macOS on Apple silicon,  Linux Intel 64-bit, Windows Intel 64-bit only | yes | - | yes |
| PHP | All | N/A | yes | yes |
| Python | All | N/A | yes | yes |
| Ruby | All | N/A | yes | yes |
| Scala | All | N/A | yes | yes |
| SQL | All | N/A | yes | yes |
| Swift | All | N/A | yes | yes |
| Visual Basic | Linux Intel 64-bit, Windows Intel 64-bit only | yes | - | yes |

Entries with "All" for the operating system indicate that the corresponding language has the associated capabilities on
all of the operating systems and architecture combinations that are supported by the Coverity CLI. These are as follows:

- Windows Intel 64-bit
- Linux Intel 64-bit
- Linux ARM 64-bit
- macOS Intel
- macOS on Apple silicon

Entries with "N/A" for "Build capture support" indicate interpreted (scripted) languages, for which build capture does not apply.
These languages require you to use buildless capture.

Buildless capture of compiled languages is not supported with the thin client with the
exception of Dart, Scala, and Swift. In other words, buildless capture of C# and Java is
NOT supported with the thin client.
