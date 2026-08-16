---
title: "Reset an application or project's SAST tool version"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/reset-an-application-or-project-s-sast-tool-version.html"
content_id: "XQ2t8MxeGQ_8gRQy5j7WoA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:15.327944+00:00"
content_hash: "5b2f0a7bb986cd8d4879f6f6bc06c5f64656f1318cfca80803781f8edad90718"
---

# Reset an application or project's SAST tool version

After you change an application or project's Coverity version, you can select Reset (at the top of the SAST Analysis panel) to remove the change. To do so, follow these steps:

1. Open the application or project's settings:
   - For an application, go to Portfolio > select an application > Settings > Analysis.
   - For a project, go to Portfolio > select an application > select a project > Settings > Analysis.
2. Select Reset (at the top of the SAST Analysis panel).

   A Reset Settings: SAST Analysis confirmation appears.
3. Select Confirm.

When you reset an application's tool version, the application will inherit your organization-level tool version. When you reset a project's tool version, the project will inherit application (if set) or organization-level tool version.
