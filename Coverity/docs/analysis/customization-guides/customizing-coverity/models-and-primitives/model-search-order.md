---
title: "Model search order"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/model-search-order.html"
content_id: "tqSFdWhwSrP~KEvCasrnqQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:29.885965+00:00"
---

# Model search order

During analysis, Coverity gives priority to custom, user models over its built-in or
derived models.

The `cov-analyze` command searches models in the following
order:

1. Custom (user) model files specified by the `--model-file` option,
   in the order that they appear on the command line.

   This use of
   `--model-file` is equivalent to the use of the
   `--user-model-file` option, but
   `--user-model-file` was deprecated in version
   7.7.0.
2. Models defined in user_models.xmldb, if such a file is
   present in the config/ directory.
3. Built-in Coverity models.
4. Derived models created during the current analysis scan.
5. C/C++ only: Previously derived models passed via the
   `cov-analyze` option `--model-file`, in
   the order that they appear on the command line.

   This use of
   `--model-file` is equivalent to the use of the
   `--derived-model-file` option, but
   `--derived-model-file` was deprecated in version
   7.7.0.

Note: The `--model-file` can specify either user or derived model files.
It automatically detects whether the files represent custom (user) models created by
`cov-make-library`, or previously derived models
created by `cov-collect-models`.
