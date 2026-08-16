---
title: "Generating Support Bundles"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/generating-support-bundles.html"
content_id: "IjbqHAC6kEPcyiCUhrfJwQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:58.582375+00:00"
---

# Generating Support Bundles

When you encounter discrepancies in component identification, licensing, or vulnerability
data in your project's Bill of Materials (BOM), you can generate a **KnowledgeBase (KB)
support bundle** directly from Black Duck SCA. The support
bundle automatically collects all the relevant component data that the Black Duck SCA support team needs to investigate your issue, reducing
the back-and-forth typically required when opening a support case.

The support bundle is downloaded as a `.zip` file that you can attach to a
new support case.

## Prerequisites

- You must have **BOM edit** permissions for the project version.
- To include BDIO files in the bundle, you must also have permission to **view
  and download BDIO files** for the project version. If you do not have
  this permission, you can still generate a bundle, but BDIO files will not be
  included.

## Generating a support bundle

You can generate a support bundle from the **BOM** page.

1. Navigate to the **BOM** or **Match Review** page for the project
   version that contains the component(s) you want to report.
2. Select one or more components that you want to include in the bundle.
3. From [image: image] for an individual component or the **Bulk
   Actions** menu if multiple components are selected, select **Generate
   Support Bundle**.
4. In the support bundle dialog, provide the following information:

   **Issue type** — Select the type of issue you are reporting. You can
   choose one of the following:

   | Issue Type | Description |
   | --- | --- |
   | **Component Mismatch** | The component identified by Black Duck SCA does not match the actual component in your code. If selected, you can provide a URL or link to the expected source (for example, a Maven repository link). |
   | **Component Version Mismatch** | The component is identified correctly, but the version is wrong. |
   | **License Incorrect** | The declared license for the component is wrong. |
   | **License Unknown** | The license for the component could not be determined and is listed as unknown. |
   | **Vulnerability False Negative** | A known vulnerability that should apply to this component is not reported. |
   | **Vulnerability False Positive** | A vulnerability is reported against this component but should not apply. |
   | **Other** | Any other KB data issue not covered above. Use the comments field to describe the problem. |

   **Details** — (Optional) Enter additional details or context about the
   issue. Maximum 10,000 characters.

   **Include BDIO files** — This checkbox is enabled by default. When
   selected, all BDIO files associated with the selected component(s) are
   automatically included in the bundle. Clear this checkbox if you do not want
   to include BDIO files. This option is only available if you have BDIO
   download permissions for the project version.
5. Click **Generate Support Bundle**.

   The bundle is generated and downloaded automatically to your browser's
   default download location.

## What's in the support bundle

The support bundle is a single `.zip` file named
`support_bundle_<timestamp>.zip` containing:

- **support_bundle_<timestamp>.json** — A structured JSON file that
  includes:

  - Project name and version
  - The issue type you selected
  - Your comments
  - For each component included in the bundle:

    - Component name, version, and UUID
    - Declared and concluded licenses
    - Match type and match confidence data
    - Origin and package URL information
    - Vulnerability data (if applicable)
    - Upgrade guidance
- **BDIO files** — (If included) All BDIO files associated with the selected
  components. These files contain the dependency data from your scans and help
  the support team reproduce and investigate the issue.

## Limits

| Limit | Value |
| --- | --- |
| Maximum components per bundle | 20 |
| Maximum comment length | 10,000 characters |

If you exceed the component limit, the error message displays the number of
components you selected so you know how many to remove. Similarly, if your comment
exceeds the character limit, the message indicates the current character count.

## Audit logging

Each time a support bundle is generated, an entry is recorded in the **project
version audit log** indicating:

- That a support bundle was generated
- Whether BDIO files were included

## Opening a support case

After downloading the support bundle:

1. Open a new support case through your normal support channel.
2. Attach the downloaded `.zip` file to the case.
3. The structured data in the bundle will help the support team investigate your
   issue more efficiently, reducing the need for follow-up requests for
   additional information.

## Notes

- The support bundle is a one-time download. It is not stored or archived
  within Black Duck SCA.
- There is no public API for generating support bundles. This feature is
  available through the user interface only.
- If your BOM was populated by certain package manager scans, automated KB
  processes may already be working to resolve some types of discrepancies.
  The support bundle dialog may display a note about this where
  applicable.
