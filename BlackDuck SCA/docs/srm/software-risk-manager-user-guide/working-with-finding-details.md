---
title: "Working with Finding Details"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/working-with-finding-details.html"
content_id: "8Nj9zFSr9wn_Gha3olz64w"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:18.380769+00:00"
content_hash: "f7d47432fa076cc3d1adb33ce75f4f080ebd146d78f28267dce3e1a6be04b057"
---

# Working with Finding Details

The Findings page gives an overview of the findings in a project, focusing on a powerful
filtering system, triage workflow, and issue tracking, with links to drill into more
details via the Findings Details page.

**To access the details for a single finding:**

1. Click the Findings icon in the navigation bar to open the Findings page.
2. Locate the finding in the Findings list and click the link in the "Type" column,
   which is next to the Finding ID.

[image: image]

For more information on each element of the individual finding page, see the
following:

- Branching. Allows you to view details for
  different branches.
- Details Summary. Provides a quick
  overview of the finding and the file where it is located.
- Severity Override. Provides the
  option to override the finding's severity level.
- Train Now Button.
  Provides a link to select training modules.
- Activity Stream. Allows you to change
  the status of the finding.
- Description. Provides a basic description
  of the finding.
- Attachments. Allows attachments to be
  linked to the finding.
- Standard Violations. Provides a
  list of standard violations.
- Training Video. Provides a link to
  select training videos.
- Evidence. Provides the raw data (results) that
  make up a finding.
- HTTP Activity. Shows the available data
  on the HTTP request.
- AI Insight (powered by Polaris Assist).*
  Generate remediation guidance for a SAST issue using a large language model
  (LLM). (The permission `Request and view finding assessments from Polaris
  Assist (Beta)` for the project is required, which is included in the
  default `Reader` role provided by SRM.)
- Source Code. Shows the contents of the
  file where the finding is located.
- Issue Tracker. Allows interaction with
  the configured issue tracker.
- Predicted Status. Provides prediction
  data for the finding based on the associated machine learning
  configuration.
- Fix By Override. Provides the option to either
  override or set a finding's fix-by date.
