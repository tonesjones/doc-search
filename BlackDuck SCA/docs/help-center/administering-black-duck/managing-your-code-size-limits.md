---
title: "Managing your code size limits"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/managing-your-code-size-limits.html"
content_id: "GG3xPW7E0aEBf0vEytuZOA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:23.249955+00:00"
---

# Managing your code size limits

Black Duck will notify you when you are approaching your code
size limit (as declared in your license). A notification, such as the following, appears
in the UI when you are at 80% or higher of your code size limit:

  
 [image: Code limit notification]   

If you exceed your code size limit, an error message appears when trying to scan (for
example, shown in log files in Jenkins or on the screen in Black Duck Detect (Desktop)) or
when uploading scans to Black Duck. You will not be able to scan or
upload scans if you exceed your code size limit.

When receiving this notification, you can:

- Contact Customer Support to upgrade your service.
- View the scan size for a project version:

  1. Select the project name using the **Watching** or **My Projects**
     dashboard. The *Project Name* page appears.
  2. Select the version name which displays the **Components** tab.
  3. Select the **Settings** tab.
  4. Select **Scans** to view the scans mapped to this project version.

       
      [image: Scans page]   

     The scan size appears above the list of scans.
- Delete
  existing scans to free up space.

  To determine the size of a scan:

  1. Click [image: image] to display the
     Scans page.
  2. Select the path of the scan that you want to view the results to open the
     *Scan Name* page.

       
      [image: Scan Name Page]   

     The **Scan Details** sections lists the scan size.

Note: You can view your current usage versus your limit on the Scans page. Values appear in the
upper right corner of the page.
