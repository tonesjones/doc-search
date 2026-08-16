---
title: "Database optimization"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/database-optimization.html"
content_id: "14U~wX~eLLuFvIG3DiGb5w"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:15.396860+00:00"
---

# Database optimization

To maintain the size of your embedded database, run the command `cov-admin-db
optimize`. This command should be scheduled to run nightly on databases
that regularly see heavy commit traffic. The command vacuums and analyzes the database,
which compresses it and updates the query planner data.

For more information, see the `cov-admin-db`
description in the Coverity 2026.6.0 Command Reference.
