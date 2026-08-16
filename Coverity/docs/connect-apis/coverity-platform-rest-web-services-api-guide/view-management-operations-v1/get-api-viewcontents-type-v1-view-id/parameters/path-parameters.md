---
title: "Path Parameters"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/path-parameters.html"
content_id: "QhvCNT_qxwS~yRLC~9nG~g"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:53.110693+00:00"
---

# Path Parameters

| Parameter name | Description |
| --- | --- |
| type | **Required.** The type of view requested. Possible values:                                            `issues    issuesByProject    functions    files    components    checkers    owners    projects    tests    trends    snapshots`  The type `projects` can be used to export views at the **Projects (View all)** level, such as the **All Projects** view. All other view types apply to views at the single-project level, such as the **Outstanding Defects** view. For example, the following retrieves all rows (all projects) of the **All Projects** view:  `localhost:8080/api/viewContents/projects/v1/All%20Projects?projectId=*`  In contrast, this example retrieves only one row (the project named `my_project`):  `localhost:8080/api/viewContents/projects/v1/All%20Projects?projectId=my_project` |
| view_id | **Required.** Name or numeric ID of the view. |
