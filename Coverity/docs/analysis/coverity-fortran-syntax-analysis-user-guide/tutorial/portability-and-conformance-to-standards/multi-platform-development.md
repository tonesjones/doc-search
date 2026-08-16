---
title: "Multi-platform development"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/multi-platform-development.html"
content_id: "xEXf~wtMj28_AZSGzLtg9w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:58.193440+00:00"
---

# Multi-platform development

If your code is standard-conforming, you will have minimal problems in porting the
pro­gram to various platforms. By creating a configuration file that is the intersection
of the language extensions available among all the platforms you support, portability
violations can be flagged with ease. Platform-specific code is analyzed correctly, since
cpp-like preprocessing is supported by Coverity Fortran Syntax Analysis.

Some types can be different on the various platforms. In that case, consistent analysis
will require the creation of a different configuration file for those different
platforms.

Coverity Fortran Syntax Analysis presents a warning if you use an implicit type in one
place in the code and the explicit type in another, e.g. when associating arguments,
because that implies a portability risk.
