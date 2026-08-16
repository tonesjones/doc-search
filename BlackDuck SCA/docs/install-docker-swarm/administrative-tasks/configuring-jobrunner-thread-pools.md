---
title: "Configuring jobrunner thread pools"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-jobrunner-thread-pools.html"
content_id: "7faWgSNzflK2IJfZFSwhlQ"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:09.330557+00:00"
---

# Configuring jobrunner thread pools

In Black Duck, there are two job pools - one that runs scheduled jobs (called the
periodic pool) and one that runs jobs that are initiated from some event, including API
or user interactions (called the ondemand pool).

Each pool has two settings: max threads, and prefetch.

**Max threads** is the maximum number of jobs a jobrunner container can run at the
same time. Adding together periodic and ondemand max threads should never be larger than
32 as most jobs use the database and there are at most 32 connections. It is very easy
to saturate the jobrunner memory, so the default thread counts are set very low.

**Prefetch** is the number of jobs each jobrunner container with grab in each round
trip to the database. Setting this higher is more efficient, but setting it lower will
spread the load more evenly across multiple jobrunners (although even load is not a
design goal of jobrunner in general).

In Docker Swarm, add the following settings to your `blackduck-config.env`
file:

```
org.quartz.scheduler.periodic.maxthreads=2
org.quartz.scheduler.periodic.prefetch=1
org.quartz.scheduler.ondemand.maxthreads=4
org.quartz.scheduler.ondemand.prefetch=2
```
