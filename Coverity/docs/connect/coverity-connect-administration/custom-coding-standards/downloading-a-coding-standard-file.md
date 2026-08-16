---
title: "Downloading a coding standard file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/downloading-a-coding-standard-file.html"
content_id: "x33Wdvj8muTQRA0MqEOwyA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:34.736564+00:00"
---

# Downloading a coding standard file

You can download a built-in coding standard file from the
Configuration → Standards
window by selecting the standard name, then clicking Download Selected.
The selected JSON standard file is downloaded to your local system.
You can then use the file as a basis for a custom coding standard.

A built-in coding standard file contains two JSON objects:

`"name"`
:   The name of the coding standard that is displayed in the Coverity Connect UI.
    For example, `"2019 CWE Top 25 - custom for myCorp"`

`"mapping"`
:   A list of paired strings. The first string is an issue type code. The second string is the value of the issue type.

    For example, here is an issue type entry from the 2019 CWE Top 25 coding standard:

    ```
        "hardcoded_credentials:secret_in_source_med" : "Rank-19",
    ```

    `"hardcoded_credentials:secret_in_source_med"` is the name of the issue.
    This string identifies the issue. It does not appear in the Coverity Connect UI.

    `"Rank-19"` is the value of the issue.
    This string appears in a column in the Coverity Connect UI.
    For the built-in standard, the column is labeled Standard 2019 CWE Top 25.
    For a custom standard, the column might be labeled Standard 2019 CWE Top 25 - custom for myCorp.

For example, a custom standard might change the value string to alter the ranking of the issue as
displayed by the Coverity Connect Issues: By Snapshot and
Issues: Project Scope lists.
