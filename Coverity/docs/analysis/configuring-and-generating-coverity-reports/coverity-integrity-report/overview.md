---
title: "Overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/overview.html"
content_id: "VhJ2487eWfWEH4fWzMUzXA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:33.267470+00:00"
---

# Overview

Leaders of software development teams use Coverity Integrity Report PDF-based charts to
see the current impact of Coverity Connect issues. Administrators set up and run
Coverity Integrity Report to produce these reports.

For extensive web-based charts that you can print to file, see "Coverity Policy Manager
usage" in the Coverity Platform 2026.6.0 User and Administrator Guide.

The Coverity Software Integrity Report is included with Coverity Analysis and Coverity Connect.
The Coverity Software Integrity Report tool generates a high-level assessment of the
code in a C/C++ application and its components. The report:

- Rates the integrity of the code and its components in relation to industry
  standards.
- Identifies the number of occurrences of important classes of high-risk and
  medium-risk defects in the code.
- Provides an overview of defect severity ratings and triage states that developers
  have assigned to the defects in Coverity Connect. The report identifies the
  number of:

  - High-severity, unspecified, and other defects in the code and code
    components.
  - Outstanding, dismissed, and fixed defects in the code.
- Can be localized.

Note: The total number of issues in the report should be equal to the sum of
all values in the Count column in Coverity Connect while in
Issues mode. This is not necessarily the same as the number of matching issues shown in
Connect.

Important: In order to invoke the Coverity Integrity Report, you must be assigned a
role that contains, at minimum, the following permissions:

- Access web services
- View project
- View defects

For more information about RBAC roles and permissions, see "Roles and role-based
access control" in the Coverity Platform 2026.6.0 User and Administrator Guide.
