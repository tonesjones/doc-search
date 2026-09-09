---
title: "Searching for Specific Findings"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/searching-for-specific-findings.html"
content_id: "IS76EOK1xAeYZzzhQM_E5w"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:01.153579+00:00"
content_hash: "b3a34b29cdc231ea41824b2994cdcfe431b82488849105d5ed926147a4cf39fa"
---

# Searching for Specific Findings

Click the Findings icon in the navigation bar to open the Findings page.

[image: image]

You can search for a specific finding using the search field. Search options are located
in the upper left corner of the page.

**To search using the Search field:**

1. Enter a search term in the search field.
2. Open the dropdown option menu and select the type of search you want to run.

   Options include the following:
   - Finding Location
   - Finding ID
   - CVE
   - CWE
   - Type/Tool
   - Host
   - Black Duck Component Policy Violations
   - Black Duck Exploit Available
   - Black Duck Project
   - Black Duck Solution Available
   - Black Duck Workaround Available
   - Brakeman Confidence
   - CPE
   - CVSS v2
   - CVSS v2 Vector
   - CVSS v3
   - CVSS v3 Vector
   - Checkmarx Path ID
   - Coverity Merge Key
   - Fortify Instance ID
   - Tinfoil Api Issue ID
   - Veracode App ID
   - Veracode App Name
   - Veracode Flaw ID
   - Azure DevOps Work Item ID

   Search results are displayed automatically.

For additional information on select search options, see the sections below.

## Searching by the Finding's Location

The default "search by" option is Location, and search terms are case-sensitive. When
searching by Location, the criteria can be any part of a file path. For example, to
look for Findings in the *webapp/javascript* folder, enter
`webapp/javascript`. To search Findings in files with the
*.java* extension, enter `.java`. You can use
`*` to indicate a wildcard: a search for
`src/*.java` will match locations like
`src/main/java/Example.java`. If you want to have the literal
asterisk (`*`) as part of your search, use `*`. If you
want to have a literal backslash (`\`) as part of your search, use
`\`.

## Searching by Finding ID

When searching by Finding ID, the same formatting rules apply as with the CWE search.
To search for Finding 123, enter `123`. To search for Findings 123,
456, and 789, enter `123, 456, 789`. Note that the search will not
look for Findings from other projects.

## Searching by CWE ID

When searching by CWE, the criteria should be a number, or a comma-separated list of
numbers. For example, to search for findings with a CWE of 91, simply enter
`91`. To search for findings with a CWE of either 91 or 94, enter
`91, 94`. Note that ranges (e.g., *100 - 200*) are currently
not supported.

## Searching by Type/Tool

When searching by Type / Tool, the criteria can be any text (case-insensitive) which
may appear in the name or grouping of a Rule or Tool descriptor. For example,
searching for "inject" by Type / Tool can match Rules like "SQL Injection," and Tool
descriptors like *PMD / Security / Possible SQL Injection*. This search is case
insensitive. Wildcards are not supported.
