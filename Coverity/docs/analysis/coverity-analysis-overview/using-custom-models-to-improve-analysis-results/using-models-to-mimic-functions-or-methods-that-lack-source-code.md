---
title: "Using models to mimic functions or methods that lack source code"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-models-to-mimic-functions-or-methods-that-lack-source-code.html"
content_id: "1ar2pZRdXCba2ISR3y1l7w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:57.417474+00:00"
---

# Using models to mimic functions or methods that lack source code

Most project code bases include a number of library functions or methods without
including their source code. Coverity Analysis cannot always analyze a function or
method if its source code is not in the code base.

For example, Coverity Analysis cannot analyze certain third-party binary libraries that
are linked to a program. Coverity Analysis *can* analyze Java Virtual Machine (JVM)
and .NET Core / .NET bytecode. In either case, it does not report defects in binary
libraries, but analyzing or modeling libraries improves the accuracy of the source code
analysis.

Coverity Analysis ships with models for most standard libraries that pertain to the
languages and platforms that Coverity Analysis supports. You do not have to model these
libraries and in general you should not alter the models provided. (You can the examine
source code for these models to learn more about writing your own custom models.) Due to
the limitations of interprocedural analysis, you might need to perform some tuning: See
Using models to tune the interprocedural analysis.

To improve the analysis of code that uses functions or methods from nonstandard
libraries, you can add custom models that emulate these functions.

Tip: The most common and useful custom models are allocators/deallocators and
*killpaths* (functions that terminate execution). Resource leaks cannot be
found without allocation models. If Coverity Analysis does not find any resource leaks,
you probably need to create allocation models for every function that behaves as an
allocator and deallocator.

If Coverity Analysis generates many false positives, it
might mean that there are missing killpath models. For more information, see "Model for adding a
killpath to a function" in the Coverity 2026.6.0 Checker Reference.
