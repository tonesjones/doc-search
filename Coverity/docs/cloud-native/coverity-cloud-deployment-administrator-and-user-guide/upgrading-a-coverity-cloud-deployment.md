---
title: "Upgrading a Coverity cloud deployment"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrading-a-coverity-cloud-deployment.html"
content_id: "J~YewQkXKAhCCAddRM1dKw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:24.648576+00:00"
---

# Upgrading a Coverity cloud deployment

This chapter describes how to upgrade a Coverity cloud deployment instance to a new
version.

Note: Once you have obtained all Coverity artifacts, this actual
upgrade will take about 10 to 15 minutes to complete, assuming that you do not need to
upgrade the database schema.

If you are upgrading the Coverity database schema, this
upgrade will include downtime because Coverity Connect is temporarily disabled
during database schema upgrade. The database schema upgrade can take from several
minutes up to hours or even longer, depending on the size of the database, database
version, and resources allocated to the database.

Important: Ensure that no users or automated pipelines
need access to Coverity during the upgrade.

Note: This procedure is not intended for migrating to the
cloud.
