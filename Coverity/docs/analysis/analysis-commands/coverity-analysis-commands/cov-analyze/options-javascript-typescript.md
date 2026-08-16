---
title: "Options: JavaScript, TypeScript"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options-javascript-typescript.html"
content_id: "LcIdH9ImQW0PWIXxBS6wlg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:41.329541+00:00"
---

# Options: JavaScript, TypeScript

--analyze-node-modules
:   By default, `cov-analyze` does not analyze code in the
    node_modules/ directories for JavaScript or
    TypeScript projects. This option enables analysis of the translation units
    in the node_modules/ directories.

    Even when you use the `--tu` or the
    `--tu-pattern` option, you must specify
    `--analyze-node-modules` in order to analyze
    translation units in node_modules/ directories.

--report-in-minified-js
:   [JavaScript application option] Enables the JavaScript checkers for minified
    source files. It ensures that Coverity Analysis scans the minified
    JavaScript source files and reports any defects that are found.
