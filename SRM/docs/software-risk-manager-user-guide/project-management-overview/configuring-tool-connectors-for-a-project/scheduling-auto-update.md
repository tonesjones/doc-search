---
title: "Scheduling Auto Update"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/scheduling-auto-update.html"
content_id: "QyfZAfEKIT_9qsu5nNVxrA"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:12.449428+00:00"
content_hash: "93fe5a3d666ca9c3a8473cb112f015eb7ece916cbf5199ab586bc46f28745163"
---

# Scheduling Auto Update

**To set an auto-update schedule for your tool connector:**

1. Click the Projects icon in the navigation bar to open the Projects page.
2. Click the Project's dropdown configuration icon and select Tool Connectors.
3. Select a tool connector, then click the dropdown configuration icon and select
   Edit.

   [image: image]

   - To choose a daily time to update, select *Every day* at and fill in
     the time of day to run the analysis.
   - To choose a specific schedule to update, select *Every* and enter
     the number of analyses to run and the time frame (minutes, hours,
     days).
4. Select *Run this connector during normal analyses* if you want your tool
   connector to run during a scheduled analysis.

Note: If you configured one of your tool connector's fields to sync with a Software Risk
Manager branch which does not yet exist, the connector will not be able to run. This
will be indicated with a warning icon next to the tool connector's name in the list of
configured tool connectors. The appropriate Software Risk Manager branch can be created
by running a normal analysis or by clicking the Run Now button and submitting the
subsequent form. Once the appropriate Software Risk Manager branch has been created,
auto-update can continue.
