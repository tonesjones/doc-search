---
title: "New and Changed Features in Version 2021.4.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features-in-version-2021.4.0.html"
content_id: "85SNi6evs2hZMXrIzqbHAA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:15.432405+00:00"
---

# New and Changed Features in Version 2021.4.0

## Rapid Scanning - Limited Customer Availability feature

Black Duck's Rapid Scanning provides a way for developers to quickly determine if the
versions of open source components included in a project violate corporate policies
surrounding the use of open source. Using Black Duck Detect, Rapid Scanning
quickly returns results as it only employs package manager scanning and does not
interact with the Black Duck server database. Use Rapid Scanning when you need quick
feedback and when persisting the data in Black Duck is not necessary.

Using Rapid Scanning enables you to run thousands of scans while eliminating the need
to deploy additional instances of Black Duck. It provides you with actionable
results (such as failing the build) that can be used without a project version or
without access to Black Duck's user interface.

Note: Rapid Scanning is a limited customer access feature in the 2021.4.0 release. To use Rapid
Scanning, contact your Black Duck account management team for assistance.

## Duplicate BOM detection

Black Duck has added duplicate BOM detection which determines if a
new package manager scan duplicates the existing BOM, and if so, stops processing
the scan and denotes it as complete. For high-frequency scans that generate
redundant (identical) data, Black Duck's duplicate BOM detection can provide
significant performance improvements.

In Black Duck 2021.4.0, this feature only impacts package manager (dependency) scans
when the set of dependencies discovered by Black Duck Detect is identical to
the set from the previous scan. This capability will be extended in future
releases.

## Ability to configure Project Manager role

Black Duck now provides the ability for system administrators to
define whether the Project Manager role can manage policy violations (override
policy violations or remove overrides) or remediate security vulnerabilities for a
project.

By default, users with the Project Manager role can manage policy violations and
remediate security vulnerabilities: users upgrading to version 2021.4.0 will not see
any changes in the Project Manager role.

## Multi-license editing enhancements

When editing a license for a KnowledgeBase or custom component version, Black Duck
now gives you the ability to easily create new or edit existing multi-license
scenarios for the components at the root level or at the same level as the original
license.

## Deep license data enhancement

Black Duck now provides the ability to add file level deep licenses or remove a
manually added license.

## Report enhancements

- The following enhancements were made to the component project version report
  (`component_date_time.csv`):
  - A new column, Component origin id, has been added to the end of the
    report. This column provides the component origin ID value that
    previously could only be obtained using the API.
  - (Hub-27206)The user
    name, date, and time was added to each comment listed in the
    Comments column.

- A new column, Knowledgebase Timed Out, has been added to the end of the
  upgrade guidance project version report
  (`project_version_upgrade_guidance_date_time.csv`).
  It indicates whether or not a Black Duck KnowledgeBase timeout error
  occurred while fetching upgrade guidance data for a component
  version/origin.

## Policy management enhancements

- Project and component conditions available for a policy rule have been
  reorganized into categories to make it easier to find and select a
  condition. Also, custom fields for projects and components have been
  separated by the type of custom field.
- A new license condition, License Expiration Date Comparison for declared or
  deep licenses, lets you compare a license expiration date with the release
  date for a project version.

## Vulnerability Impact enhancement

A new vulnerability condition for policy rules, Reachable from Source, is now
available enabling you to create policy rules for vulnerabilities which have been
identified as reachable. Use this condition to prioritize those vulnerabilities with
a different (higher) priority.

## Changes to LDAP or SAML group synchronization

To reduce authentication errors, Black Duck has modified LDAP or SAML group
synchronization. Now, if you enabled group synchronization when configuring LDAP or
SAML for Black Duck, group names on your LDAP or SAML server and the Black Duck
server must be identical. If you change the name of a group in Black Duck, you must
also change the name of the group on your LDAP or SAML server to match the new name
(and vice versa). If the names are not identical, then the groups may be out-of-sync
and user permissions for that group will be lost.

## Container enhancement

A health check was added to the Binaryscanner container.

## (HUB-25902)Enhancement to the Source tab

A new filter, Code View Available, has been added to the project version
**Source** tab.

## Component and project search enhancement

The Find page for component and project searches now provides the ability to sort
search results.

## (HUB-28421) Saved search enhancement

Sorted search results are supported for saved searches letting you view the results
in the interested order on the Dashboard page.

## Performance improvement to the *Project Name* page

To improve performance, you now must select the policy violation icon ( [image: Policy violation icon] ) or override icon ( [image: Policy violation override icon] ) to view policy violation information on the **Overview** tab on the
*Project Name* page.

## Cloning enhancements

The following enhancements were made to cloning a project version:

- The default cloning options have changed. Now, all cloning options are
  enabled when a project is created.
- A new option, **Version Settings**, has been added which clones these values:
  - License
  - Notes
  - Nickname
  - Release Date
  - Phase
  - Distribution
- A new Clone Version dialog box appears when you select **Clone** from the
  *Project Name* page. If the **Version Settings** cloning option
  is enabled, only the new version name appears in the dialog box.
- To eliminate confusion, the **Version to Clone** field has been removed
  from the Create a New Version dialog box.

## License conflicts enhancement

Manual edits to a BOM, including changing the usage for a component or the license of
the project version using the **License Conflicts** or **Components** tab will
now trigger a recalculation of the license conflict.

## Enhancements to the System Information page

The usage categories on the System Information page have been enhanced.

- In the **usage: project** section, the "Scans by project" section now
  lists "Top 10 scans by project."
- In the **usage: rapid scan completion** section, "Rapid Scans by User" now
  lists the "Top 10 rapid scans by User."
- The **usage: scan completion** section has been reformatted into tables
  and includes an "identical package manager" row for duplicate BOM detection.
  Two new tables have also been added: "Code location summary information" and
  "Duplicate BOM information."

These pages show six months of data or the number of months the system has data,
whichever value is smaller.

A new job, CollectScanStatsJob, collects scan statistics shown on the **usage: scan
completion** section on the System Information page.

## Removal of installation guides

The *Installing Black Duck using Kubernetes* and the *Installing Black Duck
using OpenShift* guides have been removed from the documentation set. These
documents only contained links to the latest documentation. These links have been
added to the Black Duck documentation page in each PDF and to the home page of the
online help.

## Enhancement to the *Project Name* page

The *Project Name* page has been reorganized and enhanced and now includes the
last scanned date for each project version.

## Enhancement to the Dashboard page

HUB-26891The Policy Violations
value for 'None" in the Policy Violations Pie Chart on the Dashboard page previously
returned either 100% (no violations) or 0% (some violations), now reflects the
actual percentage for violations.

## Supported browser versions

- Safari Version 14.0.3 (15610.4.3.1.7, 15610)
- Chrome Version 90.0.4430.72 (Official Build) (x86_64)
- Firefox Version 88.0 (64-bit)
- Microsoft Edge Version 90.0.818.41 (Official build) (64-bit)

## Container versions

- blackducksoftware/blackduck-postgres:1.0.16
- blackducksoftware/blackduck-authentication:2021.4.0
- blackducksoftware/blackduck-webapp:2021.4.0
- blackducksoftware/blackduck-scan:2021.4.0
- blackducksoftware/blackduck-jobrunner:2021.4.0
- blackducksoftware/blackduck-cfssl:1.0.1
- blackducksoftware/blackduck-logstash:1.0.9
- blackducksoftware/blackduck-registration:2021.4.0
- blackducksoftware/blackduck-nginx:1.0.31
- blackducksoftware/blackduck-documentation:2021.4.0
- blackducksoftware/blackduck-upload-cache:1.0.16
- blackducksoftware/blackduck-redis:2021.4.0
- blackducksoftware/blackduck-bomengine:2021.4.0
- blackducksoftware/bdba-worker:2021.03
- blackducksoftware/rabbitmq:1.2.2

## Japanese language

The 2021.2.0 version of the UI, online help, and release notes has been localized to
Japanese.
