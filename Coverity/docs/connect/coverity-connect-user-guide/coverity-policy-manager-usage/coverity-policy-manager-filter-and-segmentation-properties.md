---
title: "Coverity Policy Manager filter and segmentation properties"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-policy-manager-filter-and-segmentation-properties.html"
content_id: "_hetTvblrMyvyX584XjQiQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:08.749167+00:00"
---

# Coverity Policy Manager filter and segmentation properties

This section describes the filters, split-by
values, and group-by values that you can use when specifying a Coverity Policy Manager
chart. The availability of these items varies by metric and chart type.

A group-by value sets the primary division of the data in a chart. A split-by value sets
a secondary division of data in a map. For an example, see Figure 1.

Table 1. Coverity Policy Manager Filters

| Filter or Segmentation Property | Filter | Segmentation | Description |
| --- | --- | --- | --- |
| Action | Yes | Yes | Triage attribute used to specify the action to take with regard to a software issue. |
| Category | Yes | Yes | Category of software issue found by a checker. Examples include Memory - corruptions, Resource leaks, Null pointer dereferences. |
| Checker | Yes | Yes | Name of a Coverity checker. |
| Coding standards and vulnerability reports | Yes | Yes | Coding standards and vulnerability reports, such as MISRA-C and OWASP Top Ten. |
| Component | Yes | Yes | Coverity Connect component. If a hierarchy configuration component filter is enabled, then the Component acts as a secondary filter. |
| Contributors | No | Yes | Filtered and weighted metrics that make up a summary metric. If a chart includes a summary metric and one or more regular (non-summary) metrics, this segmentation property will not be available. |
| Custom Attributes | Yes | Yes | Custom picklist-type triage attributes. Such attributes contain a preconfigured list of one or more attribute values. |
| CWE | Yes | Yes | [Common Weakness Enumeration](http://cwe.mitre.org/) documentation of a software issue. The Coverity Connect Triage pane displays a CWE for a software issue. |
| Detected In | (Not a Filter) | Yes | Name of a Coverity Connect stream in which the issue was detected. |
| First Detected | Yes | (Not a *-by Option) | Filter for narrowing the scope of issues detected (or not detected) in snapshots up to 40 days in the past. Accepts a value of zero (0) to 40. |
| Fix Target | Yes | Yes | Triage attribute used to set the release in which to fix an issue. See Fix Target. |
| Impact | Yes | Yes | Issue impact as determined by Coverity Connect: High, Medium, Low, or Audit. |
| Issue Kind | Yes | (Not a *-by Option) | Any of the following kinds of issues: Quality, Security, Test, or Various issue. |
| Legacy | Yes | Yes | Triage attribute used to indicate whether an issue is a legacy issue or not. Some companies mark as Legacy those issues that existed undetected in the code base prior to a Coverity Analysis upgrade or change to checkers used to analyze the code base. |
| LOC | Yes | (Not a *-by Option) | Lines of code in the source code files. |
| Owner | Yes | Yes | Filter for entering the username of the owner of software issues. |
| Owner Name | Yes | Yes | Filter for entering a glob pattern that matches the first or last name (or names) of the owner of software issues. |
| Severity | Yes | Yes | Triage attribute that identifies the severity of software issues. Built-in Severity values: Unspecified, Major, Minor, Moderate. Alternative custom values are possible. |
| Status | Yes | Yes | Triage attribute that identifies the status of software issues. Status values: New, Triaged, Dismissed, Fixed. |
| Type | Yes | Yes | Descriptions of software issues (sometimes called checker subcategories) found by a checker. |
