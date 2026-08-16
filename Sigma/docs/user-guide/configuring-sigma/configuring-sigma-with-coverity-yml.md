---
title: "Configuring Sigma with coverity.yml"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/configuring-sigma-with-coverity.yml.html"
content_id: "_FxEuYxEkH6V4uHTV8ai~A"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:08.835814+00:00"
---

# Configuring Sigma with coverity.yml

Sigma can be configured using files in the `coverity.yml` format.

- When running Sigma directly:

  You can either add a file named
  `coverity.yml` to the repository root, or pass a file in
  this format with the `--coverity-config` option. In either
  case, you can also use the `.yaml` extension or a JSON file
  with the same options.
- When running Sigma in the Rapid Scan Workflow on Polaris:

  You can add a file
  named `coverity.yml` to the repository root. You can also use
  the `yaml` extension or `coverity.json` with
  the same options. This file can be used to configure both Rapid Scans and
  Full Scans on Polaris. It also works with Coverity-on-Polaris, Coverity, and
  the Coverity CLI.

The list of options in the `coverity.yml` format can be found at [Options reference](https://docs.blackduck.com/r/coverity/latest/coverity-documentation/options-reference.html). Sigma supports the
following options. Other options do not affect Sigma’s analysis:

- `analyze.checkers.cra`
- `analyze.enable-check-set`
- `analyze.sigma.*`
- `capture.encoding`
- `capture.files.exclude-glob`
- `capture.files.exclude-regex`
- `capture.files.include-glob`
- `capture.files.include-regex`
- `capture.languages`

Sigma prints a warning for any option used in the file that it does not support.
