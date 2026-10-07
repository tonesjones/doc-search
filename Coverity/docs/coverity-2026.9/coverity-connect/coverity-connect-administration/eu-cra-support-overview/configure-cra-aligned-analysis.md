---
title: "Configure CRA-aligned analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/configure-cra-aligned-analysis.html"
content_id: "EuSiaw6qtFXN0c6XFIiyOg"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:15.164284+00:00"
---

# Configure CRA-aligned analysis

Run analysis with the CRA-aligned checker configuration.

Review the requirements for running Coverity analysis. For command syntax and
additional options, see Coverity Analysis commands.

CRA-aligned analysis enables the checkers and settings used to
support EU-CRA workflows.

Using the `--cra` option helps ensure that
CRA-relevant security checkers are applied consistently and
provides a standardized analysis baseline for EU-CRA reporting
workflows.

Important: Generate EU-CRA artifacts only from analysis performed with the
`--cra` option. Reports generated from other analysis
configurations might omit CRA-relevant findings and provide incomplete or misleading
results.

1. Run cov-analyze with the
   --cra option.

   ```
   cov-analyze --cra
   ```
2. **Optional:** 
   To run analysis using only the CRA-aligned checker
   configuration, add the
   --disable-default option.

   ```
   cov-analyze --cra --disable-default
   ```
3. **Optional:** 
   To apply CRA-aligned analysis consistently across builds,
   add the CRA analysis option to the corresponding
   cov-analyze command in your automated
   analysis workflow.

Coverity runs analysis with the CRA-aligned checker
configuration.

After committing the analysis results, you can review findings
by Security Impact and generate EU-CRA artifacts.

To enforce analysis configuration requirements across projects and streams, see the
Coverity Checker Policy Enforcement overview.

For information about generating EU-CRA artifacts, see Generate EU-CRA artifacts.
