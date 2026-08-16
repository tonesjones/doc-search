---
title: "Using components"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-components.html"
content_id: "U7NmJKDEytesEQONbH8faA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:15.049650+00:00"
---

# Using components

The Coverity Connect components feature allows you to logically group source code files
in named entities. Defining components allows you to:

- Filter issues and files to show the relationship between source code and
  development teams.
- Assign issues to only the users or groups that are responsible for a
  particular section of the code.
- Limit access to code and issues, for example, to address, intellectual
  property concerns, to prevent exposing third party code, or to prevent
  exposing vulnerabilities in the code.

Generally, you create components with source files of related functionality, such as
libraries or software subsystems. For example, if a particular software group is working
on a specific set of functions within a product, the group might only be interested in
issues found in the source code of those functions.

A user with configuration privileges can create a component for the group containing the
source files for these functions. For information on setting configuration privileges,
see Roles and role-based access control.

Members of the group can view and filter these issues in the Source screen and receive
automatic email notification of issues found in these files.

Note: After components have been added, deleted, or changed, users need to logout and login
again for the changes to take effect.
