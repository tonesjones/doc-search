---
title: "Converting a project version to LTS"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/converting-a-project-version-to-lts.html"
content_id: "zp9OB_3KTR1SAXnnGY01xg"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:18.830793+00:00"
---

# Converting a project version to LTS

Long-Term Support (LTS) project versions are designed to track new
vulnerabilities for released software artifacts. They are not intended for use
by developers or workflows related to application development or compliance
workflows.

LTS versions omit project and scan data. This includes:

- Source file information
- Scans and all information related to match types
- Snippets
- IaC results, unmatched component data, and malware information
- Comments
- License conflicts, copyrights, and deep license data
- Vulnerability triage information
- BOM custom fields

## Important considerations before converting your project versions to LTS

- Converting from an LTS version back to Active is not currently supported.
- AI models are not retained.
- Custom component vulnerability associations are preserved during LTS
  conversion. If a custom component version is associated with vulnerabilities
  through a valid CPE 2.3 identifier, those vulnerabilities remain available
  in the LTS project version.
- Vulnerability records with multiple remediation origins and different statuses
  will be merged during conversion. The most severe remediation status among the
  merged records will be retained.
- Comments from all merged remediation records will be concatenated into a single
  consolidated comment. This normalization is intentional and ensures consistency
  in the LTS model, which does not support remediation information at the origin
  level.
- This behavior reflects the transition from origin-based remediation tracking to
  the LTS model’s component-version-based approach and applies when converting
  active projects to LTS.

## How to convert a project version to LTS

To convert a project version to LTS status:

- Log in to Black Duck SCA.
- Select the project name using the **Watching** or **My Projects**
  dashboard. The *Project Name* page appears.
- Click [image: Options button] for the desired project version and select **Convert to LTS**.
- Configure the SBOM report that will be generated during the conversion
  process:

  - Select a SBOM
    Template. You can expand the **Template Details** section
    to view the enabled fields which will appear in the SBOM report.
  - Select a SBOM specification and report format.
  - Click **Convert**.

Once the conversion is complete, the project version will be moved from the **Active
Versions** tab of project versions to the **Long-Term Support (LTS) Versions**
tab.
