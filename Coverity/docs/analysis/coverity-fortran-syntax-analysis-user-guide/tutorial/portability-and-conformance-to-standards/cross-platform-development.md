---
title: "Cross-platform development"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cross-platform-development.html"
content_id: "zt7Vj8y6ZBxr8U3s6r83MQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:56.912440+00:00"
---

# Cross-platform development

Coverity Fortran Syntax Analysis can also be used for cross-platform development. By
specifying the compiler emulation file of the target platform Coverity Fortran Syntax
Analysis will analyze the program as if you were compiling on that target. Problems
might arise when include files are being used which are not available, or have filenames
that are not acceptable on the host. See the next subsection. It could also be necessary
to create interfaces for system calls that are not known on the host.
