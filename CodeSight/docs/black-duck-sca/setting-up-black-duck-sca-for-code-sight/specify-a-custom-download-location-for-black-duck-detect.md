---
title: "Specify a custom download location for Black Duck Detect"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/specify-a-custom-download-location-for-black-duck-detect.html"
content_id: "Qe8_LrjchYrhSZ4GzxR3rw"
version: "2026.9.0"
section: "Black Duck SCA with Code Sight"
scraped_at: "2026-10-06T23:39:54.332401+00:00"
---

# Specify a custom download location for Black Duck Detect

You can change the URL (URI) from which Code Sight downloads Detect, the engine that runs SCA scans and communicates with the Black Duck server.

**Version requirements:**

Please see the “Black Duck Products and Servers” table on the Code Sight Support Matrix page.

**Requirements for the Detect URL and server installation:**

- The URL must use the HTTP or HTTPS protocol.
- Detect should be hosted on the server as a ZIP file, with the same file name it has on the [Artifactory](https://repo.blackduck.com/artifactory/bds-integrations-release/com/blackduck/integration/detect/) page.

  Attention: Use the air-gap version that includes NuGet; for example, detect-<version>-air-gap-no-docker.zip.
- The server where you post the zipped Detect application must not require authentication to retrieve the file.

**Steps to change the URL:**

1. Log in to your Black Duck page.
2. [image: image]  In the sidebar, click the Admin icon.
3. On the Administration page, navigate to System Settings → Black Duck®
   Detect.
4. In the Hosting Location field, enter your host URL.
5. Click the Save button to the right. 

   From now on, downloads of Detect, including those launched by Code Sight, will obtain the Detect ZIP file from this new location.
