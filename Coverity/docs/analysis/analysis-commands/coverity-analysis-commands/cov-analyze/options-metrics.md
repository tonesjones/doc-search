---
title: "Options: Metrics"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options-metrics.html"
content_id: "YdAvD8989GZTNfhmuYGuoQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:41.983863+00:00"
---

# Options: Metrics

--enable-callgraph-metrics
:   Creates <intermediate_directory>/output/callgraph-metrics.csv,
    <intermediate_directory>/output/callgraph-metrics.txt,
    and <intermediate_directory>/output/checked-return.csv.

    The callgraph-metrics.[csv|txt] files store information about which
    functions are analyzed. The files list whether a function is implemented,
    which means it is analyzed, or whether a function is unimplemented, which
    means that it is not analyzed. A model is used if it is available. It also
    shows the number of callers for each function.

    The checked-return.csv file stores information on the
    percentage of times that each return value of each function is checked.
    This information can help you understand situations where the statistical
    checkers report different defects in local builds than they do in full
    builds.

    For details, see Coverity Analysis 2026.6.0 User and Administrator Guide.

    Applies to all programming languages.

--use-modified-ccm
:   Instead of computing the McCabe's Cyclomatic Complexity metric, compute the Modified McCabe's
    Cyclomatic Complexity metric. The modified metric considers that all switches increase the
    complexity by 2, regardless of how many cases are present.
