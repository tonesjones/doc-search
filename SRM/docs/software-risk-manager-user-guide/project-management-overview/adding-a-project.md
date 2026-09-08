---
title: "Adding a Project"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/adding-a-project.html"
content_id: "EO3iEJZDEIXjKsnJ~LOpAQ"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:07.781088+00:00"
content_hash: "aa911d6d131a3d4d5a64b104d27e57063b4b1444981e0effde6fad2a6e3211ef"
---

# Adding a Project

Before you can run an analysis, you need to create a project.

**To add a project:**

1. Click the Projects icon in navigation bar to open the Projects page.

   [image: image]
2. Click Add Project.

   [image: image]
3. Enter a unique project name.
4. Select or enter the default branch.

   For more information on project branches,
   see Project Branches below.
5. Click Save.

## Project Branches

A *Branch* is a unique line of development containing a collection of scans over
time. Each project contains at least one branch.

New branches can only be created by running an analysis. When
creating a new branch for an analysis, a parent branch needs to be chosen.
Conceptually, this represents the development line that this new branch was forked
from. The new branch will be created by cloning the *Findings* and
*Results* from the chosen parent branch, and then running the new analysis.
The newly created branch will have the same contents as if the analysis had been run
on the parent branch. However, since this is a new branch, the parent branch will be
left untouched, and thus the two branches will be able to be tracked independently
of each other over time.

The Branch Management page is used to manage the branches for a project and is
accessible by users with the `manage`
[role](http://localhost:8080/help/html/user_guide/Project-Management/user-roles-config.html).

Click the Projects icon in the navigation bar, then click the project's dropdown
configuration icon and select Manage Branches.

[image: image]

From the Manage Branches page, you can view all branch hierarchies for a project as
well as rename and delete individual branches. To navigate to a project's Branch
Management page, click the project's dropdown configuration icon and select Manage
Branches.

When viewing the finding and result information for a branch, a contextualized view of
that information is given. Some information is shared globally across all branches
containing the finding, while other information may differ based on the branch.

Globally shared finding information will be visible on every branch where that
finding is present and will not change based on which branch is being viewed.

Information that is global includes the following:

- Comments added to findings by the user
- Issue Tracker Associations
- Tags

Contextual information will be tailored to the selected branch. Contextual
information includes the following:

- **Finding Status.** Each branch includes a finding status, which includes
  "new," "existing," and "gone."
- **Severity Override.** Each branch has its own severity override for each
  finding.
- **Associated Results.** Different results may be present on each branch,
  depending on the analyses performed.
- **Location.** Note that line numbers may differ between branches.
- **Source Code.** Source code mapping will be based on the latest copy of
  source code uploaded for the branch.

The Activity Stream will
be tailored for the branch that is being viewed and will include the global
information as well as the contextual information (listed above) that is relevant to
the branch. Contextual information is inherited from the parent branch at the time
the branch is created. After the analysis for a new branch begins, any changes to
the parent branch will diverge from the new branch and will not be visible in the
child branch.

## Project Groups

Projects may be repositioned in a hierarchy, where one project may become the parent
(or group) containing another project.

Once you move one or more projects into a parent project, the parent project can be
considered as a "project group." The Projects page displays project groups as a
summary of all findings for all projects in that group, including the group project
itself.

Note: A project group is still a project, and can still have findings of its own. The
summary of findings specific to the parent project will appear above the child projects
when you expand the group. There is no inherent limit to how deeply-nested projects can
be. A child project can have its own child projects, and so on.
