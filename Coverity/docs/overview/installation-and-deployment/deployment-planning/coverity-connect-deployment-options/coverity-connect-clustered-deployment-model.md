---
title: "Coverity Connect clustered deployment model"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-connect-clustered-deployment-model.html"
content_id: "plcBS2XjzEO1cFRk4bKLeg"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:43.104621+00:00"
---

# Coverity Connect clustered deployment model

The Coverity Connect clustered deployment model allows you to deploy clusters of Coverity
Connect instances on which centrally managed data is synchronized in an enterprise.
Importantly, developer-set triage states can be updated automatically across the
cluster. For Coverity Connect to synchronize data, it is necessary to set up one
instance of Coverity Connect as the central Coordinator and to configure other Coverity
Connect instances into a cluster of Subscribers with which the Coordinator can
communicate.

When a developer updates an issue through the Coordinator or through a Subscriber, the
update propagates to other members of the cluster. In this way, the Coordinator is
responsible for synchronizing triage data updates across Coverity Connect
Subscribers.

[image: image]

The benefits of using a clustered environment include the following:

- You can distribute the commit load over the subscribers or coordinator and you can
  choose specific hardware for the clustered components (for example, clustered
  components that will accept larger commit loads might have a different hardware
  configuration than those with lesser commits.)
- The number of Coverity Connect users can be distributed across the environment so as
  to not limit performance. For example, if the number of users on the system exceeds
  the numbers recommended in the recommended maximum
  limits for a stand-alone system, you can set up a clustered environment
  to offset the performance load.
- If you have users in separate geographic locations, you can set up subscribers for
  any number of locales and still share issue information.
- Clustered components can be set with either embedded or external databases.

Note: If possible, the coordinator instance should act solely as coordinator, and have no
projects, streams, or snapshots configured. This will ensure that no individual project
or stream information is lost in the event of failure.

For more information about how the data is synchronized and to set up a clustered
environment, see the Coverity Platform 2026.6.0 User and Administrator Guide.
