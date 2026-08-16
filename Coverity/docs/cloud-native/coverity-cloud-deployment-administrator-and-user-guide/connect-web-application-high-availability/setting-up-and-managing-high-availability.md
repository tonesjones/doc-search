---
title: "Setting up and managing high availability"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-up-and-managing-high-availability.html"
content_id: "Z_qJyWSpg1lYGx6egddtDA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:25.525916+00:00"
---

# Setting up and managing high availability

The following list outlines tasks that you need to perform to set up and manage Coverity
Connect web app high availability. These tasks are in addition to all other
infrastructure, Helm chart, and deployment tasks you need to perform to deploy Coverity
Connect in the cloud. HA setup and management tasks include:

1. Based on your anticipated workloads, plan the desired HA configurations and
   resources.
2. Create the infrastructure to provide the resources. See Coverity deployment scenarios.
3. Set the `cim.cimweb.replicas` Helm key for the desired number of
   cimweb pod replicas. See Managing cimweb pod replicas and cim.cimweb Helm keys.
4. Set the `cim.commit-server.replicas` Helm key for commit performance.
   See Optimizing commit performance vs throughput using commit-server pods.
5. Optionally, you can define affinities and anti-affinities to distribute pods on
   specific nodes. See Using affinities to distribute pods on nodes.
6. Perform a `helm install` to install the deployment. See Installing chart releases for your deployment.
7. Manage scaling and resources over time.
