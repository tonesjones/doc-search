---
title: "Configuring jobrunner thread pools"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-jobrunner-thread-pools.html"
content_id: "gZYXnje3uV_IM4wiKqbPQw"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:20.423121+00:00"
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

In Kubernetes, you can override the thread counts settings using the following override
file:

```
jobrunner:
     maxPeriodicThreads: 2
     maxPeriodicPrefetch: 1
     maxOndemandThreads: 4
     maxOndemandPrefetch: 2
```
