---
title: "Viewing Sigma Issues Reports"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/viewing-sigma-issues-reports.html"
content_id: "6VlaE7lZ6TtRA720zEOV9g"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:26.044179+00:00"
---

# Viewing Sigma Issues Reports

If you are reporting issues through Jenkins, rather than using Sigma as a quality gate,
use the following process to view issues.

When the Warnings Next Generation plugin has recorded the issues Sigma has identified,
they are viewable in the Jenkins build.

Note: This section highlights how to view the issues, but the full functionality of the
Warnings Next Generation plugin is not covered here. For more information please see
<https://github.com/jenkinsci/warnings-ng-plugin/blob/master/doc/Documentation.md>.

1. When a build completes and has Sigma issues recorded you will see Black Duck
   Rapid Scan Static Warnings in the Jenkins action pane of the build.
2. Click Black Duck Rapid Scan Static Warnings.

   A report is shown in Jenkins showing the issues Sigma has identified. You can then see the details of the
   issues and navigate to the source code where the issue occurs.

   [image: image]
