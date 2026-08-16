---
title: "Version Details report"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/version-details-report.html"
content_id: "e7JvfdzlTAawddhUnXvq2g"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:48.942022+00:00"
---

# Version Details report

Depending on the categories you select, running a project version report creates
these comma-separated files:

- `bom_component_custom_fields_date_time.csv` lists the
  same information as the `components_date_time.csv`
  report, but also includes BOM component, component, and component version
  custom field labels and the values selected for this project version.
- `components_date_time.csv` lists each component in the
  project version, including the respective licensing, usage, match type,
  operation risk information, policy violation information, and review
  status.
- `crypto_date_time.csv` lists the cryptography
  information for each component in the project version, including the
  algorithm ID, algorithm name, key length type, and key length.
- `license_conflicts_date_time.csv` lists the license
  conflicts for this project version.
- `license_term_fulfillment_date_time.csv` lists the
  license terms and fulfillment status for this project version.
- `project_version_custom_fields_date_time.csv` lists the
  project version custom field labels and the values selected for this project
  version.
- `project_version_upgrade_guidance_date_time.csv` lists the
  upgrade guidance information for all components for this project version as well
  as sub-projects.

  As Black Duck caches this data, the information shown in this report may lag
  Black Duck KnowledgeBase up to 24 hours.
- `scans_date_time.csv` lists the mapped scans.
- `security_date_time.csv` lists the security risk
  associated with each component, including the vulnerability ID and
  description, vulnerability scores, and remediation information.
- `source_date_time.csv` lists the individual files and
  dependencies associated with each component, including match type, usage
  information, and policy violation information.
- `version_date_time.csv` lists the name and details of
  the project version, including the release date, phase, method of release,
  and policy violation information.
- `vulnerability_matches_date_time.csv` lists the
  component, vulnerability data, and vulnerability impact analysis data (called function, qualified
  name, and line number) for each component potentially reached by a
  vulnerability.

  This report is empty if there are no components that are potentially
  reachable.

For these project version reports:

- The archive file name is
  <ProjectName-ProjectVersion>_<YYYY-MM-DD>_<HHMMSS>.zip (time stamp
  in system timezone).
- The directory and filename are
  <ProjectName-ProjectVersion>_<YYYY-MM-DD>_<HHMMSS>/<fileName>_<YYYY-MM-DD>_<HHMMSS>.csv
  (same time stamps as archive file name).
- The following characters < > \ / | : * ? + “ in the project or version
  name are replaced with underscores (_).

**To run a project version detail report:**

1. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
2. Select the version of the project for which you want to run the report.
3. Select the **Reports** tab.
4. Click **+ Create New Report** and select **Version Details**.
5. Check or uncheck the **Include Subprojects** checkbox.
6. Select the categories you would like to include in the report:
   - Component
   - Component Additional Fields
   - Cryptography
   - License Conflicts
   - License Terms
   - Project Version Additional Fields
   - Scans
   - Source
   - Upgrade Guidance
   - Version Details
   - Vulnerabilities
   - Vulnerability Matches
7. Click **Create** to run the report.

   A link that includes the project and
   version name appears when the report completes. Any user who is a member of
   the project can access the link.
8. Download the report and extract the zip locally.
