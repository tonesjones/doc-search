---
title: "Analysis with Sigma checkers"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/analysis-with-sigma-checkers.html"
content_id: "PpUqtku4LkrqcXI~xxaONw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:29.460873+00:00"
---

# Analysis with Sigma checkers

Sigma is a static analysis engine that complements Coverity analysis by providing
additional security and quality checks. When enabled, Sigma runs together with Coverity
analysis and contributes defects to the analysis results.

Sigma is enabled by default when running Coverity analysis.

Coverity Analysis employs a number of underlying technologies: For example, analysis of
Ruby code is supported by the integration of the Brakeman Pro technology. With the
release of Coverity 2021.9.0, the Sigma analysis engine was integrated into Coverity Analysis.

Sigma checkers, noted in flagged issues by the prefix SIGMA, add support
for more languages and replace some Coverity checkers.

For a complete list of the checkers
being replaced, see the Coverity Installation and Upgrade Guide.

The `cov-analyze` command now also runs the Sigma analysis engine on
supported platforms, which are a subset of what `cov-analyze` supports.
For information about the languages, platforms, file formats, and software issue types
that Sigma supports, see the [Sigma User Guide](https://docs.blackduck.com/r/sigma/latest/sigma-documentation/sigma-user-guide.html).

You can also consult the Sigma Checker Reference for additional
information about Sigma checkers: CWE support, detailed description of checkers, and so
on.

Note:

With the Coverity CLI, you can capture all files analyzed by Sigma by
invoking `coverity capture` without specifying a --build-command.
For example:

```
coverity capture --project-dir <sourceDirectory>
```

... This method captures files analyzed by Coverity Analysis as well as by Sigma.

With Coverity Analysis, you can perform an analysis that uses only Sigma checkers
by specifying the --sigma-enable-check-set option. For example:

```
cov-analyze --disable-default --sigma-enable-check-set all
```

For more information, see "Options: Checkers" for `cov-analyze` in the
Coverity Command Reference.

The Rapid Scan Static product can run Sigma scans in a standalone environment, or from within Code Sight.

Attention:
We only support replacing the Sigma binary with a different version than
the version installed with Coverity through the upgrade processes described in Upgrading Sigma.

## Interaction with Coverity checkers enablement

When Sigma is enabled, analysis results may include defects for Coverity security
checkers that are documented as disabled by default.

This occurs because Sigma may detect issues that correspond to Coverity security
checkers, regardless of whether those Coverity checkers are explicitly enabled. As a
result, defects may be reported even if the corresponding Coverity checkers are not
explicitly enabled.

To control this behavior, you can:

- Disable Sigma analysis, or
- Explicitly disable specific Coverity checkers using standard checker configuration
  options

In this section:

- Importing analysis results from Rapid Scan Static (Sigma)
- Upgrading Sigma
