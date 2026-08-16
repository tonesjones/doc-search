---
title: "Building Projects that use Xcode 10"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/building-projects-that-use-xcode-10.html"
content_id: "fpt1oAmUFyjqdOaDd~e99Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:30.337521+00:00"
---

# Building Projects that use Xcode 10

Coverity does not support the Apple modern build system for Xcode 10. Attempting to capture C,
C++, or Objective-C source code compiled with Clang will result in a 0% capture rate. To
work around this issue, configure the project to use the legacy build system. You can do
this within the Xcode IDE by selecting the File > Project Settings or File > Workspace Settings menu option, then selecting Legacy Build System
from the drop-down option for Build System.

Alternatively, at build time you can choose to use the legacy build system, instead of the
modern build system, by passing the `-UseModernBuildSystem=NO` option to
`xcodebuild`.
