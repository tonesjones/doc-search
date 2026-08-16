---
title: "Configuring Sigma Output"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/configuring-sigma-output.html"
content_id: "URk08ADiZX3YuipU67QwTg"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:08.202704+00:00"
---

# Configuring Sigma Output

Sigma output includes information about the found issues, their severity, and remediation
advice. Output can be shown as standard output in the console or in the CI/CD UI after
Sigma executes.

By default, results are placed in a file named sigma-results.json in the
current working directory.

- Use the `-f` option of the sigma analyze command
  to change the *format* of the output file.

  Output is formatted as one of `JSON` or `SARIF`
  formats.

  You can select the COVERITY output format when running Sigma with Coverity
  Connect. For more information, see [cov-import-sigma](https://docs.blackduck.com/r/coverity/latest/coverity-documentation/cov-import-sigma.html).
- Use the `-o` option of the sigma analyze command
  to change the *location* of the results file.

In addition:

- If you are using Sigma as a quality gate, additional info about the policy that was
  violated and the associated issue will also be displayed in the console.
