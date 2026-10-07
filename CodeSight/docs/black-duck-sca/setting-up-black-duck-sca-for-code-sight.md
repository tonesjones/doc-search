---
title: "Setting Up Black Duck SCA for Code Sight"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/setting-up-black-duck-sca-for-code-sight.html"
content_id: "Y9B7668P4~xQljnygNKjeg"
version: "2026.9.0"
section: "Black Duck SCA with Code Sight"
scraped_at: "2026-10-06T23:39:54.221003+00:00"
---

# Setting Up Black Duck SCA for Code Sight

## Setup considerations

- Code Sight runs the Detect scan engine to
  perform Black Duck®
  SCA scans. Your system must meet Detect's requirements. See [General Requirements](https://documentation.blackduck.com/bundle/detect/page/gettingstarted/requirements.html)
- Code Sight downloads the scan engine from the [Black Duck public repo](https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/detect/).
  However, it can also be hosted on-premises. See ‘Specify an internally hosted
  location’ below for details.

## Specify an internally hosted location

You can configure a custom URL from which Code Sight downloads Detect.

**Version requirements:**

We recommend that you verify compatibility between the current Black Duck®
SCA version and the selected Detect version. [Learn more about Detect version
compatibility](https://documentation.blackduck.com/bundle/blackduck-compatibility/page/topics/Black-Duck-Release-Compatibility.html)

**Requirements for the Detect URL and server installation:**

- The internally hosted Detect location must use HTTP or HTTPS protocol
- Detect should be hosted on the server as a ZIP file, with the
  same file name it has on the [Black Duck public repo](https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/detect/)

  - Use the packaging with name detect-<version>-air-gap-no-docker.zip
- The server where you post the zipped Detect application must not
  require authentication to retrieve the file
- The location should be accessible by Code Sight

## Steps to set the internally hosted Detect location

- Log in to Black Duck®
  SCA
- Navigate to Admin → System Settings → Black Duck
  Detect
- Select **Internally Hosted**
- Set the location in **Hosting Location for Black Duck
  Detect**

See also: Black Duck SCA setup considerations.
