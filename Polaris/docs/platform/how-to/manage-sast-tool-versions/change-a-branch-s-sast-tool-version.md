---
title: "Change a branch's SAST tool version"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/change-a-branch-s-sast-tool-version.html"
content_id: "3l0KRma_wPq4lg32BrQhlg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:14.700188+00:00"
content_hash: "0f0859db6e8b02de89ee3e423851e6193b4cfb6457b66a5528fdfece72f7a5d2"
---

# Change a branch's SAST tool version

The version of Coverity used for static analysis can be modified at the organization, application, project, and branch level. To change a branch's Coverity version, follow these steps:

Note: Only Organization Administrators, Organization Application Managers, Application Administrators, Application Contributors, and other users with permissions to manage branch settings can complete these steps.

1. Go to Portfolio, open an application, and open a project.
2. Go to Branches.
3. Select the options [image: icon polaris options] icon at the end of the branch's row and select Edit.

   The Edit Branch window opens.
4. Under SAST Analysis, select the appropriate Coverity version, as required.
   - To use the latest supported version of Coverity, select Automatically use latest version (recommended).

     Selecting this option ensures that the branch always uses the most recent supported version of Coverity. When a new version of Coverity is available, the branch will automatically use it for SAST tests.
   - To use a specific version of Coverity, select Use a specific tool version, and select the appropriate version from the dropdown.

     Important: Here, you can select the latest supported version of Coverity, or a deprecated one. When you choose a specific version of Coverity, the version assigned to the branch will not change when a new version of Coverity is added to Polaris, even if support for the version you selected is removed. When support for a version of Coverity ends, SAST tests that attempt to use the unsupported version will not run. To resume testing, you must activate a supported version of Coverity.

     When you choose to use a specific Coverity version (including the recommended version), the corresponding version of Rapid Scan Static (Sigma) is locked, and won't change when newer Sigma versions are available.
5. Select Save.

Important: After you change a branch's Coverity version, a full SAST test must be performed on the branch before rapid SAST tests can run.
