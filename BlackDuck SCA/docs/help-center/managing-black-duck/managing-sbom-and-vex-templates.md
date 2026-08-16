---
title: "Managing SBOM and VEX Templates"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/managing-sbom-and-vex-templates.html"
content_id: "_pqFdvrTK1PymUy2CZIsWA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:20.048276+00:00"
---

# Managing SBOM and VEX Templates

Use SBOM and VEX templates to control the scope of data included in your exported SBOM and VEX documents. Templates let you
define reusable configurations so that reports are generated consistently across your
organization.

To access templates, go to **Manage > SBOM and VEX Templates**.

Note: The VEX Templates tab is only visible when the VEX module is enabled in
your license.

## Navigating the SBOM and VEX Templates page

The SBOM and VEX Templates page is organized into two tabs:

- **SBOM** — Create and manage
  templates that control the scope of data included in SBOM exports
  (CycloneDX, SPDX).
- **VEX** — Create and manage templates that
  control the scope of data included in CSAF 2.0 (VEX) exports.

Click the appropriate tab to access the template type you want to work with.

Note: The VEX Templates tab is only visible when the VEX module is enabled
in your license. If you do not see the VEX Templates tab, contact your Black
Duck administrator to verify your license includes the VEX module.

## SBOM templates

From this page, you can see all SBOM templates that exist in your environment. By
default, the following SBOM template has been created by the system:

- **NTIA Minimum**: Template containing [NTIA Minimum required fields](https://www.ntia.doc.gov/files/ntia/publications/sbom_minimum_elements_report.pdf). This
  template can be enabled or disabled, and cannot be deleted.

For more information on the SBOM templates displayed, click the [image: View details button] on the top right corner of any template box.

Users with the Custom Fields Administrator role can perform the following actions:

- Create, edit, or delete SBOM
  templates
- Set a template
  as active or inactive
- Set a SBOM template as
  default

## VEX templates

VEX templates control which data elements are included when you generate a CSAF 2.0
(VEX) report. You can create multiple templates to serve different audiences or
compliance requirements.

Black Duck SCA includes a pre-configured **System** template with the following
defaults:

| Field | Default value |
| --- | --- |
| Legal Disclaimer | Disabled |
| TLP Designation | Disabled |
| Subproject Vulnerabilities | Disabled |
| Comments | Disabled |
| CVE | Enabled |
| EUVD | Enabled |
| BDSA | Enabled |

The System template:

- Is the default template until you designate a different one
- Cannot be edited, deactivated, or deleted

Users with the Custom Fields Administrator role can perform the following actions:

- Create, edit, or delete VEX
  templates
- Set a
  template as active or inactive
- Set a VEX template
  as default
