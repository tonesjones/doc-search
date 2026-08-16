---
title: "New and Changed Features in Version 2021.2.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features-in-version-2021.2.0.html"
content_id: "tLbx47_M7R0rEP_VTLpacQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:19.416365+00:00"
---

# New and Changed Features in Version 2021.2.0

## New custom vulnerability dashboards

So that you can easily view the vulnerabilities that are important to you, in
2021.2.0, the Security Dashboard has been replaced with custom vulnerability
dashboards based on your saved vulnerability searches. Black Duck now provides the
ability for you to search for vulnerabilities used in your projects and/or Black Duck KnowledgeBase using a variety of attributes, save the search, and then
use the Dashboard page to view dashboards from those saved searches.

For each vulnerability, the custom vulnerability dashboard displays the following
information:

- BDSA or NVD vulnerability ID. Selecting the vulnerability ID shows more
  information on the vulnerability, such as additional score values.
- Number of project versions affected by this vulnerability with a link to view
  the **Affected Projects** tab for the vulnerability which lists the
  project versions affected by this vulnerability.
- Overall risk score.
- Whether a solution, workaround, or exploit is available.
- Date when a vulnerability was first detected, published, and last
  modified.
- Common Weakness Enumeration (CWE) number for this security vulnerability.

## Vulnerability search enhancements

Searching for vulnerabilities has been enhanced by the attributes you can use to
search for the vulnerability and the information shown in the search results. You
can select whether to search for vulnerabilities in your projects or vulnerabilities
in Black Duck KnowledgeBase.

The following attributes are available when searching for vulnerabilities:

- Affecting projects
- Default Remediation
- Reachable
- Exploit
- First Detected
- Remediation Status
- Solution
- Base Score
- Exploitability Score
- Impact Score
- Overall Score
- Published Year
- Severity
- Source (BDSA or NVD)
- Temporal Score
- Workaround

These vulnerability search results can now be saved and view in the Dashboard page,
as described previously.

## Ability to manage license conflicts for projects

To reduce the risk of license infringement, you need to understand when a component
in your BOM has a license with terms that are incompatible with the declared license
of a project. Black Duck now identifies these license term conflicts and displays
them on a new **License Conflict** tab located on the **Legal** tab.

You can also set a policy rule that is triggered when a component's license is in
conflict with the license of a project version.

Note that Black Duck only determines license conflicts for component versions with
high license risk. For the Black Duck license risk model, "high risk" means that
licenses in this family tend to have license conflicts under this business scenario
(combination of distribution type and component usage) making them incompatible.
Medium or low risks means it may have risks if the business scenario changes (or is
defined incorrectly) or due to other, non-license conflicts factors.

## Dependencies

When direct or transitive dependencies are found in a Black Duck Detect scan, Black
Duck now lists the number of matches for each type of dependency in the project
version's **Security** tab.

For transitive dependencies, a dependency tree shows the components that brought in
this dependency, the vulnerabilities by severity level, and a match count for the
number of times the component was brought in with that dependency path.

## Report database enhancements

A new table for ignored components, (`component_ignored`, has been
added to the report database. It has these columns:

- `id`. ID
- `project_version_id`. Project version ID.
- `component_id`. Component ID.
- `component_version_id`. Component version ID.
- `component_name`. Component name.
- `component_version_name`. Component version name.
- `version_origin_id`. Version origin ID.
- `origin_id`. Origin ID.
- `origin_name`. Origin name.
- `ignored`. Boolean that indicates whether the component is
  ignored.
- `policy_approval_status`. Policy approval status.
- `review_status`. Review status of the component.
- `reviewed_by`. User who reviewed the component.
- `reviewed_on`. When the component was reviewed.
- `security_critical_count`. Number of critical security
  vulnerabilities.
- `security_high_count`. Number of high security
  vulnerabilities.
- `security_medium_count`. Number of medium security
  vulnerabilities.
- `security_low_count`. Number of low security
  vulnerabilities.
- `security_ok_count`. Number of no security
  vulnerabilities.
- `license_high_count`. Number of high license risk.
- `license_medium_count`. Number of medium license risk.
- `license_low_count`. Number of low license risk.
- `license_ok_count`. Number of no license risk.
- `operational_high_count`. Number of high operational risk.
- `operational_medium_count`. Number of medium operational
  risk.
- `operational_low_count`. Number of low operational risk.
- `operational_ok_count`. Number of ok operational risk.

A new table for user information, `user`, has been added to the report
database. It has these columns.

- `id`. ID.
- `first_name`. User's first name.
- `last_name`. User's last name.
- `username`. User's username in Black Duck.
- `email`. User's email address.
- `active`. A boolean that indicates whether this user is
  active.
- `last_login`. Time that the user last logged in to Black Duck.

## License editing enhancements

The following enhancements were made when editing licenses in the BOM.

- When editing a license for a component, Black Duck now gives you the ability
  to easily create new or edit existing multi-license scenarios for the
  components in your BOM at the root level or at the same level as the
  original license.
- If you selected a different license for a component, you can now revert the
  license to its original license as defined in Black Duck KnowledgeBase.

- A new option in the *Component Name Version* Component License dialog
  box makes it easily discernible that there is an edit mode.

## Report enhancement

A new column, Archive Context and Path, has been added to the end of the
`source_date_time.csv` project version report. This
column concatenates the information shown in the existing Path and Archive Content
columns to provide the full path for each component.

## Notices File Report

The Notices File Report has been improved so that copyright data no longer contains
duplicate information for a single component-origin.

## Binary scan enhancement

(HUB-27327 25496)Binary scans now
return partial matches in addition to full matches.

## Deep license data enhancement

When reviewing evidence of deep license data in a file, Black Duck
now highlights the license text that triggered the license text match.

## BOM Engine

To improve Black Duck UI response time, license updates will now be performed by the
BOM Engine. This process can be seen as a "License Update" or "License Term
Fulfillment Update" event in the BOM Processing Status dialog box, accessible from
the BOM.

## Black Duck tutorials

To easily view training for Black Duck, you can now select **Black Duck
Tutorials** from the Help menu ( [image: Help Menu icon] ) in the Black Duck UI.

## Modification to password configuration

Users with the System Administrator role can now set password requirements for local
Black Duck accounts. Users with the Super User role can no longer configure password
requirements.

## Policy rule enhancement

Policy management now provides the ability to create policy rules based on project
version custom fields for Boolean, Date, Drop Down, Multiple Selections, Single
Selection, and Text field types.

## Hosting location for Black Duck Detect

Black Duck customers with limited external connectivity can now define the internal
hosting location of Black Duck Detect. Using this information, these users
can leverage Code Sight for deployment across their developer base to run on-demand
Software Composition Analysis (SCA) scans.

## Saved search dashboard enhancements

For each saved search shown on the Dashboard page, Black Duck now lists the date and
time the search was last updated. A popup displays the saved search filters with a
link so that you can open the Find page to edit and save a revised saved search.

## Snippet triage enhancement

Icons have been added to the **Source** tab to make it easier to differentiate
unconfirmed ( [image: image] ),
confirmed ( [image: image] ), and
ignored ( [image: image] )
snippets.

## Supported browser versions

- Safari Version Version 14.0.3 (15610.4.3.1.6, 15610)
- Chrome Version Version 88.0.4324.150 (Official Build) (x86_64)
- Firefox Version 85.0.2 (64-bit)
- Microsoft Edge Version 88.0.705.63 (Official build) (64-bit)

## Container versions

- blackducksoftware/blackduck-postgres:1.0.16
- blackducksoftware/blackduck-authentication:2021.2.0
- blackducksoftware/blackduck-webapp:2021.2.0
- blackducksoftware/blackduck-scan:2021.2.0
- blackducksoftware/blackduck-jobrunner:2021.2.0
- blackducksoftware/blackduck-cfssl:1.0.1
- blackducksoftware/blackduck-logstash:1.0.9
- blackducksoftware/blackduck-registration:2021.2.0
- blackducksoftware/blackduck-nginx:1.0.30
- blackducksoftware/blackduck-documentation:2021.2.0
- blackducksoftware/blackduck-upload-cache:1.0.15
- blackducksoftware/blackduck-redis:2021.2.0
- blackducksoftware/blackduck-bomengine:2021.2.0
- blackducksoftware/bdba-worker:2020.12-1
- blackducksoftware/rabbitmq:1.2.2

## Supported Docker versions

Black Duck installation supports Docker versions 18.09.x, 19.03.x, and 20.10.x (CE or
EE).

## Docker webapp-volume

HUB-26971The Docker webapp-volume
is no longer used in orchestration. Optionally, users can backup and prune the
Docker webapp-volume; otherwise no action is required.

## Ubuntu operating system

The preferred operating system for installing Black Duck in a Docker environment for
Ubuntu is now version 18.04.x.

## Japanese language

The 2020.12.0 version of the UI, online help, and release notes has been localized to
Japanese.
