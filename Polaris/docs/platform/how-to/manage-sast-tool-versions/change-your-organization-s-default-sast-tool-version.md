---
title: "Change your organization's default SAST tool version"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/change-your-organization-s-default-sast-tool-version.html"
content_id: "6eY9ZrhMT6gr72IZq9ms9Q"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:12.817982+00:00"
content_hash: "b5777fb1316b1716b37e5bbed588319fb3ea5581eddfbc1745e445705ed7a7a0"
---

# Change your organization's default SAST tool version

The version of Coverity used for static analysis can be modified at the organization, application, project, and branch level. To change your organization's default Coverity version, follow these steps:

Note: Only Organization Administrators can complete these steps.

1. Go to My Organization > Analysis.
2. Under SAST Analysis, select Edit.
3. Select the appropriate Coverity version, as required.
   - To use the latest supported version of Coverity, select Automatically use latest version (recommended).

     Selecting this option ensures that the most recent supported version of Coverity is used by default. When a new version of Coverity is available, it becomes the default automatically.
   - To use a specific version of Coverity, select Use a specific tool version, and select the appropriate version from the dropdown.

     Important: Here, you can select the latest supported version of Coverity, or a deprecated one. When you choose a specific version of Coverity, the version will not change when a new version of Coverity is added to Polaris, even if support for the version you selected is removed. When support for a version of Coverity ends, SAST tests that attempt to use the unsupported version will not run. To resume testing, you must activate a supported version of Coverity.

     When you choose to use a specific Coverity version (including the recommended version), the corresponding version of Rapid Scan Static (Sigma) is locked, and won't change when newer Sigma versions are available.
4. Select Save.

Important: After you change your organization's default Coverity version, a full SAST test must be performed on at least one branch in affected projects before rapid SAST tests can run.
