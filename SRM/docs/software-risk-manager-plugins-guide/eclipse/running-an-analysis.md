---
title: "Running an Analysis"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/running-an-analysis.html"
content_id: "kYHUmolLN8ZY14FY97eSjw"
version: "latest"
section: "Software Risk Manager Plugins Guide"
scraped_at: "2026-09-08T20:05:58.374717+00:00"
content_hash: "e0e231e3f88b10c0ce24d77b98691646a235e84afbc1353681c05ee1858f8efb"
---

# Running an Analysis

If you have the `create`
role
on a Software Risk Manager project, you have the ability to perform Software Risk
Manager analyses on that project from within the Eclipse IDE. Just select the *Run
Analysis* option from the *Code Dx* menu.

  
 [image: image]   

When the dialog is displayed, select the Software Risk Manager project from the dropdown,
the Eclipse projects from the list, and click *Run*.

  
 [image: image]   

An Eclipse job is created and the progress is displayed in the bottom right corner of the
IDE. This will create a zip file containing all local source code from the configured
project and send it to be analyzed by Software Risk Manager. The Findings table will
automatically be updated upon completion of the analysis.
