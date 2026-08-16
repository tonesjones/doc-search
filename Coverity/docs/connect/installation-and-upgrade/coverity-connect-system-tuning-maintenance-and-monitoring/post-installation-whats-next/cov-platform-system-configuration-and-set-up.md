---
title: "cov-platform system configuration and set-up"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cov-platform-system-configuration-and-set-up.html"
content_id: "C~Gqwpd7F0QabVMvs7um5g"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:10.112333+00:00"
---

# cov-platform system configuration and set-up

Except for performance tuning and monitoring, the tasks mentioned below are described in
full in the Coverity Platform 2026.6.0 User and Administrator Guide.

*Configuring sign-in options*
:   Controls user access to Coverity Connect.

*Setting up SSL*
:   Configure Coverity Connect to encrypt communications using SSL.

*Connecting to an LDAP database*
:   The LDAP configuration feature for Coverity Connect allows site administrators
    to enter this information only once, and all LDAP-compliant applications can use
    this central resource.

*Configuring email notification*
:   You can enable Coverity Connect to send email to notify developers of new issues
    or issues that changed triage states.

*Creating and/or importing users*
:   Create or import users into your system. You can also create and organize users
    in groups.

*Setting up role-based access control*
:   Role-based access control (RBAC) is a feature that restricts system access to
    authorized Coverity Connect users.

*Creating streams and projects*
:   You create a stream to support issue data on a portion of your code base. Each
    stream is organized into a project, which can support multiple streams.

*Creating data stores*
:   A triage store is a repository for the current and historical triage values of
    CIDs. In Coverity Connect, each stream must be associated with a single triage
    store so that users can triage issues (instances of CIDs) found in the
    streams.

*Configuring components*
:   The components feature allows you to logically group source code files in named
    entities. Defining components allows you to filter issues and files to show the
    relationship between source code and development teams, assign issues to only
    the users or groups that are responsible for a particular section of the code,
    and limit access to code and issues

*Configuring and managing databases*
:   Database size can be optimized for performance, and clean-up processes can be
    scheduled to remove unneeded information. In addition, databases can be backed
    up and restored. Procedures are provided for backing up and restoring embedded
    databases in both stand-alone and clustered deployments.

*Tuning the embedded database*
:   See Coverity Connect system and database tuning.

*Tuning the Coverity Connect server*
:   See Coverity Connect system and database tuning.

*Monitoring and diagnosing performance*
:   See Monitoring and diagnosing Coverity Connect performance.
