---
title: "Options categories"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options-categories.html"
content_id: "DymndzuWt6uxsmabK9S_Tw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:10.384824+00:00"
---

# Options categories

The options accepted by `cov-run-desktop` fall into several
categories:

Note: Each of the items below are linked to other sections in this document. Many link to
the relevant definition in the `cov-run-desktop` section, while the
analysis options link to `cov-analyze`.

Options that affect what code will be analyzed
:   - `--analyze-captured-source`
    - `--analyze-scm-modified`
    - `--analyze-untracked-files`
    - `--ignore-all-files-regex`
    - `--ignore-modified-file-regex`
    - `--ignore-modified-non-psf`
    - `--ignore-untracked-file-regex`
    - `--modification-date-threshold`
    - `--restrict-all-files-regex`
    - `--restrict-modified-file-regex`
    - `--restrict-untracked-file-regex`
    - `--tu-pattern`

Options for using your Source Code Management (SCM) system
:   - `--analyze-untracked-files`
    - `--ignore-untracked-file-regex`
    - `--restrict-untracked-file-regex`
    - `--scm`
    - `--scm-project-root`
    - `--scm-tool`
    - `--scm-tool-arg`

Options that control the analysis
:   - `--aggressiveness-level`
    - `--all`
    - `--android-security`
    - `--checker-option`
    - `--concurrency`
       (C/C++)
    - `--debug`
    - `--debug-flags`
       (C/C++)
    - `--disable`
    - `--disable-android-security`
    - `--disable-default`
    - `--disable-fnptr`
       (C/C++)
    - `--disable-misra`
       (C/C++)
    - `--disable-parse-warnings`
       (C/C++)
    - `--distrust-all`
    - `--distrust-mobile-other-app`
    - `--distrust-mobile-other-privileged-app`
    - `--distrust-mobile-same-app`
    - `--distrust-mobile-user-input`
    - `--distrust-console`
    - `--distrust-database`
    - `--distrust-environment`
    - `--distrust-filesystem`
    - `--distrust-http`
    - `--distrust-http-header`
    - `--distrust-js-client-cookie`
    - `--distrust-js-client-external`
    - `--distrust-js-client-html-element`
    - `--distrust-js-client-http-referer`
    - `--distrust-js-client-http-header`
    - `--distrust-js-client-other-origin`
    - `--distrust-js-client-url-query-or-fragment`
    - `--distrust-network`
    - `--distrust-rpc`
    - `--distrust-servlet`
    - `--distrust-system-properties`
    - `--enable`
    - `--enable-audit-mode`
    - `--enable-callgraph-metrics`
    - `--enable-constraint-fpp`
    - `--enable-fnptr`
       (C/C++)
    - `--enable-parse-warnings`
       (C/C++)
    - `--enable-single-virtual`
       (C/C++)
    - `--enable-virtual`
       (C/C++)
    - `--extend-checker`
    - `--extend-checker-option`
    - `--fnptr-models`
       (C/C++)
    - `--hfa`
       (C/C++)
    - `--ident`
    - `--ignore-deviated-findings`
    - `--info`
    - `--inherit-taint-from-unions`
       (C/C++)
    - `--jobs`
    - `--max-loop`
       (C/C++)
    - `--max-mem`
    - `--model-file`
    - `--no-field-offset-escape`
       (C/C++)
    - `--not-tainted-field`
       (C#, Java, Visual Basic)
    - `--override-worker-limit`
       (C/C++)
    - `--parse-warnings-config`
       (C/C++)
    - `--paths`
       (C/C++)
    - `--redirect`
    - `--rule`
       (C/C++)
    - `--security`
       (C/C++)
    - `--security-file`
    - `--skip-android-app-sanity-check`
       (Java Android)
    - `--strip-path`
    - `--tainted-field`
       (Java)
    - `--tmpdir`
    - `--trust-all`
    - `--trust-mobile-other-app`
    - `--trust-mobile-other-privileged-app`
    - `--trust-mobile-same-app`
    - `--trust-mobile-user-input`
    - `--trust-console`
    - `--trust-database`
    - `--trust-environment`
    - `--trust-filesystem`
    - `--trust-http`
    - `--trust-http-header`
    - `--trust-js-client-cookie`
    - `--trust-js-client-external`
    - `--trust-js-client-html-element`
    - `--trust-js-client-http-referer`
    - `--trust-js-client-http-header`
    - `--trust-js-client-other-origin`
    - `--trust-js-client-url-query-or-fragment`
    - `--trust-network`
    - `--trust-rpc`
    - `--trust-servlet`
    - `--trust-system-properties`
    - `--tu-pattern`
       (C/C++)
    - `--use-reference-settings`
    - [Deprecated] 
      `--user-model-file`

      This option is deprecated and has been replaced by the
      `--model-file` option.
    - `--verbose`
    - `--wait-for-license`
    - `--webapp-security-aggressiveness-level`
       (C#, Java, Visual Basic)
    - `--webapp-security`
       (C#, Java, JavaScript, Visual Basic)
    - `--whole-program`

Options to specify connection and triage information for the Coverity Connect server
:   - `--auth-key-file`
    - `--certs`
    - `--connect-timeout`
    - `--disconnected`
    - `--host`
    - `--mark-fp`
    - `--mark-int`
    - `--on-new-cert`
    - `--password`
    - `--port`
    - `--reference-snapshot`
    - `--set-new-defect-owner`
    - `--set-new-defect-owner-limit`
    - `--set-new-defect-owner-to`
    - `--ssl`
    - `--stream`
    - `--user`

Output and filtering options
:   - `--add-ignore-modified-file-regex`
    - `--add-restrict-modified-file-regex`
    - `--category-regex`
    - `--checker-regex`
    - `--cid`
    - `--component-not-regex`
    - `--component-regex`
    - `--confine-to-scope`
    - `--custom-triage-attribute-not-regex`
    - `--custom-triage-attribute-regex`
    - `--cwe-category-regex`
    - `--exit1-if-defects`
    - `--file-regex`
    - `--file-not-regex`
    - `--first-detected-after`
    - `--first-detected-before`
    - `--function-regex`
    - `--ignore-modified-file-regex`
    - `--ignore-all-files-regex`
    - `--impact-regex`
    - `--include-missing-locally`
    - `--json-output-v10 <filename>`
    - `--kind-regex`
    - `--lang`
    - `--language-regex`
    - `--local-status-not-regex`
    - `--local-status-regex`
    - `--merge-key-regex`
    - `--MISRA-category-regex`
    - `--no-default-triage-filters`
    - `--no-text-output`
    - `--occurrences`
    - `--ownerLdapServerName-regex`
    - `--print-path-events`
    - `--present-in-reference`
    - `--relative-paths`
    - `--relative-to`
    - `--report-rws`
    - `--restrict-all-files-regex`
    - `--restrict-modified-file-regex`
    - `--sort`
    - `--subcategory-regex`
    - `--text-output`
    - `--text-output-style`
    - `--triage-attribute-not-regex`
    - `--triage-attribute-regex`
