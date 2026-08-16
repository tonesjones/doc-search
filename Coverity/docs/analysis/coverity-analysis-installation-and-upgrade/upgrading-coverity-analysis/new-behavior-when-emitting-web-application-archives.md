---
title: "New behavior when emitting web application archives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/new-behavior-when-emitting-web-application-archives.html"
content_id: "HeU2SFAN5iW9oFbm4bP2pA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:45:20.556961+00:00"
---

# New behavior when emitting web application archives

Emitting a web application archive (`.WAR` file, `.EAR`
file, or equivalent unpacked directory) with `cov-emit-java`
`--war`, `--ear`, or similar now emits JavaScript code in
that webapp archive. Users who emit such files might see an increase in lines of code
analyzed, analysis runtime, and defects reported. You can disable emission of JavaScript
code by specifying the `--skip-emit-war-javascript-source` option with
the `cov-emit-java` command.
