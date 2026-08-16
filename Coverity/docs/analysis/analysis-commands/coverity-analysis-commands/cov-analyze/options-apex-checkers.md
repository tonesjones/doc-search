---
title: "Options: Apex checkers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options-apex-checkers.html"
content_id: "uZQoZj2wD3BxtiM17eN3HA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:33.785732+00:00"
---

# Options: Apex checkers

--disable-pmd
:   [PMD analysis option for Apex and SalesForce VisualForce] Disables PMD
    analysis. The PMD for Apex and SalesForce VisualForce analysis is enabled by
    default.

    An error will occur if you combine `--enable-pmd` with
    `--disable-pmd`

--enable-pmd
:   [PMD analysis option for Apex and SalesForce VisualForce] The PMD for Apex
    and SalesForce VisualForce analysis is enabled by default. If PMD analysis
    is disabled, this option enables PMD for Apex and SalesForce VisualForce
    analysis (version 1.0.1) of captured Apex source code. See "PMD.*" in the
    Coverity 2026.6.0 Checker Reference for details.

    An error will occur if you combine `--enable-pmd` with
    `--disable-pmd`

--pmd-max-mem
:   [PMD analysis option for Apex and SalesForce VisualForce] Sets the JVM heap
    size of the VM that is running PMD. This option is similar to
    `--max-mem` in that it takes an integral value of
    megabytes, but differs in that the action to take if PMD execution runs out
    of memory is to provide a larger value. If the option is not specified, the
    default value is 1024.
