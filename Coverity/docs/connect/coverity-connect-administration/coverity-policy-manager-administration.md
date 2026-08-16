---
title: "Coverity Policy Manager administration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-policy-manager-administration.html"
content_id: "zWWWoD6h~mHCdv15IdgxPg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:59.716921+00:00"
---

# Coverity Policy Manager administration

Coverity Policy Manager administrators set up the hierarchies that are used to specify the
data source and structure of Coverity Policy Manager heatmaps and charts. For your organization to use Coverity
Policy Manager, it is necessary to specify at least one hierarchy and to assign the
appropriate Coverity Policy Manager role to users and/or groups (see Coverity Policy Manager roles and permissions).

Coverity Policy Manager is a companion product to Coverity Connect that shares the
Coverity Connect user database and servlet container and is fully integrated into the
Coverity Connect UI.

> **Licensing**
>
> If you need to update or import a license for Coverity Policy Manager, you need to
> import it through Coverity Connect. For details, see Coverity Connect license information.

> **Daily data synchronization**
>
> Coverity Policy Manager synchronizes Trend Report data with the Coverity Connect
> database once per day, starting between midnight and 1:00 am. The time needed to
> complete the data synchronization depends on the amount of data being
> transferred.
>
> Alternately, Status Reports are updated periodically throughout the day, waiting one
> hour after the end of each update to start the next one. For example, if an update
> takes 30 minutes to run, the Status Reports will be updated approximately every 90
> minutes.
>
> Note: In general, Policy Manager does not store data indefinitely.
> In the absence of other activity, daily data is kept for 40 days, weekly data is kept
> for 30 weeks, monthly data is kept for 24 months, and only yearly data is kept
> indefinitely. However, Policy Manager does not save historical data in terms of previous
> configurations of component map and stream settings, and if the current project
> configurations are changed, Policy Manager data is recomputed based on those
> changes.
>
> For information about data synchronization between coordinators and subscribers, see
> Synchronizing Coverity Policy Manager data across the cluster.

In this section:

- Managing a Coverity Policy Manager hierarchy
- Importing/exporting a Coverity Policy Manager hierarchy
- Scheduling the Extract Transform Load (ETL) process
- Creating summary metrics
- Coverity Policy Manager roles and permissions
