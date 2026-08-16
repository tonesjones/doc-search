---
title: "Maintaining the size of a database"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/maintaining-the-size-of-a-database.html"
content_id: "dEyyqh1OCOeywkvqC7mntg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:14.781123+00:00"
---

# Maintaining the size of a database

With each commit to Coverity Connect or any additions to the number of Coverity Connect
entities (users, groups, components), the size of your database will grow. The rate that
the database grows is based on many factors including the number of defects and
snapshots (which will vary for every organization) and the number of lines of code in a
given project. Because of this, predicting the size of database over time is extremely
difficult, however is it important to both monitor and maintain the size of your
database over time.

The database password is located in the
<install_dir>/config/cim.properties file.
