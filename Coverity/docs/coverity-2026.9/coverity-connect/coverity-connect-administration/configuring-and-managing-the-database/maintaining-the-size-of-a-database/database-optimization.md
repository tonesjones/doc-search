---
title: "Database optimization"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/database-optimization.html"
content_id: "14U~wX~eLLuFvIG3DiGb5w"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:06.947852+00:00"
---

# Database optimization

To maintain the size of your embedded database, run the command `cov-admin-db
optimize`. This command should be scheduled to run nightly on databases
that regularly see heavy commit traffic. The command vacuums and analyzes the database,
which compresses it and updates the query planner data.

For more information, see the `cov-admin-db`
description in the Coverity Command Reference.
