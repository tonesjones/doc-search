---
title: "Viewing LTS project versions"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/viewing-lts-project-versions.html"
content_id: "UrVxTDLIOBzVHBnaMTpqcg"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:19.688621+00:00"
---

# Viewing LTS project versions

To view the list of LTS project versions:

- Log in to Black Duck SCA.
- Select the project name using the **Watching** or **My Projects**
  dashboard. The *Project Name* page appears.
- Click the **Long-Term Support (LTS) Versions** tab.

  [image: Long-Term Support (LTS) Versions page]

## What can I do on the Long-Term Support (LTS) Versions tab?

From the **Long-Term Support (LTS) Versions** tab, you can:

- Filter the table to help find desired versions. You can filter by:

  - Distribution
  - License
  - License Risk
  - Operational Risk
  - Release Phase
  - Security Risk
- View specific LTS project versions BOMs. Click the desired project version in
  the table brings you to its **Components** tab to view its BOM.
- Delete a LTS project version. Click [image: Options button] and select **Delete**.

## Viewing a LTS project version BOM

[image: LTS Components tab]

When you click an LTS project version from the list, you'll be taken directly to the
Components tab for that version, where you can review the associated bill of
materials (BOM):

- Component. The component's name and version.
- License. The component's license.
- Vulnerabilities. Displays a count of the component's known vulnerabilities
  (Critical, High, Medium, Low). This section also displays upgrade recommendations to mitigate risk.
- SBOM
  Fields. The SBOM values for the component's PURL, CPE,
  Originator, Supplier, License Comment, Package Valid Until Date, and
  Download Location.

## Vulnerabilities tab

[image: LTS Vulnerability tab]

The Vulnerabilities tab provides a centralized view of all known vulnerabilities
assocated with the selected LTS project version. This view is designed to help users
quickly assess vulnerability exposure, prioritize remediation efforts, and filter
relevant information.

The tab includes the following:

- **Risk profile bar**: A visual summary showing the total number of
  vulnerabilities, broken down by severity: Critical, High, Medium, and
  Low.
- **Filter and Search options**: Allows the user to narrow the list of
  vulnerabilities by specific criteria or search for particular vulnerability
  IDs or keywords.
- **Vulnerability table**: Displays detailed information for each
  vulnerability, including:

  - Vulnerability ID: The unique identifier assigned to the
    vulnerability. This may be a CVE or a BDSA ID.
  - Affected Components: The component(s) within the project version that
    are impacted by the vulnerability.
  - Overall Score: The highest severity score for the vulnerability
    across supported scoring systems (e.g., CVSS 3.1, CVSS 4.0, BDSA).
    Used to prioritize risk.
  - Status: Indicates the current remediation status of the
    vulnerability.
  - Exploit: A checkmark appears if there is known exploit code publicly
    available for this vulnerability.
  - Workaround: A checkmark appears if there is a known workaround
    available that may mitigate the vulnerability without an official
    fix.
  - Solution: A checkmark appears if a documented solution or patch is
    available to address the vulnerability.

  Note: The Exploit, Workaround, and Solution columns display a checkmark only
  when applicable information is available to address the
  vulnerability.

In addition to viewing vulnerability details, you can set the remediation status for
each vulnerability. This status helps track whether a vulnerability has been
addressed or remains unresolved.

To set the status of a vulnerability:

1. Select the desired vulnerability or vulnerabilities by:

   - Checking the checkbox next to the desired vulnerability and then
     clicking [image: Remediate button] . You can select multiple vulnerabilities to remediate using
     this method.
   - Expanding the vulnerability by clicking the [image: Expand icon] and either:

     - Check the checkbox next to the desired vulnerability and then
       click [image: Remediate button] .
     - Hover your mouse cursor over the **Component** or
       **Status** areas and then click the [image: Wrench icon] .

   This opens the **Remediate Vulnerability** modal. Clicking the [image: Expand icon] displays the selected vulnerability and the affected component
   version.

   [image: Remediate Vulnerability modal]
2. Choose a status from the **Status** drop down menu. Click here for more information on
   remediation statuses.
3. Select a **Target Date** or **Actual Date** if updating the
   vulnerability remediation. Click here for more information on these two fields.
4. Add any comments in the **Comments** field.
5. Click **Update**.

Note: Remediation is applied at the component version level. If a component version has
multiple origins, all origins will be remediated simultaneously. It is not possible
to remediate individual origins separately.

## Reports tab

The Reports tab contains the SBOM report created when the project version was
converted to LTS.

## Details tab

The Details tab contains the same
information as displayed when the project was Active.

## Settings tab

You can delete the project version from the Settings tab. Once you delete a version,
you can't restore it and you will lose all information related to it.
