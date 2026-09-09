---
title: "Working with Components"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/working-with-components.html"
content_id: "zRzHWTDczWvHZCBQVXB33g"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:15.199062+00:00"
content_hash: "c371074eb3fc4b53bec6832624739013af32bfdc9cd5b11af2027db2f04492ee"
---

# Working with Components

Software Risk Manager provides a comprehensive list of a project's components that can be
accessed through the Findings page.

Open a project's Findings page, then select the Components tab to display a list of that
project's components.

[image: image]

The component view shows all of the components that are part of the project, regardless
of the status of any individual finding. (Use the filters to the left of the list to
search; click the column headings to sort.)

The Component page provides the following information:

- Component Name
- Version
- Match Type (direct or transitive dependency)
- License Name
- License Family

Click the component name to open the Component Details and Security Details view for that
specific component.

Select the Component Details tab to view detailed information about the component.

[image: image]

The Component Details tab provides the following information:

- Security Risk
- Component Name
- Component Description
- Component Links
- Component Origins
- Upgrade Guidance

Select the Security Details tab to view additional security information about the
component.

[image: image]

The Security Details tab provides the following information:

- Security Risk
- Component Name
- Finding ID
- Vulnerability ID
- Vulnerability Score
- Status

Note: If the project is configured with a component correlation mode that doesn't include
vulnerability, then the Vulnerability ID and Vulnerability Score columns won't appear in
the table. (For more information, see Analysis
Configuration Options.)
