---
title: "Analysis with Sigma checkers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/analysis-with-sigma-checkers.html"
content_id: "PpUqtku4LkrqcXI~xxaONw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:41.405346+00:00"
---

# Analysis with Sigma checkers

Coverity Analysis employs a number of underlying technologies: For example, analysis of
Ruby code is supported by the integration of the Brakeman Pro technology. With the
release of Coverity 2021.9.0, the Sigma analysis engine was integrated into Coverity Analysis.

Sigma checkers, noted in flagged issues by the prefix SIGMA, add support for
more languages and replace some Coverity checkers.
All Dart, PHP, Swift, and OpenAPI analysis is performed on the Sigma engine.

For a complete list of the checkers
being replaced, see the Coverity 2026.6.0 Installation and Upgrade Guide.

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
Coverity 2026.6.0 Command Reference.

The Rapid Scan Static product can run Sigma scans in a standalone environment, or from within Code Sight.

Attention:
We only support replacing the Sigma binary with a different version than
the version installed with Coverity through the upgrade processes described in Upgrading Sigma.

In this section:

- Importing analysis results from Rapid Scan Static (Sigma)
- Upgrading Sigma
