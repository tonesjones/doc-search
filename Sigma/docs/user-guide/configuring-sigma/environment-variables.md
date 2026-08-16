---
title: "Environment Variables"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/environment-variables.html"
content_id: "rfx9ekNj7q2izwVVsD_HfA"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:12.852644+00:00"
---

# Environment Variables

Use the following environment variables to define Sigma behavior.

| Variable | Action |
| --- | --- |
| `SIGMA_ANALYZE_IGNORE_SCM` | Ignore all source-code-management related processing.  When this environment variable is set, the .gitignore file is ignored. |
| `SIGMA_ANALYZE_OUTPUT_FILE` | The name of the file where Sigma should store scan results.  **Default:** sigma-results.json in current working directory. |
| `SIGMA_ANALYZE_OUTPUT_FORMAT` | Analyze output format: `json`, `sarif`, or `COVERITY`.  You can select the COVERITY output format when running Sigma with Coverity Connect. For more information, see [cov-import-sigma](https://docs.blackduck.com/r/coverity/latest/coverity-documentation/cov-import-sigma.html).  **Default:** `markdown` |
| `SIGMA_BASE_CHECK_SET` | Enable a base set of checks. Only one of the following values can be used:   - `all` - this will enable all checks - `default` - this will enable all checks, except for the   disabled checks (either by default, or explicitly disabled with the   `--disable` option) - `empty` - this will disable all checks, except for the checks   which are explicitly enabled using the `--enable` option - `cis` - this will enable the CIS (Center for Internet   Security) benchmark checks - `cra` - this will enable the EU Cyber Resilience Act (EU-CRA) checks - `owasp-web-top-10-2021` - this will enable the 2021 OWASP Top 10 checks - `owasp-web-top-10-2025` - this will enable the 2025 OWASP Top 10 checks - `cwe-top-25-2023` - this will enable the 2023 CWE Top 25 checks - `cwe-top-25-2024` - this will enable the 2024 CWE Top 25 checks - `cwe-top-25-2025` - this will enable the 2025 CWE Top 25 checks - `owasp-mobile-top-10-2016` - this will enable the 2016 OWASP Mobile Top 10 checks - `owasp-mobile-top-10-2024` - this will enable the 2024 OWASP Mobile Top 10 checks   `SIGMA_ENABLE` and `SIGMA_DISABLE` have priority over `SIGMA_BASE_CHECK_SET`.  `SIGMA_BASE_CHECK_SET` has priority over `SIGMA_ENABLE_ALL`. |
| `SIGMA_CHECKERS_FORMAT` | Output format of the `sigma checkers` command. Possible values: `html`, `markdown`. |
| `SIGMA_CHECKERS_OUTPUT` | Output file to store the result of the `sigma checkers` command. **Default:** `stdout` |
| `SIGMA_CONFIG_FILE` | The name of the configuration file.  **Default:** .sigma-config.yml Note: This option cannot be used to pass a file in the `coverity.yml` format. |
| `SIGMA_DISABLE` | Name of the check or checker to disable. To disable multiple checks/checkers, use a comma-separated list of check/checker names. Note: Disabling a checker automatically disables all of the associated checks. Disablement overrides enablement. See also the `sigma analyze --enable/--disable` examples. |
| `SIGMA_ENABLE` | Name of the check or checker to enable. To enable multiple checks/checkers, use a comma-separated list of check/checker names. Note: Enabling a checker enables the associated checks which are enabled by default, but not the checks which are disabled by default. Checks that are disabled by default need to be explicitly enabled. See also the `sigma analyze --enable/--disable` examples. |
| `SIGMA_ENABLE_ALL` | Enable all checks disabled by default. Important: `SIGMA_ENABLE_ALL` is deprecated as of Sigma 2023.4.0. Use `SIGMA_BASE_CHECK_SET all` instead.  Note: There are justifiable reasons for checks to be disabled by default. It is recommended to run Sigma with the default set of enabled checks or to explicitly enable checks using the `SIGMA_ENABLE` environment variable or the `--enable` option.  Note: `SIGMA_DISABLE` has precedence over `SIGMA_ENABLE_ALL`. |
| `SIGMA_ENABLE_CHECK_SET` | Bulk-enable an additional set of checks. One or more of the following values can be used:   - `all` - this will enable all checks - `default` - this will enable all checks, except for the   disabled checks (either by default, or explicitly disabled with the   `--disable` option) - `empty` - this will disable all checks, except for the checks   which are explicitly enabled using the `--enable` option - `cis` - this will enable the CIS (Center for Internet   Security) benchmark checks - `cra` - this will enable the EU Cyber Resilience Act (EU-CRA) checks - `owasp-web-top-10-2021` - this will enable the 2021 OWASP Top 10 checks - `owasp-web-top-10-2025` - this will enable the 2025 OWASP Top 10 checks - `cwe-top-25-2023` - this will enable the 2023 CWE Top 25 checks - `cwe-top-25-2024` - this will enable the 2024 CWE Top 25 checks - `cwe-top-25-2025` - this will enable the 2025 CWE Top 25 checks - `owasp-mobile-top-10-2016` - this will enable the 2016 OWASP Mobile Top 10 checks - `owasp-mobile-top-10-2024` - this will enable the 2024 OWASP Mobile Top 10 checks   `SIGMA_ENABLE` and `SIGMA_DISABLE` have priority over `SIGMA_ENABLE_CHECK_SET`. |
| `SIGMA_EXCLUDE_FILE_PATH` | Exclude a list of files from the analysis. This option takes a list of globs to exclude files. Standard Unix-style glob syntax is supported. Include options take precedence over exclude. |
| `SIGMA_INCLUDE_ALL` | Include all files by disabling code exclusion completely, exploring the `.git` directory and ignoring the `.gitignore` file. Include options take precedence over exclude. |
| `SIGMA_INCLUDE_FILE_PATH` | Includes a list of files in the analysis. This option takes a list of globs to include files. Useful when you want to override otherwise excluded files. Standard Unix-style glob syntax is supported. Include options take precedence over exclude. |
| `SIGMA_MALICIOUS_URL_PATTERNS_FILE` | Enable and customize the behaviour of the `malicious_url` checker, which is used to detect malicious URLs in source code.  This option takes a list of files. Each file should contain a list of URLs that need to be reported, with one URL per line. |
| `SIGMA_METADATA_DOCUMENTATION_JSON_OUTPUT` | Specify the output file for the `sigma metadata documentation json` command. |
| `SIGMA_METADATA_DOCUMENTATION_JSON_PRETTY` | Pretty-print the JSON output of the `sigma metadata documentation json` command. |
| `SIGMA_METADATA_DOCUMENTATION_JSON_SCHEMA` | When running the `sigma metadata documentation json` command, output the JSON schema instead of the metadata. |
| `SIGMA_METADATA_DOCUMENTATION_JSON_VERSION` | When running the `sigma metadata documentation json` command, specify the version of the output. |
| `SIGMA_METADATA_HARCODED_SECRET_PATTERNS_​​OUTPUT` | Specify the output file for the `sigma metadata hardcoded-secret-patterns text` command. |
| `SIGMA_NUM_THREADS` | The number of threads to use in executing the command.  There is no limit. By default it is set to the number of CPUs. |
| `SIGMA_POLICY_FILE` | The name of the file containing the policy.  **Default:** .sigma-policy.yml located at the root of the repository.  Note: This environment variable is deprecated. |
| `SIGMA_REPO_ROOT` | Make the issue file paths relative to the specified absolute repo root. |
| `SIGMA_TMPDIR` | Location where to store temporary files.  **Default:** .sigma-dir |
