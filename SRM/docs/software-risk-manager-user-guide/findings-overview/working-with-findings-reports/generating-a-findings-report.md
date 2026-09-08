---
title: "Generating a Findings Report"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/generating-a-findings-report.html"
content_id: "lHmovsa7A3THduwcb4UTbQ"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:16.703004+00:00"
content_hash: "a8938bb003ab3fd4b4b84d51300de58ec92d8f52fc579f5b9b7af2d9301a043d"
---

# Generating a Findings Report

Click the Findings icon in the navigation bar and click Generate Report to open the
*Generate Report* dialog. This dialog is used to select the type of report and
allows you to customize the report.

[image: image]

SRM supports the following report types:

- PDF
- Compliance (PDF)
- XML
- CSV
- AlienVault/NBE
- Nessus

Instructions for generating each type of report are given below, according to report
type.

## PDF Report

You can customize the PDF report in several ways. There are options to include or
exclude a simplified or detailed executive summary section; finding details (with or
without source code); tool details; and comments that appear in the Activity Stream
(on the Finding Details page). The "Result details" section contains these options:
"Include result provided details" and "Include HTTP requests and responses."

Note: The "Include result provided details" option *must* be selected if you
want to include the HTTP requests and responses in the PDF report.

[image: image]

If you'd like your company logo to appear on the cover sheet, please contact your
Software Risk Manager administrator to configure it for you.

## Compliance (PDF)

[image: image]

## XML Report

Customizations for the XML report include the option to enumerate standards
violations for each finding, provide source code snippets, and whether to include
copies of the rule descriptions for each finding.

**Note:** There is a limit of eight lines of code per source snippet for each
finding. When the limit is exceeded, no source code is provided.

[image: image]

## CSV Report

The CSV report provides options allowing you to select which columns will be included in the
generated file.

[image: image]

## AlienVault/NBE Report

Software Risk Manager users will be able to select the AlienVault/NBE report. This
reporter generates an NBE report that is compatible with AlienVault.

The report options require that a host address (IPv4) be specified for inclusion in
the report.

[image: image]

## Nessus Report

Software Risk Manager users will be able to select the Nessus report. This reporter
generates a report in the *Nessus* format, which can be imported by many
applications.

The default host and MAC address fields are required, while the operating system and
NetBIOS name fields are optional. When exporting a finding that doesn't contain any
request data, the default host value will be used.

[image: image]
