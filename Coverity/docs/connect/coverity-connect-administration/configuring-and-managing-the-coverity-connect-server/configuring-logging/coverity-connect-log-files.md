---
title: "Coverity Connect log files"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-connect-log-files.html"
content_id: "NnpAis0VqMUbRb~qaARMlw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:02.080740+00:00"
---

# Coverity Connect log files

If an error occurs, you can examine the following log files to help diagnose the
issue.

catalina.out
:   Log that is used only in case of a catastrophic Tomcat failure, when the file
    can contain standard error and output.

cim.log
:   Basic information about startup, shutdown, and access to Coverity Connect. It
    also records output from the `cov-manage-im` command.
    Errors during commits are stored in this log. This log is rotated daily. The
    size of the log can grow over time, taking up database space. It is
    recommended that you monitor the log size and remove logging information as
    needed.

cov-admin-db.log
:   Records `cov-admin-db` activity, such as a change to a
    password or the creation of a database archive file.

cov-archive.log
:   Records stream export and import actions resulting from the execution of the
    cov-archive command.

coverity_service.log
:   Windows-only log file that records activity pertaining to Coverity Connect as
    a service. The file can be present only if Coverity Connect is installed as
    a service.

catalina.log
:   Internal information about the embedded Tomcat server. This log is rotated
    daily.

The log files are written to the <install_dir>/logs
directory. Note that most Coverity Connect system commands log process and environment
data.
