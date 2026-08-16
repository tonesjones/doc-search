---
title: "Creating a SCM project"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/creating-a-scm-project.html"
content_id: "BZbQjcBg53WdJmlXoprhjA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:13:59.603913+00:00"
---

# Creating a SCM project

If you have SCM integration
enabled, you can create projects based from the repositories found in your
SCM providers. The process to create a project adds an additional step to select the SCM
repository from where the project originates. The servers displayed will depend on what
SCM providers your
organization has configured for use.

Important:
Users with only the **Global Project Viewer** role cannot view SCM projects.
To create, view, and manage SCM projects, users must have either the
**Lite Global Project Manager** role or the **Integration Manager** role.

## Creating projects from a SCM Provider

To create a SCM project:

1. Log into Black Duck SCA as a Global Code Scanner user.
2. Click **+ Create Project** at the top of any page.
3. Select **SCM Project** from the menu.
4. Select the SCM provider that applies to your project. You must be authenticated to use the SCM provider.
5. Select any number of repositories from the **Repository** list presented.
   Repositories maked with the Mapped tag have already been
6. Click the **Create and Scan** button.

A project will be created for each repository scanned and the default branch will be
used as the project version. You will be given the opportunity to scan other
branches afterwards. The result of the scan creates a read-only bill of materials
(BOM) which is lighter than the usual BOM.
