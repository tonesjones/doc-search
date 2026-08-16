---
title: "The cov-run-desktop command"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-cov-run-desktop-command.html"
content_id: "KkLEtjqiReQA_7pHBLunpQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:56.426490+00:00"
---

# The cov-run-desktop command

The `cov-run-desktop` command is the primary interface for using Desktop
Analysis. The following diagram illustrates the main processes performed by
`cov-run-desktop`, with explanations below:

Figure 1. `cov-run-desktop`
[image: image]

Select translation units to analyze
:   In general, `cov-run-desktop` analyzes the files passed explicitly at the
    end of the command line (`cov-run-desktop --dir
    intermediate_directory file1 file2`).
    However, it is also possible to use your Source Control Management system
    (SCM) to decide which files should be analyzed, using the
    `--analyze-scm-modified` option. See Source code management system integration for more
    information. Another option is to analyze previously captured source, by
    using the `--analyze-captured-source` option.

Download analysis summaries from Coverity Connect
:   In order to generate results that are both fast and accurate, Desktop Analysis depends on
    analysis summaries from Coverity Connect to provide relevant information
    about your source code. When you call `cov-run-desktop`,
    use the `--stream` option to specify a reference stream from
    which to pull summary data.

    Optionally, you can also use the
    `--reference-snapshot` command to specify a
    particular snapshot within your reference stream from which to pull
    analysis summaries. Use the snapshot created closest to, but not later
    than, the creation date of your intermediate directory. For more
    information, see `--reference-snapshot` in the Coverity 2026.6.0 Command Reference.

Analyze selected translation units
:   With analysis summaries downloaded from Coverity Connect, Desktop Analysis can analyze
    individual files and understand their impact on the rest of your source
    code, without having to analyze all of the other files therein.
    Additionally, `cov-run-desktop` collects summaries of
    locally analyzed code. This keeps the analysis summary information as
    current as possible for subsequent local analyses on different source files.

Retrieve triage data for analysis results
:   Aside from analysis summaries, Coverity Connect also provides triage data for any
    previously known issues also found by Desktop Analysis.
    `cov-run-desktop` retrieves the triage information for
    these issues and displays it in the output.

Filter locally found issues
:   To return only the most relevant analysis results, Desktop Analysis automatically filters
    out any issues with Classification of "False Positive" or "Intentional,"
    issues with Action set to "Ignore," those found in non-primary source files,
    as well as any issues found in third party code. Third party code is
    identified as any that belongs to a component with a file rule that contains
    "`[Tt]hird.*[Pp]arty`."

    There are additional options
    that can be used to further specify the list of issues returned, or to
    remove the default filters from your results (for example, the
    `--no-default-triage-filters` option).

    See "Output and filtering options" in the `cov-run-desktop` description in
    the Coverity 2026.6.0 Command Reference for more information.

Output returned analysis data
:   The `cov-run-desktop`
    command has options to specify the desired format
    and order of the defect output. By default, the list of defects is printed
    as text output that mimics compiler syntax errors. However, there are
    several options for customizing the defect output. These include changing
    the text output style, using JSON output format, and customizing the sort
    order of your defect list. The JSON output format is described in detail in
    Desktop Analysis JSON output syntax.

    See "Output and filtering options" in the `cov-run-desktop` description in
    the Coverity 2026.6.0 Command Reference for more information
    on other options related to Desktop Analysis output.

Classify locally found issues
:   Once you have received the results of a local analysis, some of the issues found may not be
    actual Bugs - they might be False Positives or Intentional. In order to mark
    them as such, you can run the xref `cov-run-desktop` command
    again, using the `--mark-fp` (False Positive) and/or
    `--mark-int` options accordingly. Each of these options
    specify a particular CID, and Classify it as either False Positive or
    Intentional, with a text comment explaining the classification. See
    `--mark-[fp | int]`
    in the Coverity 2026.6.0 Command Reference for details.
