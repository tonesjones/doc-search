---
title: "System overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/system-overview.html"
content_id: "IcRxXDLtyP9qGiQaotoGAQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:18.798066+00:00"
---

# System overview

The examples in the following scenarios use the BusyBox open-source project to represent
a product's code base for an unnamed organization. The codebase was analyzed using
Coverity Analysis, and was committed to the following streams, each representing a
different way in which the software is built:

- allyesconfig
- allnoconfig
- defconfig
- randconfig

The user scenarios in this section concentrate on a project called
busybox_dev which contains the
allyesconfig and allnoconfig stream
associations.

The following organizational chart displays the users that are key participants in the
busybox_dev project, and the development groups to which they
belong:

Figure 1. busybox_dev users
  
 [image: image]

admin
:   The Coverity Connect system administrator. Responsible for creating/importing
    users, configuring groups, setting user permissions, and so forth.

busybox_owner
:   Leads a team of nine developers and is responsible for team's overall
    productivity and for assigning issues and project tasks to developers. Knows
    the exact issues contained in the project areas for assignment. Manages
    multiple groups and requires the groups to have limited access to certain
    portions of the codebase. Has configuration (Project Owner)
    privileges.

user1-user9
:   Use Coverity tools to find and resolve issues in the codebase. Have User
    privileges to view, filter, and triage issues.

    Note: For information about creating users, creating groups, and adding users to
    groups, see Managing users, groups, and roles.
