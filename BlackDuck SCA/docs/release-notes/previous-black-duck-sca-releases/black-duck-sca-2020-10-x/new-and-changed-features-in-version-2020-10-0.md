---
title: "New and Changed Features in Version 2020.10.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features-in-version-2020.10.0.html"
content_id: "Y6EH4CYYx5OrcgbBIBER1Q"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:26.301824+00:00"
---

# New and Changed Features in Version 2020.10.0

## New custom component dashboards

So that you can easily view the component versions that are important to you, in
2020.10.0, the Component Dashboard has been replaced with custom component
dashboards based on your saved component searches. Black Duck now provides the
ability for you to search for components used in your projects using a variety of
attributes, save the search, and then use the Dashboard page to view dashboards from
those saved searches.

For each component version, the custom component dashboards display the following
information:

- Number of project versions using this component version and for each project
  version, the phase, license, review status, and security risks
- Number of vulnerabilities by risk category
- License and operational risk
- Policy violations
- Approval status
- Date the component version was first detected
- Date when the component was released, according to the Black Duck
  KnowledgeBase
- Number of new versions
- Date when a vulnerability for the component was last updated

## Component and Black Duck KnowledgeBase search enhancements

Searching for components has been enhanced by the attributes you can use to search
for the component and the information shown in the search results. The UI has also
been enhanced so that you can easily differentiate searches for components used in
your projects and searches for components in Black Duck KnowledgeBase.

While the search attributes for Black Duck KnowledgeBase searches has not changed,
the following attributes are available when searching for component versions used in
your Black Duck projects:

- Security risk
- License risk
- Operational risk
- Policy rule
- Policy violation severity
- Review status
- Component approval status
- First detected
- License family
- Missing custom field data
- Release date
- License
- Vulnerability CWE
- Vulnerability reported date

For each component version matching your search criteria, the following information
is shown:

- Number of project versions using this component version and for each project
  version, the phase, license, review status and security risks
- Number of vulnerabilities by risk category
- License and operational risk
- Policy violations
- Approval status
- Date the component version was first detected
- Date when the component was released, according to the Black Duck
  KnowledgeBase
- Number of new versions
- Date when a vulnerability for the component was last updated

These component search results can now be saved and view in the Dashboard page, as
described previously.

For each KnowledgeBase component search result, the following information is
shown:

- Number of project versions that use this component and a list of each project
  version, its phase, component version used, and associated security risk
- Commit activity trend
- Last commit date
- Number of component versions
- Tags for this component

## Enhancement to saved searches

Black Duck now provides the ability to filter and sort saved searches on the
Dashboard page.

## License conflicts

In the 2020.10.0 release, Black Duck now provides the ability for you to designate
incompatible custom license terms. You can define the custom license terms for
forbidden or required actions that are in conflict with Black Duck KnowledgeBase
terms or with your custom license terms.

Note: Currently, you cannot view incompatible license terms in a project version BOM. This
ability will be available in a future Black Duck release.

## License Management Enhancements

These three new filters have been added to the **License Terms** tab in License
Management:

- Is Associated with License(s)
- Has Incompatible Term(s)
- Responsibility

## New component usage

Black Duck has added an "Unspecified" usage which you can use to indicate that you
need to investigate the usage of the component. You may find it useful to use this
usage as the default value instead of existing defaults such as Dynamically Linked
to eliminate confusion about whether the component is assigned its true usage value
or the default value.

## New tier

Black Duck has added a tier 0, which you can use to designate as the most critical
tier.

Due to this new tier, these default policy rules have been modified to include tier
0:

- No External Tier 0, Tier 1 or Tier 2 Projects With More Than 1 High
  Vulnerability
- No External Tier 0, Tier 1 or Tier 2 Projects With More Than 3 Medium
  Vulnerabilities

There is no change to the existing tiers.

## Enhancements to custom fields

The following enhancements have been made to custom fields

- Black Duck now provides the ability for you to denote that a
  custom field is required.
  - A warning message "* Additional fields are required" appears when
    viewing custom field information. However, users can still view and
    save non-custom field information and information for non-required
    custom fields on the page if data is not entered for the required
    custom field.
  - A new filter, "Missing Custom Field Data", has been added to the BOM
    so that you can view those components in the project version BOM
    which are missing information.
- An option to clear the selection has been added when viewing custom field
  information for Boolean and single select field types.

## Allowed signature lists

Signature lists define the signatures Black Duck sends to Black Duck KnowledgeBase
web service to identify the open source software contained in the your scanned code.
Signature Scanner now has two new parameters which
you can use to create allowed signature lists for binary or source file extensions.
Each list is optional and works independently of the other list.

- **--BinaryAllowedList** *x, y, x* where *x*, *y*, *z*
  are the approved file extensions for SHA-1 (binary) files.
- **--SourceAllowedList** *a, b, c* where *a*, *b*, *c*,
  are the approved file extensions for clean SHA-1 (source code) files.

## Enhancements to vulnerability impact analysis

The following enhancements have been made to vulnerability impact analysis:

- A new column, "Reachable", has been added to the end of the
  `security_date_time.csv` project version
  report to denote whether the security vulnerability is reachable (true) or
  not reachable (false).
- A new filter, "Reachable", has been added to the project version
  **Security** tab.

## Report enhancements

The following reports have been enhanced:

- A new column, "Comments", has been added to the end of the
  `components_date_time.csv` project version
  report and lists the comments for each component.
- A new column, "Match type", has been added to the end of the
  `vulnerability-status-report_date_time.csv`
  report to identify the match type.

## Enhancements to the Report Database

The following columns have been added to the component matches table
(`component_matches`):

- `match_confidence`. Represents the confidence in the match,
  excluding snippet, binary, or partial file matches.
- `match_archive_context`. Local path to the archived file
  relative to the project’s root directory.
- `snippet_confirmation_status`. Review status of the snippet
  matches.

## HTTP/2 and TLS 1.3

To improve security and rendering of the Black Duck UI in a browser, Black Duck now
supports HTTP/2 and TLS 1.3 in the Black Duck NGINX webserver. Note that the Black
Duck NGINX Webserver continues to support HTTP/1.1 and TLS 1.2.

## Change to jobs for purging scans

The BomVulnerabilityNotificationJob and the LicenseTermFulfillmentJob now also remove
old audit events.

## Supported browser versions

- Safari Version 13.1.2 (14609.3.5.1.5)
- Chrome Version 86.0.4240.80
- Firefox 82 (64-bit)
- Internet Explorer 11.572.19041.0

  Note that support for Internet Explorer 11 is deprecated and Black Duck will be
  ending support for Internet Explorer 11 starting with the Black Duck 2021.2.0 release.
- Microsoft Edge 86.0.622.51 (Official build) (64-bit)

## Container versions

- blackducksoftware/blackduck-postgres:1.0.13
- blackducksoftware/blackduck-authentication:2020.10.0
- blackducksoftware/blackduck-webapp:2020.10.0
- blackducksoftware/blackduck-scan:2020.10.0
- blackducksoftware/blackduck-jobrunner:2020.10.0
- blackducksoftware/blackduck-cfssl:1.0.1
- blackducksoftware/blackduck-logstash:1.0.6
- blackducksoftware/blackduck-registration:2020.10.0
- blackducksoftware/blackduck-nginx:1.0.26
- blackducksoftware/blackduck-documentation:2020.10.0
- blackducksoftware/blackduck-upload-cache:1.0.15
- blackducksoftware/blackduck-redis:2020.10.0
- blackducksoftware/bdba-worker:2020.09
- blackducksoftware/rabbitmq:1.2.2

## Japanese language

The 2020.8.0 version of the UI, online help, and release notes has been localized to
Japanese.
