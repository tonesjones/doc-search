---
title: "Using Filters to Display Findings Data"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/using-filters-to-display-findings-data.html"
content_id: "4KYebJmUmujsXyQsGnKIQQ"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:02.881323+00:00"
content_hash: "35d877132afda6c4dc7aedc3b1f8565ac2fa25af2b4e9d6f6dc6c270b7229661"
---

# Using Filters to Display Findings Data

Software Risk Manager provides a variety of filters and filter options that allow you to
target specific information.

Click the Findings icon in the navigation bar to open the Findings page.

[image: image]

Filters are displayed to the left of the findings.

[image: image]

Clicking the arrow icon to the left of the filter name will expand the window and show
the filter options and filter-specific information about the findings. Clicking any of
the filter options will immediately apply those parameters to the list of findings.

The available filters include the following, and are detailed in the sections that follow:

- Policy Violations
- Fix-by Urgency
- Type
- Project
- Project Metadata
- Tool
- Detection Method
- Severity
- Location
- Container Image
- Age
- First Seen by SRM
- Date Modified
- Tool Overlaps
- Standards
- Tags
- Assignee
- Predicted Status
- Triage Status
- Pending Triage Status
- Finding Status
- Issue Tracker Association (if configured)
- Issue Tracker Resolution (if configured)

## Policy Violations Filter

The Policy Violations filter allows you to filter findings based on existing policy
violations. Expand the filter window and select which filter options you want to
apply to the list of findings.

[image: image]

The filter window shows the number of findings and the percentage of violations
compared to the total number of findings.

## Fix-by Urgency Filter

The Fix-by Urgency filter allows you to filter findings based on urgency. Expand the
filter window and select which filter options you want to apply to the list of
findings.

[image: image]

The filter window shows the number of findings for each of the following urgency levels:

- Overdue
- Due Soon
- On Track
- No Fix-by Set

## Type Filter

The Type filter allows you to filter findings based on finding type. Expand the
filter window and select which filter options you want to apply to the list of
findings.

[image: image]

The filter window shows the number of findings associated with a specific finding
type.

## Project Filter

The Project filter allows you to filter findings based on individual projects. Expand
the filter window and select which filter options you want to apply to the list of
findings.

[image: image]

Note: This filter only appears on "aggregated" versions of the Findings page, that is,
for "All Projects," or for a project group with its members.

The filter window displays the projects associated with the findings in two ways:

- Projects displayed as a flat list.
- Projects displayed in a tree view.

You can switch between display modes by selecting it from the first dropdown menu in
the filter's header.

## Project Metadata Filter

The Project Metadata filter allows you to filter findings based on defined metadata
(see Adding and Configuring
Project Metadata Fields).

Note: "Multiline"
metadata is not supported.

Expand the filter window and select which metadata options you want to apply to the
list of findings.

[image: image]

Note: This filter only appears on "aggregated" versions of the Findings page, that is,
for "All Projects."

## Tool Filter

The Tool filter allows you to filter findings based on a specific tool's result
types. Expand the filter window and select which filter options you want to apply to
the list of findings.

[image: image]

The filter window displays a list of the tools used in the analysis and the number of
findings associated with each tool. The tool result type hierarchy typically follows
a hierarchy of "Tool" » "Category" » "Name," following the same hierarchy as in the
Tool Config
page.

## Detection Method Filter

The Detection Method filter allows you to filter findings based on the detection
method used to create the finding. Expand the filter window and select which filter
options you want to apply to the list of findings.

[image: image]

Note: Only the categories that apply to your project will be displayed.

The filter window lists the supported detection methods and displays the number of
findings associated with each one:

- `Cloud Infrastructure Analysis`: Findings pertaining to
  cloud-hosted infrastructure
- `Component Analysis`: Third-party dependencies in your
  project that have known vulnerabilities
- `Container Analysis`: Findings within container runtimes or
  container images
- `Database Analysis`: Findings pertaining to databases
- `Dynamic Analysis`: Findings detected by Dynamic Application
  Security Testing (DAST) techniques
- `Hybrid Analysis`: Findings detected by multiple detection
  methods, for example, Static Analysis plus Dynamic Analysis
- `Interactive Analysis`: Findings detected by Interactive
  Application Security Testing (IAST) techniques
- `Network Analysis`: Findings pertaining to network
  infrastructure
- `Static Analysis`: Findings detected by Static Application
  Security Testing (SAST) techniques
- `Threat Modeling`: Findings detected by threat modeling
  techniques
- Plus any custom detection method

## Severity Filter

The Severity filter allows you to filter findings based on the level of severity that
is reported by a specific tool. Expand the filter window and select which filter
options you want to apply to the list of findings.

[image: image]

The filter window displays the number of findings belonging to each of the following
risk categories:

- Info
- Low
- Medium
- High
- Critical
- Unspecified

For more information on risk mapping, see Tool Status and Severity
Mapping.

## Location Filter

The Location filter allows you to filter findings based on the finding's location.
Expand the filter window and select which filter options you want to apply to the
list of findings.

[image: image]

The filter window shows where each finding is located, reflecting the directory and
file hierarchy of the codebase. Location categories that may apply to your project
include files, URLs, and logical locations.

For .NET results, in some cases (especially if PDB files are not uploaded), source
locations may not be available. Instead, a *Logical Locations*item will be
shown, along with locations organized by namespace, class, and method.

## Container Image Filter

The Container Image filter allows you to filter findings based on the names of
container images that were discovered in Container Analysis results. Expand the
filter window and select which filter options you want to apply to the list of
findings.

Note: Images without an associated name are not shown in the filter.

The filter window
lists the supported container images and the findings associated with
each.

## Age Filter

The Age filter allows you to filter findings according to when that finding first
appeared in an analysis. The Age filter calculates age based on tool-reported dates
(when available). If the finding has no supported tools, the date reported is the
first time the finding was seen by SRM. Note that the "first seen" date is fluid;
that is, if new data is ingested from a tool with an earlier date, the relevant
findings will be updated to reflect this earlier date.

Expand the filter window and select which filter options you want to apply to the
list of findings.

[image: image]

The filter window displays a set of pre-defined age ranges and the number of related
findings.

## First Seen by SRM Filter

The date the finding was first seen by SRM. Note: This date is not the same as the
"first seen on" date for the finding, which is shown in the header of the Finding
details page.

Note: This filter will not appear on "aggregated" versions of the Findings page, that is,
for "All Projects," or for a project group with its members.

[image: image]

## Last Modified Filter

Displays when the finding was last modified.

Note: This filter will not appear on "aggregated" versions of the Findings page, that is,
for "All Projects," or for a project group with its members.

[image: image]

## Tool Overlaps Filter

The Tool Overlaps filter allows you to filter findings based on correlation logic.
Expand the filter window and select which filter options you want to apply to the
list of findings.

[image: image]

The filter windows displays a breakdown of findings based on the degree of
correlation of its associated tool results. For example, *Was a finding detected
by 1 tool, 2 tools, or more?* Or *Were the 2 tools SpotBugs and PMD, or
JSHint and PMD?* Actual correlation logic is determined by the project's
Analysis
Configuration.

## Standards Filter

The Standards filter allows you to filter findings related to a specific industry
standard. Expand the filter window and select one or more filter options to apply to
the list of findings.

[image: image]

The filter window displays a list of the following standards and the number of
findings related to each one:

- Architectural Concepts
- CERT C Secure Coding Standards
- CERT C++ Secure Coding Standards
- CERT Java Secure Coding Standards
- CISQ Quality Measures (2016)
- CISQ Quality Measures (2020)
- CLASP
- CWE All
- CWE Development Concepts View
- CWE Research Concepts View
- CWE Top 25 Most Dangerous Software Errors (2019)
- CWE Top 25 Most Dangerous Software Errors (2022)
- DISA STIG 3.10
- DISA STIG 4.10
- DISA STIG 5.1
- HIPAA
- Hardware Design
- MISRA C (2012)
- MISRA C++ (2008)
- NIST 800-53 Revision 4
- OWASP ASVS v4
- OWASP Mobile Top 10
- OWASP Top Ten (2013)
- OWASP Top Ten (2017)
- OWASP Top Ten (2019)
- OWASP Top Ten (2021)
- PCI DSS 3.1
- PCI DSS 4.0
- Seven Pernicious Kingdoms
- Software Fault Patterns
- WASC Threat Classification

## Tags Filter

The Tags filter allows you to filter findings based on finding tags. Expand the
filter window and select which filter options you want to apply to the list of
findings.

[image: image]

The filter window shows the distribution of findings based on an assigned tag. Each
number corresponds to the number of findings to which each tag has been
assigned.

## Assignee Filter

The Assignee filter allows you to filter findings based who was assigned to that
finding. Expand the filter window and select which filter options you want to apply
to the list of findings.

[image: image]

## Predicted Status Filter (if configured)

The Predicted Status filter allows you to filter findings based on existing machine
learning configuration settings. Expand the filter window and select which filter
options you want to apply to the list of findings

[image: image]

The Predicted Status filter is shown only if machine learning is enabled (see the
Machine Learning
Control Panel section).

Filtering options include filtering against findings with *Predicted Status* of
To Be Fixed, False Positive, or Unknown, as well as filtering against *Prediction
Confidence*, which ranges from 0 to 100 percent. Selecting multiple predicted
statuses to filter on will include any finding that has any one of the selected
predicted statuses. Selecting a sub range for prediction confidence will include any
finding that has a predicted status matching one of the selected statuses as well as
a prediction confidence that exists in the selected sub range (inclusively).

Note: This filter is only available in Software Risk Manager with the Machine Learning
Triage Assistance add-on.

## Triage Status Filter

The Triage Status filter allows you to filter findings based on the triage status of
the finding (e.g., fixed, mitigated, etc.). Expand the filter window and select
which filter options you want to apply to the list of findings.

[image: image]

## Pending Triage Status Filter

The Pending Triage Status filter shows triage status requests that are pending
approval. Expand the filter window and select which filter options you want to apply
to the list of findings.

[image: image]

## Finding Status Filter

The Finding Status filter allows you to filter findings based on the status of the
finding (e.g., new, existing, or gone). Expand the filter window and select which
filter options you want to apply to the list of findings.

[image: image]

## Issue Tracker Association (if configured)

The Issue Tracker Association filter allows you to filter findings based on whether a
finding has an associated issue. Expand the filter window and select which filter
options you want to apply to the list of findings.

[image: image]

This filter option appears only if the project has been configured for issue tracking
(see [Issue Tracker Configuration](http://localhost:8080/help/html/user_guide/Project-Management/issue-tracker.html)). The filter
window shows findings broken down by whether there is an associated issue, which
issue tracker type (Jira, Azure DevOps, ServiceNow, GitHub, GitLab, etc.) the issue is
associated with, the issue's status, and the specific issue.

Note: Terminology can differ between different issue trackers (e.g., "issue" vs "work
item," "status" vs "reason," etc.), but Software Risk Manager defaults to "issue"
and "status" when a generic term is needed.

## Issue Tracker Resolution (if configured)

The Issue Tracker Resolution filter allows you to filter findings based on resolution
status. Expand the filter window and select which filter options you want to apply
to the list of findings.

[image: image]

This filter option appears only if the project has been configured for issue tracking
(see Issue Tracker
Configuration). The filter window shows findings broken down by whether
there is an associated issue, which issue tracker type (Jira, Azure DevOps,
ServiceNow, GitHub, GitLab, etc.) the issue is associated with, whether the issue is
resolved, the resolution status, and the specific issue.
