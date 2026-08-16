---
title: "Using a Configuration File in a CI/CD Pipeline"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/using-a-configuration-file-in-a-ci/cd-pipeline.html"
content_id: "4ncdnf~eblEZjG153YG3qA"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:13.506377+00:00"
---

# Using a Configuration File in a CI/CD Pipeline

**To use the configuration file in a CI/CD pipeline:**

1. Create a Sigma configuration file named `coverity.yml` (or
   `.sigma-config.yml`).
2. Check in the configuration file into your project's root directory in GitHub or
   GitLab. 

   By default, Sigma will look for a configuration file named `coverity.yml` (or
   `.sigma-config.yml`) in the current working directory
   where the Sigma binary is executed.
