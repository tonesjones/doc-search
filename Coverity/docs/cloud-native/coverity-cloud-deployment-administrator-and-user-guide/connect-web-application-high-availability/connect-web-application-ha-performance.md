---
title: "Connect Web application HA performance"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/connect-web-application-ha-performance.html"
content_id: "dENMiDoi~pBFqk8umOr_9A"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:24.881120+00:00"
---

# Connect Web application HA performance

Using Coverity Connect Web application HA has the following performance benefits:

- **Single point of failure**: Having multiple instances of the Connect Web
  application eliminates a single point of failure, ensuring that the Connect web
  application is highly available.
- **Workload distribution**: Having multiple replicas of an application reduces
  load pressures from existing replicas​.
- **Commit throughput**: Having multiple commit server replicas improves
  throughput by adding more instances of the application.​ Multiple commit server
  replicas increases overall commit throughput. Any commit can be assigned to one
  of multiple pods as opposed to waiting for a single pod to become available.
  Here are some commit throughput test results:

  - 2 replicas provide 18% more throughput than 1 replica.
  - 4 replicas provide 150% more throughput than 1 replica.

  Note: Using Connect Web application HA for concurrent commits
  to the same stream does NOT increase throughput. Connect Web application HA does
  NOT speed up a single commit.

  Note: At low loading requests, extra `cimweb`
  replicas might reduce commit performance. For example, with commit concurrency
  less than 30, caching overhead between two replicas could cause commits to take
  50% longer to complete (1.5 times longer). This is especially true for large
  idirs greater than 10Gb.
- **API throughput**: API throughput is better with HA than with a single Connect
  `cimweb` pod. In an environment with many concurrent users, using
  HA enables load balancing between multiple `cimweb` pods. This
  prevents overloading one single pod. Here are some API throughput test results:
  - Two replicas provide around 60% more API throughput than 1 replica for
    50+ concurrent users.
