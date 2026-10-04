---
title: "Reset a branch's Coverity configuration"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/reset-a-branch-s-coverity-configuration.html"
content_id: "7rylFqEhOOXEgs71EvRoWw"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:16.328195+00:00"
content_hash: "bbb5ba8aa4cf05d8416f16d6abfad7563450954e4a5cb1aba93d65b83fe94967"
---

# Reset a branch's Coverity configuration

After you assign a Coverity configuration to a branch, you can reset it. When you reset a branch's configuration, the branch inherits its project's configuration (if set), its application's configuration (if set), or your organization's configuration.

1. Go to Portfolio, open an application, and open a project.
2. Go to Branches and select the branch you want to modify.
3. Under Coverity Configuration, select Reset.

   A Reset Coverity Configuration notification appears.
4. Select Reset to confirm.
5. Select Save.

The branch's Coverity configuration is removed. The next time the branch is tested, it will use the configuration inherited from the project, application, or organization.
