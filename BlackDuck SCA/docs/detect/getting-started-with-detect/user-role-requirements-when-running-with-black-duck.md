---
title: "User role requirements when running with Black Duck"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/user-role-requirements-when-running-with-black-duck.html"
content_id: "UiQ9jl05zrlcZSeSlF8qUg"
version: "11.5.1"
section: "Getting started with Detect"
scraped_at: "2026-08-08T23:44:15.721193+00:00"
---

# User role requirements when running with Black Duck

Any user can download Detect and run a scan, however you must configure a user/API token in Black Duck SCA for the Detect scan to be analyzed by Black Duck SCA.

For more information on creating a Black Duck SCA user token, please consult the documentation provided by Black Duck SCA under the topic: [Managing user access tokens](https://docs.blackduck.com/r/blackduck/latest/black-duck-documentation/managing-user-access-tokens.html).

**The following user roles are required for the user that you create in Black Duck SCA**

- The user must have the Project Creator overall role in order to create Black Duck SCA projects.
- The user must have the Global Project Viewer overall role, or be a member of the project, in order to create Black Duck SCA project versions.
- The user must have the Project Code Scanner project role, or the Global Code Scanner overall role, in order to populate the project BOM.
