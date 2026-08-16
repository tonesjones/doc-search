---
title: "Running analyses that use derived models for C and C++ source code"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/running-analyses-that-use-derived-models-for-c-and-c-source-code.html"
content_id: "ZNFEuu0vHRRFsqjFRMKMYQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:21.684526+00:00"
---

# Running analyses that use derived models for C and C++ source code

Coverity Analysis performs interprocedural analyses that generate models of all the source code that is
analyzed. Because the source code that you are developing often calls functions in
libraries and other peripheral source that are unlikely to change much (if at all), it
can be time-consuming and unnecessary to reanalyze them. To help address this issue,
Coverity Analysis allows you to use the models that were derived from the original
analysis of such code.

After building and completing an analysis of all source code (which includes source code
that is undergoing development and the libraries and other peripheral code that it
uses), you can continue to re-run the analysis on the source code that is undergoing
development. However, instead of always running the analysis directly on the source for
the libraries and other peripheral code, you can make analysis use the models that were
derived from the analysis of the full code base.

**To use derived models:**

1. Generate a derived_models.xmldb file through the
   `--output-file` option to the
   `cov-collect-models` command.

   This is a one-time step to
   perform only after running an analysis of the full code base, including the
   libraries and other peripheral code. You will need to repeat the remaining steps
   according to your internal build and analysis schedule.
2. Pass the file to `cov-analyze` through the
   `--derived-model-file` option.
3. Rebuild only the portion of the code base that is undergoing development, omitting the
   peripheral code bases.

   You typically use `cov-build` for this
   step.
4. Reanalyze the build along with the derived models in
   derived_models.xmldb.

   The
   derived_models.xmldb file is not read by default. When
   you invoke `cov-analyze`, specify the
   .xmldb file by using the
   `--derived_model_file` option.

   For each analyzed
   function call, the model in the derived_models.xmldb file
   for that function is used only if there are no other matching user models (or
   any other models) that are undergoing analysis in the current intermediate
   directory. When developers modify their source files, models will be
   automatically generated for the functions in that code, and any models in the
   derived_models.xmldb file for those functions will be
   ignored because they are outdated.

There will be no links into the details for derived models.
