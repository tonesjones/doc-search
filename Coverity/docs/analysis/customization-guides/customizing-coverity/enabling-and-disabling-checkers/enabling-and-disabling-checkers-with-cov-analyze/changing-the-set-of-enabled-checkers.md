---
title: "Changing the set of enabled checkers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/changing-the-set-of-enabled-checkers.html"
content_id: "zANvHjL1qYOAKQsJOjTALg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:17.205319+00:00"
---

# Changing the set of enabled checkers

You can enable or disable checkers when you invoke
`cov-analyze`.

1. Consult the Checker enablement and option defaults
   by language
   table to view a list of checkers that can be run, and which are disabled by
   default.

   The Checker Enablement table is available in the HTML installed version of
   this document and in the online documentation, and includes guidance on enabling
   the checkers that are not enabled by default.
2. Consult the Checker enablement and option defaults by language table to view a list of checkers
   that can be run, and which are disabled by default.

   The Checker Enablement table includes guidance on
   enabling the checkers that are not enabled by default.
3. Enable one or more checkers.

   There are various ways to enable checkers, as listed here:
   - To enable an individual checker, use the option
     `--enable`. For example:

     ```
     > cov-analyze --dir idir --enable SWAPPED_ARGUMENTS
     ```

     This
     example runs the SWAPPED_ARGUMENTS checker in addition to the
     checkers that are enabled by default.
   - To enable most of the checkers that are not already enabled by default,
     use the `--all` option.
   - To enable checkers for coding standards (CERT-C, MISRA, ISO, and so on),
     use the `--coding-standard-config` option.
   - To enable C/C++ concurrency checkers that are disabled by default, use
     the `--concurrency` option. For example:

     ```
     > cov-analyze --dir idir --concurrency
     ```
   - To enable C/C++ security checkers, use the `--security`
     option. For example:

     ```
     > cov-analyze --dir idir --security
     ```
   - To enable all Web application security checkers, use the
     `--webapp-security` option.
   - To enable compilation warning checkers (parse warning, recovery warning,
     and semantic warning checkers), use the
     `--enable-parse-warnings` option.

     See Enabling compilation warning checkers (PW.*, RW.*, SW.*).
4. Disable one or more checkers.

   As with enabling, there are various ways to disable checkers.
   - To disable an individual checker, use the `--disable`
     option. For example:

     ```
     > cov-analyze --dir directory --disable BAD_OVERRIDE
     ```
   - To disable the default checkers, use the `--disable-default` option. The
     following example disables all checkers that are enabled by default:

     ```
     > cov-analyze --dir directory --disable-default
     ```
   - **PMD analysis option for Apex and SalesForce VisualForce:** The PMD analysis option
     for Apex and SalesForce VisualForce enables PMD for Apex and SalesForce
     VisualForce analysis (version 1.0.1) of captured Apex source code. See
     the "PMD.*" checker description
     in the Coverity 2026.6.0 Checker Reference.

     The following example
     enables the PMD for Apex analysis while disabling all other default
     checkers: Use the `--enable-pmd` option along with
     `--disable-default`.

     ```
     > cov-analyze --dir directory --enable-pmd --disable-default
     ```

     To disable PMD for Apex analysis, use the
     `--disable-pmd` option.
   - To disable parse warnings (if you previously enabled them but no longer
     need to see them), use the `--disable-parse-warnings`
     option.
   - To disable all Web application security checkers, use the
     `--disable-webapp-security` option.
