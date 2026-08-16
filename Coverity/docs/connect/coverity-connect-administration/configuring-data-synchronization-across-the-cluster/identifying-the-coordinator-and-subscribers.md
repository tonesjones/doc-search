---
title: "Identifying the coordinator and subscribers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/identifying-the-coordinator-and-subscribers.html"
content_id: "sN0CRw5AF6aY8MEIbGSSqA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:41.122419+00:00"
---

# Identifying the coordinator and subscribers

This section describes how to edit the cim.properties file to
identify the Coordinator and Subscribers in a cluster. It also describes how to remove a
Subscriber from the cluster.

**To identify the Coordinator and Subscribers:**

This configuration takes place through settings in a configuration file
(cim.properties) on each Coverity Connect instance. Each
Subscriber instance must specify the address of the Coordinator in this file.

Important: If you are setting up a new Subscriber instance, the instance should
not contain any pre-existing issue data or any settings or records that will be managed
by the Coordinator. As Coordinator responsibilities
explains, the Coordinator handles all centrally managed configurations, so they should
not be set up on any of the Subscribers.

1. Configure one instance of Coverity Connect as the Coordinator.

   You need to add the following properties to
   <install_dir>/config/cim.properties on the
   Coordinator:

   - remoteconfig.mode: Set the remote configuration mode
     to `coordinator`.

   Coordinator configuration example:

   ```
   remoteconfig.mode=coordinator
   ```

   - Set up SSL
     communications.
2. Configure one or more *clean* instances of Coverity Connect as
   Subscribers.

   You need to add the following properties to
   <install_dir>/config/cim.properties on each
   Subscriber:

   - remoteconfig.mode: Set the remote configuration mode
     to `subscriber`.
   - remoteconfig.coordinator: Provide the IP address or
     fully qualified domain name (not an alias) followed by the Commit port
     number (the Coverity Connect default is `9090`) for the
     Coordinator on each Subscriber in the cluster.

     Note: Even if you use the Coverity Connect HTTPS port for commiting defect
     data, you must continue to use the Commit port for Coordinator to
     Subscriber communication.

   Subscriber configuration example:

   ```
   remoteconfig.mode=subscriber
   remoteconfig.coordinator=cim.london.ex.com:9090
   ```

   - Set up SSL
     communications.

Since the `remoteconfig` SSL negotiation uses the operating system's
host name resolution system to validate SSL certificates from other hosts in the
cluster, that infrastructure must be capable of resolving the host names of the peers in
the cluster.

Normally this is not an issue since Coverity Connect servers are assumed to be installed
in an environment with a working host name resolution system. However, in some
environments this may not be the case. In such environments, you may need to enable host
name resolution on your server or edit /etc/hosts.

Removing a subscriber from the cluster

In order to remove a Coverity Connect instance from the cluster, navigate to
<install_dir>/config/cim.properties and set the
remoteconfig.mode property to `none`.

```
 remoteconfig.mode=none
```

After your properties file is updated, restart Coverity Connect.

Note: Once a subscriber changes to a non-subscriber, it cannot be changed back. So it is
recommended that you back up all subscriber data before configuration.
