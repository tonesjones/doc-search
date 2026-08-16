---
title: "About Linux distributions in Black Duck"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-linux-distributions-in-black-duck.html"
content_id: "O9yHvpQJhNADCDnAUAgIDg"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:15:02.846480+00:00"
---

# About Linux distributions in Black Duck

Linux distributions combine the Linux kernel with other software, mostly open source
software, to create a complete package. Black Duck reports
on the vulnerabilities associated with the OSS components in these packages. However,
this may lead to false positives as Linux distribution packages can be patched and these
patches are not tracked by NVD.

Black Duck displays these vulnerabilities with a remediation
status of "Needs Review", "Patched", or "New" (if Black Duck
has verified that the vulnerability affects that version of the OSS component).

If you determine that the version of your package has been patched, you can change the
remediation status to "Patched." A remediation status of "Patched" removes the CVE from
the security risk calculation.

## Viewing Linux distributions in Black Duck

Black Duck shows the origin and origin ID:

- In the **Component** column when viewing details for a component on the
  Project Version page/**Components** tab
- In the list of components shown in the Project Version page/**Security**
  tab
- In the **Component** column when viewing details in the Project Version
  page/**Source** tab.

You can add or edit the
origin and origin ID shown for a component.
