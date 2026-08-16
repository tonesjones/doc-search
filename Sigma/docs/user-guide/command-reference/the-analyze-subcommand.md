---
title: "The analyze Subcommand"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/the-analyze-subcommand.html"
content_id: "2W16ngdei_TguwpPR6dZng"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:31.867562+00:00"
---

# The analyze Subcommand

## Syntax

sigma analyze [FLAGS] [OPTIONS] [--] [path] ...

## Description

The analyze subcommand analyzes your applications. Flags and options determine how the analysis is done: what files are scanned, what checks are used, what output format is used for results, and so on.

## Parameters

path - Specifies the directories and files that will be analyzed.

## Flags

| Flag | Description |
| --- | --- |
| `--follow-symlinks` | Follow symlinks while discovering what files exist for analysis. |
| `--ignore-hidden-files` | Ignore hidden files and directories. |
| `--ignore-scm` | Ignore all source-code-management related processing.  With this flag, the .git directory is explored and the .gitignore file is ignored.  This is equivalent to setting the environment variable `SIGMA_ANALYZE_IGNORE_SCM` to `1`. |
| `--make-paths-absolute` | Make the file path (for the source files where the issues are flagged) absolute. |

## Options

| Option | Description |
| --- | --- |
| `--base-check-set <default|all|empty|cis>` | Enable a base set of checks. Only one of the following values can be used:   - `all` - this will enable all checks - `default` - this will enable all checks, except for the   disabled checks (either by default, or explicitly disabled with the   `--disable` option) - `empty` - this will disable all checks, except for the checks   which are explicitly enabled using the `--enable` option - `cis` - this will enable the CIS (Center for Internet   Security) benchmark checks - `cra` - this will enable the EU Cyber Resilience Act (EU-CRA) checks - `owasp-web-top-10-2021` - this will enable the 2021 OWASP Top 10 checks - `owasp-web-top-10-2025` - this will enable the 2025 OWASP Top 10 checks - `cwe-top-25-2023` - this will enable the 2023 CWE Top 25 checks - `cwe-top-25-2024` - this will enable the 2024 CWE Top 25 checks - `cwe-top-25-2025` - this will enable the 2025 CWE Top 25 checks - `owasp-mobile-top-10-2016` - this will enable the 2016 OWASP Mobile Top 10 checks - `owasp-mobile-top-10-2024` - this will enable the 2024 OWASP Mobile Top 10 checks   If this option is not set, the default set of checks will be enabled (equivalent to using `--base-check-set default`).  You can also set this value using the environment variable `SIGMA_BASE_CHECK_SET`.  The `--enable` and `--disable` options have priority over `--base-check-set`.  The `--base-check-set` option has priority over the `--enable-all` option. |
| `--disable <check_name> | <checker_name>` | Name of the check or checker to disable.  You can also set this value using the environment variable `SIGMA_DISABLE`.  This option takes only one value. You can repeat it to disable multiple checks or checkers.  `--disable <check1> --disable <check2>`  Note: Disabling a checker automatically disables all of the associated checks. Disablement overrides enablement. |
| `--enable <check_name> | <checker_name>` | Name of the check or checker to enable.  You can also set this value using the environment variable `SIGMA_ENABLE`.  This option takes only one value. You can repeat it to enable multiple checks or checkers.  `--enable <check1> --enable <check2>`  Note: Enabling a checker enables the associated checks which are enabled by default, but not the checks which are disabled by default. Checks that are disabled by default need to be explicitly enabled. |
| `--enable-all` | Enable all checks and checkers disabled by default. Important: The `--enable-all` option is deprecated as of Sigma 2023.4.0. Use `--base-check-set all` instead. This is equivalent to setting the environment variable `SIGMA_ENABLE_ALL` to `1`.  Note: There are justifiable reasons for checks to be disabled by default. It is recommended to run Sigma with the default set of enabled checks or to explicitly enable checks using the `SIGMA_ENABLE` environment variable or the `--enable` option.  Note: `--disable` has precedence over `--enable-all`. |
| `--enable-check-set` | Bulk-enable an additional set of checks. One or more of the following values can be used:   - `all` - this will enable all checks - `default` - this will enable all checks, except for the   disabled checks (either by default, or explicitly disabled with the   `--disable` option) - `empty` - this will disable all checks, except for the checks   which are explicitly enabled using the `--enable` option - `cis` - this will enable the CIS (Center for Internet   Security) benchmark checks - `cra` - this will enable the EU Cyber Resilience Act (EU-CRA) checks - `owasp-web-top-10-2021` - this will enable the 2021 OWASP Top 10 checks - `owasp-web-top-10-2025` - this will enable the 2025 OWASP Top 10 checks - `cwe-top-25-2023` - this will enable the 2023 CWE Top 25 checks - `cwe-top-25-2024` - this will enable the 2024 CWE Top 25 checks - `cwe-top-25-2025` - this will enable the 2025 CWE Top 25 checks - `owasp-mobile-top-10-2016` - this will enable the 2016 OWASP Mobile Top 10 checks - `owasp-mobile-top-10-2024` - this will enable the 2024 OWASP Mobile Top 10 checks   You can also set this value using the environment variable `SIGMA_ENABLE_CHECK_SET`.  The `--enable` and `--disable` options have priority over `--enable-check-set`. |
| `--exclude-file-path list of globs` | Exclude a list of files from the analysis. This option takes a list of globs to exclude files. Standard Unix-style glob syntax is supported. You can also set this value using the environment variable `SIGMA_EXCLUDE_FILE_PATH`. Note: Include options take precedence over exclude. |
| `-f format`, `--format format` | The output format (`coverity`, `json`, `sarif`)  You can also set this value using the environment variable `SIGMA_ANALYZE_OUTPUT_FORMAT`.   - The `coverity` format converts Sigma issues into a JSON-supported format that Coverity tools can parse.   **Default:** `json` |
| `--include-all` | Include all files by disabling code exclusion completely, exploring the `.git` directory and ignoring the `.gitignore` file. Note: The code exclusion feature automatically excludes folders and files from the scan that are likely to have test code, examples or localization files.  Include options take precedence over exclude. Thus `--include-all` would override values specified with the `--exclude-file-path` option.  This is equivalent to setting the environment variable `SIGMA_INCLUDE_ALL` to `1`. |
| `--include-file-path list of globs` | A list of glob patterns. Sigma will filter out files that do not match any of these patterns. Each pattern has an implicit `**` at the beginning, so that leading path components are ignored automatically. See examples. You can also set this value using the environment variable `SIGMA_INCLUDE_FILE_PATH`. |
| `-o file`, `--output file` | The output file to store scan results.  You can also set this value using the environment variable `SIGMA_ANALYZE_OUTPUT_FILE`.  **Default:** sigma-results.json in the current working directory. |
| `--malicious-url-patterns-file list of files` | The `--malicious-url-patterns-file` option is used to enable and customize the behaviour of the `malicious_url` checker, which is used to detect malicious URLs in source code.  This option expects arguments as a comma separated list of files. A file given as parameter to the `--malicious-url-patterns-file` option should contain a list of URLs that need to be reported, with one URL per line.  You can also set this value using the environment variable `SIGMA_MALICIOUS_URL_PATTERNS_FILE`. |
| `--repo-root root` | Make the issue file paths relative to the specified absolute repo root.  You can also set this value using the environment variable `SIGMA_REPO_ROOT`. |
| `--sbom SBOM_file` | Enables component version specific checks based on the versions listed in the provided SBOM file. The component version specific checks are currently limited to CycloneDX format SBOMs. |

## Example: `sigma analyze --enable/--disable`

Checker `A` has two checks `A_foo` and `A_bar`. If `A_foo` is enabled by default and `A_bar` is disabled by default, the `sigma analyze --enable/--disable` command produces the following results:

| Command | Result |
| --- | --- |
| `sigma analyze --enable A_bar` | both `A_foo` and `A_bar` are enabled (`A_foo` is enabled by default) |
| `sigma analyze --enable A` | only `A_foo` is enabled (`A_bar` is disabled by default) |
| `sigma analyze --disable A` | both `A_foo` and `A_bar` are disabled |
| `sigma analyze --enable A --disable A_foo` | both `A_foo` and `A_bar` are disabled (disablement overrides enablement) |

## Example: `sigma analyze --include-file-path/--exclude-file-path`

Note: For Windows, use a "\" backward slash for a file separator instead of a forward slash "/".

Table 1. Examples of globs

| Glob | Description | Matching Examples | Not Matching Examples |
| --- | --- | --- | --- |
| `test` | Matches any file named `test` in any directory. | `dir/test` `dir/subdir/test`  `test` | `dir/other` |
| `test/*.java` | Matches any file whose name ends in `.java` located in a directory named `test`. | `dir/test/Class.java` `test/Class.java` | `test/dir/Class.java` `test/script.py` |
| `test/**` | Match any file recursively located in a directory named `test`. | `dir/test/a` `test/a/b` | `test` `other/a` |

## Example: using `--base-check-set` and `--enable-check-set`

The following command lines are equivalent; they enable the CIS benchmark checks (no other checks are enabled):

```
sigma analyze --base-check-set cis
```

```
sigma analyze --base-check-set empty --enable-check-set cis
```

## Example: using `--malicious-url-patterns-file`

| Command | File content | Result |
| --- | --- | --- |
| `sigma analyze --malicious-url-patterns-file /path/to/file.txt` | *file.txt*  `http://www.some_malicious_site.com` | Lines of code containing `http://www.some_malicious_site.com` will be reported as a defect under the `malicious_url` checker group. |
| `sigma analyze --malicious-url-patterns-file ./file1.txt,./file2.txt,./file3.txt` | *file1.txt*  `http://www.other.com`  `http://www.somesite.com`  *file2.txt*  `www.danger.cn`  *file3.txt*  `cdn.danger.io`  `cdn.other.io` | Lines of code containing any of the following strings:  `http://www.other.com`  `http://www.somesite.com`   `www.danger.cn`   `cdn.danger.io`   `cdn.other.io`  will be reported as a defect under the `malicious_url` checker group. |

**Use case for `--malicious-url-patterns-file`: Polyfill example**

In February 2024, a popular open source JavaScript library called `polyfill.js` had its CDN service domain purchased by a malicious actor. Attackers injected malicious code into the Polyfill library. Polyfill is used to add functionality to older browsers, and thus, a lot of websites were affected.

A common way Polyfill is used is by including it as a CDN hosted script. This will cause the browser to fetch the `polyfill.js` file from the `cdn.polyfill.io` domain which now host malicious content.

Code example

```
<script src="https://cdn.polyfill.io/v2/polyfill.min.js"></script>
```

Using the following `patterns.txt` file, this line of code would be reported as a `malicious_url` defect.

*patterns.txt*

```
bootcdn.net
bootcss.com
staticfile.net
staticfile.org
unionadjs.com
xhsbpza.com
union.macoms.la
newcrbpc.com
https://cdn.polyfill.io/v2/polyfill.min.js
https://www.googie-anaiytics.com/html/checkcachehw.js
https://www.googie-anaiytics.com/ga.js
https://cdn.bootcss.com/highlight.js/9.7.0/highlight.min.js
https://newcrbpc.com/redirect?from=bscbc
https://kuurza.com/redirect?from=bitget
https://union.macoms.la/jquery.min-4.0.2.js
```
