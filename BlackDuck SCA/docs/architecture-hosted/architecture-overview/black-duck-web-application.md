---
title: "Black Duck web application"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/black-duck-web-application.html"
content_id: "F_F6xSX7Q_tkFG36odNUkA"
version: "2026.7"
section: "Hosted Architecture and Network Communications"
scraped_at: "2026-08-08T15:32:52.239601+00:00"
---

# Black Duck web application

After the scan completes, the Scan Client sends the signatures to Black Duck's web application. Black Duck's web application, accessed via a browser, provides a central point for managing
and viewing all of the information captured. User connections to Black Duck's web application (from a browser or other
supported client) are secured using HTTP/2 and TLS1.3 (or HTTP 1.1 and/or TLS 1.2 if
the browser does not support HTTPS/2 and/or TLS 1.3).

The Black Duck application runs in the Black Duck hosted
environment. Within the Black Duck application, each customer has its
own set of containers and their data is physically isolated from all other customers’
data in its own encrypted PostgreSQL instance.

The Black Duck application will send the signatures to
the Black Duck KnowledgeBase (KB) web service to identify the open
source software contained in the code which has been scanned and retrieve the
associated metadata for each component. It will then generate a BOM, which details
the open source components/versions and presents the associated risk factors –
security risk, license risk, and operational risk.

End users can review and edit the BOMs, filter results based on risk and other
factors, and drill down to get more detailed information on the vulnerabilities,
licenses, files, and other information associated with each of the components in the
BOM. The Black Duck application also includes features
such as policy management, search, vulnerability mitigation status and tracking,
reporting, and so on.

The Black Duck application is built on top of various
open source components – such as Apache Tomcat web server, PostgreSQL database, and
so on and is deployed and managed as a set of Docker containers.
