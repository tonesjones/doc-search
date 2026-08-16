---
title: "Creating a report that uses a custom standard based on a MISRA category"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-a-report-that-uses-a-custom-standard-based-on-a-misra-category.html"
content_id: "72m~qrdHOX6Dd9SsAO9HDA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:51.476937+00:00"
---

# Creating a report that uses a custom standard based on a MISRA category

The MISRA Report Generator must be installed.

1. In Configuration > Standards, choose the MISRA template to use, and then click Download
   Template.
2. Edit the downloaded template file by replacing its name with your own desired name
   (for example, `my standard`), and then replacing the values with your
   desired values.

   Important: The values you add must be valid MISRA
   Categories.
3. Use a text editor to open Coverity Reports/config/config.yaml.
4. In config.yaml, fill in the mandatory fields:
   - For the `url` (or `host`) field, replace the
     default string with the URL of the Coverity Connect server that you use.
   - For the `project` field, specify the project for which you
     specified custom values.
   - Add the following field (using the name you actually specified):

     ```
     misra-report:
         support_custom_standards: true
         supported_custom_standard_name: "my standard"
     ```
   - Save config.yaml.
   - Go to the Coverity Reports/bin/ directory, and then run
     the following command:

     ```
     $ ./cov-generate-misra-report.exe ../config/config.yaml --password console
     ```

     When
     prompted, enter your password.

     The MISRA Report Generator creates
     your custom report.
