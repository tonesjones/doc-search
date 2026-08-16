---
title: "System diagnostics overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/system-diagnostics-overview.html"
content_id: "I1QYYBxabzUm1OBKw4JWnQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:08.585424+00:00"
---

# System diagnostics overview

The System Diagnostics page provides the following features:

- Check the current operating status of the server

  The Overview tab displays information and statistics about
  the current operating condition of the Coverity Connect server. The data are
  updated in real time.
- Check the load on the system

  The Graph tab provides five different types of graphs,
  each measuring different processes that contribute to or indicate system load.
  The graphs will update in real time if the check box is selected, as long as the
  tab remains open.
- Check the status of the cluster

  If the Coverity Connect server is a subscriber or coordinator, the
  Cluster tab displays information about the cluster
  status.
- Check user information

  The Users tab displays information about several
  categories of users. If the number of allowed users has been reached, this tab
  will help you know which ones to delete.
- Check database information

  The Database tab displays information about database size
  and current query.
- Check configuration files, environment variables, and Java properties

  The Config Files tab displays a list of configuration
  files, environment variables, and Java properties used by Coverity Connect. The
  contents of the files can be viewed by clicking on each item, or the files can
  be downloaded as a set.
- Check WebSocket connectivity

  The WebSocket Connectivity tab enables you to test whether
  the server's WebSocket Connectivity is functioning properly. This test must
  succeed for the server to accept commits over HTTPS.
- Check logs and log information

  The Logs tab displays a list of log files used by Coverity
  Connect. The contents of the files can be viewed or downloaded.
