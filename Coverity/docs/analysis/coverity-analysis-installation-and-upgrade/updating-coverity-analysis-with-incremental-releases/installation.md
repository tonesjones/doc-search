---
title: "Installation"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/installation.html"
content_id: "jLKoeU6BgDcOODlKcf2jew"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:45:21.849135+00:00"
---

# Installation

Coverity Analysis now includes a utility (`cov-install-updates`) for
applying incremental updates. These updates include timely enhancements to
`cov-analysis` as they become available. Since incremental updates
include only the difference between the current and preceding versions, installer
packages are expected to be smaller and installation times shorter compared to a full
upgrade.

Incremental releases are intended to avoid changes that will introduce churn (Understanding churn). However, critical bug fixes and security
enhancements may still cause churn. It is recommended to review the incremental updates
being offered (using the `list` subcommand) and avoid those that may
disrupt your workflow.

Several updates may be applied in one session. This is done automatically, so a
deployment can easily be brought up-to-date with the latest incremental release.
Normally, updates apply only to the latest major release. However, it is possible to
install upgrades as well as updates by specifying the desired target version
explicitly.
