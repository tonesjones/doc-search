---
title: "Important recommendations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/important-recommendations.html"
content_id: "EdI4~a83Oz_mq7RQVsQZKA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:02.596376+00:00"
---

# Important recommendations

Note: If Coverity Connect is deployed in the cloud, this section does not apply.

After installing Coverity Connect, keep in mind these important recommendations:

- Do not move Coverity Connect from its installation location.
- Do not rename the Coverity Connect installation location.
- Do not start Coverity Connect from a different machine.
- Do not start Coverity Connect with a user other than the user who installed it.
- Do not use version numbers in the name of your installation directory. While using
  version numbers is permitted, it could cause problems when you upgrade to a new
  version. When you upgrade, the installation directory name is unmodified.

If you have to make these types of configuration changes, you should create a new
installation, backup your old system, and restore the backup into the new installation
instance. See Upgrading Coverity Connect.
