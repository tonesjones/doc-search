---
title: "Coverity Analysis engine"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-analysis-engine.html"
content_id: "oW5HelyXJVtxZKU0ty6_8Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:37.498501+00:00"
---

# Coverity Analysis engine

- Use of inappropriate checker settings, which might lead the tool to ignore
  defects. For example, modifying checker options or command line options might
  affect what the checkers report.

  > **The user is responsible for checking the correct checker settings.**
  >
  > For details about settings available to individual checkers, see the Coverity 2026.6.0 Checker Reference. For example, see the MISRA_CAST
  > checker options.
- Changes to analysis settings that might result in issues being falsely reported
  as no longer present. For example, you might introduce such changes by using
  models, directives, or code-line annotations to model an API; such changes can
  introduce false negatives or false positives if you don't model the API
  correctly.

  > **The user is responsible for checking the correct analysis settings.**
  >
  > For the most consistent and accurate results on coding-standard scans (CERT, MISRA, etc.),
  > run a separate scan for each coding-standard with all other checkers disabled.
  > For example, if you want to scan for MISRA and CERT C issues,
  > run one scan with only MISRA checkers enabled and then run a separate scan with only CERT C checkers enabled.
  > Running a scan for multiple coding standards simultaneously might suppress some results.
  >
  > Coverity optimizes its
  > model of your application based on the specific set of checkers enabled in
  > the configuration. Some checkers might display small variances in the number
  > of findings when run in conjunction with other checkers. To minimize
  > variances, you should run Coverity with a consistent configuration.
  > Variances can also result from changes to the compiler, build environment,
  > source code, Coverity engine version, or other factors.
  >
  > The analysis
  > settings must be kept constant over a period of time to maintain a clear
  > baseline of issues. For details about these settings, see the Coverity 2026.6.0 Command Reference as well as the "Analyzing source code from the command line" section in the Coverity Analysis 2026.6.0 User and Administrator Guide. See also "Enabling and disabling
  > checkers" in Customizing Coverity for various
  > analysis workflows.
- If you build your own checker using CodeXM or Extend, or if you use the customizable checkers
  (`TEXT.CUSTOM_CHECKER`, `DF.CUSTOM_CHECKER`,
  or `DC.CUSTOM_CHECKER`, you might get false positives or false
  negatives. Test your checker carefully. For information, see Coverity
  CodeXM Checkers Development Guide.
- Inappropriate categorization of issues reported by the analysis, for example,
  marking a critical issue as *Intentional* as opposed to a *Bug*

  > **The user is responsible for the correct categorization of issues.**
  >
  > Inappropriate categorization can take place within Coverity Connect and the
  > Coverity Desktop plugins to IDEs such as Eclipse, Visual Studio, and
  > Intellij. See "Triaging
  > issues" in Coverity Platform 2026.6.0 User and Administrator Guide and the
  > "Details View" sections within the Coverity
  > Desktop guides
  > .
- Execution of the tool against code compiler versions that are not supported by
  the product

  > **The tools must only be run against compiler versions that are listed in the supporting
  > documentation.**
  >
  > See "Supported languages, compilers, and frameworks for
  > Coverity Analysis" in Coverity 2026.6.0 Installation and Upgrade Guide for
  > the lists of compilers that are supported by Coverity.

## `cov-manage-emit` and the `'had_recoverable_errors("true")'` option

The `cov-manage-emit` command's Translation Unit pattern-matching option `--tu-pattern 'had_recoverable_errors("true")' list`
returns a list of the names of files that reported recoverable errors during the build.

Attention:
To ensure that your code base is compliant, make sure that the following command returns an empty file:

```
cov-manage-emit --dir rdir --tu-pattern "failure() || had_recoverable_errors('true')" print-tuid --output-file incomplete-tus.log
```

A result of an empty file indicates that Analysis has encountered no further recovery or emit failures.
