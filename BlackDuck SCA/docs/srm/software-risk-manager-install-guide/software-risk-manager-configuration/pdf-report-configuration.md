---
title: "PDF Report Configuration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/pdf-report-configuration.html"
content_id: "4KVwx4_s1RDnbgpmGQDjmQ"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:30.488291+00:00"
content_hash: "f293a6f1a1bcf0c638bfa38dc970a163914a35c0b49fc613d3b0ee5bf03d2b4c"
---

# PDF Report Configuration

## Company Logo

Your company logo can be displayed on the cover of PDF reports. For best results, the
image should be at least 432 pixels wide or 144 pixels tall. Set the
`report.pdf.custom-logo` property to the filename of the logo.
The file can be located in the same folder as the `codedx.props` file
or, if the file is located elsewhere, specify the path with the filename. The
default is no company logo.

## Limits

There are limitations in place on the PDF report. Depending on the hardware
configuration of the machine running Software Risk Manager, you may be able to
increase these limits. Be aware that raising these limits will increase memory
requirements.

The limits may be changed by adjusting the following options:

- `report.pdf.dast-body-limit` [default: 8192] - sets the limit,
  in bytes, of DAST bodies to be displayed in the PDF report.
- `report.pdf.details-simple-limit` [default: 50000] - sets the
  number of findings to restrict simple details to in the PDF report.
- `report.pdf.details-source-limit` [default: 5000] - sets the
  number of findings to restrict source code display to in the PDF
  report.
- `report.pdf.dast-finding-limit` [default: 1000] - sets the
  number of findings to allow DAST request/response bodies to be displayed for
  in the PDF report.
- `report.pdf.host-finding-limit` [default: 10000] - sets the
  number of findings to allow host information to be displayed for
  in the PDF report.

## Extended Customization

There are options allowing for extended customization. These customizations may be
made by adjusting the following options:

- `report.pdf.show-code-dx-logo` [default: true] - controls
  whether the Software Risk Manager logo will be included on the
  cover.
- `report.pdf.pdf-title` [default: "{{report.title}}:
  {{project.name}}"] - sets the title of generated PDF reports; see the Report Configuration
  Templates section for details on valid values.
- `report.pdf.cover-page-title` [default: "{{report.title}}"] -
  sets the title shown on the cover page of generated PDF reports; see the
  Report Configuration
  Templates section for details on valid values.
- `report.pdf.page-header` [default: "{{project.name}} -
  Software Risk Manager {{report.title}}"] - sets the header displayed at the
  top of all PDF report pages; see the Report Configuration Templates section for
  details on valid values.
- `report.pdf.disable-page-header` [default: false] - if true,
  the page header will be suppressed on all pages.
- `report.pdf.disable-page-footer` [default: false] - if true,
  the page footer will be suppressed on all pages.
- `report.pdf.japanese-mode` [default: false] - if true,
  Japanese fonts will be used as the primary font for all text in PDF reports.
  if false, Japanese fonts will only be used to render Japanese
  characters.
