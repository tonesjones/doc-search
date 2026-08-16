---
title: "Pre-defined filters"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/pre-defined-filters.html"
content_id: "tmJJxt5q0QIbe1dlJBo16w"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:49:28.068142+00:00"
---

# Pre-defined filters

Pre-defined filters represent common search criteria to quickly focus your list of
issues. You can add filter expressions, or edit the attributes and values in these
filters to customize them. For information about editing pre-defined filters, see custom filters.

Coverity Desktop provides the following pre-defined filters:

Table 1. Built-in filter fields

| Column | Description |
| --- | --- |
| All Issues | Displays all issues present in the current analysis. |
| All Outstanding Issues | Displays all outstanding issues present in the current analysis. |
| Fix Required | Displays all issues that have action - fix required. |
| Found Today | Displays all issues that were found by the analysis for the current day. |
| High Impact | Displays all issues that have an impact rating of High. |
| Local Only | Displays only local issues that are not present in the reference stream. |
| Major Severity | Displays all issues with a severity of Major. |
| Missing Locally | Displays only issues that are present in the reference stream, but not found in the latest local analysis. |
| Triage Needed | Displays all issues that are unclassified. |
| My Outstanding* | Displays all outstanding issues that are assigned to the current user. |
| Outstanding Defects | Displays all outstanding quality defects. |
| Outstanding Security Risks | Displays all security vulnerabilities found by Coverity Analysis. |

*. To modify the owner of the My Outstanding issues filter, manually set the Owner field
to the user name of the person you want to own the issues listed as My Outstanding.
