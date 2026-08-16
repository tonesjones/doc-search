---
title: "Synopsis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/synopsis.html"
content_id: "8vHgDNkrelFkQlRaFqH6jg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:52.341617+00:00"
---

# Synopsis

```
cov-format-errors
    --dir <intermediate_dir>     
    [--emacs-style]
    [--exclude-files <regex>]
    [--file <file_substring>]
    [--filesort]
    [--function <func]
    [--functionsort]
    [--html-output <directory>]
    [--include-files <regex>]
    [--json-output-v10 <filename>]
    [--lang <language>]
    [--misra-only]    
    [--output-tag <name>]
    [--preview-report <file>]
    [--security-file <license file>]
    [--sort <sort_spec>]
    [--strip-path <path>]
    [--text-output-style <style>]
    [--title <text>]
    [-x]
    [-X | --noX]
    [FILTERING_OPTIONS]   
    [SHARED_OPTIONS]
```

**[FILTERING_OPTIONS]**:

```
    [--category-regex <regex>]
    [--checker-regex <regex>]
    [--cid <rangeFilter>]
    [--component-not-regex <regex>]
    [--component-regex <regex>]
    [--custom-triage-attribute-not-regex <attrName> <regex> ]
    [--custom-triage-attribute-regex <attrName> <regex>]
    [--cwe-category-regex <regex>]
    [--file-not-regex]
    [--file-regex <regex>]
    [--first-detected-after <date>]
    [--first-detected-before <date>]
    [--function-regex <regex>]
    [--impact-regex <regex>]
    [--kind-regex <regex>]
    [--language-regex <regex>]
    [--merge-key-regex <regex>]
    [--MISRA-category-regex <regex>]
    [--no-default-triage-filters]
    [--occurrences <range>]
    [--ownerLdapServerName-regex <regex>]
    [--subcategory-regex <regex>]
    [--triage-attribute-not-regex <attrName> <regex>]
    [--triage-attribute-regex <attrName> <regex>]
```

**[SHARED_OPTIONS]**:

```
    [--debug]
    [--ident]
    [--info]
    [--tmpdir <tmp>]
    [--verbose <level>]
```
