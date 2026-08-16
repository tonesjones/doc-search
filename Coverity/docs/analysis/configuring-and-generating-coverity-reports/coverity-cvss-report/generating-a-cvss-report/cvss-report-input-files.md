---
title: "CVSS report input files"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cvss-report-input-files.html"
content_id: "zakaI621gW9xHmmR3_pQmg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:20.666878+00:00"
---

# CVSS report input files

The CVSS Report input files use input data from the following files to update the CVSS
metrics and generate the PDF report:

- config/config.yaml

  This template file should be created or updated by the user via command line.
  Changes to the file name and content are allowed.
- <security-profile-file>.json

  A JSON file that is created by the security team (and not the user). Its
  structure is similar to the
  Master_CWE_CVSS_Base_Score_Mapping-v1.json file.
  Comments are allowed.
- config/Master_CWE_CVSS_Base_Score_Mapping-v1.json

  The master JSON file which contains default mappings between CWE and CVSS
  metrics. This file must remain in the config/ folder and
  should not be removed.
