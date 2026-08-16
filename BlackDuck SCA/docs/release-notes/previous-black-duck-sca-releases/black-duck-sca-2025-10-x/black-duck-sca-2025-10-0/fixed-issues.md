---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "wY16oKeMeAHwC~Rs8uyKBg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:22.705609+00:00"
---

# Fixed issues

The following customer-reported issues have been fixed in this release:

- (HUB-36738). Resolved a bug in Black Duck SCA versions 2022.7.x
  and 2022.10.x that caused re-scanning projects with backslash syntax to fail
  with a "412 Precondition Failed" error; upgrading to Black Duck SCA 2025.10.0 allows successful re-scans with such
  project names.
- (HUB-43219). Addressed a bug causing unmatched SBOM components to display blank
  names and missing version info after import; initial fixes have been
  implemented, with further updates planned for the 2025.10.0 release to improve
  the handling and editing of unmatched components.
- (HUB-44281). Updated the REST API documentation to remove references to the
  Hierarchical BOM (HBOM) feature, which is no longer offered.
- (HUB-44483). Resolved a bug causing intermittent missing Component Link
  information in generated reports in Black Duck SCA, affecting
  versions 2024.7.3, 2024.10.1, and later; a temporary workaround involving
  database modifications and service restarts has been identified.
- (HUB-44511). The Integrations Manager role in Black Duck SCA was
  unable to manage SCM integrations, as it could only manage the Artifactory
  integration. This functionality has now been corrected to ensure that the
  Integrations Manager role can manage SCM onboarding configurations, aligning
  with expectations for role responsibilities.
- (HUB-44558). Resolved a "412 Precondition Failed" error when adding different
  versions of the same project to a Bill of Materials (BOM), which arose from
  overly restrictive cyclic dependency detection; the fix removes the restrictive
  check and implements improved cycle detection, addressing legitimate use cases
  for customers using multiple project versions.
- (HUB-44580). Fixed an issue where Detect Desktop scans failed with the error
  message "Request authentication failed" due to a trailing slash (/) in the
  blackduck_url, which caused authentication failures during scans.
- (HUB-44817). Resolved an issue where user sessions did not expire after the
  configured timeout of 1800 seconds, causing security concerns; the issue was
  linked to browser session cookies not expiring.
- (HUB-44895). Fixed an issue where users with the project-level Project Manager
  role could incorrectly assign any project-level user roles (including Project
  Administrator) to themselves and others.
- (HUB-44558). Resolved a bug that resulted in a 412 error when attempting to add a
  different version of a project to the Bill of Materials (BOM) of another version
  of the same project. This issue blocked valid use cases, particularly for
  customers who utilize multiple versions of the same project in their BOMs, such
  as in microservices architectures. The problem originated from a fix designed to
  prevent projects without versions from being added to BOMs; however, it
  unintentionally restricted the addition of different versions of the same
  project. The team has decided to remove this restrictive check, allowing for the
  addition of different project versions without causing unnecessary upgrade
  friction. Cyclic dependency detection will continue to be enforced to prevent
  recursive references, ensuring a balance between functionality and safety.
- (HUB-45006). Resolved a bug where Japanese characters in uploaded source code
  were not displayed properly due to encoding issues; the root cause was
  identified as the backend storage service returning raw bytes without encoding
  info.
- (HUB-45115). Resolved a bug preventing users with the Project Code Scanner role
  from mapping or unmapping projects as expected, due to backend permission checks
  on the codelocation API; UI improvements and API enhancements were implemented
  to clarify scan access post-unmap. A warning is now displayed in the UI before
  unmapping to inform users about potential access loss.
- (HUB-45186). Resolved an issue where the view for policy violations did not
  accurately reflect unfulfilled licenses in the component version view.
- (HUB-45308). Resolved a bug causing mismatches in vulnerability counts between
  the upgrade guidance and component details pages, where UI icons inaccurately
  displayed vulnerabilities.
- (HUB-45356, HUB-45541, HUB-46005). Fixed additional cases of security risk count
  discrepancies.
- (HUB-45396). Resolved a bug in SBOM import where the '+' character in PURLs was
  incorrectly encoded as '%20' instead of '%2B', leading to unmatched components;
  the root cause was a flaw in the package URL library, which has been fixed by
  updating to a new dependency version.
- (HUB-45399). Resolved a connectivity bug in Docker Swarm environments where Black Duck SCA could not connect to an external PostgreSQL
  database, with SSL mode enabled or disabled; the issue was traced to incorrect
  SSL certificate path settings and permissions. A fix was implemented by adding a
  new docker-compose.externaldb-cert-volume.yml for proper certificate volume
  mounting and adjusting the HUB_POSTGRES_SSL_MODE variable.
- (HUB-45434). Addressed an API bug where deleting an LTS version via the general
  version delete endpoint returned a 204 No Content response instead of a 4xx
  error; this behavior led to inconsistencies where the version appeared deleted
  in the UI but remained in the database. The fix ensures that attempts to delete
  or manipulate an LTS version using the incorrect endpoint will be rejected,
  providing an appropriate error response instead.
- (HUB-45472). Resolved an issue where adjustments to component matches were
  indicated as successful in the UI, displaying the message "The component changes
  were successfully saved," and returning a status 200 for the PUT request.
  However, the edits were not being applied as expected. This issue has been fixed
  to ensure that component match adjustments are correctly applied.
- (HUB-45488). Resolved a bug causing roles to be duplicated within user groups.
  This issue stemmed from identical role names for projects and groups in the
  backend API, leading to inconsistencies. The user interface alone could not
  address the duplication, necessitating backend changes to differentiate role
  names—such as adding "Project Group Viewer" to avoid overlaps. Additionally,
  similar scope-based fixes referenced from a previous issue (HUB-44826) were
  implemented to further prevent duplication by utilizing role scopes. It was also
  noted that certain roles, including BOM Annotator, BOM Manager, Policy Violation
  Reviewer, and Project Code Scanner, were not appearing correctly. This fix
  ensures accurate role representation and resolves the duplication issue.
- (HUB-45537). Resolved a bug in the binary scan results UI where match type,
  component name, license, and usage information were not displayed, unlike
  package manager scans.
- (HUB-45593). Resolved a bug in the search function on the online help page that
  caused it to become unresponsive and return no results when using the Japanese
  or Simplified Chinese language setting in the browser.
- (HUB-45605). Resolved a bug where uploading a valid SBOM with no components
  incorrectly marked the project version as "Never Scanned," causing confusion in
  reporting; the fix ensures that the scanned timestamp updates correctly even
  when no PURLs are present.
- (HUB-45617). Fixed an issue where the login page would still appear when the Black Duck SCA was actually down.
- (HUB-45648). Resolved a bug where the system-level project setting for License
  Conflicts was not inherited when creating a project by uploading BDIO files;
  unlike projects created through scanning or the UI, the License Conflicts
  setting was not enabled in the automatically created project. The fix ensures
  that this setting is now inherited correctly across all project creation
  methods.
- (HUB-45675). Improved handling of RESERVED CVEs in the Black Duck SCA API by updating UI messaging; previously, a 404
  error for RESERVED CVEs was indistinguishable from invalid CVEs. The UI now
  displays a specific message for RESERVED CVEs when accessed via BDSA links,
  indicating they are "Reserved but not yet published by the NVD," while direct
  navigation to invalid CVE URLs presents a generic "not found" message.
- (HUB-45734). Fixed an issue in SCASS-enabled NPM package manager scans that
  resulted in unexpected and incorrect match results compared to non-SCASS scans.
  The issue arose due to the use of fuzzy matching in SCASS-enabled scans, which
  led to incorrect version matches, while HUB's default setting utilized exact
  matching. Additionally, uploading BDIO files bypassed SCASS, yielding more
  accurate results than live SCASS scans.
- (HUB-45781). Fixed an issue where unknown licenses did not appear in Notice File
  reports unless part of an AND/OR clause.
- (HUB-45782). Resolved a bug that prevented users from removing Originator
  information set for components under 'SBOM Fields'; users could input Originator
  Entity and Name but were unable to clear these fields upon updating.
- (HUB-45788). Resolved a performance issue where the "Dashboard Summary" page took
  longer than expected to load all sub-blocks for some customers. The
  investigation identified that the `GET
  /internal/dashboard-top-security-risk` endpoint was causing
  significant delays in page rendering.
- (HUB-45835). Resolved documentation errors in the Black Duck SCA
  User Guide, including adjustments to snippet matching size, BOM/JSON file
  naming, and project creation instructions. The maximum snippet size is now
  correctly stated as adjustable between 1-4 MB with a default of 1 MB. Outdated
  BOM/JSON naming instructions were removed, and project creation clarity was
  improved based on SCM integration status.
- (HUB-45851). Clarified the behavior of the "Component Adjustments" setting in
  project versions by updating the UI text to accurately reflect that adjustments
  apply across all project versions where the component exists, while manually
  added components must be handled individually. The revised description and a
  proposed "Learn More" link to documentation enhance user understanding.
- (HUB-45868). Resolved a bug that caused the average signature scan size metric to
  display as 0.0 MB in system usage reports due to incorrect data reading in the
  backend, confirmed as an API issue related to improper SQL result indexing. The
  fix corrects the query for reading monthly scan statistics, with updates
  scheduled for releases in 2025.10.0 and 2026.1.0.
- (HUB-45873). Resolved a bug where no versions were detected for the
  googleapis/go-genproto component in scanned Docker container binaries; the issue
  stemmed from a bug in signature generation that incorrectly identified the
  parent component alongside the correct subcomponents.
- (HUB-45886). Resolved a problem with Black Duck's data
  retention settings that incorrectly triggered premature unmapping of scans
  following manual .BDIO file uploads. The issue was identified when data
  retention rules activated immediately after uploads, disrupting workflows. The
  fix ensures that data retention policies now consider manual uploads, preventing
  premature unmapping and aligning with expected behavior.
- (HUB-45970). Resolved a bug that allowed the creation of selector-type custom
  fields with zero options, leading to UI crashes on component version custom
  fields pages. The issue was caused by the backend API returning an empty options
  array for these fields, affecting all component versions since version 2019.2.0.
  The fix disallows the creation of selector custom fields without options,
  improving UI stability. A temporary workaround involved disabling or adding
  options to existing custom fields.
- (HUB-45975). Resolved a "Duplicate Key" error on the Issues endpoint caused by
  multiple BOM entries with the same component/version IDs but different names.
  The root cause was identified as KB component name changes not being handled in
  the KBUpdate Job, leading to conflicts in the version_bom_component table.
- (HUB-45977). Resolved a bug where editing a snippet on the Source page resulted
  in the snippet count being incorrectly doubled upon rescanning; this caused the
  system to display 4 matches for the edited snippet instead of the expected 2.
  The issue arose from the system summing file adjustments or counting them twice
  per scan. The fix ensures that snippet matches are accurately counted during
  rescans, maintaining consistent match counts across versions.
- (HUB-45979). Resolved an issue where the
  `vulnerable-bom-components` API endpoint incorrectly
  displayed components that have been removed from layers in a container scan.
- (HUB-46073). Resolved a bug where binary scan results displayed extra components
  in the Source tab, leading to confusion for users. The issue involved two DLL
  files showing an unexpected number of component matches, particularly when
  selecting "All Subfolders" in the Source tab, which incorrectly added extra
  components not linked to the BOM. The fix ensures accurate representation of
  components in the Source tab, aligning with expected results observed in
  standalone binary scans.
- (HUB-46084). Resolved a bug in the /source-trees API endpoint where pagination
  parameters (?limit, offset) stopped working after Black Duck 2025.1.1, disrupting customer workflows. The issue was traced to the UI not
  passing the limit parameter due to a refactor.
- (HUB-46126). Resolved a bug where ignored snippet matches caused license
  conflicts in a main project after scanning a subproject. The issue arose when
  GPL-licensed snippets from external projects were ignored during the subproject
  scan, but their licenses carried over and caused conflicts in the main project
  with a non-GPL proprietary license.
- (HUB-46132). Addressed an intermittent scan failure issue where scans returned a
  "NOT_INCLUDED" status due to the deletion of redundant scans before Detect could
  request BOM status.
- (HUB-46133). Resolved a bug that caused a 400 Bad Request error when cloning
  project versions with over 500 distinct component versions containing
  vulnerability remediations in Black Duck SCA. The issue stemmed
  from a SQL query exceeding column limits, leading to an "index out of range"
  exception.
- (HUB-46139, HUB-46164, HUB-46194). Clarified the documentation to specify the use
  of `scass.blackduck.com` as the SCASS Hostname for proper
  configuration. Added details on SCASS communication security, confirming that no
  changes have been made to the transmitted data, only to internal query
  processing. Expanded the documentation to outline the benefits and disadvantages
  of SCASS, noting that while SCASS scans may appear slower, they significantly
  reduce resource requirements for non-specialized scanning. Additionally,
  referenced Gen05 hardware scaling guidance, highlighting that Gen05 requires
  about 25% less hardware for the same scan volume compared to Gen04, reflecting
  the improvements in SCASS.
- (HUB-46144). Resolved a bug in container scans where components were incorrectly
  shown as both added and removed in the same base layer, leading to discrepancies
  in component listings. The issue was observed when scanning base images
  separately compared to their use in derived images, specifically affecting
  components like the GNU C Library. The fix ensures accurate representation of
  components across scans, eliminating confusion in the results.
- (HUB-46154). Resolved a discrepancy in snippets count displayed between the BOM
  page and the Source View; the mismatch occurred due to the aggregation of
  snippet matches for files with multiple snippets linked to different components.
  The fix ensures that when sorting by component or license, entries for files
  with multiple snippets are split into separate rows, accurately reflecting the
  total snippet count.
- (HUB-46182). Resolved an issue that caused delays in processing changes to
  project version custom fields. The computation for these changes is now handled
  as a background process, significantly improving response times and overall
  efficiency.
- (HUB-46260). Resolved an error where snippet scanning returned "ERR01_1001 Server
  returned an error (Bad Request)" when scanning from folders with spaces in their
  names. This fix ensures that folders such as "Test Scan" can be scanned
  successfully without encountering errors.
- (HUB-46324). Improved efficiency in the KB update workflow by addressing the
  performance issue with the ProjectGroupCacheRepository, which was causing
  slowdowns during scans.
