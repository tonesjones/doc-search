---
title: "Code Sight version 2025.2.0"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2025.2.0.html"
content_id: "lF9KJd90Xtad8INc88_gUA"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:58.446384+00:00"
---

# Code Sight version 2025.2.0

This release switches from support for the older Synopsys Detect to support for Black Duck®
Detect.
See the “Enhancements” section on this page.

## Enhancements

- Code Sight is ending support for downloading or installing Synopsys Detect.
  (Detect is the executable that powers both Black Duck SCA and Rapid Scan SCA.)
  That includes versions of Detect older than 10.0.
  Beginning with Code Sight version 2025.2.0, Code Sight will download and install
  Black Duck®
  Detect, which starts with version 10.0.

  If Synopsys Detect was already installed on your system, Code Sight will continue using that.
  However, Detect updates will now come from
  <https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/detect/>.

  If you wish to install Detect to a custom location, see
  Setting Up Black Duck SCA for Code Sight.
- In the Code Sight help, The QuickStart for the Code Sight Standard Edition has been updated to correct
  some out-of-date text.
- Portions of the Polaris with Code Sight section have also been updated to improve
  clarity and correctness.
- Customers who use an IP safelist should add repo.blackduck.com (34.149.5.115) to this list.

  The sig-repo.synopsys.com site at its old IP (34.110.245.127) will continue to be available through February 2025.
- Code Sight Standard Edition customers who use an IP safelist should add codesight.blackduck.com (34.8.121.57) to this list.

  The codesight.synopsys.com site at its old IP (34.95.116.38) will continue to be available through March 2025.

## See also

Code Sight Support Matrix

Code Sight Known Issues
