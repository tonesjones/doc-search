---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "s_nvmEl4wKBO0Y4Q1XnHlA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:36.553982+00:00"
---

# Description

The `cov-emit-java` command parses Java source code and bytecode, and
saves `javac` outputs. It stores these outputs to an emit repository for
subsequent static analysis and outputs it into a directory (emit repository) that can
later be analyzed with `cov-analyze`. The
`cov-emit-java` command is typically called by
`cov-build`.

You need to invoke this command when you are running Java Web application security
analysis and in the rare case that you cannot compile your Java code with
`cov-build`. For details about the latter case, see the discussion
of the alternative build process in the Coverity Analysis.

When specifying multiple source files, you need to separate each source file by a space,
for example:

`src/pkg/SomeClass.java src/pkg/OtherClass.java`

Note that you can specify the options to `cov-emit-java` in any order,
but the list of source files must appear last.
