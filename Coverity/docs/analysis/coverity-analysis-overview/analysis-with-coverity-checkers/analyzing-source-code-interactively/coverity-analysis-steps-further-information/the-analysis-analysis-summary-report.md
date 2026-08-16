---
title: "The analysis: Analysis Summary Report"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-analysis-analysis-summary-report.html"
content_id: "r6PVgiGmg67l~RBi4guk4w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:54.832093+00:00"
---

# The analysis: Analysis Summary Report

The output of the `cov-analyze` command is an analysis summary report.
Here is sample output of the report (depending on your platform, the details of the output might differ):

```
[Looking for translation units
|0----------25-----------50----------75---------100|
****************************************************
[STATUS] Computing links for 1 translation unit
|0----------25-----------50----------75---------100|
****************************************************
[STATUS] Computing virtual overrides
|0----------25-----------50----------75---------100|
 ****************************************************
[STATUS] Computing callgraph
|0----------25-----------50----------75---------100|
***************************************************
[STATUS] Topologically sorting 12 functions
|0----------25-----------50----------75---------100|
***************************************************
[STATUS] Computing node costs
|0----------25-----------50----------75---------100|
****************************************************
[STATUS] Starting analysis run
|0----------25-----------50----------75---------100|
****************************************************
2013-10-11 21:29:02 UTC - Calculating 34 cross-reference bundles...
|0----------25-----------50----------75---------100|
****************************************************
Analysis summary report:
------------------------
Files analyzed                 : 1
Total LoC input to cov-analyze : 8584
Functions analyzed             : 12
Paths analyzed                 : 49
Time taken by analysis         : 00:00:02
Defect occurrences found       : 18 Total
                                  1 DEADCODE
                                  1 FORWARD_NULL
                                  1 NEGATIVE_RETURNS
                                  1 OVERRUN
                                  7 RESOURCE_LEAK
                                  1 REVERSE_INULL
                                  1 REVERSE_NEGATIVE
                                  1 SIZECHECK
                                  1 SIZEOF_MISMATCH
                                  1 UNINIT
                                  1 UNUSED_VALUE
                                  1 USE_AFTER_FREE
```

The results of the analysis summary report include the following information:

Files analyzed
:   The total number of files having classes/structs or functions requiring analysis on this run of `cov-analyze`.
    Files that do not contain classes/structs or functions (such as a header file that contains only macro
    definitions) are not reflected in this total.

Total LoC input to cov-analyze
:   The total number of lines of code analyzed.

Functions analyzed
:   The total number of functions actually requiring analysis or re-analysis.
    If the count is 0, this output field is not displayed.

Paths analyzed
:   The sum of paths traversed for all analyzed functions.
    (There is some complexity to the calculation that is used to produce this sum.)

Time taken by analysis
:   The amount of time taken (in hours, minutes, and seconds) for the analysis to complete.

Defect occurrences found
:   The number of defect occurrences found by the analysis, followed by a breakdown by checker.
    When the snapshot is committed to Coverity Connect, it merges similar defects from a
    given stream into a single CID, so the total number of CIDs shown by Coverity Connect
    is likely to differ from the number shown in the "Defect occurrences" field.

A log file with information about the analysis is saved to
<intermediate_directory>/output/analysis-log.txt.
