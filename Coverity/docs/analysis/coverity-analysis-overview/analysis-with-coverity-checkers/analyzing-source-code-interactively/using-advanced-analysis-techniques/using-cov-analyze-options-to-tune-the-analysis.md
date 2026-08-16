---
title: "Using 'cov-analyze' options to tune the analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-cov-analyze-options-to-tune-the-analysis.html"
content_id: "lmhteV_9fWhz0uOqWJ3s1w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:17.541774+00:00"
---

# Using 'cov-analyze' options to tune the analysis

The `cov-analyze` command accepts several options that tune the
analysis, affecting both the results and the speed.

Table 1. Tuning options to `cov-analyze`

| Option | Effect on Speed | Effect on Results |
| --- | --- | --- |
| `--enable-virtual` | The analysis can take significantly longer for C++ code. This option does not affect C or C# code. | This option enables virtual call resolution to more precisely analyze calls to virtual functions, which can increase the number of defects reported. |
| `--enable-constraint-fpp` | The analysis can take 10% to 20% longer. | This option uses a false-path pruner (FPP) to perform additional defect filtering. It can increase the analysis time but decrease the number of false positives occurring along infeasible paths. Because this FPP uses an approximate method for pruning false positives, it is possible that a very small number of true positives will also be pruned. |
