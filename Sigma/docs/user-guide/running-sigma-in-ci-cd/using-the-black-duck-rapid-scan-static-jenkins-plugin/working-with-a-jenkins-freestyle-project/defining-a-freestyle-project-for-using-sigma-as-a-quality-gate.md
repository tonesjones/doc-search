---
title: "Defining a Freestyle Project for Using Sigma as a Quality Gate"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/defining-a-freestyle-project-for-using-sigma-as-a-quality-gate.html"
content_id: "l8diHpSt_mEs7Q9RsU12nQ"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:18.711246+00:00"
---

# Defining a Freestyle Project for Using Sigma as a Quality Gate

Follow these steps to define a freestyle project and use Sigma as a quality
gate:

1. In the main Jenkins dashboard, click New Item and select FreeStyle
   Project.
2. Specify the name of the project.
3. Select Execute Black Duck Rapid Scan Static from the list of build
   steps.
4. Select which Sigma Tool should be used.

   Pick the Sigma tool that is compatible with the operating system of the
   Jenkins agent in use with the build.

   The Sigma tool installs Sigma on the Jenkins agent if you opted for automatic
   installation when Sigma was configured as a Jenkins tool.
5. Uncheck the Ignore Policies checkbox.

   If a .sigma-policy.yml file is present in the Jenkins workspace, that policy
   file is used by default. Otherwise, you can submit a
   .sigma-policy.yml file to define policies for a
   quality gate into your source code repository .

   If you would like to use a policy file other than
   .sigma-policy.yml, please see Setting Sigma Policy Files.
