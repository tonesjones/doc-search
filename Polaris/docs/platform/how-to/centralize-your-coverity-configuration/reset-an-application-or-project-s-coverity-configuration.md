---
title: "Reset an application or project's Coverity configuration"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/reset-an-application-or-project-s-coverity-configuration.html"
content_id: "clEJ8DPH17tbJHnlxYoEqg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:16.314941+00:00"
content_hash: "78fa3684a65c84262d2210c5045d71218e9c07613541e8d080a6f7aa91a5cad8"
---

# Reset an application or project's Coverity configuration

After you assign a Coverity configuration to an application or project, you can reset it. When you reset an application's configuration, the application inherits your organization's configuration. When you reset a project's configuration, the project inherits its application's configuration (if set), or your organization's configuration.

1. Open the application or project settings:
   - For an application, go to Portfolio > select an application > Settings.
   - For a project, go to Portfolio > select an application > select a project > Settings.
2. Under Coverity Configuration, select Reset.

   A Reset Coverity Configuration notification appears.
3. Select Reset to confirm.

The application or project's Coverity configuration is removed. The next time the application or project is tested, it will use the configuration inherited from the next level up in the hierarchy (for example, an application reverts to the organization-level configuration; a project reverts to the application-level configuration if one exists, otherwise the organization-level configuration).
