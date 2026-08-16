---
title: "Working with the Coverity CVSS report generator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/working-with-the-coverity-cvss-report-generator.html"
content_id: "gy4_iu37kq96XyPjV5qCJQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:17.801384+00:00"
---

# Working with the Coverity CVSS report generator

This section describes the different user workflows for getting started with Coverity
CVSS Report Generator.

**Security Team:**

1. Follow the instructions in Installing the report generator to install
   the cov-generate-cvss-report tool.
2. Create the following CVSS attributes: CVSS_Audited,
   CVSS_Score, CVSS_Severity, and
   CVSS_Vector.
3. Create the <security-profile-file>.json file for your users. This file
   overrides the
   config/Master_CWE_CVSS_BASE_SCORE_PROFILE_V1.json
   file.

   Note: The <security-profile-file>.json file path must be specified in
   the config/config.yaml file.
4. Use the --scores option to update the CVSS attributes. For
   example:

   ```
   /bin/cov-generate-cvss-report \
         --password <spec> \
         --project <project-name> \
         --profile <security-profile-file> \
         --scores \
         config/config.yaml
   ```
5. Verify that the `<CVSS_Vector>` value for each defect is
   correct.
6. Once you have verified that the `<CVSS_Vector>` value is
   correct, set the `<CVSS_Audited>` field to
   `<Yes>`.
7. **Optional:** If a change needs to be made, update
   <security-profile-file>.json and run the tool
   with the --scores option again.

**Development Team:**

1. Follow the instructions in Installing the report generator to install
   the cov-generate-cvss-report tool.
2. Create the following CVSS attributes: CVSS_Audited,
   CVSS_Score, CVSS_Severity, and
   CVSS_Vector.
3. In Coverity Connect, create a project with snapshots.
4. Use the <security-profile-file>.json file for your CWE-CVSS vector
   mappings. The <security-profile-file>.json file is
   created by the security team.
5. **Optional**: If the <security-profile-file>.json file has not been
   created for you, then use the default
   config/Master_CWE_CVSS_Base_Score_Mapping-v1.json
   file.
6. Update the config/config.yaml file to reflect the users'
   settings.
7. Use the --scores option to update the CVSS attributes. For
   example:

   ```
   /bin/cov-generate-cvss-report \
       --password <spec>  \
       --project <project-name> \
       --profile <security-profile-file> 
       --scores \
       config/config.yaml
   ```
8. Once all the updates are made, use the --report option to generate the CVSS
   Report. For example:

   ```
   /bin/cov-generate-cvss-report \
       --output <output-file> \
       --password <spec> \
       --project <project-name> \
       --report \
       config/config.yaml
   ```
