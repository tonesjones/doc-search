---
title: "Creating a tuning job yaml file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-a-tuning-job-yaml-file.html"
content_id: "30fb93YZXhXEXmpyffxOrA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:16.057469+00:00"
---

# Creating a tuning job yaml file

Create a tuning job yaml file using the appropriate YAML file template:

- Performing a tuning using the `static-tuning-write.yaml` file
  template writes the PostgreSQL settings to the PostgreSQL distribution. See the
  `static-tuning-write.yaml` template in the section that follows: static-tuning-write.yaml - Tuning-write template.
- Performing a tuning using the `static-tuning-suggest.yaml` file
  template returns suggested tuning parameters in the `cim.log` file.
  You can review the suggested parameters, then modify the PostgreSQL parameters as
  needed. See the `static-tuning-suggest.yaml` template in the section
  static-tuning-suggest.yaml - Acquiring database static tuning suggestions.
