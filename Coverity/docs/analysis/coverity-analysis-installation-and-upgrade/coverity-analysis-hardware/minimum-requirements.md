---
title: "Minimum requirements"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/minimum-requirements.html"
content_id: "UY4eTZvbzYFUbaL06VyTeQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:46.991502+00:00"
---

# Minimum requirements

Coverity analysis can use hardware CPU parallelism (multiprocessor, multi-core, and
simultaneous multi-threading), assuming adequate additional memory is available. When
sufficient memory is available, Coverity analysis will attempt to make use of it to
improve performance by performing more computation in parallel.

When you start an analysis, Coverity Analysis will automatically compute how many
analysis workers to use based on the amount of memory the analysis requires and how much
memory is available. It will issue a warning if there is not enough memory.

You can use this section to understand memory requirements without starting an
analysis.

Coverity requires a minimum of **3GB**. However, recommended memory varies by use case
as follows:

- *Recommended for C/C++ scanning with default checkers:* 8 GB for projects
  with less than 1 million lines of code; 5GB + 3GB per million lines of code for
  larger projects.
- *Recommended for all other scans:* At least 12 GB. For larger code bases,
  9GB + 3GB per million lines of code.

Memory usage for a scan depends on many complex factors that are difficult to predict.
The best predictor of memory usage for scanning a code base is how much memory a scan of
the same code base took last time.

## Options that impact memory usage

Tuning the analysis with `cov-analyze` options such as
`--max-mem` and `--jobs` affects the required
minimum. By default, Coverity will allocate a number of parallel analysis workers
based on available memory, assuming that each worker consumes 512 MB of memory.
Using `cov-analyze --jobs N` bypasses this computation and instead
uses exactly `N` parallel workers. Using fewer workers consumes less
memory at the expense of less opportunity for parallel computation and thus
potentially longer runtime. Using `cov-analyze --max-mem M` changes
the memory budget for each parallel worker to `M` megabytes (from the
default of `512`); higher `max-mem` means workers are
free to consume more memory, but may lead to fewer workers being allocated; lower
`max-mem` constrains worker memory, potentially at the expense of
analysis depth and thus false negatives and false positives.

When running analysis for third-party integrations (PMD for Apex), minimum memory
requirements are based on the sizing of the machine. The memory requirements can be
tuned or reduced using the appropriate memory maximum flag
(`--jvm-max-mem` or `--pmd-max-mem`). These are
the default minimum memory requirements:

- For machine size < 8GB, the minimum is 1GB
- For machine size 8-16GB, the minimum is 2GB
- For machine size 16GB+, the minimum is 4GB

See the description of the `cov-analyze` command in the Coverity 2026.6.0 Command Reference for details.
