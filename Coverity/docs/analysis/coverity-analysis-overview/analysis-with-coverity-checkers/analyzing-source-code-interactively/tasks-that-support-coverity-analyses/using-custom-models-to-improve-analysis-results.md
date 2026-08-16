---
title: "Using custom models to improve analysis results"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-custom-models-to-improve-analysis-results.html"
content_id: "G4nxqvxpe5~PtbWVpX0LiQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:56.770900+00:00"
---

# Using custom models to improve analysis results

A custom model is a piece of source code that is written by a developer to replace the
actual implementation of a function or method. Custom models can lead to a more accurate
analysis by helping Coverity Analysis find more issues and eliminate false positive
results. Candidates for modeling include functions and methods in your source code that
the analysis interprets in an unexpected way
(see Using models to tune the interprocedural analysis) and/or functions and
methods in third-party libraries that Coverity does not model
(Using models to mimic functions or methods that lack source code).

After a developer writes a custom model (for details, see
"Models and primitives" in
Customizing Coverity), you (the administrator) need to include it in
the analysis configuration by running the `cov-make-library` command
(see `cov-make-library` in the Coverity 2026.6.0 Command Reference).
The `cov-make-library` command creates a file called
user_db that you need to include in the script that runs
Coverity Analysis.

For further information, also see the "Models and primitives" chapter
