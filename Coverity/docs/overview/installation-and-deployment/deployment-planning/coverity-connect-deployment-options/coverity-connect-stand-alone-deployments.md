---
title: "Coverity Connect stand-alone deployments"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-connect-stand-alone-deployments.html"
content_id: "OFlkTY~MAnvZDhAoJwogQw"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:42.281228+00:00"
---

# Coverity Connect stand-alone deployments

In this model, Coverity Connect is deployed as a standalone application. Users within
your organization will log in to and access a central instance of Coverity Connect.
There can be multiple instances of Coverity Connect in your organization, but issue
data, classification states (triage), and trending metrics are not shared among the
individual instances (for information about deploying Coverity Connect as a shared
environment, see Coverity Connect clustered deployment model). Coverity
Connect comprises two main components:

- The Coverity Connect application server that hosts the application and its
  associated tools and features.
- The database, which is a PostgreSQL database that contains all of the analysis
  and defect data, as well as user and system components.

In a standalone environment, Coverity Connect can be installed either with an embedded or
external PostgreSQL database:

[image: image]

Installs the Coverity Connect application server and the
PostgreSQL database at the same time and on the same machine. This option is generally
used for its ease of use. It is the default option during installation and is useful for
getting the system up and running quickly. It might also be a good alternative for
organizations that do not have a dedicated Database Administrator.

Allows you to install the Coverity Connect application server in
one location, and associate it with a separately installed PostgreSQL database. The
benefits to using an external database are:

- You can maintain and scale the PostgreSQL database separately. For example, you
  have finer control of database system resources, such as kernel parameters and
  file system options.
- You can associate the Coverity Connect application server to an existing
  PostgreSQL database.

When you install Coverity Connect, you are prompted to choose a Production or Demo
performance tuning option. The installer will inform you if your current system settings
are not properly configured. If this occurs, you will have to adjust your system
settings in order for Coverity Connect to run. For more information, see Installing Coverity Connect.

Both of the standalone deployment options are subject to system limits. So, it is
recommended that you determine the load on your system using the deployment checklist and then reference your
results with the Coverity
Connect deployment limits table. If you think that your system might exceed
theses limits, you might to consider deploying Coverity Connect in a clustered
environment.
