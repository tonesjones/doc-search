---
title: "Defining a Freestyle Project for Using Sigma to Report Issues"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/defining-a-freestyle-project-for-using-sigma-to-report-issues.html"
content_id: "menGZ1OEJn_Soxaex7LMVQ"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:19.357622+00:00"
---

# Defining a Freestyle Project for Using Sigma to Report Issues

Follow these steps to define a freestyle project and use Sigma to report
issues:

1. In the main Jenkins dashboard, click New Item and select FreeStyle
   Project.
2. Specify the name of the project.
3. Select Execute Black Duck Rapid Scan Static from the list of build
   steps.
4. Select which Sigma Tool should be used.

   Pick the Sigma tool that is compatible with the operating system of the
   Jenkins agent in use with the build.

   The Sigma tool installs Sigma on
   the Jenkins agent if you opted for automatic installation when Sigma was
   configured as a Jenkins tool.
5. Make sure the Ignore Policies checkbox is checked.
6. To report Sigma issues within Jenkins, select a post-build-action from the
   Add build step drop down.

   For example, Record compiler warnings and static analysis
   results.
7. Select Black Duck Rapid Scan Static
   from the Tool drop down.

When Sigma runs, it produces a file named sigma-results.json by default. The
Sigma tool parses the contents of the file and records the issues to be viewed in
Jenkins.

For more information on how to configure this Post Build Action, see the Warnings Next
Generation plugin documentation: <https://github.com/jenkinsci/warnings-ng-plugin/blob/master/doc/Documentation.md>
