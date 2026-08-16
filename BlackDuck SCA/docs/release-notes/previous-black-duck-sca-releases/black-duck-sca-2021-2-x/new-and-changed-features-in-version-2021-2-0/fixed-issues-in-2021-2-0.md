---
title: "Fixed Issues in 2021.2.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2021.2.0.html"
content_id: "UiAAN5xTNOnTtyxfZW270w"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:20.535529+00:00"
---

# Fixed Issues in 2021.2.0

The following customer-reported issues were fixed in this release:

- Hub-24409 - solved with new vuln search; Hub-26860 - no Hub fix; HUB-26959 -
  fixed in 2020.12.0; 27618 - reopened of item to be fixed in 21.4
- (Hub-22103). Fixed an issue whereby the Black Duck server did not respond in
  time when updating a license status.
- (Hub-22623). Fixed an issue whereby the Summary Dashboard frequently timed
  out for enterprise customers when loading in the UI.
- (Hub-24332). Fixed an issue where scanning the same code location caused
  duplicated notifications.
- (Hub-25374). Fixed a permission error for database azure_maintenance.
- (Hub-25549). Fixed an issue with /api/uploads where the created code location
  was not mapped to the project/version when codeLocationName contained
  Japanese characters.
- (Hub-25580). Fixed an issue whereby components shown in the BOM were
  incorrectly sorted after page 9.
- (Hub-25666). Fixed a pagination issue for the endpoint /usergroups/<group
  #>/roles.
- (Hub-26030). Fixed an issue where sorting options were not retained for a
  dashboard by project name after performing an action.
- (Hub-26324). Fixed an issue where the following error
  "java.lang.IllegalStateException: Parent of
  [file:/C:/src/External/PackageManager/ProjectTemplates/com.unity.template.universal-10.1.0.tgz]
  does not exist" occurred when uploading a scan.
- (Hub-26343). Fixed an issue where Black Duck could not be registered as the
  registration container ran out of heap space.
- (Hub-26493). Fixed a confusing error message which appeared when a user
  removed themselves as a member of a project.
- (Hub-26501). Fixed an issue whereby the cordova-plugin-inappbrowser component
  could not be selected in the Edit Component dialog box.
- (Hub-26536). Fixed an issue whereby a watched project displayed the Unwatched
  icon ( [image: image] ) in the
  page header.
- (Hub-26540). Fixed an issue whereby the initial configuration of SAML did not
  go into effect unless Black Duck was restarted.
- (Hub-26615). Fixed an issue whereby a user with the Project Manager role in
  Project A and Project Manager and Project Code Scanner roles in Project B
  could upload scans to Project A.
- (Hub-26616). Fixed an issue whereby attempting to ignore a snippet would fail
  with the following error message: "Unable to update existing snippet
  adjustment because changing the consumer, producer, adjustment type, start
  line, end line is not supported."
- (Hub-26712, 26962). Fixed an issue whereby the snippet icon shown in the tree
  view on the **Source** tab did not clear after a snippet match was
  confirmed.
- (Hub-26726). Fixed an issue whereby the "not in" option was not available for
  custom fields when creating a policy rule.
- (Hub-26807). Fixed an issue whereby a HTML status code 404 was received when
  attempting to GET custom fields for the BOM component version.
- (Hub-26815). Fixed an issue whereby saving SAML integration settings caused
  the page to reload and switch Identity Provider Metadata settings.
- (Hub-26904). Fixed an issue whereby the match count value shown on the
  project version **Activity** section on the **Settings** tab was not
  the same as on the *Scan Name* page.
- (Hub-26930). Fixed an issue where notifications where not triggered for a
  component.
- (Hub-27002). Fixed an issue whereby the wrong notification was sent when a
  cloned project was created.
- (Hub-27049). Fixed an issue whereby the License Terms category for a Project
  Version Report could not be seen in the Black Duck UI without a user being
  assigned the License Manager role.
- (Hub-27208). Fixed an issue with blackduck-nginx whereby Black Duck Alert
  failed to load when SAML was configured.
- (Hub-27227). Fixed an issue whereby snippet matching took a long time to
  complete.
- (Hub-27264). Fixed an issue whereby reviewing a component reset its usage to
  its default value.
- ( Hub-27344). No Hub fix.
- (Hub-27681). Fixed an issue whereby the BOM Engine had to be started by a
  root user when deployed on Kubernetes with a custom security context.
