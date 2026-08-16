---
title: "Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/analysis.html"
content_id: "QHX4kB02T616bVSXmn~Vqw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:33.485737+00:00"
---

# Analysis

In this chapter we describe concisely what Coverity Fortran Syntax Analysis actually does
and what the generated output means. The analysis is carried out in four stages: the
analysis of the separate program units, the generation and analysis of the reference
structure (call tree), the determination of the dependencies of modules, and the
analysis of the integral program. Command-line options determine which of the analysis
stages are activated. Beside specifying these options you can specify language
extensions and analysis options in the configuration file used.
